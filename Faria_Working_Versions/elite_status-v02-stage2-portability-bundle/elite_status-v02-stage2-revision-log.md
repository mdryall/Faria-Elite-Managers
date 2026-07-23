# Stage 2 Revision Record

## Authority and scope

- Authoritative manuscript header: `% TRUTH VERSION: elite_status-v02.tex`
- Authoritative uploaded source: `elite_status-v02(1).tex`
- Authoritative-source SHA-256: `1a25382edf830d9008ec7bd6b667f124c0a95783a0cf424fd5763ebcbdc31c5c`
- Formal sub-branch: `elite_status-v02-portability-subbranch.tex`
- Final sub-branch SHA-256: `d77fad7748d2a287ad9ff3657beaaf7d947f8511695d825befc6dae693ee8245`
- File role: Stage 2 imperfect-qualification-portability development; not authoritative.
- The authoritative manuscript, bibliography, and supplied figures were not edited.
- Scope completed here: Stage 2 only. The approved result is developed and proved in a separate sub-branch. It is not integrated into the front end, positional model, or dynamics.
- The Stage 1 record remains in `elite_status-v02-stage1-revision-log.md`; this record adds the Stage 2 dispositions.

Status terms:

- **Accepted—implemented:** approved and incorporated in the formal sub-branch.
- **Rejected:** considered but not adopted, with the reason recorded.
- **Deferred:** deliberately reserved for Stage 3 or a later extension.
- **Flagged:** preserved for author attention rather than silently repaired.

## Accepted—implemented

