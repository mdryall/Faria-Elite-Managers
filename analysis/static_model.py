"""
The Market for Elite Status -- static clubs model with heterogeneous status taste.
Companion verification/computation script for the static section of the paper.

MODEL (see manuscript Section 3)
--------------------------------
Continuum of agents, measure 1. Two private goods: y1 (input, numeraire) and
y2 (consumption output, price p2). Endowment e = (k, 0).

Agents differ only in status taste eta ~ F on [0, inf). Utility over a private
goods bundle y and membership list L:

    u(y, L) = D(L; eta) * h(y1, y2),      h = sqrt(y1*y2)

    D = 1                     leisure (no memberships)
    D = dM * (1 + eta)        elite manager   (elite school m2 + slot m41)
    D = dM                    competent manager (serious school m1 + slot m31)
    D = dL                    laborer, competent firm (m32)
    D = dL * (1 - chi)        laborer, elite firm (m42)

with 0 < dM, dL < 1 (disutility of school/work) and chi in [0,1) (distaste for
working under elite management). Status utility attaches to the elite-manager
membership m41 only.

Group types:
    serious school  (S; s)  y = (-r, 0)
    elite school    (S; s*) y = (-tau*r, 0),  tau >= 1
    competent firm  (M, 2L; f)  y = (-c, phi)
    elite firm      (EM, 2L; f*) y = (-beta*c, alpha*phi),  beta >= 1, alpha > 0

Since h is homothetic, an agent with net income w spends w/2 on each good and
attains indirect utility D * w / (2*sqrt(p2)). All occupational-indifference
conditions are therefore independent of p2.

EQUILIBRIUM (derived in manuscript / verified below)
----------------------------------------------------
mu = 1/dM, lam = 1/dL, lam* = lam/(1-chi).
Net incomes:  w_M = mu*k,  w_L = lam*k,  w_L* = lam**k;
marginal elite manager eta*:  w_E = mu*k/(1+eta*).
Prices:  q1 = r, q2 = tau*r, q31 = k - r - w_M, q32 = k - w_L,
         q41 = k - tau*r - w_E, q42 = k - w_L*.
Competent-firm zero profit:  p2*phi = c + r + (mu + 2*lam - 3)*k
Elite-firm zero profit pins eta*:
    mu*k/(1+eta*) = Z := alpha*[c + r + (mu+2*lam-3)*k] - beta*c - tau*r + (3 - 2*lam*)*k
Interior elite sector requires 0 < Z < mu*k; then eta* = mu*k/Z - 1 and the
measure of elite managers is m* = 1 - F(eta*).
Market clearing in y1 pins the measure n of competent firms.

PROPOSITION 1 (coexistence of strictly less productive elite firms):
alpha < 1 with an active elite sector iff
    (w_M - w_E) > 2*(w_L* - w_L) + (beta-1)*c + (tau-1)*r
evaluated at the equilibrium eta* -- the marginal manager's status discount
must exceed the laborers' compensating differential plus the resource burn.
"""

import sympy as sp
import numpy as np

# ----------------------------------------------------------------------------
# 1. SYMBOLIC VERIFICATION
# ----------------------------------------------------------------------------
print("=" * 72)
print("SYMBOLIC VERIFICATION")
print("=" * 72)

k, r, c, tau, beta, alpha, phi, p2 = sp.symbols(
    'k r c tau beta alpha phi p2', positive=True)
mu, lam, lams, eta = sp.symbols('mu lambda lambda_s eta_star', positive=True)
mstar, n = sp.symbols('m_star n', nonnegative=True)

wM, wL, wLs = mu * k, lam * k, lams * k
wE = mu * k / (1 + eta)

q1, q2 = r, tau * r
q31 = k - r - wM
q32 = k - wL
q41 = k - tau * r - wE
q42 = k - wLs

# (a) Occupational indifference / cutoff conditions (common 1/(2 sqrt p2) dropped)
assert sp.simplify(sp.Rational(1, 1) / mu * wM - k) == 0          # dM*wM = k
assert sp.simplify(sp.Rational(1, 1) / lam * wL - k) == 0         # dL*wL = k
assert sp.simplify((1 + eta) / mu * wE - k) == 0                  # marginal elite mgr
print("[ok] occupational indifference and elite-manager cutoff conditions")

# (b) Budget balance -> p2 and the eta* equation
p2_sol = sp.solve(sp.Eq(q31 + 2 * q32 - c + p2 * phi, 0), p2)[0]
p2_expected = (c + r + (mu + 2 * lam - 3) * k) / phi
assert sp.simplify(p2_sol - p2_expected) == 0
print("[ok] competent-firm zero profit: p2*phi = c + r + (mu+2*lam-3)k")

