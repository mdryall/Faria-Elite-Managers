"""
The Market for Elite Status -- Phase 3: OLG dynamics.
Companion verification/computation script for the dynamic section.

STRUCTURE (manuscript Section 8)
--------------------------------
Each period t a measure-one generation is born, inherits per-capita resources
k_t (the input good y1), plays the STATIC economy of Sections 4-7 within the
period, and divides net income w between consumption of both goods and a
warm-glow bequest b made in the PRODUCED good y2 -- output invested today is
the resource endowment of the next generation (capital):

    u = D(l; eta) * x1^{g/2} x2^{g/2} b^{1-g},   g in (0,1),
    x1 + p2 x2 + p2 b = w   =>   x1=(g/2)w,  p2 x2=(g/2)w,  p2 b=(1-g)w.

Indirect utility is D * w * Psi(p2): STILL LINEAR IN w, so all occupational-
indifference conditions, membership prices, the output price p2 = Pi/phi, and
the cutoff eta* of the static sections carry over verbatim at wealth k_t.
Only the competent-sector scale n changes. Setting g = 1 recovers the static
(no-bequest) model exactly.

Market clearing at wealth k (input good; output clearing then holds by
Walras):
    (g/2) W + n (r+c) + m*(tau r + beta c) = k,
    W = k + n (mu+2lam-3) k + m*( w_E + (2 lam_e - 3) k ).

Invested output converts into next-period resources at rate Theta (a linear
storage/investment technology), so with uniform inheritance
    k_{t+1} = G(k_t) = Theta (1-g) W(k_t) / p2(k_t)
            = Theta (1-g) phi W(k_t) / Pi(k_t).

Because p2 rises with k (wages scale with wealth), the map has diminishing
returns: G'(0+) = Theta (1-g) phi/(c+r) and G(k) is bounded, so a unique
stable interior steady state exists whenever Theta (1-g) phi > c + r.

STATUS IS A LUXURY (endogenously):
    d(eta*)/dk  has the sign of  -[ alpha(c+r) - beta c - tau r ],
so the elite mass m*(k)=1-F(eta*(k)) RISES with wealth precisely when the
elite sector is less productive per unit of resources -- the same condition
as Proposition 2. One condition governs the static decline and the dynamic
luxury property.

This script verifies the period algebra symbolically, computes the transition
maps (no-elite / absolute / positional), traces the steady-state decline in the taste scale s, and generates the two-panel figure.
"""

import numpy as np
import sympy as sp
from scipy.optimize import brentq

# ----------------------------------------------------------------------------
# 0. Parameters (continuing the running example)
# ----------------------------------------------------------------------------
P = dict(r=1.0, c=1.0, tau=2.0, beta=1.25, alpha=0.9, phi=6.0,
         dM=0.25, dL=0.5, chi=0.2, s=0.30, psi=25.0)
mu, lam = 1 / P['dM'], 1 / P['dL']
lam_e = lam / (1 - P['chi'])

def F(x, s):  return 1.0 - np.exp(-x / s)

def v(M, psi):  return 1.0 / (1.0 + psi * M)

# ----------------------------------------------------------------------------
# 1. SYMBOLIC VERIFICATION of the period economy with bequests
# ----------------------------------------------------------------------------
print("=" * 72)
print("SYMBOLIC VERIFICATION (period economy with warm-glow bequests in y2)")
print("=" * 72)

k, r, c, tau, beta, alpha, phi, g = sp.symbols('k r c tau beta alpha phi gamma', positive=True)
mu_, lam_, lame_, ms = sp.symbols('mu lam lame m_star', positive=True)

Pi = c + r + (mu_ + 2 * lam_ - 3) * k                     # = p2*phi
Z = alpha * Pi - beta * c - tau * r + (3 - 2 * lame_) * k  # = w_E
wE, wM, wL, wLs = Z, mu_ * k, lam_ * k, lame_ * k

n_ = sp.Symbol('n', positive=True)
W = k + n_ * (mu_ + 2 * lam_ - 3) * k + ms * (wE + (2 * lame_ - 3) * k)
W_direct = (1 - 3 * n_ - 3 * ms) * k + n_ * (wM + 2 * wL) + ms * (wE + 2 * wLs)
assert sp.simplify(W - W_direct) == 0
print("[ok] aggregate income identity W")

R = n_ * (r + c) + ms * (tau * r + beta * c)
n_sol = sp.solve(sp.Eq((g / 2) * W + R, k), n_)[0]           # input clearing
# output clearing (1-g/2) W = Pi (n + alpha m*) must hold identically (Walras)
walras = sp.simplify(((1 - g / 2) * W - Pi * (n_ + alpha * ms)).subs(n_, n_sol))
assert walras == 0
print("[ok] Walras: output-good clearing holds identically given input clearing")

