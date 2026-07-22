# Claim-Support Audit (Phase 6 of the JPE revision roadmap)

**Date:** 2026-07-21. **Manuscript state:** post-integration of Theorem 2 (displacement boundary), rebuilt front end, magnitude block.
Support categories per roadmap §12 Phase 6: **GT** general theorem · **CT** conditional theorem · **EX** numerical example · **EV** external evidence · **IN** interpretation · **CJ** conjectured extension.
A claim passes if its prose strength matches its support category; mismatches found during the audit are listed with their resolution at the bottom.

## Abstract

| Claim | Support | Verdict |
|---|---|---|
| Competition eliminates complete-product dominance, not material-only dominance | Thm 2(i)+(ii) — CT (equivalence, strict dominance, interiority proviso, desirable endowments) | PASS: abstract-level summary; formal hypotheses stated in §5.6 and App C |
| Status-equivalent cheaper technology "would displace... in every equilibrium" | Thm 2(i), pricing route — CT | PASS with note: "every equilibrium" elides the interiority proviso, which every equilibrium characterized in the paper satisfies; precise augmented-economy statement is in the body (displacement discussion, second consequence) |
| Resource-dominated school–firm complex survives in the strong core | Thm 2(ii)(b,c), open set — CT | PASS |
| Gross salary premia + net status discount | Cor 1 — CT (central configuration $1<\alpha<(\beta c+\tau r)/(c+r)$) | PASS: configuration named in §4/§5 |
| Output falls as taste spreads | Prop 2 — CT (resource-dominance condition, maintained configuration) | PASS |
| Positional: over-entry; tax raises welfare, "and output as well under a stated condition our example satisfies" | Props 4–6 — CT + EX | PASS: output claim explicitly conditioned |
| Richer economies support larger elites | Prop 7 — CT (same condition) | PASS |
| "Correct anticipation need not undo the mechanism" | Prop invariance (App E) — CT (degree-one common-factor class) | PASS after fix (was "does not"; changed to "need not" per roadmap) |
| Example economy converges to permanently lower material wealth | EX (+ Prop 8 orderings) | PASS: example-scoped, wealth (not welfare) language |

## Introduction

| Claim | Support | Verdict |
|---|---|---|
| Result 1 para: membership-equivalent cheaper type "cannot be active in any equilibrium" | Thm 2(i) — CT | PASS (same proviso note as abstract) |
| "An institution can lose every material comparison and survive in the strong core" | Prop 1 (α<1 polar case) + Thm 1 — CT | PASS |
| Serious school = the entrant, fails only at qualification clause | Thm 2(ii)(a) — CT, parameter-free clauses | PASS |
| "The elite premium prices the qualification, not the classroom" | IN of Thm 2(ii)(a) | PASS: interpretive but anchored |
| Result 2 para: decomposition, zero tuition incidence | Cor 1 + machine-verified wage identity — CT | PASS (verified prior rounds) |
| Result 3 para: decline with firm-level superiority | Prop 2 — CT | PASS |
| Result 4 para: syllogism "valid for complete products, invalid for material projections" | Thm 1 + Thm 2 — CT | PASS |
| "Within the environments we model, it locates where a genuine market failure must live" | IN, scoped | PASS after earlier scoping fix |
| Positional para: existence/uniqueness/self-limiting/inefficiency/over-entry | Props 3–5 — CT | PASS |
| Tax raises welfare and output together "as it does in our example" | Prop 6(iii) + EX | PASS |
| Luxury "in equilibrium" with mechanism stated | Prop 7 — CT | PASS after earlier "by theorem" fix |
| Drag + steady-state wealth ordering | Prop 8 — CT (single-crossing provisos stated in prop) | PASS |
| Invariance sentence (degree-one class named in text) | Prop invariance — CT | PASS: class restriction carried in the sentence itself |
| "Rational societies really do let it happen" | IN of recursivity + invariance | PASS: anchored to formal results in same paragraph |
| Three novelty claims (produced status; firm-level persistence; theorem-drawn boundaries) | Lit section §2 | PASS (verified prior rounds; boundaries claim now backed by Thm 2) |

## Displacement subsection (§5.6)

