# The Market for Elite Status — v04 Package

## Authoritative source

The authoritative manuscript in this package is:

`elite_status-v04.tex`

Its exact source-control header begins:

```text
% TRUTH VERSION: elite_status-v04.tex
% FILE ROLE: AUTHORITATIVE MANUSCRIPT
% PREVIOUS TRUTH VERSION: elite_status-v03.tex; SUPERSEDED
```

The authoritative manuscript SHA-256 is:

`f6392439f7ebf54f7b995e28583af2dadfac4972c0f5c861688496ecd61fd11a`

Version v04 supersedes v03. The positioning candidate and all earlier manuscript
versions should be ignored when reviewing or editing this package.

## Package contents

- `elite_status-v04.tex` — authoritative manuscript
- `elite-status-refs-v02.bib` — matching bibliography database
- `figures/status_taste_comparative_statics.pdf`
- `figures/positional_tax.pdf`
- `figures/dynamics_collapse.pdf`
- `POSITIONING-MEMO.md` — record of the bounded v03-to-v04 positioning pass
- `SHA256SUMS.txt` — checksums for the substantive package files

The separately uploaded file named `references.bib` is not the bibliography for
this manuscript and is intentionally excluded.

## Compilation

From this directory, use:

```bash
pdflatex elite_status-v04.tex
bibtex elite_status-v04
pdflatex elite_status-v04.tex
pdflatex elite_status-v04.tex
```

The manuscript requests the BibTeX style `chicago.bst`. The compilation environment
must provide that style. The current verification environment did not contain
`chicago.bst`; consequently, citation and full-document verification was also run
with a temporary `plainnat` substitution. That temporary substitution is not
present in the authoritative source.

## Verification record

- All 52 citation keys resolve against `elite-status-refs-v02.bib`.
- All 78 labels are unique and all internal cross-references resolve.
- The theorem, proposition, lemma, corollary, assumption, definition, and remark
  inventories are unchanged from v03.
- The formal framework through the discussion and the complete appendices are
  byte-for-byte unchanged from v03.
- The manuscript and all three supplied figures load successfully.
- v04 and v03 have the same rendered page count under identical verification
  conditions.

Package assembled July 23, 2026.