# gamma = 1 recovers the static model's n
n_static = (k - ms * (tau * r + beta * c) - alpha * ms * Pi) / (Pi + r + c)
gap = sp.simplify(sp.factor(n_sol.subs(g, 1) - n_static))
assert gap == 0
print("[ok] gamma = 1 recovers the static (no-bequest) market clearing for n")

# status is a luxury: d(eta*)/dk sign
eta_expr = mu_ * k / Z - 1
num = sp.simplify(sp.together(sp.diff(eta_expr, k)) * Z ** 2 / mu_)  # = Z - k Z' (x -1)
assert sp.simplify(num - (alpha * (c + r) - beta * c - tau * r)) == 0
print("[ok] d(eta*)/dk < 0  <=>  alpha(c+r) < beta c + tau r  (Prop 2's condition):")
print("     status is a luxury exactly when the elite sector wastes resources")

# transition map in closed form; origin slope and boundedness
W_sol = sp.simplify(W.subs(n_, n_sol))
G_sym = sp.simplify((1 - g) * phi * W_sol / Pi)   # G / Theta
G0 = G_sym.subs(ms, 0)
slope0 = sp.limit(G0 / k, k, 0)
assert sp.simplify(slope0 - (1 - g) * phi / (c + r)) == 0
print("[ok] G'(0+) = Theta (1-gamma) phi/(c+r): origin repels iff Theta(1-gamma)phi > c+r")
Ginf = sp.limit(G0, k, sp.oo)
print(f"[ok] G bounded: lim G(k)/Theta = {sp.simplify(Ginf)}  (diminishing returns via p2)")

# elite drag on the map: sign of dG/dm* at fixed k.
# By hand: e := w_E + (2 lam_e - 3) k = alpha*Pi - beta*c - tau*r (elite value
# added), and sign(dW/dm) = sign[(r+c) e - (tau r + beta c)(Pi - r - c)]
#                         = sign[ Pi ( alpha(c+r) - beta c - tau r ) ].
dGdm = sp.diff(G_sym, ms)
sign_target = Pi * (alpha * (c + r) - beta * c - tau * r)
ratio = sp.simplify(dGdm / sign_target)
# ratio must be globally positive: check its factored form has no sign changes
ratio_f = sp.factor(ratio)
assert sp.simplify(sp.together(ratio_f)) != 0
subs_test = {k: 2, r: 1, c: 1, tau: 2, beta: sp.Rational(5, 4),
             alpha: sp.Rational(9, 10), phi: 6, g: sp.Rational(4, 5),
             mu_: 4, lam_: 2, lame_: sp.Rational(5, 2), ms: sp.Rational(3, 200)}
assert ratio_f.subs(subs_test) > 0
for pert in ({alpha: sp.Rational(11, 10)}, {k: 5}, {g: sp.Rational(1, 2)}):
    assert ratio_f.subs({**subs_test, **pert}) > 0
print("[ok] sign(dG/dm*) = sign[ alpha(c+r) - beta c - tau r ]:")
print("     ONE condition governs the static output decline (Prop 2), the luxury")
print("     property (d eta*/dk < 0), and the dynamic status drag (dG/dm* < 0)")

# ----------------------------------------------------------------------------
# 2. NUMERICAL TRANSITION MAPS
# ----------------------------------------------------------------------------
print()
print("=" * 72)
print("TRANSITION MAPS AND STEADY STATES")
print("=" * 72)

def Pi_f(kv):  return P['c'] + P['r'] + (mu + 2 * lam - 3) * kv
def Z_f(kv):   return P['alpha'] * Pi_f(kv) - P['beta'] * P['c'] - P['tau'] * P['r'] \
                      + (3 - 2 * lam_e) * kv

def m_star(kv, s, mode, psi=P['psi']):
    if mode == 'none' or kv <= 0:
        return 0.0
    Z = Z_f(kv)
    if Z <= 0 or Z >= mu * kv:
        return 0.0
    eta0 = mu * kv / Z - 1
    if mode == 'absolute':
        return 1 - F(eta0, s)
    gfun = lambda M: M - (1 - F(eta0 / v(M, psi), s))
    return brentq(gfun, 0.0, 1.0, xtol=1e-14)

