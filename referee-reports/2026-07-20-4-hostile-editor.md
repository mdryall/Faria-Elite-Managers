# Referee Pass 4: Hostile Editor (full read; numbers audited against scripts)

*Adversarial editor simulation, 2026-07-20. Status annotations added after the repair pass: [FIXED] = repaired in commit df461f6; [DECIDED: keep] = author decision; [OPEN] = outstanding.*

**Verification summary:** All three analysis scripts run clean. Essentially every number quoted in the text matches computed output, with one exception (finding 2). LaTeX recompiles with no undefined references; all figure files exist.

## Findings

1. **FATAL — garbled math-mode text in Proposition 5 and its proof** (`$t^\ast equal to the wedge...$`; "Pareto-improvable improvements"). [FIXED]
2. **MAJOR — numerical contradiction:** appendix ξ′ = 0.31 vs text 0.17; script says 0.174. [FIXED]
3. **MAJOR — stale capital Z in the cutoff equation.** [FIXED]
4. **MAJOR — leftover capital-M notation from the code colliding with M = membership set** (mixed within single equations; figure caption). [FIXED]
5. **MAJOR — undefined symbol H in the wedge derivation** (defined h₀, then used H). [FIXED]
6. **MAJOR — symbol collision on λ** (population measure vs wage multiplier), the most visible violation of the paper's own conventions. [FIXED: measure renamed ι]
7. **MAJOR — dangling back-reference** ("the first of the amplification channels just noted" — nothing noted). [FIXED]
8. **MAJOR — missing regularity assumptions for the wedge and tax results** (v′, density of F never assumed; f collides with the firm characteristic). [FIXED: v ∈ C¹, finite mean, density written F′]
9. **MAJOR — general propositions proved by numerical example** (stability, m(t) monotonicity, steady-state ordering). [FIXED: statements weakened to what is proven, with example facts labeled as such; further de-exampling per author policy in progress]
10. **MINOR — quasi-circular hypothesis** ("Assumption 1 applied at M = m\*"); positivity condition for m\* > 0 absent from the proposition. [FIXED]
11. **MINOR — symbol reuse across sections** (m\* baseline vs positional; unsubscripted membership m; s school vs taste scale; t tax vs time). [PARTIALLY FIXED: m unified; s and t reuse disclosed in the conventions paragraph as deliberate]
12. **MINOR — symbols used before definition** (ψ(p₂); the list bound written M=2). [FIXED]
13. **MINOR — Proposition (map) never cited by tag; "Part (iii)'s final sentence" mis-pointer.** [FIXED]
14. **MINOR — Corollary quantifier tangle; forward reference to Prop 1.** [FIXED]
15. **MINOR — structure: the polar case leads** (first labeled proposition is the α<1 case the paper disclaims as empirically irrelevant; consider demoting to follow Prop 2). [DECIDED: keep — author prefers the current proposition order]
16. **MINOR — redundancy of the slogans** ("Markets work; material efficiency does not follow" ×3; "tuition reimbursement, not productivity" ×4; "growth finances the status spending that arrests it" ×3). [FIXED: trimmed to abstract/thesis + conclusion bookends]
17. **MINOR — tone/overclaiming residue** (aphoristic chains; "discovery"; the three-firsts sentence stacking priority claims — the third the most exposed given Caucutt). [FIXED: "discovery" softened; third first-claim narrowed with Caucutt cited; remaining flourishes at author's discretion — full voice pass pending]
18. **COSMETIC — em-dash density** (76 lines; a copy editor will halve them). [OPEN: style pass to author's voice pending]
19. **COSMETIC — proofs folded into lemma statements.** [FIXED]
20. **COSMETIC — stale committed PDF (one compile behind).** [FIXED]

## (a) Editor's overall verdict (as delivered, pre-repair)

A genuinely interesting paper with a clean, correct-looking core: the numerical apparatus is exemplary, the central welfare contrast is well-conceived, and the compensation decomposition is a publishable insight on its own. But the manuscript was one polish pass short of submittable: a garbled proposition statement, a numerical contradiction, a paragraph referring to deleted content, and leftover code-notation violating the paper's own covenant. More substantively, several general propositions were proved only up to "verified in the example," and the wedge rested on unstated smoothness assumptions. Verdict: major revision before this leaves the building; days of work, not months; nothing threatens a result.

## (b) Three toughest JPE referee demands (forecast)

1. **"Your dynamic and policy propositions are theorems in name only — prove them or restate them."** Stability, monotonicity under the tax, and steady-state ordering were established by example; the wedge needed unstated assumptions. Expect a demand for general proofs, with machine verification in a robustness role. [Addressed by restatement; residual exposure noted.]
2. **"What is the marginal contribution beyond Becker–Murphy–Werning plus Noguchi–Zame?"** The referee will argue the baseline efficiency result is a corollary of EGSZ Theorem 1 applied to an example, and the positional inefficiency an application of known widespread-externality logic — and will demand either a general theorem class beyond the four-group economy or a quantitative discipline exercise, plus a defense of the priority claims against Caucutt. [Priority claims hedged and narrowed; the general-class and quantitative demands remain strategic decisions.]
3. **"The empirical content section identifies nothing."** The two regimes are observationally similar in cross-section; the proposed tests confront no data; the status discount and the burn are unmeasured. Expect a demand for at least one calibrated confrontation before the policy asymmetry is taken as more than a possibility result. [Post-repair, the section's predictions are model-true and the magnitudes are honestly bounded; a calibration remains undone by design.]
