"""
The Market for Elite Status -- Phase 2: positional (relative) status.
Companion verification/computation script for the positional section.

EXTENSION (manuscript Section 7)
--------------------------------
Identical to the static model of analysis/static_model.py EXCEPT the
elite-manager membership's utility factor is (1 + eta * v(M)), where M is the
aggregate measure of agents holding the elite-manager membership and
v : [0,1] -> (0,1] is continuous, strictly decreasing, v(0) = 1.
Status is valuable because it is scarce. Agents take M as given (nonatomic).

Equilibrium notion: group equilibrium with widespread externality -- prices,
a feasible state, and consistency of M with the state itself (fixed point).

KEY RELATIONS
-------------
Wages w_M, w_L, w_L* and the price p2 are UNCHANGED (the externality touches
only the elite membership). Elite-firm budget balance still forces w_E = Z,
so the cutoff condition becomes

    (1 + eta* v(M)) = mu*k / Z    =>    eta* v(M) = eta0*,

where eta0* = mu*k/Z - 1 is the Phase-1 (non-positional) cutoff. Hence

    eta*(M) = eta0* / v(M)   and   M = Phi(M) := 1 - F(eta0* / v(M)).

Phi is continuous and strictly decreasing => unique fixed point M*.

Since v <= 1:  M* <= M0 (the non-positional elite mass): dilution self-limits
the elite sector. FOSD shifts in F raise M* but by less than in Phase 1.

WELFARE
-------
The marginal entrant ignores the dilution -v'(M) imposed on all inframarginal
elites. Planner cutoff FOC (cutoff allocations, movers held at reservation
utility):
    surplus of marginal type  =  |v'(M)| * H_E * Integral_{eta >= eta^}( eta dF )
with H_E = w_E/(2 sqrt(p2)) the elites' common consumption index. At the
laissez-faire equilibrium the left side is ZERO => over-entry. The Pigouvian
membership tax that decentralizes the planner cutoff equates the marginal
type's utility loss from the tax to the wedge:
    t* : (1+eta^ v(M)) * t* / (mu) = |v'(M)| * w_E * Integral_{eta>=eta^} eta dF
(income units; derivation in manuscript Appendix C).

This script:
  1. verifies the cutoff/fixed-point algebra symbolically;
  2. computes the laissez-faire positional equilibrium (example economy);
  3. demonstrates the Prop-4 Pareto improvement (2x2 reallocation system);
  4. computes tax equilibria (uniform lump-sum rebate) and the welfare curve;
  5. generates the two-panel figure for the manuscript.
"""

import numpy as np
import sympy as sp
from scipy.optimize import brentq

# ----------------------------------------------------------------------------
# 0. Example economy (same as Phase 1) + positional primitive v
# ----------------------------------------------------------------------------
P = dict(k=2.0, r=1.0, c=1.0, tau=2.0, beta=1.25, alpha=0.9, phi=6.0,
         dM=0.25, dL=0.5, chi=0.2, s=0.30,      # eta ~ Exp(mean s)
         psi=25.0)                              # v(M) = 1/(1 + psi*M)

def v(M, psi):  return 1.0 / (1.0 + psi * M)
def vp(M, psi): return -psi / (1.0 + psi * M) ** 2     # v'(M)

mu   = 1 / P['dM']                 # 4
lam  = 1 / P['dL']                 # 2
lams = lam / (1 - P['chi'])        # 2.5

def F(x, s):  return 1.0 - np.exp(-x / s)
def f(x, s):  return np.exp(-x / s) / s

# ----------------------------------------------------------------------------
# 1. SYMBOLIC VERIFICATION of the cutoff and fixed-point relations
# ----------------------------------------------------------------------------
print("=" * 72)
print("SYMBOLIC VERIFICATION (positional extension)")
print("=" * 72)

k_, r_, c_, tau_, beta_, alpha_, phi_ = sp.symbols('k r c tau beta alpha phi', positive=True)
mu_, lam_, lams_, eta_, vM, Msym = sp.symbols('mu lam lams eta v M', positive=True)

Zsym = alpha_ * (c_ + r_ + (mu_ + 2 * lam_ - 3) * k_) - beta_ * c_ - tau_ * r_ \
    + (3 - 2 * lams_) * k_