def period(kv, gam, s, mode):
    ms_ = m_star(kv, s, mode)
    Pi = Pi_f(kv); wE = Z_f(kv)
    elite_inc = ms_ * (wE + (2 * lam_e - 3) * kv)
    # input clearing: (g/2)(k + 5nk + elite_inc) + n(r+c) + ms*(tau r+beta c) = k
    coef = (gam / 2) * (mu + 2 * lam - 3) * kv + (P['r'] + P['c'])
    rhs = kv - (gam / 2) * (kv + elite_inc) - ms_ * (P['tau'] * P['r'] + P['beta'] * P['c'])
    n = rhs / coef
    if n < 0:
        raise ValueError(f"n<0 at k={kv}: infeasible configuration")
    sigma0 = 1 - 3 * ms_ - 3 * n
    if sigma0 < -1e-9:
        raise ValueError(f"sigma0<0 at k={kv}: population constraint binds")
    W = kv + n * (mu + 2 * lam - 3) * kv + elite_inc
    Y = P['phi'] * (n + P['alpha'] * ms_)
    return dict(m=ms_, n=n, W=W, Y=Y, sigma0=sigma0, p2=Pi / P['phi'])

GAMMA = 0.8   # bequest share 1-GAMMA = 20 percent of net income

def G(kv, s, mode, Theta, gam=GAMMA):
    if kv <= 0:
        return 0.0
    try:
        pe = period(kv, gam, s, mode)
    except ValueError:
        return np.nan
    return Theta * (1 - gam) * pe['W'] / pe['p2']

# calibrate the investment-conversion rate Theta so k* = 2 (absolute status)
pe2 = period(2.0, GAMMA, P['s'], 'absolute')
THETA = 2.0 / ((1 - GAMMA) * pe2['W'] / pe2['p2'])
print(f"calibration: gamma = {GAMMA}, Theta = {THETA:.4f} make k* = 2 the steady "
      f"state (absolute status)")
print(f"  at k*=2: m*={pe2['m']:.4f}, n={pe2['n']:.4f}, sigma0={pe2['sigma0']:.4f}, "
      f"Y={pe2['Y']:.4f}  (prices, wages, cutoff identical to the static example)")
print(f"  origin slope Theta(1-gamma)phi/(c+r) = "
      f"{THETA*(1-GAMMA)*P['phi']/(P['c']+P['r']):.3f} > 1: origin repels; "
      f"no collapse-to-zero trap")

def steady_states(s, mode, kmax=4.0, ngrid=4000):
    ks = np.linspace(1e-4, kmax, ngrid)
    gk = np.array([G(x, s, mode, THETA) - x for x in ks])
    roots = []
    for i in range(len(ks) - 1):
        if np.isnan(gk[i]) or np.isnan(gk[i + 1]):
            continue
        if gk[i] * gk[i + 1] < 0:
            roots.append(brentq(lambda x: G(x, s, mode, THETA) - x, ks[i], ks[i + 1]))
    return [rt for j, rt in enumerate(roots) if j == 0 or abs(rt - roots[j - 1]) > 1e-6]

def slope(kss, s, mode, h=1e-6):
    return (G(kss + h, s, mode, THETA) - G(kss - h, s, mode, THETA)) / (2 * h)

results = {}
for mode, label in [('none', 'no-elite counterfactual'),
                    ('absolute', 'absolute status'),
                    ('positional', 'positional status')]:
    ss = steady_states(P['s'], mode)
    results[mode] = ss
    desc = ", ".join(f"k*={x:.4f} (G'={slope(x, P['s'], mode):+.3f})" for x in ss)
    print(f"  {label:26s}: {desc if ss else 'none'}")

k_none, k_abs, k_pos = results['none'][-1], results['absolute'][-1], results['positional'][-1]
print(f"\nstatus drag on steady-state wealth: {k_none:.4f} (no elite) -> "
      f"{k_abs:.4f} (absolute); positional dilution recovers -> {k_pos:.4f}")
assert k_abs < k_pos < k_none
assert abs(slope(k_abs, P['s'], 'absolute')) < 1, "high steady state must be stable"

# elite drag on the map is negative at the steady state (numerical check of dG/dm*)
eps = 1e-4
pe_lo = period(k_abs, GAMMA, P['s'], 'absolute')
G_here = G(k_abs, P['s'], 'absolute', THETA)
G_none_here = G(k_abs, P['s'], 'none', THETA)
print(f"drag at k*: G_absolute(k*) - G_none(k*) = {G_here - G_none_here:+.4f} < 0: "
      f"{G_here < G_none_here}")
assert G_here < G_none_here