| ID | Exact searchable anchor | Disposition |
|---|---|---|
| P-01 | `\section{Qualification Portability and Recognition}` | Added a self-contained static absolute-status extension before `\section{Numerical Example}`. The section expressly leaves the original four-type economy unchanged outside this sub-branch. |
| P-02 | `g_5 =` | Added the approved portable firm type \(g_5=(\pi_2;f^\ast;(-(\beta c+c_R),\alpha\phi))\). It uses the existing competent-manager profile and elite organizational characteristic, so it introduces no new membership characteristic or organizational characteristic. |
| P-03 | `Fix a real verification or conversion input $c_R` | Defined \(c_R\geq0\) as a real verification, conversion, or complementary-training input—not a fee or transfer. |
| P-04 | `For a recognition index $\varrho\in[0,1]$` | Defined deterministic recognition intensity \(\varrho\), using a new symbol because \(\rho\) already denotes the positional fixed-point map. Recognition is not modeled as admission or placement risk. |
| P-05 | `All consumption sets and preferences on the original membership domain are unchanged.` | Preserved every original consumption set and preference ranking. The only added feasible managerial chain is \(\{m_1,m_{5.1}\}\); the portable labor membership receives the existing elite-condition labor factor. |
| P-06 | `\begin{equation}\label{eq:portable-prices}` | Extended the baseline price support with \(q_{5.2}=q_{4.2}\) and \(q_{5.1}=q_{4.1}+c_R\), and verified budget balance for \(g_5\). |
| P-07 | `D\equiv(\tau-1)r-c_R` | Defined the portable chain's resource advantage and maintained the approved nondegenerate region \(D>0\) and \(0<z<z+D<\mu k\). |
| P-08 | `\begin{equation}\label{eq:portable-indices}` | Reduced occupational choice to the upper envelope of \(U_N=\mu k\), \(U_P=(1+\varrho\eta)(z+D)\), and \(U_E=(1+\eta)z\). |
| P-09 | `\begin{equation}\label{eq:recognition-thresholds}` | Derived the activation threshold \(\varrho_A=z[\mu k-(z+D)]/[(z+D)(\mu k-z)]\) and distribution-free displacement threshold \(\varrho_D=z/(z+D)\), with \(0<\varrho_A<\varrho_D<1\). |
| P-10 | `\begin{proposition}[Imperfect recognition and displacement]` | Proved the three recognition regimes: baseline sorting below activation; nonelite/portable/incumbent coexistence between thresholds; and strict portable-route dominance at and above \(\varrho_D\). |
| P-11 | `\begin{equation}\label{eq:portable-cutoffs}` | Derived the coexistence cutoffs \(\eta_P\) and \(\eta_{EP}\), including their ordering and recognition comparative statics. |
| P-12 | `\begin{equation}\label{eq:portable-masses}` | Derived exact incumbent and portable sector masses for all three regimes. Added the bounded-support qualification that incumbent activity may vanish before the distribution-free dominance threshold. |
| P-13 | `\begin{equation}\label{eq:portable-clearing}` | Derived the competent-sector and leisure masses \(n^P\) and \(\sigma_0^P\); made existence conditional on both remaining positive. |
| P-14 | `Sorting and sector masses are unique on this interior branch` | Limited uniqueness to sorting and sector masses, apart from zero-measure cutoff types. No uniqueness is claimed for prices of inactive memberships. |
| P-15 | `\begin{corollary}[Career-chain displacement]` | Established strong-core and strong-Pareto support for the furnished absolute-status equilibria and proved that, at full recognition and \(D>0\), no equilibrium with positive private-goods consumption activates the incumbent elite school–firm chain. |
| P-16 | `The incumbent and portable firms have different manager profiles` | Flagged why the manuscript's single-group displacement theorem cannot be applied mechanically. The appendix instead replaces the two complete school–firm chains and all associated memberships. |
| P-17 | `\begin{equation}\label{eq:portable-burn}` | Derived excess resource use separately for incumbent and portable elite-format chains. |
| P-18 | `\label{eq:portable-output}` | Derived the exact aggregate-output identity and recorded that recognition has no generally monotone effect on total resource burn or output because substitution and demand expansion work in opposite directions. |
| P-19 | `Continue the parameters of Section~\ref{sec:example} and set $c_R=9/4$.` | Added the approved numerical continuation: \(D=3/4\), \(w_P=13/2\), \(\varrho_A=23/39\), and \(\varrho_D=23/26\). |
| P-20 | `The entire recognition path $\varrho\in[0,1]$ remains` | Verified that \(n^P>0\) and \(\sigma_0^P>0\) throughout the numerical path. At full recognition the incumbent is displaced, while total elite-format management and burn rise and output falls in the example. |
| P-21 | `This section is confined to the static absolute-status economy.` | Added an explicit scope boundary: the positional and dynamic sections continue to use the original group set \(G\) until Stage 3 authorial decisions are made. |
| P-22 | `\section{Portable Qualifications: Proofs}` | Added complete appendix proofs of price support, threshold ordering, upper-envelope sorting, bounded-support behavior, consistency, goods-market clearing, optimization, interior existence, comparative statics, strong-core support, chain displacement, and resource accounting. |
| P-23 | `\path{analysis/portability_extension.py}` | Added a reproducible companion check using exact rational arithmetic for the displayed algebra and a dense numerical scan over the full recognition interval. |
| P-24 | `where $N$ collects leisure and the payoff-equivalent` | Removed the obsolete numerical count of outside choices after the portable labor membership was added. This is a wording correction only. |
| P-25 | `Using \eqref{eq:portable-clearing}, aggregate output can be written` | Restored the required plus sign between the baseline-output term and the elite-format adjustment in the displayed output identity. The companion script verifies the corrected identity exactly. |

## Rejected

