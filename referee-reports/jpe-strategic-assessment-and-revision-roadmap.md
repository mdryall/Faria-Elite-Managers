# The Market for Elite Status

## Strategic Assessment and Revision Roadmap for a JPE Submission

**Prepared for coauthor discussion**  
**Date:** July 21, 2026  
**Authoritative manuscript reviewed:** `market-for-elite-status.tex`  
**Truth-version header:** `% TRUTH VERSION: market-for-elite-status.tex`

---

## Executive assessment

The paper contains a genuinely important and unusually clean economic idea. Its central result is not that competition sometimes fails to eliminate a materially wasteful institution. It is more surprising: competition can work exactly as competitive general-equilibrium theory says it should, all agents can optimize, all relevant memberships and ordinary goods can be priced, the allocation can lie in the strong core, and materially wasteful institutions can nevertheless remain active. The reason is that the institution produces something omitted by an ordinary productivity comparison: status membership. A firm that is superior in material production but does not supply the same membership product is not a complete economic substitute.

That result directly challenges a common partial-equilibrium intuition in current debates about elite education, credentialism, high-status employment, and institutional waste. The usual argument—more materially productive institutions will undercut and displace less productive ones—implicitly compares only material outputs. The paper shows that this comparison can be incomplete in general equilibrium. Competition disciplines inefficiency in the space of complete products, including memberships and status services; it need not eliminate an institution dominated only in the material projection.

The prior adversarial reports substantially strengthen confidence in the manuscript. They establish that the equilibrium construction, EGSZ implementation, core argument, compensation decomposition, positional extension, tax incidence, transition map, and numerical work have been attacked and repaired rather than merely asserted. Later verification rounds re-derived the repairs and ended with all computational checks green. The technical foundation should therefore be treated as an asset, not as the principal risk.

The paper is nevertheless not yet a safe JPE submission. The remaining obstacle is not internal coherence. It is whether a top-journal editor and referee will regard the main insight as a sufficiently general contribution of this paper, rather than an illuminating application of the Ellickson–Grodal–Scotchmer–Zame welfare theorem to a carefully constructed four-group economy. The existing manuscript explains what is different from prior work, but it does not yet convert that difference into a general theorem about the boundary between material and competitive dominance.

The recommended classification is therefore:

> **MAJOR REVISION for JPE.** The current manuscript is not yet JPE-acceptable, but it is not a rejection-level project. A focused revision can materially improve its chances without discarding its idea, replacing the model, or turning it into a different paper.

The highest-return path is:

1. Add a compact general result characterizing when a materially superior group type displaces another type and when material comparisons are insufficient.
2. Use that result to recast the paper’s headline contribution as a distinction between **material dominance** and **full-product competitive dominance**.
3. State the technology and entry boundary precisely: markets select among feasible status-production technologies; they do not invent a status-equivalent technology that is absent from the feasible set.
4. Keep the dynamic extension, because it answers the natural anticipation objection, but narrow its rhetoric to what is established: correct anticipation need not eliminate the drag, and the example generates lower accumulation and lower steady-state material resources.
5. Add a modest quantitative discipline exercise or credible magnitude bound. A full empirical paper is unnecessary, but the manuscript should distinguish the theoretical possibility result from claims about the aggregate importance of actual elite institutions.
6. Conduct a final claim audit so that every prominent sentence in the abstract, introduction, and conclusion is no stronger than the theorem or calibrated example supporting it.

This route preserves the paper’s structure and intellectual identity. It asks the authors to make the core idea more general and more explicit, not to abandon it.

---

## 1. Basis for this assessment

This memorandum evaluates the current authoritative manuscript together with the following prior reports:

- `2026-07-20-1-ge-theory.md`
- `2026-07-20-2-macro-dynamics.md`
- `2026-07-20-3-empirics.md`
- `2026-07-20-4-hostile-editor.md`
- `2026-07-20-r2-summary.md`
- `2026-07-20-r3-r4-final.md`

The sequence matters. The first-round reports found several genuine errors and overstatements. Those reports should not be read as descriptions of the current manuscript. Their findings were repaired, a second round identified additional problems in the repairs, and Rounds 3–4 independently verified the final corrections. The terminal record reports a 43-page manuscript with no LaTeX or reference errors and all three computational verification engines green.

The proper inference is not that repeated stress tests guarantee acceptance at a top journal. They do not. They establish something narrower but important: the manuscript’s principal remaining risks are contribution, framing, scope, and external discipline—not hidden algebraic defects or an incoherent equilibrium.

That distinction is essential for choosing the next revision. It would be wasteful to rebuild parts of the model that have already survived serious scrutiny. The next round of work should be allocated to the strategic questions the reports explicitly left open.

---

## 2. What the paper contributes at its strongest

### 2.1 The central general-equilibrium insight

The paper’s most compelling proposition can be expressed in plain language:

> A materially inefficient institution can survive perfect competition and belong to a Pareto-efficient allocation when its resource shortfall is the cost of producing a valued membership product.