elite_balance = q41 + 2 * q42 - beta * c + p2_sol * alpha * phi
Z = alpha * (c + r + (mu + 2 * lam - 3) * k) - beta * c - tau * r + (3 - 2 * lams) * k
assert sp.simplify(elite_balance - (Z - mu * k / (1 + eta))) == 0
print("[ok] elite-firm zero profit  <=>  mu*k/(1+eta*) = Z")

# (c) Proposition 1: alpha < 1  <=>  status discount > hate premium + waste
status_discount = wM - wE
hate_premium = 2 * (wLs - wL)
waste = (beta - 1) * c + (tau - 1) * r
p2phi_comp = c + r + (mu + 2 * lam - 3) * k
p2phi_elite = beta * c + tau * r + (mu / (1 + eta) + 2 * lams - 3) * k
gap = sp.simplify((p2phi_comp - p2phi_elite) - (status_discount - hate_premium - waste))
assert gap == 0
print("[ok] Proposition 1: alpha<1 iff (wM-wE) > 2(wL*-wL) + (beta-1)c + (tau-1)r")

# (d) Market clearing in y1 and Walras check for y2
sigma0 = 1 - 3 * mstar - 3 * n
demand_y1 = (sigma0 * k / 2 + mstar * wE / 2 + 2 * mstar * wLs / 2
             + n * wM / 2 + 2 * n * wL / 2
             + mstar * (tau * r + beta * c) + n * (r + c))
n_sol = sp.solve(sp.Eq(demand_y1, k), n)[0]
n_sol = sp.simplify(n_sol)
print("[ok] market clearing solves for n:")
print("     n =", n_sol)

demand_y2 = (sigma0 * k / 2 + mstar * wE / 2 + 2 * mstar * wLs / 2
             + n * wM / 2 + 2 * n * wL / 2) / p2_sol
supply_y2 = phi * (n + alpha * mstar)
walras = sp.simplify((demand_y2 - supply_y2).subs(n, n_sol).subs(
    eta, sp.solve(sp.Eq(mu * k / (1 + eta), Z), eta)[0]))
assert walras == 0
print("[ok] Walras: y2 market clears given y1 clearing and budget balance")

# ----------------------------------------------------------------------------
# 2. NUMERICAL EXAMPLE (manuscript Section 5)
# ----------------------------------------------------------------------------
print()
print("=" * 72)
print("NUMERICAL EXAMPLE")
print("=" * 72)

P = dict(k=2.0, r=1.0, c=1.0, tau=2.0, beta=1.25, alpha=0.9, phi=6.0,
         dM=0.25, dL=0.5, chi=0.2, s=0.30)   # eta ~ Exp(mean s)

def solve_equilibrium(P):
    k_, r_, c_, tau_, beta_, alpha_, phi_ = (P[x] for x in
                                             ('k', 'r', 'c', 'tau', 'beta', 'alpha', 'phi'))
    mu_ = 1 / P['dM']; lam_ = 1 / P['dL']; lams_ = lam_ / (1 - P['chi'])
    out = {}
    out['p2'] = (c_ + r_ + (mu_ + 2 * lam_ - 3) * k_) / phi_
    Z_ = alpha_ * (c_ + r_ + (mu_ + 2 * lam_ - 3) * k_) - beta_ * c_ - tau_ * r_ \
        + (3 - 2 * lams_) * k_
    if not (0 < Z_ < mu_ * k_):
        raise ValueError(f"no interior elite sector: Z={Z_:.4f} not in (0, {mu_*k_:.4f})")
    out['eta_star'] = mu_ * k_ / Z_ - 1
    out['m_star'] = np.exp(-out['eta_star'] / P['s'])          # 1 - F for Exp(mean s)
    wE_ = mu_ * k_ / (1 + out['eta_star'])
    wM_, wL_, wLs_ = mu_ * k_, lam_ * k_, lams_ * k_
    out.update(wE=wE_, wM=wM_, wL=wL_, wLs=wLs_)
    out['q'] = dict(q1=r_, q2=tau_ * r_, q31=k_ - r_ - wM_, q32=k_ - wL_,
                    q41=k_ - tau_ * r_ - wE_, q42=k_ - wLs_)
    ms = out['m_star']
    num = (k_ - (1 - 3 * ms) * k_ / 2 - ms * wE_ / 2 - ms * wLs_
           - ms * (tau_ * r_ + beta_ * c_))
    den = (wM_ / 2 + wL_ - 3 * k_ / 2 + r_ + c_)
    out['n'] = num / den
    out['sigma0'] = 1 - 3 * ms - 3 * out['n']
    out['output'] = phi_ * (out['n'] + alpha_ * ms)
    out['input_burn'] = ms * ((beta_ - 1) * c_ + (tau_ - 1) * r_)
    # feasibility checks
    checks = {'p2>0': out['p2'] > 0, 'n>=0': out['n'] >= -1e-12,
              'sigma0>=0': out['sigma0'] >= -1e-12, 'wE>0': wE_ > 0,
              'Prop1 (alpha<1 coexistence)':
                  (wM_ - wE_) > 2 * (wLs_ - wL_) + (beta_ - 1) * c_ + (tau_ - 1) * r_}
    out['checks'] = checks
    return out