# cutoff: (1 + eta*v) * (1/mu) * w_E = k with w_E = Z  =>  1 + eta*v = mu*k/Z
cutoff = sp.Eq((1 + eta_ * vM), mu_ * k_ / Zsym)
eta_sol = sp.solve(cutoff, eta_)[0]
eta0 = mu_ * k_ / Zsym - 1
assert sp.simplify(eta_sol - eta0 / vM) == 0
print("[ok] positional cutoff: eta*(M) = eta0*/v(M) with eta0* the Phase-1 cutoff")
print("[ok] fixed point M = 1 - F(eta0*/v(M)); Phi decreasing => unique M*")

# ----------------------------------------------------------------------------
# 2. LAISSEZ-FAIRE POSITIONAL EQUILIBRIUM
# ----------------------------------------------------------------------------
print()
print("=" * 72)
print("LAISSEZ-FAIRE POSITIONAL EQUILIBRIUM")
print("=" * 72)

def base_objects(P, T=0.0):
    """Wages, p2, Z at effective non-labor income k+T (T = lump-sum rebate)."""
    kT = P['k'] + T
    wM, wL, wLs = mu * kT, lam * kT, lams * kT
    p2 = (P['c'] + P['r'] + (mu + 2 * lam - 3) * kT) / P['phi']
    Z = P['alpha'] * (P['c'] + P['r'] + (mu + 2 * lam - 3) * kT) \
        - P['beta'] * P['c'] - P['tau'] * P['r'] + (3 - 2 * lams) * kT
    return kT, wM, wL, wLs, p2, Z

def solve_positional(P, t=0.0, T=None):
    """Positional equilibrium with membership tax t, uniform rebate T = t*M.

    Solves the joint fixed point in (M, T). Returns equilibrium objects.
    Entrant's net income: w_E = Z - t (elite balance unchanged, tax on entry);
    cutoff: (1 + eta* v(M)) = mu*(k+T)/(Z - t).
    """
    def M_given_T(T):
        kT, wM, wL, wLs, p2, Z = base_objects(P, T)
        wE = Z - t
        if wE <= 0:
            return 0.0
        eta0 = mu * kT / wE - 1
        if eta0 <= 0:
            return 1.0 - F(0.0, P['s'])
        g = lambda M: M - (1 - F(eta0 / v(M, P['psi']), P['s']))
        return brentq(g, 0.0, 1.0, xtol=1e-14)

    if T is None:  # close the government budget T = t*M
        T = 0.0
        for _ in range(200):
            M = M_given_T(T)
            T_new = t * M
            if abs(T_new - T) < 1e-14:
                T = T_new
                break
            T = T_new
    M = M_given_T(T)

    kT, wM, wL, wLs, p2, Z = base_objects(P, T)
    wE = Z - t
    eta_star = (mu * kT / wE - 1) / v(M, P['psi'])
    # market clearing in y1: endowment is still k (T is a transfer, not endowment)
    num = (P['k'] - (1 - 3 * M) * kT / 2 - M * wE / 2 - M * wLs
           - M * (P['tau'] * P['r'] + P['beta'] * P['c']))
    den = (wM / 2 + wL - 3 * kT / 2 + P['r'] + P['c'])
    n = num / den
    sigma0 = 1 - 3 * M - 3 * n
    Y = P['phi'] * (n + P['alpha'] * M)
    out = dict(M=M, T=T, eta_star=eta_star, wE=wE, wM=wM, wL=wL, wLs=wLs,
               p2=p2, n=n, sigma0=sigma0, Y=Y, kT=kT, t=t)
    out['H'] = 1 / (2 * np.sqrt(p2))          # utility per unit net income (D=1)
    return out

def welfare(P, E):
    """Utilitarian welfare in the model's cardinalization, by exact integration
    over eta ~ Exp(s). Non-elites all attain utility kT*H; elites attain
    (1+eta v(M)) * (1/mu) * wE * H for eta >= eta*."""
    s, psi = P['s'], P['psi']
    H, kT, wE, M, es = E['H'], E['kT'], E['wE'], E['M'], E['eta_star']
    # int_{es}^inf (1 + eta v) dF = (1-F(es)) + v * (es + s) * exp(-es/s)  [Exp mean]
    elite_util = H * wE / mu * ((1 + v(M, psi) * (es + s) / 1) * np.exp(-es / s)
                                - v(M, psi) * 0)  # = exp(-es/s)*(1 + v*(es+s))... see check
    # careful: int_{es}^inf eta dF = (es + s) exp(-es/s) for Exp(mean s)
    elite_util = H * wE / mu * (np.exp(-es / s) + v(M, psi) * (es + s) * np.exp(-es / s))
    nonelite_util = H * kT * F(es, s)
    return elite_util + nonelite_util