The crucial phrase is “membership product.” Standard productivity comparisons treat the institution as if it supplied only ordinary goods. The paper embeds school and firm memberships in the commodity structure. Agents care about those memberships, group budgets price them, and the status-valuing manager finances the relevant resource cost through a lower net position. Once status is recognized as output, the apparently dominated institution need not be economically dominated.

This is not an argument that every observed waste is efficient, or that status should count normatively without debate. It is an argument that material-output data alone cannot establish a market failure. A claim of inefficiency requires either:

- excluding status utility from the welfare criterion;
- showing that status is positional and therefore creates an externality;
- identifying an unpriced effect, market power, misinformation, or another friction; or
- showing that a status-equivalent but materially superior feasible technology is being excluded.

This is a valuable conceptual clarification because public and academic discussions routinely move directly from resource use to market failure. The paper identifies the missing step.

### 2.2 Incidence: who pays for status production

The model does more than append status utility to an otherwise standard economy. It locates the financing of the institution. The group budget constraints imply that the elite organization’s resource shortfall cannot be shifted to an unidentified outside party. It is financed through equilibrium membership prices and compensation, with the manager who values elite membership accepting a status discount net of education costs.

That incidence result is economically appealing for three reasons:

1. It makes the mechanism falsifiable. The model has implications for gross compensation, education cost, and the net position of participants.
2. It distinguishes the model from a reduced-form status term attached to an occupation. Institutions produce and sell the status service, and real resources are used in production.
3. It explains why firm-level accounts can look favorable even while the broader school–firm complex consumes more resources per unit of material output.

The strongest version of the paper is therefore not simply “status matters.” It is:

> When status is institutionally produced, competitive prices determine both its resource cost and who bears that cost; those prices can sustain organizations that look inefficient in material accounts while the complete allocation remains in the core.

### 2.3 The absolute-versus-positional welfare boundary

The baseline and positional regimes form a useful conceptual pair.

- Under absolute status, the membership is a privately valued consumption object. Its resource cost can reduce material output without creating a Pareto inefficiency. The EGSZ welfare theorem applies.
- Under positional status, entry dilutes the status enjoyed by incumbents. The externality crosses groups and falls outside the baseline club-pricing system. The equilibrium can then exhibit over-entry, fail to lie in the core, and admit a corrective membership tax.

This contrast prevents the paper from becoming a blanket defense of elite institutions. It supplies a sharp diagnostic question: is the membership valuable because of what it positively provides, or because others do not possess it? The policy conclusion differs across those cases.

The phrase “absolute status” may require careful explanation because some readers will regard all status as intrinsically relative. The economics does not require winning that semantic dispute. The baseline can be interpreted as identity, affiliation, recognition, access, or membership utility that does not mechanically fall when another group forms. The positional extension then isolates the scarcity component. The manuscript should make clear that these are analytically distinct components of a potentially mixed real-world object.

### 2.4 Why the dynamic extension belongs

The dynamic extension answers the most natural objection to the static result:

> If an expanding status sector lowers aggregate material resources, would forward-looking agents not recognize the consequence and avoid it?

The paper’s answer is that recognizing an aggregate consequence does not by itself create a profitable unilateral deviation. Agents are atomistic. Each chooses among available occupations and memberships, internalizing the private cost and benefit but not controlling the aggregate path.

The transfer-motive appendix adds substantive robustness. Within the stated degree-one, common-continuation-factor class, a common forecast or continuation value cancels from occupational comparisons. It can change saving volumes and therefore the transition, but it does not change the within-period membership prices, wages, cutoff, or elite mass. This supports a meaningful, though limited, proposition:

> Correct anticipation of the aggregate path need not unravel the status mechanism.

The extension should be retained. Removing it would leave the paper exposed to an obvious objection that the current version can answer. But the extension should be presented as a robustness and propagation result, not as a general theory of dynastic altruism, intertemporal efficiency, or balanced growth.

### 2.5 Empirical content that is now genuinely model-based

The empirical section is much stronger after the prior review cycle. Its best elements are:

- zero incidence of an elite-specific tuition change on the elite salary, because the change is absorbed by the status discount;
- the joint prediction of zero tuition pass-through and an inferior net position relative to the non-elite track;
- credentialing resources per managerial position as a more faithful observable than aggregate TFP;
- a quantity response distinguishing positional from absolute status, since dilution dampens expansion of the elite share;
- the distinction between private admission returns and the aggregate return to expansion of the elite sector.

These are real predictions, not loose analogies. The current empirical weakness is that they are largely untested and the model’s large numerical effects come from a deliberately outsized elite sector. That is a limitation on external importance, not a contradiction in the theory.

---

## 3. What the prior stress tests establish

### 3.1 General-equilibrium theory

The GE review verified that the paper accurately represents the EGSZ primitives, group-equilibrium conditions, and welfare theorems. It reproduced the baseline prices, cutoff, clearing conditions, compensation decomposition, coexistence condition, output identities, and numerical regimes. It also found the exact-feasibility and collinearity core of the positional Pareto-improvement construction to be sound.

