# Final Positioning Pass: Editorial and Integrity Memo

## Status

The positioning candidate documented below was approved and promoted on July 23,
2026:

- authoritative manuscript: `elite_status-v04.tex`
- authoritative v04 SHA-256: `f6392439f7ebf54f7b995e28583af2dadfac4972c0f5c861688496ecd61fd11a`
- superseded truth version: `elite_status-v03.tex`
- v03 SHA-256: `721eab3beee8956680f68d3851637e434d231de53a45a1c31a24c12977ab0762`
- pre-promotion positioning candidate SHA-256: `8cf7c6280262b038677417553ae1906416c8a672ec867cb4f9a9337c863f5398`

The v03 source was not edited. The promoted v04 header records the v03 base hash
and the pre-promotion candidate hash. Version v04 is now the sole authoritative
manuscript.

## Objective of the pass

The fresh review's decisive objection was not internal coherence or an unresolved
acceptance-bar complaint. It was the perception that the paper offers only a
combination of familiar ingredients: equalizing differences, competitive markets
for status, product dominance, and existing club-equilibrium machinery.

The bounded response is to make the paper's actual applied-theory contribution
impossible to miss:

> A partial-equilibrium comparison of material inputs and output can misidentify
> both the relevant product and the operation of competition. Once the linked
> school--qualification--career product and the incidence of its resource cost are
> placed in general equilibrium, competitive survival, lower material output, and
> Pareto efficiency can coexist. Competition displaces the incumbent when a rival
> reproduces the complete product at lower resource cost.

This is not presented as a new general theory of clubs or a new theorem about
pricing amenities. The manuscript now says explicitly that those are inherited
ingredients. The contribution is the institutional general-equilibrium implication
for a salient phenomenon and the exact competitive boundary supplied by
qualification portability.

The pass deliberately does **not** try to answer the novelty objection by adding a
new theorem, mechanism, extension, calibration, or literature survey. That would
change the paper rather than position it and would recreate the length problem the
authors want to avoid.

## Changes made

### Abstract

The abstract now begins with the inference the paper overturns rather than with a
catalogue of model results. It identifies material production and the complete
product as different objects, states the central strong-core and Pareto conclusion,
and immediately explains who finances the resource-intensive chain.

Competition is described as operating on complete products, not as failing to
operate. Portability is stated as the displacement boundary. Positionality and
dynamics are retained in one sentence each as boundaries and consequences, rather
than being presented as coequal contributions.

The abstract was tightened during verification so that the candidate does not add a
rendered page.

### Introduction

The opening now grants the standard dominance proposition and isolates the disputed
premise: what counts as the product. This makes clear that the paper is not claiming
that inefficient production technologies can survive when they produce the same
complete commodity. It is showing why a material-output comparison is incomplete
when membership, qualification, career access, and standing are traded jointly.

The introduction now explains why general equilibrium is economically necessary.
The framework jointly determines tuition, compensation, occupational choice, sector
size, resource allocation, and welfare, while linked memberships carry
qualifications from schools into firms. This is the structure needed to establish
the complete product, identify who bears its cost, and define the relevant rival.

The hierarchy of results is now explicit:

1. The central result is the coexistence of material underperformance,
   competitive support, and Pareto efficiency.
2. The compensation decomposition explains how buyers finance the institutional
   chain despite visible gross salary premia.
3. The displacement theorem shows that competition remains exacting once products
   are compared on a membership- and qualification-equivalent basis.
4. Portability makes that competitive boundary economically substantive rather
   than leaving it to the baseline binary qualification restriction.
5. Positionality and dynamics locate the welfare boundary and the accumulation
   consequence of the central mechanism.

The contribution paragraph no longer describes the paper as merely a “set of
connected boundaries.” It makes the singular institutional implication the lead
contribution and assigns the extensions subordinate roles.

### Related literature

The literature discussion now concedes inherited ingredients directly:

- competitive pricing of nonpecuniary amenities is established;
- markets for status and prestigious careers already exist in the literature;
- the paper uses rather than extends the Ellickson clubs machinery.

Those concessions sharpen rather than weaken the contribution. The revised text
states the difference in economic object: the paper studies the competitive
persistence, financing, welfare, and displacement of a complete institutional chain
linking costly education, qualification, control rights, and elite career access.