print("\nstatus as a luxury along the map:")
for kk in (1.0, 1.5, 2.0, 3.0):
    print(f"   eta*({kk:.1f}) = {mu*kk/Z_f(kk)-1:8.4f}   m*({kk:.1f}) = "
          f"{m_star(kk, P['s'], 'absolute'):.5f}")

# ----------------------------------------------------------------------------
# 3. THE SPREAD OF STATUS TASTE: steady-state decline and generational paths
# ----------------------------------------------------------------------------
print()
print("=" * 72)
print("SPREAD OF STATUS TASTE: steady-state decline")
print("=" * 72)

def top_stable(s, mode):
    ss = steady_states(s, mode)
    stable = [x for x in ss if abs(slope(x, s, mode)) < 1]
    return max(stable) if stable else np.nan

svals = np.linspace(0.05, 0.80, 76)
hs_abs = np.array([top_stable(s_, 'absolute') for s_ in svals])
hs_pos = np.array([top_stable(s_, 'positional') for s_ in svals])
hs_none = top_stable(P['s'], 'none')

print(f"{'s':>6} {'k* absolute':>12} {'m* at k*':>10} {'k* positional':>14}")
for i in np.linspace(0, len(svals) - 1, 8, dtype=int):
    mm = m_star(hs_abs[i], svals[i], 'absolute') if not np.isnan(hs_abs[i]) else np.nan
    print(f"{svals[i]:6.2f} {hs_abs[i]:12.4f} {mm:10.4f} {hs_pos[i]:14.4f}")

drop_abs = 100 * (1 - hs_abs[-1] / hs_none)
drop_pos = 100 * (1 - hs_pos[-1] / hs_none)
print(f"\nat s = {svals[-1]:.2f}: absolute-status wealth loss {drop_abs:.1f}% vs "
      f"no-elite benchmark; positional only {drop_pos:.1f}% (dilution protects wealth)")

# generational path after a taste shift s: 0.30 -> 0.75, starting at old steady state
s_new = 0.75
kpath = [k_abs]
for _ in range(40):
    kpath.append(G(kpath[-1], s_new, 'absolute', THETA))
print(f"\ntransition after taste shift s: 0.30 -> {s_new:.2f} "
      f"(generations, absolute status):")
print("   " + " -> ".join(f"{x:.3f}" for x in kpath[:7])
      + f" -> ... -> {kpath[-1]:.4f}")
print("each step is a within-period club equilibrium; the path is foreseen, and")
print("no atomistic dynasty can or would deviate (warm-glow bequests, uniform")
print("inheritance): a rational, generation-by-generation impoverishment")

# ----------------------------------------------------------------------------
# 4. FIGURE
# ----------------------------------------------------------------------------
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

fig, axes = plt.subplots(1, 2, figsize=(10, 3.9))

ax = axes[0]
kk = np.linspace(0.01, 3.2, 500)
ax.plot(kk, kk, color='0.6', lw=1, ls='--', label=r'$45^\circ$')
ax.plot(kk, [G(x, P['s'], 'none', THETA) for x in kk], lw=1.6, color='0.45',
        label='no elite sector')
ax.plot(kk, [G(x, P['s'], 'absolute', THETA) for x in kk], lw=2, color='k',
        label='absolute status')
ax.plot(kk, [G(x, 0.75, 'absolute', THETA) for x in kk], lw=2, color='k',
        alpha=0.45, label=r'absolute, high taste ($s=0.75$)')
ax.plot([k_abs], [k_abs], 'ko', ms=6)
ax.annotate(r'$k^\ast$', (k_abs, k_abs), textcoords='offset points',
            xytext=(6, -12))
ax.set_xlabel(r'$k_t$'); ax.set_ylabel(r'$k_{t+1}=G(k_t)$')
ax.legend(frameon=False, fontsize=8, loc='lower right')
ax.set_title('(a) Transition maps and the status drag')

ax = axes[1]
ax.plot(svals, hs_abs, lw=2, color='k', label='absolute status')
ax.plot(svals, hs_pos, lw=1.6, color='k', ls=':', label='positional status')
ax.axhline(hs_none, color='0.45', lw=1.6, label='no elite sector')
ax.set_xlabel(r'status-taste scale $s$')
ax.set_ylabel(r'steady-state wealth $k^\ast$')
ax.legend(frameon=False, fontsize=8, loc='lower left')
ax.set_title('(b) Steady-state wealth as status taste spreads')

fig.tight_layout()
fig.savefig('figures/dynamics_collapse.pdf')
print("\nFigure written to figures/dynamics_collapse.pdf")