Earlier deficiencies involving the leisure anchor, uniqueness, compensation of displaced elite managers, regularity assumptions, coalition feasibility, local nonsatiation, and strong-core language have been repaired. Those issues should not be raised again as current defects.

The implication for revision is positive: the paper can confidently use the club framework. It does not need a simpler substitute model merely to reassure readers that equilibrium exists or that the core result is formally valid.

### 3.2 Macro and dynamics

The macro report described the period economy, transition-map construction, and numerical implementation as unusually coherent. The original report’s major concerns—domain restrictions, excessive stability claims, the technological source of the luxury result, and oversold foresight language—were either repaired or narrowed.

Most importantly, the current transfer-motive propositions substantially answer the prior request for forward-looking robustness. They do not solve dynasty-specific inheritance or prove intertemporal efficiency, but those are now extensions rather than prerequisites for the paper’s intended claim.

The implication is that the dynamics do not require reconstruction. They require disciplined exposition:

- “lower accumulation” rather than a permanent reduction in a growth rate;
- “lower steady-state material resources” rather than unqualified social impoverishment;
- conditional or example-specific convergence language;
- correct anticipation within the established class, not unrestricted full foresight.

### 3.3 Empirical interpretation

The first empirical report found that an earlier headline prediction had the wrong sign and that several claims exceeded what the model or evidence supported. Those findings were serious, but they have been repaired. Round 2 characterized the empirical section as close to referee-proof and the later rounds re-derived the zero-pass-through identity and checked the credentialing-resource observable.

The implication is that another wholesale empirical rewrite is unnecessary. The remaining question is whether the paper should add external discipline to improve its top-journal prospects. That is a strategic choice, not a repair of invalid claims.

### 3.4 Editorial execution

The hostile-editor report found the paper genuinely interesting and identified the compensation decomposition as potentially publishable on its own. Mechanical and expositional problems were subsequently corrected. The final verification record is unusually strong.

The same report, however, forecast three demands that remain relevant:

1. What is the marginal contribution beyond EGSZ and Noguchi–Zame?
2. Where is the quantitative confrontation or other external discipline?
3. How far does the anticipation result extend beyond the pooled warm-glow economy?

The first is the binding issue. The second would materially improve the submission. The third can be handled through precise scope unless the authors want to undertake a much larger extension.

---

## 4. Evaluation from three referee perspectives

| Perspective | Present assessment | What would satisfy the reader |
| --- | --- | --- |
| General-equilibrium theorist | The equilibrium and welfare analysis are formally acceptable. The EGSZ machinery is correctly used and economically functional. | State a general result defining the boundary between material dominance and dominance in the complete commodity–membership space. Be precise about the feasible technology set. |
| Macro theorist | The dynamic section is acceptable as an extension and robustness exercise. It is not an independent macro contribution. | Narrow claims about foresight, convergence, growth, and welfare; bring the transfer-motive robustness result closer to the main discussion. |
| Stringent JPE referee | The paper contains a broad and potentially important message, but its most general welfare result currently looks inherited. | Convert the message into a theorem of the paper, demonstrate that the result is not a knife-edge artifact, and add enough quantitative or empirical discipline to support claims of contemporary importance. |

This yields an important distinction between intellectual classification and likely editorial outcome. The project merits **major revision**, because a credible path exists within the present architecture. Yet an as-written JPE submission could still be rejected rather than invited to revise: top-journal editors may regard the unresolved contribution question as too central for an R&R.

---

## 5. The principal unresolved JPE risks

### 5.1 The paper’s theorem versus an application of someone else’s theorem

The central baseline welfare result follows from EGSZ once the constructed allocation is shown to be a group equilibrium. This is legitimate economics, and applying a powerful framework in a new setting can be valuable. But at JPE the natural skeptical summary is:

> The authors designed a four-group economy in which status is a membership good, then invoked the existing clubs welfare theorem; the positional result adds a familiar widespread externality.

The manuscript presently responds by emphasizing new institutional objects: a supply side for status, real resource use, linked school and firm memberships, compensation incidence, competitive entry, and dynamics. Those differences are meaningful. The unresolved question is what general conclusion requires them.

The best response is not a longer literature review. It is a theorem that extracts the economic principle from the example.

### 5.2 Entry, invention, and the feasible status technology

The framework takes the group technology set as exogenous and finite. This is standard. A model of competitive equilibrium is not ordinarily required to model invention of every absent technology.

Nevertheless, the current introduction says that no entrant can offer “status without waste.” Taken literally, that is broader than the theorem. The theorem establishes that no coalition using the available group types can block the equilibrium. It does not establish that a new organization could never produce an equivalent status service at lower material cost.

This must be handled with precision rather than defensiveness:

- **Not a valid internal-coherence objection:** “The model assumes a technology set, therefore competition is fake.” Every production model conditions equilibrium on feasible technologies.
- **A valid scope question:** “Why is a cheaper institution status-equivalent to the incumbent not in the feasible set?” The paper currently treats institutional identity and membership characteristics as primitives.
- **A valid top-journal contribution opportunity:** characterize what happens if a status-equivalent, materially superior type is feasible. It should displace the inferior type. Then show that material superiority without status equivalence does not imply displacement.

This converts an apparent vulnerability into the central theorem: competition works against full-product dominance; it does not act on material dominance alone.

The paper should not claim that prestige can never be copied cheaply. It should explain that status equivalence is an economic restriction, not a relabeling operation. A newly created “elite” institution does not automatically inherit the identity, affiliation, qualification consequences, or recognition supplied by an incumbent membership. Endogenizing that credibility could be valuable, but it is a separate theory of reputation formation and is not necessary for the conditional GE result.

### 5.3 The aggregate-importance gap

The numerical example shows large steady-state losses, while the empirical section correctly acknowledges that real-world elite credentialing is a small share of aggregate resources. A skeptical referee may therefore accept the possibility theorem but reject rhetoric suggesting that the mechanism explains large movements in aggregate productivity or national wealth.

The paper has three choices:

1. Make no quantitative claim and present the result as a conceptual theorem about market discipline and welfare.
2. Provide credible bounds showing the maximum plausible aggregate effect under realistic sector sizes.
3. Undertake a calibration or empirical exercise linking the mechanism to actual credential markets.

For the present project, the second option is likely optimal. It adds discipline without converting the paper into a large empirical undertaking. The result may be that plausible aggregate effects are modest. That would not invalidate the theory. It would shift the applied claim from “a major explanation of aggregate stagnation” to “a mechanism that changes how institution-level waste and policy should be interpreted, with potentially meaningful effects in sectors where status production is large.”

### 5.4 Claim strength

Several prominent phrases are more expansive than the supporting results:

| Current or recurring formulation | Risk | Recommended formulation |
| --- | --- | --- |
| “No entrant offering status without waste” can improve on equilibrium | The model does not include technological invention or establish status equivalence of a hypothetical entrant. | “No coalition using the available status-production technologies can improve on equilibrium; a status-equivalent lower-cost technology, if feasible, would displace the inferior type.” |
| Societies converge “with full foresight” | The formal robustness applies within a common-factor, degree-one class, not arbitrary dynastic continuation values. | “Correct anticipation of the aggregate path need not eliminate the status margin.” |
| Growth finances status spending that “arrests” growth | The model primarily generates a level effect and lower accumulation, not a permanent balanced-growth-rate effect. | “Rising resources expand status production, which lowers accumulation and the steady-state level of inherited resources in the example.” |
| Competition is making society “permanently poorer” | “Poorer” may be read as lower welfare or as an empirical statement about actual societies. | “The equilibrium can produce permanently lower material resources than the status-free counterfactual.” |
| Status is a luxury “by theorem, not assumption” | The result depends on fixed resource requirements relative to wages that scale with wealth. | “Given the model’s fixed resource cost of elite production, the elite share rises with wealth.” |
| Positionality is the only possible market failure | The paper compares two modeled regimes, not every possible friction. | “Within the modeled environments, positional dilution is the force that breaks core efficiency.” |

This is not cosmetic caution. At a top journal, the abstract and introduction determine which objections the referee feels invited to make. Precise claims focus attention on the real contribution.

### 5.5 Breadth versus depth

The paper covers static equilibrium, compensation, aggregate output, core efficiency, positional externalities, corrective taxation, OLG dynamics, empirical implications, and several robustness results. This breadth is impressive, but it creates a risk that the new contribution looks diffuse while the deepest theorem is inherited.

The revision should not add another major application. It should deepen the common principle tying the existing sections together. The general material-versus-full-product result is attractive partly because it unifies the paper:

- the baseline shows coexistence without inefficiency;
- the positional model shows how an unpriced cross-group effect breaks the result;
- the tax corrects that specific externality;
- the dynamics show that anticipation does not automatically remove the static margin;
- the empirical section explains why firm-level material measures do not identify the welfare regime.

---

## 6. The recommended new theoretical contribution

### 6.1 Core concept: status-equivalent group technologies

The paper should introduce, with notation chosen only after coauthor agreement, a concept of status or membership equivalence between group types. Informally, two types are status-equivalent if replacing one with the other preserves everything agents value or require about membership except the associated vector of ordinary private goods.

The definition must be stronger than “the organizations have the same label.” It should preserve:

- membership profiles and role requirements;
- utility consequences of the relevant memberships for all affected agents;
- acquired qualifications and eligibility for subsequent groups;
- organizational or peer characteristics entering preferences;
- the mapping between school and firm memberships, where relevant; and
- feasibility of forming the replacement group at the same scale.

With this definition, ordinary material productivity becomes a comparison holding the complete membership product fixed.

### 6.2 Proposed result 1: elimination of full-product dominance

The first result should establish approximately the following:

> **Full-product dominance.** Suppose an active group type has a feasible status-equivalent replacement that uses weakly fewer ordinary goods in every relevant dimension and strictly fewer in at least one dimension, while preserving the membership services and qualification consequences of the original type. Then the original type cannot be active in a core allocation, subject to the replication and feasibility conditions of the group economy.

The proof logic should be short. The affected members form the status-equivalent replacement group. The replacement preserves their membership utilities and releases a strictly positive material surplus. That surplus can be distributed so that all coalition members are weakly better off and at least one is strictly better off, producing a block.

This result openly grants the strongest version of the standard competition argument. If a cheaper organization truly produces the same complete product, the inferior organization should disappear.

### 6.3 Proposed result 2: material dominance is incomplete

The second result should state the paper’s positive insight:

> **Material dominance without membership equivalence.** A group type can be materially dominated by another type and nevertheless remain active in a core equilibrium when the two types supply different membership products. The paper’s elite-school–elite-firm economy provides an open set of parameters supporting such coexistence.

It is important to establish an open set rather than point only to the numerical example. The existing strict inequalities likely make this possible with modest additional work. The result should identify the economically relevant restrictions—status willingness to pay, resource burn, compensating differentials, and the material productivity comparison—and show that coexistence is robust to small perturbations.

### 6.4 Proposed result 3, if feasible: an incidence corollary

A useful companion result would generalize the financing logic:

> **Competitive incidence of membership production.** Under group budget balance, the material shortfall associated with a status-producing group is financed by the equilibrium membership prices of those who value or require its memberships. There is no unidentified external subsidy within the baseline economy.

This may be a direct consequence of the framework rather than a deep independent theorem. Even so, writing it generally would clarify why the EGSZ apparatus is indispensable. The framework is not being used merely to attach a welfare theorem to an example; it determines the incidence of institutionally produced status.

### 6.5 Why this is the best revision

These results would answer several objections simultaneously:

- **Novelty:** the paper contributes a general distinction and characterization rather than only a four-group application.
- **Entry:** it states exactly what a cheaper entrant would need to preserve to displace the incumbent.
- **Interpretation:** it explains why material productivity is not the correct ordering of organizations supplying different memberships.
- **Policy:** it clarifies that material waste alone does not establish a corrective role, whereas positional dilution can.
- **Empirics:** it shows why firm accounts and material-output comparisons cannot identify full economic dominance.

The addition should be concise—potentially a short subsection after the general framework plus an application corollary in the model section. The objective is not to create another long formal layer. It is to make the paper’s implicit theorem explicit.

### 6.6 A caution about theorem strength

Before committing to the statement, the authors should verify that the EGSZ membership representation permits the required equivalence mapping without effectively assuming the conclusion. Memberships are indexed by group type, so a replacement type may create formally different membership objects even if the intended economics is identical. The definition must specify utility and qualification equivalence across those objects.

If the fully general theorem becomes notation-heavy, a more modest but still useful alternative is an augmented-technology proposition for the class of linked school–firm economies studied in the paper. That would be less general, but it would still answer the entrant question directly and demonstrate robustness beyond the single four-type configuration.

---

## 7. Revision of the dynamic section

### 7.1 Keep the extension

The dynamic extension should remain. It answers a question that virtually every seminar audience will ask and connects the static possibility result to broader concerns about credential expansion and accumulation.

### 7.2 Change its assigned role

The section should be presented as:

- an iteration of the static club economy;
- a demonstration that the same material-drag condition has dynamic consequences;
- a robustness exercise showing that correct anticipation need not eliminate the within-period status margin; and
- an illustration of lower accumulation and steady-state material resources.

It should not be presented as:

- a general theory of long-run growth;
- a proof that rational societies knowingly reduce welfare;
- a model of heterogeneous dynasties or intergenerational elite persistence;
- a global convergence theorem for every admissible parameterization; or
- evidence that actual elite credentialing causes large national wealth losses.

### 7.3 Bring the anticipation answer forward

The savings-motive invariance result currently appears in the appendix. Because anticipation is a central motivation for the dynamics, the main text should state its content explicitly and early. A short corollary or formal remark could say that, within the degree-one common-factor class, forecasts affect saving and the transition but not the static membership margin at a given wealth level.

This would let the introduction make a precise claim without forcing readers to discover the qualification much later.

### 7.4 Do not build the full dynastic extension before submission

A dynasty-specific inheritance model would require heterogeneous wealth, occupation-dependent continuation values, and a new equilibrium distribution. It could become a second paper. It may also introduce mobility and persistence mechanisms that compete with the current clean market-for-status result.

Unless the authors independently want that project, it should remain an extension. For the current submission, the proper statement is that dynasty-specific inheritance and unrestricted altruism are outside the established robustness class.

---

## 8. Quantitative and empirical discipline

### 8.1 What JPE does and does not require

JPE does not require every theory paper to contain a large empirical exercise. A sufficiently general and important theory contribution can stand on its own. But this manuscript motivates itself with contemporary elite institutions, uses empirical evidence in the introduction, and presents large numerical steady-state effects. That combination invites a magnitude question.

