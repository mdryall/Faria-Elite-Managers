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
| `market-for-elite-status.tex` | **Current manuscript.** Static clubs model, Propositions 1&ndash;2 and Theorem 1, numerical example, proofs. |
| `elite-status-refs.bib` | Curated bibliography. Entries flagged `TODO-VERIFY` need checking against the published source before submission. |
| `analysis/static_model.py` | Symbolic verification of every equilibrium formula in the paper (11 checks) plus the comparative-statics figure. Run with `python3 analysis/static_model.py`. |
| `figures/` | Generated figures included by the manuscript. |
| `literature/` | Source PDFs of the Ellickson et al. papers. |
| `drafts/` | Archived prior drafts and notes (superseded). |
| `Joao_Model/` | Jo&atilde;o's original OLG derivations and numerical work. |

## Status and plan

Six-phase plan (Mike is project lead through the next full draft; Jo&atilde;o rejoins for
final edits).

- [x] **Phase 0 &mdash; Scaffolding.** Repo structure, notation scheme, curated `.bib`, verification harness.
- [x] **Phase 1 &mdash; Static core.** Heterogeneous-status model; Proposition 1 (coexistence of wasteful elite firms), Proposition 2 (efficient decline of output), Theorem 1 (no market correction); numerical example; machine-verified appendix.
- [ ] **Phase 2 &mdash; Positional extension.** Relative status as a widespread externality; failure of the first welfare theorem; over-entry and corrective membership tax.
- [ ] **Phase 3 &mdash; Dynamics (OLG).** `k_t` as state variable; within-period allocation is the Phase 1 equilibrium; multiple steady states and rational-expectations decline paths.
- [ ] **Phase 4 &mdash; Framing, literature, empirics.** Introduction, related-work confrontations, empirical-implications section.
- [ ] **Phase 5 &mdash; Stress-test and circulation.** Adversarial review, seminars, submission.

## Building

```sh
python3 analysis/static_model.py          # regenerate figures + verify algebra
pdflatex market-for-elite-status
bibtex   market-for-elite-status
pdflatex market-for-elite-status
pdflatex market-for-elite-status
```