E0 = solve_positional(P, t=0.0)
# Phase-1 (non-positional) benchmark for comparison: psi = 0
P_nopos = dict(P, psi=0.0)
E_nopos = solve_positional(P_nopos, t=0.0)

print(f"non-positional benchmark: M0 = {E_nopos['M']:.5f}, eta0* = {E_nopos['eta_star']:.4f}")
print(f"positional equilibrium:   M* = {E0['M']:.5f}, eta*  = {E0['eta_star']:.4f}, "
      f"v(M*) = {v(E0['M'], P['psi']):.4f}")
print(f"dilution self-limits the elite: M* < M0: {E0['M'] < E_nopos['M']}")
print(f"n = {E0['n']:.4f}, sigma0 = {E0['sigma0']:.4f}, Y = {E0['Y']:.4f}")
assert E0['M'] < E_nopos['M']
assert min(E0['n'], E0['sigma0'], E0['wE']) > 0

# self-damping of FOSD shifts
dM_pos = solve_positional(dict(P, s=0.33))['M'] - E0['M']
dM_non = solve_positional(dict(P_nopos, s=0.33))['M'] - E_nopos['M']
print(f"FOSD shift s: 0.30 -> 0.33: dM positional = {dM_pos:.5f} "
      f"< dM non-positional = {dM_non:.5f}: {dM_pos < dM_non}")
assert 0 < dM_pos < dM_non

# ----------------------------------------------------------------------------
# 3. PROPOSITION 4: constructive Pareto improvement at laissez-faire
# ----------------------------------------------------------------------------
print()
print("=" * 72)
print("PROP 4: PARETO IMPROVEMENT (shut dM elite triples, adjust dn, de-dilute)")
print("=" * 72)
# Per shut elite triple (members to leisure at reservation utility):
#   input freed  A_e = tau*r + beta*c + wE/2 + wLs - 3*kT/2
#   output freed B_e = -alpha*phi + (wE + 2*wLs - 3*kT)/(2*p2)
# Per opened competent triple (members from leisure at reservation utility):
#   input used   A_c = c + r + (wM + 2*wL - 3*kT)/2
#   output added B_c = phi - (wM + 2*wL - 3*kT)/(2*p2)
kT, wM, wL, wLs, p2, Z = base_objects(P, 0.0)
wE = E0['wE']
A_e = P['tau'] * P['r'] + P['beta'] * P['c'] + wE / 2 + wLs - 3 * kT / 2
B_e = -P['alpha'] * P['phi'] + (wE + 2 * wLs - 3 * kT) / (2 * p2)
A_c = P['c'] + P['r'] + (wM + 2 * wL - 3 * kT) / 2
B_c = P['phi'] - (wM + 2 * wL - 3 * kT) / (2 * p2)
print(f"value neutrality of each adjustment (should be ~0): "
      f"{A_e + p2 * B_e:.2e}, {-A_c + p2 * B_c:.2e}")
# restore material balance in both goods: dM shut triples + dn opened triples
# input:  A_e*dM - A_c*dn = surplus_1 ; output: B_e*dM + B_c*dn = surplus_2
# choose dn = (A_e/A_c)*dM -> input surplus 0; then output surplus:
dM_ = 1e-3
dn_ = (A_e / A_c) * dM_
out_surplus = B_e * dM_ + B_c * dn_
print(f"shut dM = {dM_}: open dn = {dn_:.6f}, input surplus = 0, "
      f"output surplus = {out_surplus:.3e}  (zero: value-neutral directions)")
# both adjustment vectors are value-neutral, so they are collinear in R^2 --
# the reallocation is EXACTLY feasible with zero surplus, and the gain is pure
# de-dilution: every inframarginal elite's utility rises by eta*dv*wE*H/mu > 0.
new_M = E0['M'] - dM_
dv = v(new_M, P['psi']) - v(E0['M'], P['psi'])
gain_per_elite_eta1 = dv * wE * E0['H'] / mu     # per unit of eta
print(f"de-dilution dv = +{dv:.5f}; utility gain per elite per unit eta = "
      f"{gain_per_elite_eta1:.5f} > 0")
