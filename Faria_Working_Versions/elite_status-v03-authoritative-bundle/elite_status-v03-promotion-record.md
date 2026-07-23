# Promotion Record: `elite_status-v03.tex`

## Promotion decision

On July 23, 2026, the author explicitly approved promotion of
`elite_status-v03.tex` from the completed Stage 3 static-portability integration
candidate to the sole authoritative manuscript.

The promoted file begins:

```tex
% TRUTH VERSION: elite_status-v03.tex
% FILE ROLE: AUTHORITATIVE MANUSCRIPT
% PREVIOUS TRUTH VERSION: elite_status-v02.tex; SUPERSEDED
% PRE-PROMOTION CANDIDATE SHA256: 2c5be85a58fb60ad6152424fe0ebdb35081b0246951ef27829489de6953eccf7
% BASE SHA256 (elite_status-v02.tex): 1a25382edf830d9008ec7bd6b667f124c0a95783a0cf424fd5763ebcbdc31c5c
% PORTABILITY SUBBRANCH SHA256: d77fad7748d2a287ad9ff3657beaaf7d947f8511695d825befc6dae693ee8245
% DOCUMENT: Journal of Political Economy Draft
```

## Authority after promotion

- `elite_status-v03.tex` is the sole authoritative manuscript.
- `elite_status-v02.tex`, `elite_status-v01.tex`, and all earlier manuscript
  versions are superseded and must be ignored unless the author explicitly
  references them.
- `elite_status-v02-portability-subbranch.tex` remains a nonauthoritative
  development branch preserved for provenance.
- `elite_status-v03-stage3-integration-log.md` remains the historical record of
  how the pre-promotion candidate was constructed.
- `elite_status-v03-stage3-integration-bundle.zip` preserves the exact
  pre-promotion candidate.
- `elite-status-refs-v02.bib` remains the correct companion bibliography despite
  its filename.
- The three supplied figure PDFs remain the correct graphics.

## Exact change

Promotion changed only the initial comment header:

1. `% TRUTH VERSION: elite_status-v02.tex` became
   `% TRUTH VERSION: elite_status-v03.tex`.
2. The revision-candidate line was removed.
3. The candidate file-role line was replaced by
   `% FILE ROLE: AUTHORITATIVE MANUSCRIPT`.
4. The previous truth version was marked superseded.
5. The exact pre-promotion candidate hash was retained in the header.

No manuscript text, notation, primitive, maintained assumption, equation,
theorem, proposition, corollary, proof, label, citation, bibliography entry, or
figure was changed.

## Hash chain

| Artifact | SHA-256 |
|---|---|
| Authoritative v01 source | `01357eda1bec9dd0e9908d0673adf9bd8d00c6c3c71ae4fd6702d1b2869c8e66` |
| Authoritative v02 source, now superseded | `1a25382edf830d9008ec7bd6b667f124c0a95783a0cf424fd5763ebcbdc31c5c` |
| Approved Stage 2 portability sub-branch | `d77fad7748d2a287ad9ff3657beaaf7d947f8511695d825befc6dae693ee8245` |
| Pre-promotion v03 candidate | `2c5be85a58fb60ad6152424fe0ebdb35081b0246951ef27829489de6953eccf7` |
| Promoted authoritative v03 | `721eab3beee8956680f68d3851637e434d231de53a45a1c31a24c12977ab0762` |

## Verification

- The manuscript body from `\documentclass` through `\end{document}` is
  byte-for-byte identical to the pre-promotion candidate preserved in
  `elite_status-v03-stage3-integration-bundle.zip`.
- The promoted source contains 2,134 lines and 163,511 bytes.
- A complete temporary QA build using `plainnat` completed with BibTeX and four
  LaTeX passes.
- All 52 cited bibliography entries rendered.
- All labels and references resolved.
- No missing-file, undefined-reference, duplicate-label, overfull-box, or PDF
  bookmark warning appeared.
- The output remained a 66-page letter-size PDF.
- `analysis/portability_extension.py` again completed 10,000 exact rational
  checks and the 20,001-point recognition scan.
- The recognition scan reproduced
  \(\varrho_A=0.589743589744\),
  \(\varrho_D=0.884615384615\),
  minimum \(n^P=0.004280977168\), and
  minimum \(\sigma_0^P=0.598186965563\).
- The deliverable source retains `\bibliographystyle{chicago}`. The temporary
  QA substitution is not present in the authoritative file.

## Next branch

The next substantive step is a fresh independent-referee assessment beginning
from the promoted `elite_status-v03.tex`. That branch must treat v03 as its sole
manuscript authority, use the revision records only as provenance, and make no
manuscript edits while acting in the referee role.