The paper should therefore choose explicitly between a pure conceptual-theory posture and a quantitatively relevant institutional posture. The current draft sometimes occupies both.

### 8.2 Recommended minimum: a disciplined magnitude exercise

The preferred addition is a compact exercise with three outputs:

1. **Sector-size benchmark.** Construct a transparent range for the share of resources devoted to the relevant elite credentialing activities. The category must match the model as closely as possible—full-cost, status-intensive credentialing linked to access to elite positions—not all higher education.
2. **Model-consistent mapping.** Translate that range into credentialing resources per elite managerial position and the implied material-output or accumulation effect under conservative parameter values.
3. **Bounded conclusion.** State what the mechanism plausibly can and cannot explain. If realistic aggregate effects are small, emphasize institutional incidence, distribution, and policy interpretation rather than national TFP.

The exercise should not treat tuition as resource cost without adjustment, should not classify all elite-education expenditure as waste, and should not use the deliberately outsized numerical example as a calibration.

### 8.3 Higher-cost empirical option: tuition-shock incidence

The sharpest potential test uses elite-specific tuition shocks in markets where students bear the posted price and subsequent salaries can be observed. Elite professional degrees are a more natural environment than heavily subsidized undergraduate education.

The design would compare salary changes across cohorts and programs exposed to different cost shocks, with a non-elite or unaffected track as a control. The status model predicts that an elite-specific tuition change is absorbed by the status discount rather than passed into gross elite salaries. Because an entry-rationed human-capital model can also generate zero pass-through, the cleanest test would combine salary incidence with a measure of the participant’s net position or another implication of status valuation.

This could be powerful, but it is not a small addition. Data quality and identification risk are substantial. It should not delay the theory revision unless credible data are already accessible.

### 8.4 Preserve the distinction between testing and illustration

The model’s comparative statics can be numerically illustrated without being empirically calibrated. The manuscript should label each exercise correctly:

- “example” when parameters are chosen to display mechanisms;
- “calibration” only when parameters target real moments;
- “prediction” when the result follows from the model;
- “evidence” only when data bear on that prediction; and
- “magnitude bound” when the exercise limits plausible size without estimating a full model.

---

## 9. Rewriting the paper’s front end

The abstract and introduction should be rebuilt around one hierarchy of claims.

### 9.1 Recommended message hierarchy

**First:** The standard displacement argument is incomplete because it orders firms by material output while the market trades complete products that include memberships.

**Second:** In a competitive group economy, status production has prices and incidence. Status-valuing members finance the resource shortfall, and the equilibrium can remain in the strong core.

**Third:** Competition would eliminate a genuinely status-equivalent, materially superior substitute. What it does not eliminate is an organization dominated only in the material projection.

**Fourth:** If status is positional, entry creates dilution outside the group-pricing system; core efficiency then fails and a membership tax can improve welfare, with an output gain under the stated dominance condition.

**Fifth:** Correct anticipation does not necessarily undo the mechanism; in the dynamic example, status expansion lowers accumulation and steady-state material resources.

This hierarchy places the new general theorem before the application details and turns the strongest anticipated objection into part of the contribution.

### 9.2 What to de-emphasize in the abstract

The abstract currently carries too many distinct claims: compensation, firm productivity, aggregate output, core efficiency, positional over-entry, taxation, luxury status, convergence, and foresight. A top-journal abstract should make the conceptual result immediately legible.

The abstract should prioritize:

1. material versus full-product dominance;
2. competitive incidence and core efficiency;
3. the positional boundary; and
4. one sentence on dynamic anticipation.

The zero-pass-through prediction and numerical convergence can remain in the body or introduction.

### 9.3 A possible one-sentence contribution statement

Without prescribing final wording, the revised paper should be able to defend a sentence close to:

> We show that competition eliminates organizations dominated in the space of complete products, but not organizations dominated only in material production; when status is an institutionally produced membership, materially inferior firms can therefore survive in the strong core, with their resource shortfall financed at market prices by status-valuing members.

That sentence communicates a theorem, a mechanism, an equilibrium result, and the use of the clubs framework.

---

## 10. Positioning relative to the closest literatures

### 10.1 Becker–Murphy–Werning

The paper should concede the broad prior insight: status can be priced and competitive trade in status can be efficient. The novelty cannot be “markets can efficiently allocate status.”

The contribution is institutional and production-side:

- status is produced through linked school and firm memberships;
- its production consumes real resources;
- group budgets determine who finances it;
- materially inferior-looking organizations can survive core discipline;
- firm-level performance can diverge from system-level material output; and
- positionality breaks the result through a cross-group dilution externality.

The revision should explain which of the new general results cannot even be formulated in a model where status is an abstract divisible good in fixed supply.

### 10.2 EGSZ

The manuscript should present EGSZ as the enabling framework, not as a rival whose theorem must be disguised. The paper’s contribution is to identify a consequential economic application and derive a general implication about material productivity comparisons in group economies.

The new theorem should make clear what is inherited and what is not:

- inherited: group-equilibrium existence and the relevant welfare theorem under maintained assumptions;
- contributed: the full-product/material-dominance distinction, the linked institutional application, incidence and compensation results, the positional boundary in this setting, and the dynamic propagation.

### 10.3 Noguchi–Zame and positional externalities

The paper should not claim that positional externalities or widespread-externality equilibria are new. Its contribution is to place such an externality inside an institutionally explicit market for status and show exactly how the welfare conclusion changes relative to the absolute-membership baseline.

### 10.4 Education, signaling, and selection

The model’s cleanest distinction from signaling is the absence of hidden information. Its elite membership is directly valued and remains operative under full information. That contrast should remain prominent.

The paper should also be clear that causal returns to elite admission do not directly measure aggregate creation of output. At the same time, large causal earnings effects put pressure on a literal interpretation in which excess tuition alone accounts for the full observed premium. The current scarcity-rent and bundled-ability qualifications should remain.

---

## 11. JPE, AER, and Review of Economic Studies

The immediate revision should target JPE, but the optimal presentation differs somewhat across top journals.

### 11.1 JPE

JPE is the best conceptual target for the paper’s current identity. The manuscript is price-theoretic, institutional, and general-equilibrium in spirit. Its appeal lies in overturning a familiar intuition using competitive equilibrium rather than a behavioral mistake or market imperfection.

For JPE, the strongest package is:

- a big, counterintuitive economic proposition stated plainly;
- a compact general theorem establishing the proposition;
- a concrete institutional economy showing incidence and observables;
- a sharp welfare boundary between absolute and positional status; and
- enough quantitative discipline to establish relevance without allowing the empirical discussion to dominate.

### 11.2 AER

