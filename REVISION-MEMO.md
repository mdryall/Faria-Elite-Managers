# Revision Memorandum — *The Market for Elite Status*

**Manuscript:** `elite_status-v01.tex` (51 pp., builds clean, all five verification engines green)
**Prepared:** 2026-07-23
**Purpose:** Consolidated point-by-point response to the accumulated review record — the document to reply to the earlier referee issues this revision was built to fix.

---

## 0. What this memorandum is

The paper has not yet been submitted to a journal, so the "referees" here are the internal adversarial review passes recorded in `referee-reports/`.
The principal charge sheet is the **JPE Strategic Assessment and Revision Roadmap** (`referee-reports/jpe-strategic-assessment-and-revision-roadmap.md`), which classified the paper **MAJOR REVISION** and set the agenda for the revision committed in `02d6676`.
Behind it stand four rounds of correctness review (rounds 1–4), a stress-test of the displacement theorem memo, and a final adversarial round (Phase 7).

This memorandum does two things:

1. **§2** responds to the strategic roadmap — the substantive contribution-level demands — pointing to the theorem, section, or exercise that answers each.
2. **§3** records the earlier round-by-round correctness findings and their dispositions, so nothing raised in review is left unaccounted for.

§4 lists the items consciously deferred (not defects), and §5 the open judgment calls flagged for the authors.
The mapping is written so it can be lifted into a journal response letter with minimal editing: each entry is *issue → what changed → where to find it*.

Manuscript locations are given by LaTeX label (e.g. `sec:displacement`, `thm:displacement`, `rem:loss`) so they survive repagination.
Every quantitative claim below is reproduced by a script in `analysis/`; the relevant engine is named where it matters.

---

## 1. Review history at a glance

| Round | Date | Scope | Terminal verdict |
|---|---|---|---|
| 1 (4 referees) | 2026-07-20 | GE theory, macro/dynamics, empirics, hostile editor | Major revision; ~5 majors per dimension, one FATAL empirical sign error — all repaired |
| 2 (3 referees) | 2026-07-20 | Re-attack + verify round-1 repairs | "One focused revision from publishable"; 2 new majors found and fixed |
| 3–4 (verification) | 2026-07-20 | Audit round-2 repairs | Caught a defective repair (tax decomposition); fixed; terminated clean |
| Memo R1 | 2026-07-21 | Displacement-theorem memo (`THEOREM-MEMO.md`) | Sound with repairs; 2 majors (boundary gaps) fixed |
| **Strategic roadmap** | 2026-07-21 | **Contribution / framing / scope** | **MAJOR REVISION — the agenda for this revision** |
| 7 (2 referees) | 2026-07-21 | Fully integrated manuscript | "Nothing remaining is a referee-report-generating defect" |

The correctness foundation (rounds 1–4, memo) was already an asset before this revision; the strategic roadmap addressed contribution and framing, not hidden defects.
§2 is therefore the substantive response; §3 documents that the foundation it builds on is sound.

---

## 2. Response to the strategic assessment (MAJOR REVISION)

The roadmap's binding demand: convert an *application of the EGSZ welfare theorem to a four-group economy* into a *general theorem of the paper*, and bring every prominent claim back within what is proven.
Each roadmap item below is answered by a concrete addition to the manuscript.

### 2.1 "The paper's theorem versus an application of someone else's theorem" (roadmap §5.1, §6)

**Raised:** A stringent referee could summarize the baseline welfare result as "designed a four-group economy in which status is a membership good, then invoked EGSZ." The general principle was implicit, never stated as the paper's own result.

**Response — new displacement theorem.**
We extract the economic principle from the example and state it as the paper's headline result.

- **Definition `def:equivalence`** (membership equivalence): two group types are status-equivalent when one can replace the other preserving everything agents value or require about membership except the vector of ordinary private goods — formalized as a qualification clause on consumption sets **(E1)** and a conditional-utility clause **(E2)**.
- **Theorem `thm:displacement`** (displacement boundary), two parts:
  - **(i) Full-product dominance eliminated.** A feasible status-equivalent replacement that uses weakly fewer ordinary goods everywhere and strictly fewer somewhere blocks the incumbent — it cannot be active in a core allocation. Proved two ways: a **core route** (grand-coalition replacement block, under a non-null interior-consumption proviso) and a **pricing route** (`(i′)`, three steps), the latter **welfare-theorem-free** and therefore valid where EGSZ does not apply.
  - **(ii) Material dominance is incomplete.** A materially dominated type can remain active in a core equilibrium when the two types supply different membership products — established on an **open set** of parameters, not merely at the example (openness verified in `analysis/displacement_theorem.py`: margins α ±4%, λ/λᵉ ±7%, others ≥±10%, joint ±1.5%).