E = solve_equilibrium(P)
print(f"parameters: {P}")
print(f"p2      = {E['p2']:.4f}")
print(f"eta*    = {E['eta_star']:.4f}")
print(f"m*      = {E['m_star']:.4f}   (elite managers; elite sector pop = {3*E['m_star']:.4f})")
print(f"n       = {E['n']:.4f}   (competent firms; competent sector pop = {3*E['n']:.4f})")
print(f"sigma0  = {E['sigma0']:.4f}   (leisure share)")
print(f"net incomes: wE={E['wE']:.3f}  wM={E['wM']:.3f}  wL={E['wL']:.3f}  wL*={E['wLs']:.3f}")
print(f"membership prices: {({kk: round(v, 3) for kk, v in E['q'].items()})}")
print(f"aggregate output Y = {E['output']:.4f};  resources burned = {E['input_burn']:.4f}")
for name, ok in E['checks'].items():
    print(f"  check {name}: {'PASS' if ok else 'FAIL'}")
assert all(E['checks'].values())

# ----------------------------------------------------------------------------
# 3. COMPARATIVE STATICS: spread of status taste (FOSD shift, s up)
# ----------------------------------------------------------------------------
print()
print("=" * 72)
print("COMPARATIVE STATICS: status-taste scale s (eta ~ Exp(mean s))")
print("=" * 72)
print("Note eta* is price-determined and independent of F; m* = exp(-eta*/s).")

svals = np.linspace(0.05, 0.60, 200)
rows = []
for s_ in svals:
    Ps = dict(P, s=s_)
    try:
        Es = solve_equilibrium(Ps)
        rows.append((s_, Es['m_star'], Es['n'], Es['sigma0'], Es['output'],
                     Es['input_burn']))
    except ValueError:
        continue
rows = np.array(rows)
print(f"{'s':>6} {'m*':>8} {'n':>8} {'sigma0':>8} {'output':>8} {'burn':>8}")
for i in np.linspace(0, len(rows) - 1, 8, dtype=int):
    print(f"{rows[i,0]:6.2f} {rows[i,1]:8.4f} {rows[i,2]:8.4f} "
          f"{rows[i,3]:8.4f} {rows[i,4]:8.4f} {rows[i,5]:8.4f}")
dY = np.diff(rows[:, 4])
print(f"\nOutput monotonically decreasing in s: {bool(np.all(dY < 1e-12))}")

# Proposition 2 check: dY/dm* < 0  <=>  alpha*(c+r) < beta*c + tau*r
lhs = P['alpha'] * (P['c'] + P['r'])
rhs = P['beta'] * P['c'] + P['tau'] * P['r']
print(f"Proposition 2 condition: alpha*(c+r) = {lhs:.3f} < beta*c+tau*r = {rhs:.3f}: "
      f"{lhs < rhs}")

# ----------------------------------------------------------------------------
# 4. FIGURE
# ----------------------------------------------------------------------------
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

fig, axes = plt.subplots(1, 2, figsize=(10, 3.8))
ax = axes[0]
ax.plot(rows[:, 0], 3 * rows[:, 1], lw=2, label=r'elite sector $3m^\ast$')
ax.plot(rows[:, 0], 3 * rows[:, 2], lw=2, ls='--', label=r'competent sector $3n$')
ax.set_xlabel(r'status-taste scale $s$')
ax.set_ylabel('population share')
ax.legend(frameon=False)
ax.set_title('(a) Sorting')

ax = axes[1]
ax.plot(rows[:, 0], rows[:, 4], lw=2, color='k', label=r'output $Y$')
ax2 = ax.twinx()
ax2.plot(rows[:, 0], rows[:, 5], lw=1.5, color='0.5', ls=':', label='resources burned')
ax.set_xlabel(r'status-taste scale $s$')
ax.set_ylabel(r'aggregate output $Y$')
ax2.set_ylabel('resources burned')
h1, l1 = ax.get_legend_handles_labels(); h2, l2 = ax2.get_legend_handles_labels()
ax.legend(h1 + h2, l1 + l2, frameon=False, loc='center left')
ax.set_title('(b) Efficient decline of measured output')

fig.tight_layout()
fig.savefig('figures/status_taste_comparative_statics.pdf')
print("\nFigure written to figures/status_taste_comparative_statics.pdf")