The [AER describes itself](https://www.aeaweb.org/journals/aer) as a general-interest journal publishing across a broad range of topics. For an AER submission, the paper would likely need a simpler front end and stronger evidence that the mechanism matters outside the model. AER readers may be less patient with the full machinery unless the empirical or quantitative payoff is immediate.

An AER-oriented version would probably require either:

- a credible empirical test of a distinguishing prediction; or
- a very transparent calibration showing economically important magnitudes.

The current JPE route—general theorem plus institutional application—is more natural.

### 11.3 Review of Economic Studies

The [Review of Economic Studies](https://academic.oup.com/restud/pages/About) explicitly emphasizes path-breaking theoretical and applied work. ReStud may be receptive to the unusual use of the group-equilibrium framework, but its comparative advantage would be technical novelty. A ReStud-oriented version would benefit from a stronger and more abstract theorem class, perhaps a characterization applying beyond status and beyond the four-group school–firm economy.

If the new full-product-dominance theorem becomes broad enough to apply to clubs, organizations, occupational identity, and other nonmaterial membership goods, ReStud becomes a plausible alternative. If the paper remains primarily an economically rich application with institutional interpretation, JPE remains the better first target.

---

## 12. Proposed revision sequence

### Phase 1: Coauthor decisions

Agree on four points before editing prose:

1. Is the headline contribution the full-product/material-dominance distinction?
2. Are the authors willing to state explicitly that a feasible status-equivalent lower-cost technology would displace the inferior type?
3. Will the paper make only a conceptual possibility claim about aggregate effects, or add a magnitude exercise?
4. Is the dynamic section a robustness extension rather than a coequal macro contribution?

These choices determine the theorem, abstract, and allocation of pages.

### Phase 2: Theorem memorandum before manuscript editing

Write a separate two-to-four-page technical memorandum containing:

- the definition of status or membership equivalence;
- the full-product-dominance proposition;
- the blocking-coalition proof;
- the material-dominance nonimplication result;
- the open-set coexistence corollary; and
- any incidence corollary.

Stress-test that memorandum before integrating it. In particular, verify the mapping of membership objects, qualifications, and utilities across group types.

**Decision gate:** If the result is essentially immediate and cannot be made economically broader than a restatement of the core, consider strengthening it into a characterization or a comparative-institutions theorem. Do not pad a trivial proposition with notation.

### Phase 3: Rebuild the introduction and contribution map

Once the theorem is secure:

- rewrite the abstract;
- replace the three-result introduction with a hierarchy centered on the general theorem;
- revise the EGSZ and BMW positioning;
- remove or qualify the hypothetical “status without waste” entrant;
- state the precise anticipation result; and
- distinguish material resources from welfare everywhere.

### Phase 4: Integrate the theorem with minimal architectural disruption

The likely placement is immediately after the general framework or at the start of the equilibrium section. The four-group economy should then become the leading application and constructive coexistence example.

Avoid changing established notation or assumptions until the theorem has been separately agreed. The current editorial covenant requires permission for such changes.

### Phase 5: Add quantitative discipline

Choose either:

- a magnitude-bound subsection using credible external resource shares; or
- a more ambitious tuition-incidence exercise if data are already available.

The first is the recommended default.

### Phase 6: Claim audit and length control

Create a table listing every claim in the abstract, introduction, proposition summaries, empirical section, and conclusion, together with its formal support:

- general theorem;
- conditional theorem;
- numerical example;
- external evidence;
- interpretation; or
- conjectured extension.

Any sentence combining categories should be split or qualified.

At the same time, remove repetition. The new theorem will permit several existing explanatory passages to be shortened because the distinction between material and complete products will have a formal reference point.

### Phase 7: Final adversarial review

The final pre-submission review should ask only unresolved strategic questions:

1. Can a referee still summarize the baseline as merely “EGSZ plus an example”?
2. Does the entrant theorem genuinely answer the technology-set objection?
3. Is the positional result framed as a new application rather than a claim to have invented positional externalities?
4. Does the macro language stay within the anticipation and accumulation results?
5. Are empirical magnitude claims separated from the deliberately illustrative numerical economy?
6. Can the paper’s contribution be explained accurately in three sentences without specialized notation?

Re-running settled algebraic objections would have low value unless the new theorem changes existing assumptions or notation.

---

## 13. What not to do

### Do not replace the club framework

The framework is the source of the paper’s distinctive equilibrium prices, linked qualifications, group budget balance, and core discipline. A simpler reduced-form status model might be easier to read but would weaken the central claim.

### Do not build an all-purpose theory of prestige formation

Endogenizing reputation, label credibility, historical incumbency, selection, and imitation would be a major new project. The current paper can acknowledge that those forces determine the feasible set of status-equivalent technologies while maintaining its conditional equilibrium result.

### Do not discard the dynamics

The anticipation objection is too natural to leave unanswered, and the current appendix provides a credible limited answer. Keep the extension but reduce claims that make it appear to promise a full macro theory.

### Do not add more extensions before deepening the main theorem

Additional heterogeneity, capacity constraints, peer effects, governance, or endogenous scarcity could all be interesting. None addresses the binding JPE question as directly as the general material-versus-full-product result.

### Do not rely on the stress tests as evidence of novelty

The reports establish correctness and careful repair. They do not themselves prove that the contribution clears a top-five threshold. The revision must make the contribution legible to an editor who has not seen the review history.

### Do not preserve rhetorically strong sentences at the expense of theorem accuracy

Phrases such as “full foresight,” “arrests growth,” and “no entrant offering status without waste” are memorable, but they invite objections broader than the paper needs to answer. The central result is strong enough without them.

---

## 14. Submission recommendation

The paper should not be abandoned or redirected immediately to a field journal. The core idea is sufficiently unusual, general-interest, and relevant to current debates to justify a serious JPE revision.

The recommended strategy is:

1. Undertake the focused theoretical revision described above.
2. Add a bounded quantitative relevance exercise if feasible.
3. Recast the abstract and introduction around material versus full-product dominance.
4. Keep the positional and dynamic extensions, with narrower claims.
5. Submit to JPE once a hostile reader can no longer dismiss the paper as only an application of an inherited welfare theorem.

If the authors choose to submit without these changes, the paper is polished enough to be read seriously, but the likely top-journal outcome remains rejection on contribution scale rather than on correctness. If the new theorem succeeds, the paper acquires a credible JPE identity: a general price-theoretic result with an institutionally rich application and a sharp policy boundary.

The decisive goal is not to prove that competition is weak. It is to state more powerfully what the current model already shows:

> Competition is stringent about the products markets actually trade. When status membership is one of those products, material productivity alone does not determine which institutions survive—and material waste alone does not diagnose market failure.

That is the paper worth sending to JPE.

---

## Appendix: concise coauthor decision sheet

### Recommended verdict

- **Intellectual quality:** strong and unusual.
- **Technical status:** extensively verified; no known proposition-threatening defect in the current version.
- **Current JPE status:** major revision.
- **Likely as-written JPE risk:** rejection for insufficiently general marginal contribution.
- **Best route upward:** generalize the central insight, not the entire model.

### Must do before JPE

- Add and verify the status-equivalence/full-product-dominance result.
- Establish robust, preferably open-set coexistence under material but not full-product dominance.
- Rewrite the abstract and introduction around that theorem.
- Correct the scope of entry and invention claims.
- Narrow the foresight, convergence, growth, and welfare language.
- Separate theoretical possibility from claims about real aggregate magnitude.

### High-value additions

- General incidence corollary for status production under group budget balance.
- Compact magnitude bounds using realistic sector shares.
- Main-text statement of the transfer-motive invariance result.
- A claim-support audit and final adversarial contribution review.

### Defer unless required

- Dynasty-specific inheritance.
- Full reputation or prestige-formation dynamics.
- Heterogeneous wealth and intergenerational mobility.
- A large causal tuition-incidence project.
- Additional institutional applications.

### One-sentence test for the revised paper

If the revision succeeds, a neutral economist should be able to say:

> The paper proves that competition eliminates full-product dominance but not material dominance, and applies that distinction to show how resource-intensive elite institutions can survive in a core-efficient market for status, with positional dilution marking the boundary at which correction becomes warranted.
