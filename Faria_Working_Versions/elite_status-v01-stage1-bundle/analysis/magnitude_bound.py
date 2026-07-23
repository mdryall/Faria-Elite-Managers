"""The Market for Elite Status -- Phase 5: magnitude-bound exercise.

Computes the MODEL-SIDE multiplier for the manuscript's magnitude-bound
subsection: how many percentage points of steady-state wealth loss the model
generates per percentage point of resources burned in elite credentialing.

Definitions (per period, at the elite-active steady state k*_e):
    burn      B(k)  = m*(k) * [(tau-1) r + (beta-1) c]      (excess resources)
    burn share b    = B(k*_e) / k*_e                        (share of endowment)
    wealth loss L   = (k*_none - k*_e) / k*_none            (vs no-elite SS)
    multiplier M    = L / b

The manuscript reports the range of M over the taste scan; the empirical
side of the exercise (sourced sector shares) then bounds the real-world
counterpart of b, and L <= M * b bounds the mechanism's aggregate bite.

Model formulas replicate analysis/dynamic_model.py verbatim (same running
example, same calibration Theta making k*=2 the absolute-status steady state
at s=0.10).  Cross-checks against that script's published numbers:
k*_none = 2.085 at s=0.10; k*_abs falls to 1.73 at s=0.19.
"""

import numpy as np
from scipy.optimize import brentq

P = dict(r=1.0, c=1.0, tau=4.0, beta=1.25, alpha=1.25, phi=6.0,
         dM=0.25, dL=0.5, chi=0.2, s=0.10, psi=25.0)
mu, lam = 1 / P['dM'], 1 / P['dL']
lam_e = lam / (1 - P['chi'])
GAMMA = 0.8

def F(x, s):  return 1.0 - np.exp(-x / s)

def Pi_f(kv):  return P['c'] + P['r'] + (mu + 2 * lam - 3) * kv
def Z_f(kv):   return P['alpha'] * Pi_f(kv) - P['beta'] * P['c'] \
                      - P['tau'] * P['r'] + (3 - 2 * lam_e) * kv

def m_star(kv, s, mode):
    if mode == 'none' or kv <= 0:
        return 0.0
    Z = Z_f(kv)
    if Z <= 0 or Z >= mu * kv:
        return 0.0
    eta0 = mu * kv / Z - 1
    return 1 - F(eta0, s)

def period(kv, gam, s, mode):
    ms_ = m_star(kv, s, mode)
    wE = Z_f(kv)
    elite_inc = ms_ * (wE + (2 * lam_e - 3) * kv)
    coef = (gam / 2) * (mu + 2 * lam - 3) * kv + (P['r'] + P['c'])
    rhs = kv - (gam / 2) * (kv + elite_inc) \
        - ms_ * (P['tau'] * P['r'] + P['beta'] * P['c'])
    n = rhs / coef
    if n < 0 or 1 - 3 * ms_ - 3 * n < -1e-9:
        raise ValueError("infeasible")
    W = kv + n * (mu + 2 * lam - 3) * kv + elite_inc
    return dict(m=ms_, W=W, p2=Pi_f(kv) / P['phi'])

def G(kv, s, mode, Theta):
    if kv <= 0:
        return 0.0
    try:
        pe = period(kv, GAMMA, s, mode)
    except ValueError:
        return np.nan
    return Theta * (1 - GAMMA) * pe['W'] / pe['p2']

pe2 = period(2.0, GAMMA, P['s'], 'absolute')
THETA = 2.0 / ((1 - GAMMA) * pe2['W'] / pe2['p2'])

def top_stable(s, mode, kmax=4.0, ngrid=4000):
    ks = np.linspace(1e-4, kmax, ngrid)
    gk = np.array([G(x, s, mode, THETA) - x for x in ks])
    roots = []
    for i in range(len(ks) - 1):
        if np.isnan(gk[i]) or np.isnan(gk[i + 1]):
            continue
        if gk[i] * gk[i + 1] < 0:
            roots.append(brentq(lambda x: G(x, s, mode, THETA) - x,
                                ks[i], ks[i + 1]))
    return max(roots)

# --- cross-checks against dynamic_model.py's published numbers --------------
k_abs0 = top_stable(P['s'], 'absolute')
k_none = top_stable(P['s'], 'none')
assert abs(k_abs0 - 2.0) < 1e-6, k_abs0
assert abs(k_none - 2.085) < 5e-3, k_none
k_abs_19 = top_stable(0.19, 'absolute')
assert abs(k_abs_19 - 1.73) < 5e-2, k_abs_19
print(f"cross-checks: k*_abs(s=0.10) = {k_abs0:.4f}, k*_none = {k_none:.4f}, "
      f"k*_abs(s=0.19) = {k_abs_19:.3f}  [match dynamic_model.py]")

# --- the multiplier over the taste scan -------------------------------------
BURN = (P['tau'] - 1) * P['r'] + (P['beta'] - 1) * P['c']
print(f"\nburn per elite manager: (tau-1)r + (beta-1)c = {BURN}")
print(f"{'s':>6} {'k*_e':>8} {'k*_none':>8} {'m*':>8} {'burn%':>8} "
      f"{'loss%':>8} {'mult':>6}")
mults = []
for s in np.arange(0.05, 0.301, 0.01):
    ke = top_stable(s, 'absolute')
    kn = top_stable(s, 'none')
    m = period(ke, GAMMA, s, 'absolute')['m']
    b = m * BURN / ke
    L = (kn - ke) / kn
    mult = L / b
    mults.append(mult)
    if round(s * 100) % 5 == 0:
        print(f"{s:6.2f} {ke:8.4f} {kn:8.4f} {m:8.4f} {100*b:8.2f} "
              f"{100*L:8.2f} {mult:6.2f}")