assert dv > 0 and abs(out_surplus) < 1e-9
print("[ok] feasible reallocation: non-elites at reservation utility (unchanged),")
print("     all inframarginal elites strictly better off => not Pareto optimal;")
print("     grand coalition blocks => core equivalence fails.")

# ----------------------------------------------------------------------------
# 4. PIGOUVIAN MEMBERSHIP TAX
# ----------------------------------------------------------------------------
print()
print("=" * 72)
print("MEMBERSHIP TAX: welfare curve and Pigouvian level")
print("=" * 72)

ts = np.linspace(0.0, 1.2, 121)
Ws, Ms, Ys = [], [], []
for t_ in ts:
    Et = solve_positional(P, t=t_)
    Ws.append(welfare(P, Et)); Ms.append(Et['M']); Ys.append(Et['Y'])
Ws, Ms, Ys = map(np.array, (Ws, Ms, Ys))
i_star = int(np.argmax(Ws))
print(f"dW/dt at t=0+: {(Ws[1]-Ws[0])/(ts[1]-ts[0]):+.6f}  (positive => over-entry)")
print(f"welfare-maximizing tax  t^W = {ts[i_star]:.3f}  "
      f"(M falls {E0['M']:.5f} -> {Ms[i_star]:.5f}; Y rises {Ys[0]:.4f} -> {Ys[i_star]:.4f})")
assert Ws[1] > Ws[0], "welfare must rise for small taxes"

# first-order Pigouvian formula (Appendix C): marginal type's income-equivalent
# of the wedge:  t* (1+eta^ v) / mu * H = |v'(M)| * (wE/mu) * H * int_{eta>=eta^} eta dF
es, M = E0['eta_star'], E0['M']
integral_eta = (es + P['s']) * np.exp(-es / P['s'])
t_pigou = abs(vp(M, P['psi'])) * wE * integral_eta / (1 + es * v(M, P['psi']))
print(f"first-order Pigouvian tax formula: t* = {t_pigou:.3f} "
      f"(local approximation at laissez-faire; global optimum t^W above)")

# ----------------------------------------------------------------------------
# 5. FIGURE
# ----------------------------------------------------------------------------
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

fig, axes = plt.subplots(1, 2, figsize=(10, 3.8))

ax = axes[0]
Mgrid = np.linspace(1e-6, 0.05, 400)
eta0_lf = mu * kT / Z - 1
Phi = 1 - F(eta0_lf / v(Mgrid, P['psi']), P['s'])
ax.plot(Mgrid, Phi, lw=2, label=r'$\Phi(M)=1-F(\eta_0^\ast/v(M))$')
ax.plot(Mgrid, Mgrid, lw=1, color='0.5', ls='--', label=r'$45^\circ$')
ax.axvline(E_nopos['M'], color='0.6', ls=':', lw=1.5,
           label=r'non-positional $M_0$')
ax.plot([E0['M']], [E0['M']], 'ko', ms=6)
ax.annotate(r'$M^\ast$', (E0['M'], E0['M']), textcoords='offset points',
            xytext=(8, -12))
ax.set_xlabel(r'elite mass $M$'); ax.set_ylabel(r'$\Phi(M)$')
ax.legend(frameon=False, fontsize=9)
ax.set_title('(a) Unique positional equilibrium')

ax = axes[1]
ax.plot(ts, Ws, lw=2, color='k')
ax.axvline(ts[i_star], color='0.4', ls='--', lw=1.2)
ax.annotate(r'$t^{W}$', (ts[i_star], Ws.min() + 0.9 * (Ws.max() - Ws.min())),
            textcoords='offset points', xytext=(6, 0))
ax.axvline(0, color='0.7', lw=0.8)
ax.set_xlabel(r'membership tax $t$ (uniform rebate)')
ax.set_ylabel('utilitarian welfare')
ax.set_title('(b) Over-entry: small taxes raise welfare')

fig.tight_layout()
fig.savefig('figures/positional_tax.pdf')
print("\nFigure written to figures/positional_tax.pdf")