- **Corollary `cor:financing`** (competitive financing): under group budget balance the status producer's material shortfall is financed by the equilibrium membership prices of those who value it — no unidentified external subsidy. This is the one technically **non-inherited** piece (aggregate-saving arbitrage ∫saving = ν(g)·p·(y′−y) > 0) and it survives the positional regime.

**Location:** `def:equivalence`, `thm:displacement`, `cor:financing` at the end of §5 (`sec:displacement`); proofs in Appendix C (`app:displacement`).
**What is inherited vs. contributed** is stated explicitly: inherited — group-equilibrium existence and the welfare theorem under maintained assumptions; contributed — the full-product/material-dominance distinction, the pricing route, the linked institutional application, financing incidence, the positional boundary, and the dynamic propagation.

### 2.2 Entry, invention, and the feasible status technology (roadmap §5.2)

**Raised:** The introduction's "no entrant offering status without waste" outran the theorem, which conditions on the feasible technology set.

**Response.**
The overclaim survives only in its **theorem-backed, inverted** form: a status-equivalent lower-cost type *would* displace the incumbent (Theorem (i)); what competition does not eliminate is a type dominated only in the material projection (Theorem (ii)).
The exact-sense exhibit for (ii) is the **serious school** — it vector-dominates the elite school and passes (E2) but fails the qualification clause (E1): "the entrant is already in G."
Reputation/prestige-formation is explicitly declined as a separate theory; the feasible set is taken as primitive, and the paper says so.

### 2.3 The aggregate-importance gap (roadmap §5.3, §8)

**Raised:** Large steady-state numbers in a deliberately outsized example, against real elite credentialing being a small resource share — inviting a magnitude objection.

**Response — compact magnitude bound (not a calibration).**
An exact closed-form steady-state loss identity, `rem:loss` (Appendix D), with a **taste-distribution-free multiplier** M = 1.2520 (constant across the entire taste scan; sympy + numeric, `analysis/magnitude_bound.py`), plus a "Magnitudes" block closing `sec:empirics`.
Sourced anchors: NCES postsecondary expenses \$702B (2020–21); BEA GDP \$23.0T (2021, smallest vintage = conservative).
Central estimate ≈ 0.04%; extreme envelope (5% enrollment, 4× spending, all burn) ≤ 0.75% ("about three-quarters of one percent, at the example's multiplier").
Stated plainly: **this mechanism does not explain aggregate stagnation**; the content is incidence, interpretation, and policy.
The exercise labels itself — "example," "prediction," "magnitude bound" — never "calibration."

### 2.4 Claim strength (roadmap §5.4) and the claim audit (roadmap §6, Phase 6)

**Raised:** Six prominent phrases stronger than their support ("full foresight," "arrests" growth, "permanently poorer," luxury "by theorem," positionality the "only" failure, the entrant claim).

**Response.**
All six rewritten to the roadmap's recommended forms; "full foresight" / "arrests" / "poorer" / growth-rate language **grep-verified absent**.
Foresight is scoped to the degree-one common-factor class at every occurrence; luxury is "in equilibrium," not "by theorem"; the market-failure claim is scoped "within the environments we model."
A full **claim-support audit** (`CLAIM-AUDIT.md`) tables every abstract/intro/§5.6/empirics/conclusion claim against its support category; the one mismatch found ("does not undo" → "need not undo") was fixed.

### 2.5 Breadth versus depth (roadmap §5.5)

**Raised:** Risk that the contribution looks diffuse while the deepest theorem is inherited.

**Response.**
No new application was added; the displacement distinction is the common spine that ties the existing sections together — baseline coexistence, the positional break, the corrective tax, the dynamic drag, and why firm-level material measures do not identify the welfare regime all now reference one formal distinction.

### 2.6 Front-end rebuild (roadmap §9)

**Raised:** Recast the abstract and introduction around the material-vs-full-product hierarchy; de-emphasize the crowded claim list.

**Response.**
Abstract and intro rebuilt on the agreed five-level hierarchy with the displacement theorem **first** and the anticipation result brought forward into the intro (roadmap §7.3).
Per the author-directed front-end reframing, the intro opens on the Turchin *End Times* "wealth pump" arc (the sanctioned framing exception), and uses as its honest headline twist that the model delivers Turchin's **drain** while **overturning the pump** — incidence is the reverse of a wealth pump (supported by the compensation corollary and `cor:financing`).

### 2.7 The dynamic section rescoped (roadmap §7)

**Raised:** Keep the extension but present it as robustness/propagation, not a macro theory; bring the anticipation-invariance result forward.

**Response.**
The transfer-motive invariance result is now stated in the §8 main text (not buried in the appendix): within the degree-one common-factor class, forecasts move saving and the transition but not the within-period membership margin at a given wealth level.
Claims narrowed to "lower accumulation" and "lower steady-state material resources"; convergence stated conditionally (single-crossing provisos the example satisfies).
Dynasty-specific inheritance and unrestricted altruism are stated as outside the established robustness class.

