# The Market for Elite Status

Research project (Jo&atilde;o R. Faria and Michael D. Ryall) modeling elite status as a
priced club membership in the general-equilibrium-with-clubs framework of Ellickson,
Grodal, Scotchmer, and Zame. Elite schools sell status but no skill; elite-managed
firms are less productive yet operate in competitive equilibrium; the resulting waste
survives competition and is Pareto optimal. Target: JPE / ReStud.

## Central thesis

*Markets work &mdash; but that does not imply material efficiency.* Because status is
priced, competition has nothing to arbitrage: an equilibrium in which elite
institutions burn resources lies in the core. Measured output falls as the taste for
status spreads, yet no reallocation Pareto-improves on it.

## Repository layout

| Path | Contents |
|------|----------|
| `market-for-elite-status.tex` | **Current manuscript.** Static clubs model (Props 1&ndash;2, Theorem 1), positional extension (Props 3&ndash;5), OLG dynamics (Props 6&ndash;8: transition map, status-as-luxury, status drag), numerical examples, proofs. |
| `elite-status-refs.bib` | Curated bibliography. Entries flagged `TODO-VERIFY` need checking against the published source before submission. |
| `analysis/static_model.py` | Symbolic verification of every static-section formula (11 checks) plus the comparative-statics figure. |
| `analysis/positional_model.py` | Verification and computation for the positional section: fixed point, Pareto-improvement construction, tax equilibria, welfare curve, figure. |
| `analysis/dynamic_model.py` | Verification and computation for the dynamic section: period-economy algebra, transition maps, steady states, taste-spread decline, figure. |
| `figures/` | Generated figures included by the manuscript. |
| `literature/` | Source PDFs of the Ellickson et al. papers. |
| `drafts/` | Archived prior drafts and notes (superseded). |
| `Joao_Model/` | Jo&atilde;o's original OLG derivations and numerical work. |

## Status and plan

Six-phase plan (Mike is project lead through the next full draft; Jo&atilde;o rejoins for
final edits).

- [x] **Phase 0 &mdash; Scaffolding.** Repo structure, notation scheme, curated `.bib`, verification harness.
- [x] **Phase 1 &mdash; Static core.** Heterogeneous-status model; Proposition 1 (coexistence of wasteful elite firms), Proposition 2 (efficient decline of output), Theorem 1 (no market correction); numerical example; machine-verified appendix.
- [x] **Phase 2 &mdash; Positional extension.** Relative status as a widespread externality; unique self-limiting equilibrium (Prop 3); failure of the first welfare theorem and core equivalence (Prop 4, constructive); over-entry and a membership tax that raises welfare *and* output (Prop 5).
- [x] **Phase 3 &mdash; Dynamics (OLG).** Warm-glow bequests in the produced good; within-period allocation is the Phase 1/2 equilibrium at `k_t`; one condition (elite output-per-resource deficit) governs the static decline, status-as-luxury (Prop 7), and the accumulation drag (Prop 8); rational, fully-foreseen impoverishment with no collapse; positional dilution protects wealth.
- [ ] **Phase 4 &mdash; Framing, literature, empirics.** Introduction, related-work confrontations, empirical-implications section.
- [ ] **Phase 5 &mdash; Stress-test and circulation.** Adversarial review, seminars, submission.

## Building

```sh
python3 analysis/static_model.py          # verify static algebra + figure
python3 analysis/positional_model.py      # verify positional results + figure
python3 analysis/dynamic_model.py         # verify dynamic results + figure
pdflatex market-for-elite-status
bibtex   market-for-elite-status
pdflatex market-for-elite-status
pdflatex market-for-elite-status
```
