# Handoff Note for João — "The Market for Elite Status"

*Prepared at Mike's direction on completion of the internal review process (July 2026). The current manuscript is `market-for-elite-status.tex` / `.pdf` (43 pages); everything below is in the repository.*

## What the paper now is

One economy, viewed at three levels, built on the general-equilibrium clubs framework of Ellickson, Grodal, Scotchmer, and Zame (2006), whose Theorem 1 (core equivalence) is the paper's engine.

- **Static core (Sections 4–6).** Elite schools sell status-conferring memberships; elite-run firms hire in the same labor market as competent rivals; everything is competitively priced. Results: the compensation decomposition (Corollary 1: gross premium = excess tuition − status discount, with zero incidence of elite tuition on gross salaries — the model's sharpest empirical prediction); coexistence of even output-inferior elite firms (Proposition 1); the efficient decline of output as status taste spreads (Proposition 2); and the central Theorem 1 — every such equilibrium is in the core, so competition cannot correct elite waste. Thesis: *markets work; material efficiency does not follow.*
- **Positional extension (Section 7).** When status is valued for scarcity (v(m) decreasing), preferences carry a widespread externality outside the clubs welfare theorems: the equilibrium is a unique, self-limiting fixed point (Proposition 4), no longer Pareto optimal or in the core (Proposition 5), with over-entry and a corrective membership tax whose output effect decomposes into de-entry, rebate, and incidence channels (Proposition 6).
- **Dynamics (Section 8, your terrain).** OLG frame: each generation inherits kₜ, plays the static club economy within the period, and transfers to the next via warm-glow gifts of the produced good (converted at rate θ). One condition — α(c+r) < βc+τr, the elite sector's resource-productivity deficit — governs the static output decline, the luxury property (richer economies endogenously support larger elites, Proposition 8), and the accumulation drag (Proposition 9). The economy converges to a steady state permanently poorer than its status-free counterfactual, with the path fully foreseen and no agent able or willing to deviate.
- **Appendix E.** The status margin (prices, wages, cutoff, elite mass) is invariant to the transfer motive within the degree-one preference class, and under pooled inheritance purely altruistic parents transfer nothing — so warm glow is the minimal transfer motive, not an evasion. The luxury/drag condition contains no preference parameters at all.

## How your original work maps in

Your two-period OLG formulation is the conceptual ancestor of Section 8, and its instincts survive in specific places: the tuition-as-investment idea became the within-period membership pricing; your savings margin became the transfer share ζ (the bequest share plays exactly the role your discount factor played); and your education-supply question is now answered by the school budget-balance conditions inside the club equilibrium. Two things changed for identifiable reasons, documented in the repository history: the early standalone OLG had internal inconsistencies at its steady state (the numerical example implied a negative gross return, hence negative old-age consumption), and a two-period life-cycle formulation with old-age consumption turns out to require the old cohort to own the capital stock, which destroys the leisure margin that anchors the entire wage system — this boundary is now stated honestly in Appendix E rather than papered over. The warm-glow formulation is what makes the static characterization carry over exactly, and Appendix E is the defense of that choice.

## Where your input is most wanted

1. **Dynasty-specific inheritance with forward-looking parents** — the extension the Discussion promises and the one referees will ask for. Note the sign the model implies: elite managers earn *lower net incomes*, so dynasty-specific bequests transmit *less* wealth down elite lines; the paper's persistence is institutional, not dynastic, and reconciling the two is the open problem.
2. **Intertemporal welfare** — the paper deliberately claims nothing about path efficiency (Diamond-type dynamic inefficiency and the warm-glow welfare-criterion question are cited but unresolved).
3. **The dynamics numerics generally** — Section 8's example (ζ=0.8, θ≈5.14, k\*=2) is a demonstration, not a calibration, by explicit policy.

## House rules (please follow; each has a reason recorded in the repo)

1. **One sentence per line** in all LaTeX prose (Mike's convention; makes review diffs legible).
2. **Notation covenant** (stated in Section 3): lowercase = parameters, functions, elements; capitals = sets; calligraphic = sets of sets; blackboard = number systems; bars = aggregates; every symbol defined at first use; exceptions are explicitly listed in the conventions paragraph. Do not introduce a symbol without defining it there and then.
3. **Machine verification.** Every algebraic claim in the paper is verified in `analysis/` (three scripts; run `python3 analysis/static_model.py` etc. from the repo root — all must end green). If you change any equilibrium formula, parameter, or quoted number, update the corresponding script *first* and let the assertion tell you whether the paper is right. Four rounds of adversarial review are archived in `referee-reports/`; every error those rounds caught was of a kind the scripts now guard against.
4. **Propositions state only what is proven** — general or explicitly conditional. Example facts live in the surrounding prose, labeled as illustrations. No claims from examples.
5. **Neutral framing throughout** (no politically coloured language), and prose in the register of Mike's published papers: complete sentences, sparing em-dashes, first-person-plural ownership of claims.

## Build

```sh
python3 analysis/static_model.py && python3 analysis/positional_model.py && python3 analysis/dynamic_model.py
pdflatex market-for-elite-status && bibtex market-for-elite-status && pdflatex market-for-elite-status && pdflatex market-for-elite-status
```

The bibliography (`elite-status-refs.bib`) is fully verified against publisher sources. The strategic submission target is JPE; the standing referee-risk items and the reasoning behind each declined piece of pre-submission work are recorded in `referee-reports/2026-07-20-r3-r4-final.md`.