### 2.8 The roadmap's six exit questions (resolved in Phase 7)

The final adversarial round confirmed all six:

| # | Exit question | Status |
|---|---|---|
| 1 | Still "EGSZ plus an example"? | Resolved — front end leads with the paper's own theorem; pricing route is welfare-theorem-free |
| 2 | Entrant theorem answers the technology-set objection? | Resolved — conditioning open, reputation declined, overclaim survives only inverted |
| 3 | Positional result framed as application, not invention? | Resolved — Noguchi–Zame credited; novelty confined to first embedding in the clubs framework |
| 4 | Macro language within anticipation/accumulation results? | Resolved — zero instances of the flagged diction; foresight scoped throughout |
| 5 | Magnitudes separated from the illustrative economy? | Resolved — closed-form identity + sourced bounds + plain concession |
| 6 | Explainable in three sentences without notation? | Resolved — the one-sentence test is passable verbatim |

Editor's terminal verdict: *"Fix the findings, then submit to JPE. Nothing remaining is a referee-report-generating defect."* All Phase-7 wording findings were applied the same day.

---

## 3. Correctness record — earlier findings and dispositions

The strategic revision builds on a foundation that was itself heavily stress-tested. This section documents that every correctness finding from rounds 1–4, the memo stress-test, and the Phase-7 technical pass is repaired. It is the backing appendix for §2: if a future referee re-raises any of these, the disposition is here.

### 3.1 General-equilibrium theory (round 1)

| Finding | Severity | Disposition |
|---|---|---|
| Lemma 1 uniqueness not forced (σ₀ = 0 permitted) | Major | Assumption (iv) strengthened to σ₀ > 0; uniqueness conditioned on a positive leisure mass |
| Positional Prop, FOSD-damping part false (shift evaluated at different cutoffs) | Major | Restated with an explicit shift-location hypothesis |
| Inefficiency Prop: "movers at reservation" wrong for dm > 0 | Major | O(dm²) mover-compensation step written out; aₑ, a_c > 0 and σ₀ > 0 staffing stated; collinearity core confirmed sound |
| Membership-tax envelope step contradicted by the paper's own example (W′(0)=0.00125 vs de-dilution 0.00058) | Major (near-fatal) | Envelope claim withdrawn; restated as over-entry wedge + example; wedge vs t^W conceptual gap corrected |
| Transition-map stability asserted, not proven | Major | Weakened to \|ξ′\|<1-in-example; oscillation explained by ξ′≈−0.08 |
| Prop 2 derivative off by factor of 2; "machine-verified" tag unbacked | Minor | Closed form corrected; check added to `static_model.py` |
| Strict-monotonicity boundary / LNS; missing wedge regularity (v∈C¹, density, finite mean); dynamic-equilibrium definition; measurability omissions | Minor | All added; LNS boundary remark for EGSZ; density written F′ to avoid collision |
| Notation: λ measure→ι, m/M mixing, garbled Prop 5 math | Cosmetic | All purged |

All round-1 GE repairs were independently **re-proven** in round 2 and confirmed sound.

### 3.2 Macro / dynamics (round 1)

| Finding | Severity | Disposition |
|---|---|---|
| Transition-map domain unstated; interior configuration fails at moderate k | Major | Proposition restated on a stated domain K with corner regimes acknowledged |
| Stability asserted while the map's own slope goes negative | Major | Weakened; damped-oscillation mechanism (ξ′<0) substituted for the unsubstantiated "overshoot" story |
| "No forecasting / rational societies let it happen" oversold; vacuous under pooled inheritance | Major | Reframed as recursivity; the substantive fix is the Appendix E transfer-motive invariance result (see §2.7) |
| "Luxury by theorem" overstates — it is a technological nonhomotheticity | Major | Honest attribution to fixed input requirements vs k-scaled wages; cost-scaling robustness remark |
| θ investment technology unpriced; uniform-inheritance "dynasty" language; intertemporal-welfare hedge under-cited | Minor | Technology assigned (CRS, profitless); "dynasty" language removed; Diamond (1965), Andreoni (1990) added; self-impoverishing sign of the status discount stated |

### 3.3 Empirics (round 1)