| Claim | Support | Verdict |
|---|---|---|
| Definition commentary: "(E1)–(E2) are restrictions, not relabeling" | IN of definition structure | PASS |
| "Concedes the strongest form of the displacement argument" | Thm 2(i) | PASS |
| "Boundary runs through the middle of G" | Thm 2(ii)(a) | PASS |
| Credibility of qualifications = primitive; reputation theory not attempted | Scope statement | PASS (roadmap §5.2 compliance) |
| Financing corollary "condition 1 rearranged, and we present it as such" | GT (trivial) — honestly labeled | PASS |

## Empirical Content

| Claim | Support | Verdict |
|---|---|---|
| Zero tuition pass-through; joint prediction isolates status mechanism | CT + machine-verified | PASS (prior rounds) |
| Credentialing-resources-per-position observable | CT + EX (machine-verified 1.0→3.5) | PASS (prior rounds) |
| Luxury/dynamic diagnostics | CT | PASS (prior rounds) |
| Magnitudes: closed-form loss identity, M taste-free | Remark (App D) — GT within OLG model; sympy + numeric verification | PASS |
| $702B / ~3% GDP / <0.5% Ivy-Plus | EV: NCES 2023 (Condition of Education), BEA 2022, Chetty-Deming-Friedman | PASS: sourced, cited, machine-checked arithmetic |
| Extreme envelope → loss ≤ 0.75%; central → hundredths of a percent | EX arithmetic through GT identity, machine-verified | PASS |
| "This mechanism does not explain aggregate stagnation" | IN of the bound | PASS: stated plainly, as roadmap demands |
| Scope notes (unbooked positional competition; not growth accounting) | IN | PASS |

## Conclusion

| Claim | Support | Verdict |
|---|---|---|
| Displacement sentence (status-equivalent tech would displace; survivor dominated only in material projection) | Thm 2 — CT | PASS |
| "Economy converging to permanently lower material wealth" | EX + Prop 8 | PASS after earlier "poorer" fix |
| Positional-only market failure "within the environments we model only in that case" | CT, scoped | PASS after earlier scoping fix |
| Tax gains "as in our example" | EX | PASS |

## Mismatches found and resolved in this audit

1. **Abstract**: "correct anticipation... *does not* undo the mechanism" overclaimed the degree-one class result → changed to "*need not*" (the roadmap's own recommended formulation). Fixed 2026-07-21.

## Standing notes (accepted, not defects)

- ~~Abstract and intro summaries state Theorem 2(i) without the interiority proviso~~ **RESOLVED in Phase 7**: Remark rem:proviso (App C) now proves every group equilibrium of our economy satisfies the proviso ($p\gg 0$ always), so "every equilibrium" reads literally; pointer added in §5.6.
- Abstract states Props 2/7 without repeating the maintained resource-dominance condition; the condition is named at every formal statement and in §4's configuration paragraph.

## Front-end reframing addendum (2026-07-22, Mike-directed)

Manuscript renamed: authoritative source is now `elite_status-v01.tex`. Abstract and intro opening rebuilt around the Turchin/*End Times* arc (elite overproduction → free-market rejoinder → our answer) per Mike's explicit direction. New claims audited:

| Claim | Support | Verdict |
|---|---|---|
| Turchin thesis + anti-elite movements (abstract sent. 1; intro ¶1) | Motivation; turchin2023endtimes cited in intro; movements described neutrally, no sides named | PASS (sanctioned exception recorded in strip-political-framing memory) |
| "The rejoinder fails in an exact way" | IN anchored to Thm 2 | PASS |
| "Would displace the elite system in every equilibrium" | Thm 2(i) + rem:proviso (proviso vacuous) | PASS |
| "Merely more productive need not displace anything" | Thm 2(ii) | PASS |
| "It is no wealth pump: ... status discount finances the entire system at market prices" | Cor 1 + Prop 1 discussion + Cor financing (budget balance forbids external transfer) | PASS |
| Intro: "incidence is the reverse of a wealth pump: the elite ... pay it" | Same support | PASS |
| "Converges, knowingly, to permanently lower wealth" | Example-scoped ("our example economy"); common-knowledge path per §8 | PASS |
| "Elite overproduction, delivered by prices rather than by capture" | IN anchored to Prop 7 + lit-review first-formalization claim | PASS |

## Phase 7 addendum (2026-07-21)

Two further mismatches caught by the final adversarial round and fixed: the abstract's "displaces nothing" universal negative (→ "need not displace anything"; sufficiency phrasing propagated to the Theorem-1 discussion and caveat), and rem:loss's first-factor claim at the α=1 boundary (→ strict inequality for α>1 only). Full record: referee-reports/2026-07-21-phase7-final.md.