| ID | Recommendation or alternative | Reason |
|---|---|---|
| R2-01 | Interpret recognition as an individual admission or placement probability. | Rejected for this sub-branch because it would require expected-utility and rationing or matching primitives not present in the manuscript. The approved \(\varrho\) is deterministic recognition intensity. |
| R2-02 | Add a costless portable route under the running numerical parameters. | Rejected because literal costless access gives \(w_P=8.75>\mu k=8\), eliminating the intended interior outside option and changing the maintained configuration. |
| R2-03 | Use \(c_R=2\) in the numerical continuation. | Rejected because the competent-sector mass becomes nonpositive before the distribution-free displacement threshold. The approved \(c_R=9/4\) preserves the interior branch on all of \([0,1]\). |
| R2-04 | Model portability through a quota, license supply, or exogenous capacity constraint. | Rejected for Stage 2 because it adds scarcity and rationing primitives and obscures the recognition threshold mechanism. |
| R2-05 | Endogenize recognition through signaling, hidden information, reputation formation, or audience learning. | Rejected for Stage 2 because it would be a new model rather than the bounded qualification-portability extension the author approved. |
| R2-06 | Reuse \(\rho\) for recognition. | Rejected because \(\rho\) already names the positional equilibrium map. The extension uses \(\varrho\). |
| R2-07 | Claim that the incumbent always remains active throughout the intermediate interval. | Rejected for bounded-support taste distributions. The sub-branch states the correct support-dependent qualification. |
| R2-08 | Claim unique prices for inactive memberships. | Rejected because inactivity does not pin every individual membership price. The result claims only the uniqueness supported by the construction. |
| R2-09 | Infer that stronger recognition must lower total burn or raise output. | Rejected: substitution toward the cheaper chain can be offset by expansion of total elite-format demand. The theorem separates displacement from aggregate material performance. |
| R2-10 | Silently fold the new route into the positional dilution aggregate or transition map. | Rejected under the editorial protocol. Those integrations require author judgment and are expressly reserved for Stage 3. |

## Deferred

| ID | Exact searchable anchor or topic | Disposition |
|---|---|---|
| D2-01 | Integration of `\section{Qualification Portability and Recognition}` into the authoritative branch | Deferred to Stage 3. The present file remains a nonauthoritative formal sub-branch. |
| D2-02 | Front-end restructuring and abstract shortening | Deferred to Stage 3 as requested. No abstract, introduction, title, or roadmap text was changed in this sub-branch. |
| D2-03 | Qualification portability under positional status | Deferred pending an author decision about whether portable and incumbent routes enter the same dilution aggregate and with what recognition weight. |
| D2-04 | Qualification portability in the overlapping-generations transition | Deferred pending the positional decision and a choice about how \(c_R\), portable recognition, and route-specific masses enter the transition map. |
| D2-05 | Placement and compression of the theorem and proof | Deferred to Stage 3. The current placement maximizes auditability rather than front-end economy. |
| D2-06 | Endogenous credibility, audience learning, or heterogeneous recognition | Deferred as possible later extensions; none is necessary for the approved threshold result. |
| D2-07 | Production build under `\bibliographystyle{chicago}` | Deferred until `chicago.bst` is supplied or available. The sub-branch retains the manuscript's Chicago style; QA used a temporary `plainnat` copy only. |
| D2-08 | Duplicate `author` field at `@article{moldovanuselashi2007,` | Carried forward from Stage 1 without silent repair; awaits author approval. It does not prevent the temporary QA build. |

## Exact insertion boundaries

The sub-branch differs from authoritative v02 in exactly three textual hunks:

1. The authority header, beginning with `% TRUTH VERSION: elite_status-v02.tex`.
2. The main extension inserted immediately before the exact anchor `\section{Numerical Example}\label{sec:example}`.
3. The proof appendix inserted immediately before the exact anchor `\section{Positional Extension: Proofs}\label{app:positional}`.

No pre-existing body text was altered.

## Verification record

- The authoritative v02 source remained byte-for-byte unchanged at SHA-256 `1a25382edf830d9008ec7bd6b667f124c0a95783a0cf424fd5763ebcbdc31c5c`.
- The final sub-branch contains 2,005 lines and 164,439 bytes.
- `analysis/portability_extension.py` completed 10,000 exact rational checks of the threshold and output identities.
- A 20,001-point scan of \(\varrho\in[0,1]\) reproduced \(\varrho_A=0.589743589744\) and \(\varrho_D=0.884615384615\).
- On that scan, the minimum competent-sector mass was `0.004280977168` and the minimum leisure mass was `0.598186965563`, both strictly positive.
- All LaTeX references and citation keys resolve; no duplicate labels, missing references, or overfull boxes were detected.
- A full temporary QA build completed with `plainnat`, BibTeX, and all three supplied figures. The resulting 61-page letter-size PDF was visually inspected across the entire new main section and proof appendix; no clipping, overlap, broken glyph, or table-layout defect was found.
- The deliverable sub-branch retains `\bibliographystyle{chicago}` and does not contain the temporary QA style substitution.