| Finding | Severity | Disposition |
|---|---|---|
| **Headline "premia co-move with tuition" is FALSE in the model** — gross elite wage is τ-free (status discount absorbs tuition one-for-one) | **Fatal** | Reversed into the headline: **zero tuition pass-through** is now the discriminating prediction; d(premium)/dr = α−1; machine-verified |
| Dale–Krueger characterized selectively; "gross premium ≤ excess tuition" bound falsified by CDF/Zimmerman magnitudes | Major | DK reconciled; decomposition reframed to bound only the **status-financed component**, scarcity rents + bundled ability carrying the remainder |
| "Net returns ≤ non-elite track" misattributed to DK | Major | Relabeled as the model's untested prediction; contrary causal evidence acknowledged |
| Firm-accounts-vs-national-accounts wedge ill-posed (NIPA books burn as education VA) | Major | Observable renamed *credentialing resources per managerial position, economy-wide* (τr constant → composition effect; machine-verified 1.0→3.5) |
| "No credential markets in poor economies" has venal-office counterexamples | Major | Restated as a within-economy comparative static holding the distribution fixed; endowment-inequality caveat + historical cites |
| Zimmerman/CDF/MPZ glosses; "tuition outpaced instructional cost" | Minor | All hedged to the papers' actual findings; motivation reframed around resource absorption |

### 3.4 Editorial / exposition (round 1)

Garbled Proposition-5 math (fatal), the ξ′=0.31-vs-0.17 numerical contradiction, stale capital-Z/M/H symbols, the λ collision, a dangling back-reference, and missing wedge regularity — **all fixed**.
General propositions "proved by example" were weakened to what is proven, with example facts labeled as such.
The author-decided items (proposition order kept; em-dash voice pass) were handled in the subsequent decisions round (em-dashes 153→53).

### 3.5 Repairs of repairs (rounds 2–4)

Two majors introduced *by* the round-1 repairs were caught and fixed:

- **Membership-tax part (iii)** went through two defective repairs before converging. Round 2 restated it as a two-term decomposition; round 3 found that omitted the tax's **direct incidence channel** (true dȳ/dt = +0.0134, not +0.0097). The final **three-channel identity** — de-entry +0.0160, rebate −0.0063, incidence +0.0037, sum +0.0134 — is machine-verified against the direct equilibrium derivative to six figures, and `positional_model.py` now **asserts channel-sum = direct derivative** as a standing check (the absence of exactly that check is what let the two-term version through). Lesson recorded: decompositions must be cross-checked against direct derivatives.
- **Appendix E invariance** hid a degree-one homogeneity assumption; restated for the degree-one class with a cardinalization-free salvage (the luxury/drag condition contains no preference parameters).

### 3.6 Displacement-theorem memo stress-test (Memo R1)

The theorem memo was attacked before integration; two majors — the core clause outrunning its proof at the consumption boundary (a machine-found configuration τ=6, α=1.1, s=1.0 gives wₑ = z = 1.95 < k = 2, so "w ≥ k" was false), and p ≫ 0 not established for the pricing route — were repaired with the **interior-consumption proviso** and the aggregate-saving argument. Five minors + two cosmetics also fixed.
The proviso was later shown **vacuous** for our economy: new **Remark `rem:proviso`** (Appendix C) proves p ≫ 0 in *any* group equilibrium here, so "every equilibrium" is literal.

---

## 4. Standing strategic items (consciously deferred — not defects)

These are recorded so a response letter can address them head-on rather than appear to have missed them.

1. **Marginal contribution over EGSZ + Noguchi–Zame.** The displacement theorem and the welfare-theorem-free pricing route are the substantive answer; a still-more-general characterization class remains a possible referee demand. The internal "a referee who calls part (i) trivial concedes the thesis" argument is **not** in the manuscript, by decision.
2. **A calibrated confrontation of the zero-pass-through prediction.** Declined pre-submission under the agreed stopping rule (presubmission work only if it corrects a false/unproven assertion or defends the central thesis). Revisit on referee demand; the compact magnitude bound (§2.3) supplies the discipline in the interim.
3. **Dynasty-specific, forward-looking inheritance.** Deferred as a potential second paper; Appendix E establishes what is provable in the pooled economy, and the Discussion states the extension honestly, including the dynastically self-impoverishing sign of the status discount.

---

## 5. Open judgment calls flagged for the authors

From Phase 7 (`referee-reports/2026-07-21-phase7-final.md`), defensible as-is; the authors' call:

- **Placement of `sec:displacement`** — billed "First" in the intro but appearing as the last subsection of §5 (part (ii) needs the equilibrium construction). Both Phase-7 referees find it defensible; a journal referee may suggest promoting it. Moving it is structural surgery.
- **Theorem numbering inversion** — the intro's "First" result is the later-numbered theorem; no error, but readers may stumble. Only fixable by reordering (tied to the placement question).
- **Deeper redundancy cuts** — the scarcity-rents discussion and the notation-conventions paragraph could recover 2–3 pp. Voice territory.

---

*Source reports: `referee-reports/` (rounds 1–4, memo R1, Phase 7, strategic roadmap). Machine checks: `analysis/{static_model,positional_model,dynamic_model,displacement_theorem,magnitude_bound}.py`. Claim audit: `CLAIM-AUDIT.md`. Theorem memo: `THEOREM-MEMO.md`.*
