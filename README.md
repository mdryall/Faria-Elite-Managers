# The Market for Elite Status

Research project (Jo&atilde;o R. Faria and Michael D. Ryall) modeling elite status as a
priced membership in the general-equilibrium-with-clubs framework of Ellickson,
Grodal, Scotchmer, and Zame. Elite schools sell status-conferring qualifications;
elite-run firms out-produce their rivals firm by firm, yet the school&ndash;firm complex
returns less output per unit of resources; the resulting drain survives competition
and is Pareto optimal. Target: JPE / ReStud.

## Central thesis

*Competition eliminates institutions dominated in the complete product they sell
&mdash; status included &mdash; not institutions dominated only in material
production* (Theorem 2, the displacement boundary). Because status is priced, a
merely-more-productive rival sells the wrong product and displaces nothing; a
status-equivalent cheaper rival would displace the elite system in every
equilibrium, and none is feasible. The drain is real (output falls as status taste
spreads) but it is no wealth pump: the status discount accepted by elite managers
finances the entire system at market prices, and every equilibrium lies in the core.

## Repository layout

| Path | Contents |
|------|----------|
| `elite_status-v01.tex` | **Current manuscript (authoritative; see its truth-version header).** Static clubs model (Props 1&ndash;2, Theorem 1, compensation decomposition Cor 1), displacement boundary (Definition 1, Theorem 2, financing Cor 2), positional extension (Props 3&ndash;5), OLG dynamics (Props 6&ndash;8), transfer-motive robustness (Props 9&ndash;10), exact steady-state loss identity, magnitude bounds, numerical examples, proofs. |
| `elite-status-refs.bib` | Curated bibliography, fully verified against publisher/journal sources. |
| `THEOREM-MEMO.md` | Standalone development of the displacement theorem (Phase-2 memorandum): definition, both proof routes, decision-gate assessment, source checks. |
| `CLAIM-AUDIT.md` | Claim-support audit: every abstract/intro/conclusion claim vs. its formal support, with addenda for each revision round. |
| `analysis/static_model.py` | Symbolic verification of every static-section formula (11 checks) plus the comparative-statics figure. |
| `analysis/positional_model.py` | Verification and computation for the positional section: fixed point, Pareto-improvement construction, tax equilibria, welfare curve, figure. |
| `analysis/dynamic_model.py` | Verification and computation for the dynamic section: period-economy algebra, transition maps, steady states, taste-spread decline, figure. |
| `analysis/displacement_theorem.py` | Openness sweep for Theorem 2(ii) (per-parameter margins) and the aggregate-saving identity of the pricing route. |
| `analysis/magnitude_bound.py` | Closed-form loss identity (sympy-verified), taste-free multiplier, and the sourced envelope arithmetic of the Magnitudes block. |
| `referee-reports/` | Complete adversarial-review record: four internal rounds (July 20), the JPE strategic assessment and revision roadmap, the theorem-memo stress test, and the final Phase-7 round with dispositions. |
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
- [x] **Phase 4 &mdash; Framing, literature, empirics.** Final introduction with motivating evidence and roadmap; full-prose related-literature section (incl. clubs lineage and elite-overproduction positioning); Empirical Content section with five falsifiable prediction blocks; Conclusion; keywords/JEL; bibliography fully verified against publisher sources.
- [x] **Phase 5a &mdash; Adversarial stress-test (4 rounds, terminated clean).** Rounds 1&ndash;2: full adversarial passes (GE theory vs. the EGSZ source, macro/dynamics, empirics vs. the cited papers' texts, hostile editor); rounds 3&ndash;4: verification passes on the repairs. Every finding repaired or explicitly dispositioned; complete record in `referee-reports/`. The scripts now include the assertions whose absence permitted the caught errors (direct-derivative cross-check, closed-form identities, pass-through).
- [x] **Phase 5b &mdash; JPE strategic revision (July 21&ndash;22).** Response to the strategic assessment (`referee-reports/jpe-strategic-assessment-and-revision-roadmap.md`): the displacement-boundary theorem (membership equivalence; full-product dominance displaces, by a core route and a welfare-theorem-free pricing route; material dominance without equivalence need not &mdash; the serious school is the "status without waste" entrant inside `G`, failing only at the qualification clause); front end rebuilt around it, later reframed on the Turchin elite-overproduction arc (drain without the wealth pump); exact steady-state loss identity with taste-free multiplier and a sourced magnitude bound (NCES/BEA/Chetty&ndash;Deming&ndash;Friedman; extreme envelope &le; 0.75% of steady-state wealth); claim-support audit; final adversarial round &mdash; all six roadmap exit questions resolved, all findings repaired (`referee-reports/2026-07-21-phase7-final.md`).
- [ ] **Phase 5c &mdash; Circulation.** Mike final read; Jo&atilde;o rejoins (see `HANDOFF-JOAO.md`); seminars; submission (target JPE).

## Building

```sh
python3 analysis/static_model.py          # verify static algebra + figure
python3 analysis/positional_model.py     # verify positional results + figure
python3 analysis/dynamic_model.py        # verify dynamic results + figure
python3 analysis/displacement_theorem.py # verify Theorem 2(ii) openness + pricing identity
python3 analysis/magnitude_bound.py      # verify loss identity + magnitude envelope
pdflatex elite_status-v01
bibtex   elite_status-v01
pdflatex elite_status-v01
pdflatex elite_status-v01
```
