# Referee Pass 2: Macro / Dynamics (Section 8, Appendix D, related framing)

*Adversarial referee simulation, 2026-07-20. Status annotations added after the repair pass: [FIXED] = repaired in commit df461f6; [OPEN] = outstanding.*

## Findings

**1. MAJOR — Proposition on the transition map proves boundedness/continuity only on the elite-free branch; the actual map is undefined at moderately high k, and the text never states the domain restriction.** [FIXED]
The k→∞ limit is machine-verified with m\* set to 0. Along the actual map, the interior configuration fails inside the paper's own example: at baseline taste the market-clearing n turns negative at k ≈ 3.1, and at s = 0.18–0.19 already at k ≈ 2.0–2.1; at k ≥ 11 every agent demands the elite path. Fix applied: proposition restated on a domain K, with a text sentence acknowledging the restriction and the corner regimes.

**2. MAJOR — Stability is asserted, not proven, and the paper's own example shows the slope going negative.** [FIXED: weakened]
A crossing from above gives ξ′ ≤ 1, not ξ′ > −1. Not hypothetical: at the post-shift steady state the slope is negative (ξ′ = −0.079 at s=0.18, −0.108 at s=0.19) — exactly why the transition path oscillates (see finding 7).

**3. MAJOR — The "no forecasting / rational societies let it happen" claim is oversold; with warm glow it is true by construction, and with uniform inheritance "no dynasty could deviate" is vacuous.** [PARTIALLY FIXED; substantive addition OPEN]
Under warm-glow preferences "no forecasting is required" is definitional — *weaker* than rational expectations, not stronger. Under pooled inheritance a parent's bequest does not reach its own child, so the atomism argument does no work. A referee will demand at least a formal remark — better, a short appendix result — with forward-looking preferences showing the drag survives. Wording repaired (the claim is now framed as recursivity, with the specification-dependence acknowledged); the dynastic/forward-looking robustness **result** remains the single most valuable addition. [OPEN]

**4. MAJOR — "Status is a luxury — by theorem, not assumption" overstates; the driver is a technological nonhomotheticity.** [FIXED]
The proof is correct, but works only because school/firm input requirements are fixed in units of the input good while outside options scale linearly in k. Elite-education costs are predominantly wages (Baumol); if the burn scaled with k the luxury property would vanish. Fixed: honest attribution to technology, with a robustness remark on cost scaling.

**5. MINOR — The θ investment technology is unowned and unpriced.** [FIXED]
One sentence added assigning it (constant-returns, freely operated, profitless) and noting the input good perishes.

**6. MINOR — Uniform inheritance: internally consistent, deferral honest, but two loose ends.** [FIXED]
(a) "Dynasty" language strained — there are no dynasties under pooling; reworded. (b) The Galor–Zeira deferral should state the sign honestly: elite parents have *lower* net income, so dynasty-specific bequests would transmit less wealth down elite lines — the status discount is dynastically self-impoverishing; the model's persistence is institutional, not dynastic. Added.

**7. MINOR — The "mild overshoot" explanation is unsubstantiated; the true mechanism is the locally negative slope of ξ.** [FIXED]
The numbers match the script, but the stated mechanism ("temporary output surge") is verified nowhere; the actual cause is ξ′ ≈ −0.08 at the new steady state (luxury feedback: higher k → larger elite → smaller net bequest), producing damped oscillation. Replaced.

**8. MINOR — Stale number in Appendix D contradicts Section 8 and the script (ξ′ = 0.31 vs 0.17).** [FIXED]

**9. MINOR — No formal definition of the dynamic equilibrium, and single-valuedness of ξ unaddressed.** [FIXED]
Definition added; selection rule (interior where viable, elite-free corner otherwise) stated; uniqueness tied to the strengthened Lemma 1.

**10. MINOR — Intertemporal welfare hedge under-cited and slightly incomplete.** [FIXED]
Diamond (1965) and Andreoni (1990) now cited; the wealth-versus-welfare distinction (a lower steady state need not be worse if the warm-glow path overaccumulates) made explicit.

**11. COSMETIC — Numerical claims all verify against the script.** [FIXED: clarifier added]
Every reported number reproduces exactly. "A fifth of the population" needed the clarifier that it counts managers plus their firms' workers. One stale script comment (taste-shift range) fixed.

## Overall assessment (as delivered, pre-repair)

The dynamics section is well above the median for internal consistency: the period-economy algebra, the one-condition unification, and every reported number are machine-verified, and the paper is commendably explicit about what it does not claim. But it would be returned for major revision on four grounds: domain restrictions unstated; stability asserted while the map's own slope goes negative; the "stronger than rational expectations" framing resting on preferences that make the claim true by construction (the paper's most quotable sentence is its least earned — a forward-looking robustness result is the single most valuable addition); and the "luxury by theorem" slogan relocating rather than removing the assumption. None fatal; all findable by a careful macro referee on a first read, because the companion code already exposes each of them.