The comparisons with the closest status, career-design, endogenous-group, and
education-status papers now turn on the question each paper answers. Vague priority
language such as “we provide the institutional theory” has been removed.

The clubs subsection now explains the framework's necessary work. Membership lists
encode qualification; firm membership combines productive roles and control rights;
membership prices represent tuition and compensation; and group budget balance
makes the incidence of real resource costs explicit. These elements allow
competition to operate over feasible school--career chains rather than isolated
school or firm technologies.

No citation key was added or removed.

### Conclusion

The conclusion now returns to the partial-equilibrium inference and states why it
fails in the model. It explains that general equilibrium is essential because the
competitive object is the complete school--career chain.

Portability is presented as discipline on persistence. Positionality and dynamics
are presented as limits to, not independent replacements for, the baseline result.
The final paragraph expressly disclaims the proposition that resource-intensive
elite organization is always efficient.

## Deliberate nonchanges

The following content is exactly unchanged from v03:

- the entire formal framework through the discussion section;
- primitives, notation, assumptions, equilibrium concepts, and group types;
- every theorem, proposition, lemma, corollary, definition, and remark;
- every proof and appendix;
- numerical values, computational claims, figures, and empirical mappings;
- the empirical-content and discussion sections.

The title and author block are also unchanged. No new claim, model, theorem,
mechanism, quantitative exercise, or citation was introduced.

## Verification

The candidate passed the following checks against v03:

- raw word count: 20,963 versus 20,999 in v03, a reduction of 36 words;
- rendered length without a bibliography: 61 pages for both versions;
- rendered length with the recovered manuscript bibliography and the same temporary
  fallback bibliography style: 66 pages for both versions;
- formal environment counts are identical: 2 theorems, 11 propositions, 3 lemmas,
  3 corollaries, 1 assumption, 2 definitions, and 3 remarks;
- label inventories are identical: 78 labels, all unique;
- all candidate cross-references point to existing labels;
- citation inventories are identical: 52 unique keys and 81 citation uses;
- the source from `\section{The Framework}` through the end of the discussion is
  byte-for-byte identical;
- the complete appendices are byte-for-byte identical;
- three `pdflatex` passes complete without a LaTeX error or unresolved internal
  reference when the three supplied figures are present.

The candidate source has more physical lines because the revised prose was wrapped
more narrowly and the source-control header is longer. This does not represent
additional manuscript content or pages.

## Bibliography-package note

The candidate, like v03, calls `elite-status-refs-v02.bib`. The uploaded
`references.bib` is a different and unrelated database: it does not contain the 52
keys cited by this manuscript.

The matching `elite-status-refs-v02.bib` was recovered unchanged from the earlier
workspace and copied alongside the candidate. Its SHA-256 is
`e9fc4ee4cf09ef61161e0a01d8cf74047ee849a886fc426739c994813207352a`.
All 52 cited keys resolve against it.

This TeX installation does not contain `chicago.bst`, so the exact requested
bibliography style could not be rendered here. A temporary `plainnat` verification
build resolved all citations and produced no internal-reference errors; neither the
authoritative source nor the recovered bibliography was altered for that test. The submission
environment must include `chicago.bst` (or the authors must intentionally choose an
available style) before final journal compilation.

## Editorial judgment after the pass

This is the economical response to the fresh review. It does not eliminate the
editorial risk that a JPE editor will want a deeper general theorem; no prose revision
can eliminate that risk. It does ensure that such a decision cannot fairly rest on
the mistaken premise that the manuscript claims novelty for pricing status, or that
the Ellickson framework is ornamental.

The paper now presents itself as applied general-equilibrium theory with one central
message: the common material-output diagnosis is a partial-equilibrium diagnosis,
and the correct competitive and welfare conclusions require the whole institutional
product and its financing to clear in equilibrium.

## Promotion completion record

The approved candidate was renamed `elite_status-v04.tex`; its truth-version and
file-role lines were promoted; v03 was marked superseded; the matching bibliography
and three figures were retained; and the promoted source hash was recorded above.
The packaged files passed checksum and clean-build verification. Exact Chicago-style
rendering remains the only environment-dependent compilation step.
