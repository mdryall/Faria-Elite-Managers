"""Machine checks for THEOREM-MEMO.md (displacement boundary).

Check 1 (openness, Theorem part (ii)): the running example satisfies
Assumption 1 and strict resource dominance with strict inequalities, and
these persist under parameter perturbations -- one-at-a-time grid (+/-3%,
with per-parameter margins up to +/-10% documented) and a random joint
sweep (+/-1.5%).

Check 2 (aggregate-saving identity, part (i')): for a membership-equivalent
cheaper elite school appended to G, the aggregate saving from full-list
substitution, integral of q.l - q.l[g->g'] over agents, equals
nu(g) * p.(y'-y) > 0 across the openness sweep -- the Step-3 identity of the
pricing proof.  Arithmetic identity check only: (i') is a proof, not a
computation.

Closed forms follow the manuscript (eqs. (4)-(9), (A.1)); exponential taste
distribution F(eta) = 1 - exp(-eta/s).
"""

import math
import random

BASE = dict(k=2.0, r=1.0, c=1.0, tau=4.0, beta=1.25, alpha=1.25,
            phi=6.0, mu=4.0, lam=2.0, lam_e=2.5, s=0.1)


def equilibrium(p):
    k, r, c = p['k'], p['r'], p['c']
    tau, beta, alpha = p['tau'], p['beta'], p['alpha']
    phi, mu, lam, lam_e, s = p['phi'], p['mu'], p['lam'], p['lam_e'], p['s']

    p2phi = c + r + (mu + 2 * lam - 3) * k                     # eq (7)
    z = alpha * p2phi - beta * c - tau * r + (3 - 2 * lam_e) * k  # eq (8)
    if not (0 < z < mu * k):
        return None
    eta_star = mu * k / z - 1                                   # eq (9)
    m_star = math.exp(-eta_star / s)                            # 1 - F(eta*)
    w_E, w_M, w_L, w_Le = z, mu * k, lam * k, lam_e * k
    num = k - (1 - 3 * m_star) * k / 2 \
        - m_star * (w_E / 2 + w_Le + tau * r + beta * c)        # eq (A.1)
    den = w_M / 2 + w_L - 3 * k / 2 + r + c
    n = num / den
    sigma0 = 1 - 3 * m_star - 3 * n
    return dict(z=z, eta_star=eta_star, m_star=m_star, n=n, sigma0=sigma0,
                p2phi=p2phi)


def interior_and_dominated(p):
    """Assumption 1 (strict) + strict resource dominance, eq (12)."""
    eq = equilibrium(p)
    if eq is None:
        return False
    dominance = p['alpha'] * (p['c'] + p['r']) < p['beta'] * p['c'] + p['tau'] * p['r']
    return (eq['n'] > 0 and eq['sigma0'] > 0 and eq['m_star'] < 1
            and dominance)


# --- Check 1: the example, then openness ------------------------------------
eq0 = equilibrium(BASE)
assert abs(eq0['z'] - 5.75) < 1e-12
assert abs(eq0['eta_star'] - 9 / 23) < 1e-12
assert abs(eq0['m_star'] - 0.019984) < 1e-4
assert abs(eq0['n'] - 0.11396) < 1e-4
assert abs(eq0['sigma0'] - 0.59810) < 1e-4
assert interior_and_dominated(BASE)

# one-at-a-time +/-3% (all pass; margins differ by parameter, see below)
for name in BASE:
    for f in (0.97, 1.03):
        pert = dict(BASE)
        pert[name] = BASE[name] * f
        assert interior_and_dominated(pert), (name, f)

# random joint sweep +/-1.5% (at +/-2%, 4/20000 corner combinations break
# interiority: the open neighborhood is genuinely small when several
# parameters move jointly against n>0)
random.seed(20260721)
fails = 0
for _ in range(20000):
    pert = {name: v * random.uniform(0.985, 1.015) for name, v in BASE.items()}
    if not interior_and_dominated(pert):
        fails += 1
assert fails == 0, fails

# document per-parameter symmetric margins (largest of 1..10% that passes):
# the neighborhood is open but NOT large in every direction -- raising alpha
# (or lowering lam_e) pushes z toward mu*k, and with s=0.1 the exponential
# tail makes the elite mass explode, breaking interiority (n>0) well before
# dominance fails.  Honest scope for the memo's openness claim.
margins = {}
for name in BASE:
    best = 0
    for pct in range(1, 11):
        ok = all(interior_and_dominated({**BASE, name: BASE[name] * f})
                 for f in (1 - pct / 100, 1 + pct / 100))
        if ok:
            best = pct
        else:
            break
    margins[name] = best
print("Check 1 (openness): example verified; +/-3% grid and 20000 joint "
      "+/-1.5% perturbations all satisfy Assumption 1 (strict) + strict "
      "dominance.")
print("  per-parameter symmetric margins (%):",
      {k: v for k, v in sorted(margins.items())})
assert all(v >= 3 for v in margins.values())

# --- Check 2: aggregate-saving identity for an equivalent cheaper school ----
# Entrant school g2' with cost tau' r < tau r, membership-equivalent to g2
# ((E1): confers omega_e; (E2): same delta_s).  Budget balance (condition 1,
# all types in G) prices seats at q2 = tau r, q2' = tau' r; p = (1, p2) with
# the input good as numeraire and y' - y = (tau r - tau' r, 0).
# Elite managers (mass nu(g2) = m*) each hold list {m2, m41}; substitution
# swaps m2 -> m2' only, so per-agent saving = q2 - q2'.  Step-3 identity:
#   integral of saving = m* (q2 - q2') = nu(g2) * p.(y'-y) > 0.
random.seed(20260722)
for _ in range(2000):
    pert = {name: v * random.uniform(0.985, 1.015) for name, v in BASE.items()}
    eq = equilibrium(pert)
    assert eq is not None
    for frac in (0.25, 0.5, 0.975):
        tau_p = pert['tau'] * frac
        q2, q2p = pert['tau'] * pert['r'], tau_p * pert['r']
        agg_saving = eq['m_star'] * (q2 - q2p)
        p_dot_dy = eq['m_star'] * ((pert['tau'] - tau_p) * pert['r'])  # p1=1
        assert agg_saving > 0
        assert abs(agg_saving - p_dot_dy) < 1e-12
print("Check 2 (aggregate-saving identity): integral of per-agent saving = "
      "nu(g2) * p.(y'-y) > 0 across 2000 sweep points x 3 entrant costs.")

print("ALL CHECKS PASS")