lo, hi = min(mults), max(mults)
print(f"\nmultiplier range over s in [0.05, 0.30]: {lo:.6f} to {hi:.6f}")

# --- the multiplier is EXACT: closed-form loss identity ---------------------
# Derivation (verified symbolically below).  Let A = mu+2lam-3, S(k) =
# r+c+(gam/2)Ak, Q = Theta(1-gam)phi, Delta = alpha(c+r)-(beta c+tau r).
# Substituting the clearing solution for n into W gives
#     W(k) = [k Pi(k) + m Pi(k) Delta] / S(k),
# so the transition map is  xi(k) = Q [k + m Delta] / S(k):  the elite map is
# the no-elite map with k shifted by m*Delta in the numerator alone.
# Subtracting the two steady-state equations k S(k) = Q[k + m Delta] and
# k_n S(k_n) = Q k_n, and using Q = r+c+(gam/2)A k_n:
#     (k_n - k_e) * (gam/2) A k_e = Q m |Delta|          [exact loss identity]
# whence  L/b = (|Delta|/BURN) * [1 + (c+r) / ((gam/2) A k_n)],
# independent of the taste distribution entirely.
import sympy as sp
k_, m_, r_, c_, tau_, beta_, alpha_, A_, g_, Q_ = sp.symbols(
    'k m r c tau beta alpha A g Q', positive=True)
Pi_ = r_ + c_ + A_ * k_
eps_ = alpha_ * Pi_ - beta_ * c_ - tau_ * r_
n_ = sp.symbols('n')
W_ = k_ + n_ * A_ * k_ + m_ * eps_
clear_ = sp.Eq((g_ / 2) * W_ + n_ * (r_ + c_) + m_ * (tau_ * r_ + beta_ * c_), k_)
n_sol = sp.solve(clear_, n_)[0]
W_sol = sp.simplify(W_.subs(n_, n_sol))
S_ = r_ + c_ + (g_ / 2) * A_ * k_
Delta_ = alpha_ * (c_ + r_) - (beta_ * c_ + tau_ * r_)
assert sp.simplify(W_sol - (k_ * Pi_ + m_ * Pi_ * Delta_) / S_) == 0
print("sympy: W(k) = [k + m Delta] Pi(k) / S(k)  -- map form verified")

A = mu + 2 * lam - 3
Q = THETA * (1 - GAMMA) * P['phi']
DELTA = abs(P['alpha'] * (P['c'] + P['r'])
            - (P['beta'] * P['c'] + P['tau'] * P['r']))
assert abs(Q - (P['r'] + P['c'] + (GAMMA / 2) * A * k_none)) < 1e-9
M_exact = (DELTA / BURN) * (1 + (P['c'] + P['r']) / ((GAMMA / 2) * A * k_none))
print(f"closed-form multiplier M = (|Delta|/burn)[1 + (c+r)/((gam/2)A k_n)] "
      f"= {M_exact:.10f}")
assert all(abs(mm - M_exact) < 1e-9 for mm in mults)
# and the loss identity itself, at the baseline steady state:
m0 = period(k_abs0, GAMMA, P['s'], 'absolute')['m']
lhs = (k_none - k_abs0) * (GAMMA / 2) * A * k_abs0
rhs = Q * m0 * DELTA
assert abs(lhs - rhs) < 1e-9
print(f"loss identity (k_n - k_e)(gam/2)A k_e = Q m* |Delta|: "
      f"{lhs:.6f} = {rhs:.6f}")
assert 0.5 < lo and hi < 3.0, (lo, hi)

# --- headline numbers for the manuscript (sourced envelope) -----------------
# Sources (verified 2026-07-21):
#   NCES, Condition of Education, "Postsecondary Institution Expenses":
#     US degree-granting postsecondary spending $702B in 2020-21
#     (constant 2021-22 dollars).
#   BEA: current-dollar GDP 2021 = $23.0T (2nd estimate, Feb 2022) --
#     the smallest published vintage, which makes the spending share, and
#     hence the bound, LARGER (conservative).
#   Chetty-Deming-Friedman: fewer than half of one percent of Americans
#     attend the twelve Ivy-Plus colleges.
HIGHERED_SPEND, GDP2021 = 702e9, 23.0e12
highered_share = HIGHERED_SPEND / GDP2021
print(f"\nUS postsecondary spending share of GDP: {100*highered_share:.2f}%")
assert 0.030 <= highered_share <= 0.031

# extreme envelope: elite segment = 5% of enrollment (an order of magnitude
# beyond Ivy-Plus scale), spending 4x the national average per student,
# ALL of it counted as burn:
env_spend_share = 0.05 * 4          # = 20% of postsecondary spending
b_extreme = highered_share * env_spend_share
L_extreme = M_exact * b_extreme
# central attribution: segment at 1% of enrollment, only the spending
# PREMIUM over the national average (taken as 1x average) counted as burn:
b_central = highered_share * 0.01 * 1
L_central = M_exact * b_central
print(f"extreme envelope: b = {100*b_extreme:.2f}% of resources -> "
      f"steady-state wealth loss {100*L_extreme:.2f}%")
print(f"central attribution: b = {100*b_central:.3f}% -> loss "
      f"{100*L_central:.3f}%")
assert L_extreme < 0.01, L_extreme          # under one percent
assert L_central < 0.0005, L_central        # a few hundredths of a percent

print("\nALL CHECKS PASS")
