# Theorem Memorandum: Full-Product Dominance and the Boundary of Competitive Displacement

**Phase-2 deliverable of the JPE revision roadmap (2026-07-21).**
**Status: for coauthor sign-off. Not manuscript text.**
**Stress-tested: adversarial GE-theory pass 2026-07-21, verdict "sound with repairs"; all findings repaired herein (report + dispositions: `referee-reports/2026-07-21-memo-r1.md`).**
**Machine checks: `analysis/displacement_theorem.py` (all green).**

This memo states, proves, and stress-assesses the general result agreed in the Phase-1 decisions: the revised paper's headline is the distinction between *material dominance* and *full-product competitive dominance*, and the paper states explicitly that a feasible status-equivalent lower-cost technology would displace the incumbent elite type. Per the roadmap's decision gate, Section 7 assesses honestly whether the result carries more than its definition. Nothing here alters the manuscript's existing notation, assumptions, or verified results; integration is Phase 4 and requires separate sign-off.

---

## 1. Setting and the substitution operator

We work inside the framework of manuscript Section 3 (Ellickson–Grodal–Scotchmer–Zame 2006): group types $(\pi,\gamma,y) \in G$, memberships $m=(\omega,(\pi,\gamma,y))$, lists $\ell \in \Lambda$, a nonatomic agent space, and the group-equilibrium and core definitions stated there. Two framework facts used below: budget balance (equilibrium condition 1) is stated for **every** type in $G$, active or not (this is where the convention acquires teeth — see the verification items in Section 8); and utility is strictly increasing in private goods for each fixed list on the interior of the goods space, with the axis caveat of manuscript Appendix B.

Let $g=(\pi,\gamma,y)$ and $g'=(\pi,\gamma',y')$ be two group types in $G$ **with a common profile** $\pi$. For each list $\ell\in\Lambda$ define the *substituted list* $\ell[g\to g']$ by

$$\ell[g\to g'](\omega,g') = \ell(\omega,g') + \ell(\omega,g), \qquad \ell[g\to g'](\omega,g) = 0,$$

and $\ell[g\to g']=\ell$ on all other memberships: every seat held in a type-$g$ group is exchanged for the same seat in a type-$g'$ group. The common profile makes this well defined; the operation preserves total list length, so the uniform bound $\bar\ell$ is respected, and as a fixed map on the finite set $\Lambda$ it preserves measurability of assignments.

## 2. Definition: membership equivalence

**Definition 1 (Membership equivalence).** Type $g'$ is *membership-equivalent* to type $g$ (write $g' \sim g$) if they have a common profile and, for almost every agent $a$:

- **(E1) Qualification equivalence.** $(x,\ell)\in X_a \iff (x,\ell[g\to g'])\in X_a$: substitution preserves feasibility of every list, including any prerequisite structure (memberships that $g$-seats require, and memberships that $g$-seats qualify the holder for).
- **(E2) Utility equivalence.** $u_a(x,\ell) = u_a(x,\ell[g\to g'])$ for every $(x,\ell)\in X_a$ such that $(x,\ell[g\to g'])\in X_a$ as well.

(E2) is stated conditionally so that it is well posed even when (E1) fails — $u_a$ is defined only on $X_a$ — which is what lets Section 3's part (ii) say precisely *which* clause a candidate replacement fails. The proofs below use only the forward direction of (E1); the biconditional is retained because the substitution map is non-injective and the two-sided form is the natural notion, but nothing turns on the extra strength. Say $g'$ *strictly materially dominates* $g$ if $y'\geq y$ and $y'\neq y$: the replacement uses weakly fewer inputs and produces weakly more output in every good, strictly in at least one.

**Commentary — where the economics lives.** Memberships are indexed by group type, so a new type creates formally different membership objects. (E1)–(E2) are therefore *restrictions on preferences and consumption sets*, not a relabeling: they assert that agents attach the same direct utility to the replacement seats **and** that the replacement seats carry the same qualification consequences (a student seat that does not qualify its holder for elite management fails (E1), whatever the label on the door). Whether any feasible type satisfies them relative to an incumbent is precisely the question of what makes status credible — a primitive here, as the technology set is in any production economy. This answers roadmap §6.6: the definition does not assume the conclusion, because equivalence is a substantive joint restriction that most cheap entrants fail; part (ii) exhibits the failure *inside our own $G$*.

## 3. The theorem

**Theorem (Displacement boundary).**

**(i) Full-product dominance displaces — core version.** Suppose $g,g'\in G$, $g'\sim g$, and $g'$ strictly materially dominates $g$. Then no feasible state in which $\nu(g)>0$ *and a non-null set of agents consumes a strictly positive goods bundle* belongs to the strong core. Consequently, if endowments are desirable, every group-equilibrium state satisfying the same interiority proviso has $\nu(g)=0$ — and every equilibrium of manuscript Lemma 1 satisfies it, since almost every agent there has strictly positive net income and interior Cobb–Douglas demand.

**(ii) Material dominance without equivalence does not displace.** In the elite-status economy of manuscript Section 4 there is an open set of parameter vectors — containing the running example — on which:

  **(a)** *(the exact-sense exhibit)* the serious school $g_1$ strictly materially dominates the elite school $g_2$ in precisely the sense of (i): common profile $\pi_1$ and $y_{g_1}=(-r,0)\geq(-\tau r,0)=y_{g_2}$, strictly. It satisfies the utility clause (E2) — both schools carry the identical amenity factor $\delta_s$ — and fails *only* the qualification clause (E1): substituting $m_2\to m_1$ in the elite manager's list $\{m_2,m_{4.1}\}$ yields $\{m_1,m_{4.1}\}\notin X_a$, because the serious school does not confer $\omega_e$. Since no other type in $G$ shares a profile with either elite type ($\pi_3$ demands $\omega_e$ where $\pi_2$ demands $\omega_m$), no type in $G$ is membership-equivalent to either elite type, and (i) has no bite;

  **(b)** the elite types are active in equilibrium and the equilibrium state lies in the strong core;

  **(c)** *(the economic gloss)* the elite complex is strictly resource-dominated, $\alpha(c+r)<\beta c+\tau r$, so elite activity strictly lowers aggregate output as status taste spreads (manuscript Proposition 2): material dominance in the resource-productivity sense — the sense in which the public argument is conducted — likewise fails to displace.

**Proof of (i).** Let $(x,\ell)$ be feasible with $\nu(g)>0$ and let $S$ be the non-null set of agents with strictly positive bundles. Construct a blocking improvement for the grand coalition $A$. Set $\hat\ell_a = \ell_a[g\to g']$ for every $a$; by (E1) individual feasibility is preserved. Consistency: the memberships released from type-$g$ groups fill type-$g'$ groups seat for seat (common profile), so $\hat\nu(g') = \nu(g')+\nu(g)$, $\hat\nu(g)=0$, all other masses unchanged. Material balance: aggregate net output changes by $\nu(g)(y'-y)\geq 0$, $\neq 0$; let $j$ be a good with $y'_j>y_j$ and distribute the released surplus $\nu(g)(y'_j-y_j)>0$ of good $j$ uniformly across $A$ (free upward disposal keeps bundles in the consumption sets). By (E2) the list substitution leaves every agent's utility unchanged; the added goods leave almost every agent weakly better off and make every agent in $S$ strictly better off, since utility is strictly increasing at interior bundles. The grand coalition thus blocks $(x,\ell)$ in the strong sense (weak improvement a.e., strict on the non-null $S$), so the state is not in the strong core. Under desirable endowments, every group-equilibrium state is in the strong core (EGSZ Theorem 1, hypotheses verified in manuscript Appendix B); the contrapositive gives $\nu(g)=0$ at any equilibrium satisfying the proviso. At the equilibria of Lemma 1 the proviso holds: net incomes are strictly positive for almost every agent — leisure-takers have $w=k>0$ and elite managers $w_E=z>0$ by Assumption 1(i); note $z<k$ is possible within Assumption 1, so positivity, not size, is what the argument uses — and Cobb–Douglas demand is then interior. $\blacksquare$

**(i′) Pricing version — displacement without the welfare theorem.** The same conclusion follows from optimization and budget balance alone, without invoking the core, and therefore extends beyond the welfare theorem's reach. Consider any group equilibrium in which a non-null set of agents consumes an interior bundle (again, all equilibria of Lemma 1 qualify).

*Step 1 ($p\gg 0$).* If some good had price zero, an agent in the interior set could add the free good at unchanged cost $\leq p\cdot e_a$ and be strictly better off, contradicting optimization.

*Step 2 (aggregate price gap).* Budget balance holds for both types — condition 1 applies to every type in $G$, active or not — so $\sum_\omega \pi(\omega)\,[q(\omega,g)-q(\omega,g')] = p\cdot(y'-y) > 0$ by Step 1.

*Step 3 (arbitrage).* Suppose $\nu(g)>0$. Integrating the per-agent saving from full-list substitution over the population, $\int \big[q\cdot\ell_a - q\cdot\ell_a[g\to g']\big]\,d\iota = \nu(g)\,p\cdot(y'-y)>0$, so a positive-measure set of agents each realizes a strictly positive saving from substituting her own list. By (E1)–(E2) the substituted list is feasible and utility-identical; spending the saving on a strictly positive amount of *every* good yields a strictly preferred, affordable choice — strictly preferred whether or not the agent's current bundle is interior, since any positive multiple of the taste factor times a positive geometric mean beats a boundary utility of zero, and beats an interior utility by strict monotonicity. This contradicts optimization; hence $\nu(g)=0$. Note the argument never swaps a single seat: the saving is evaluated on the whole list, which is what (E1)–(E2) license.

The pricing version applies **in the positional equilibrium of manuscript Section 7**, where the welfare theorem fails — provided the positional objects are generalized as in Section 5 below, under which the substitution leaves the elite-class mass unchanged and (E2) holds at every fixed value of the externality argument. $\blacksquare$

**Proof of (ii).** At the running example ($k=2$, $r=c=1$, $\tau=4$, $\beta=\alpha=1.25$, $\phi=6$, $\mu=4$, $\lambda=2$, $\lambda^e=2.5$, $s=0.1$) Assumption 1 holds with strict inequalities ($z=5.75\in(0,8)$, $n\approx 0.114>0$, $\sigma_0\approx 0.598>0$) and the dominance condition of (c) is strict ($\alpha(c+r)=2.5<5.25=\beta c+\tau r$). Every equilibrium object is a closed-form continuous function of the parameter vector, so all strict inequalities persist on an open neighborhood; there Lemma 1 delivers the active-elite equilibrium and manuscript Theorem 1 places it in the strong core, giving (b). Clause (a) is verified against the manuscript directly: profiles from Section 4.1, the prerequisite $\ell(m_{4.1})\geq 1 \Rightarrow \ell(m_2)\geq 1$ hard-coded in consumption sets (line 263), and the common amenity factor $\delta_s$ for both schools (line 273); these are parameter-free, hence hold on the whole neighborhood. Machine verification of the openness claim (`analysis/displacement_theorem.py`): all conditions hold on a ±3% one-at-a-time grid and under 20,000 random joint ±1.5% perturbations; per-parameter symmetric margins are ±4% ($\alpha$), ±7% ($\lambda$, $\lambda^e$), and ≥±10% (all others). The honest scope note for the manuscript: the neighborhood is open but not large in every direction — raising $\alpha$ pushes $z$ toward $\mu k$ and, with the thin exponential tail at $s=0.1$, the elite mass grows fast enough to break interiority ($n>0$) well before the dominance inequality fails. Coexistence is robust; the *interior* configuration is what binds, exactly as Assumption 1 says. $\blacksquare$

**Remark 1 (the sharpest reading of (ii)).** Our economy already contains the "status without waste" entrant: the serious school costs $r<\tau r$, supplies the identical direct amenity, and fails to displace the elite school *only* at the qualification clause (E1). The boundary between (i) and (ii) is not an artifact of a sparse technology set — it runs through the middle of $G$ — and it is exactly the credibility of the qualification, not the school's amenity value, that the elite premium prices.

**Remark 2 (what a displacing entrant must supply).** By (i), an entrant type displaces the elite school if and only if it (a) confers $\omega_e$ itself — its graduates are accepted as elite managers, (E1) — and (b) is valued identically by students, (E2), at strictly lower resource cost. Precisely: in the augmented economy $G\cup\{g_2'\}$, the incumbent $g_2$ is inactive in *any* group equilibrium and any strong-core state satisfying the interiority proviso. (The statement is about all equilibria of the augmented economy, not about existence of one; existence would follow from EGSZ Theorem 2 upon verifying its hypotheses, which we do not need.) The theorem therefore locates the persistence of the burn in the infeasibility of (a) — a claim about what makes status credible, taken as primitive here and flagged as such (roadmap §5.2). The paper's existing caveat paragraph (manuscript lines 433–438) becomes a theorem plus one honest sentence.

## 4. Financing corollary

**Corollary (Competitive financing of membership production).** In any group equilibrium, for every type $g=(\pi,\gamma,y)\in G$: $\sum_\omega \pi(\omega)\, q(\omega,g) = -\,p\cdot y$. Any material shortfall ($p\cdot y<0$) is financed exactly by the aggregate membership payments of the group's own members — some of whom receive rather than pay — with no transfer from non-members anywhere in the price system. Combined with occupational indifference, this delivers the manuscript's compensation decomposition (Corollary 1) and coexistence condition (Proposition 1).

*Proof:* rearrangement of equilibrium condition 1. $\blacksquare$

Deliberately labeled a corollary of the framework, not a deep result, and deliberately *financing*, not incidence: the identity says who pays at equilibrium prices, not who bears the welfare burden — the latter needs the indifference conditions, which is exactly the work Corollary 1 and Proposition 1 do. Its value is the general statement that the clubs apparatus *determines who finances status production*, which the four-type economy then makes concrete. One short paragraph in the manuscript.

## 5. Positional compatibility (required manuscript adjustments — twofold)

For (i′) to span replacement types, **two** positional objects must be generalized, not one:

1. **The class mass**: $m = \iota\big(\{a : \ell_a(\omega_e, g)\geq 1 \text{ for some } g\}\big)$ — defined over the *characteristic* $\omega_e$, not the membership object $m_{4.1}$.
2. **The status factor**: attached to *any* employment seat carrying $\omega_e$, i.e., to $(\omega_e,\cdot)$-memberships generically, not to $m_{4.1}$ specifically. Under the current manuscript wording (factor on $m_{4.1}$; positional factor $1+\eta v(m)$ with $m$ counting $m_{4.1}$ holders, lines 273 and 486), a replacement type's $(\omega_e,g')$ seat would carry no status factor, (E2) would fail automatically for every entrant, and the displacement remark would be vacuous.

Definition 1 must correspondingly quantify over the externality argument in the positional regime: $u_a(x,\ell;m) = u_a(x,\ell[g\to g'];m)$ for all $m$. Given the two generalizations, the substitution preserves the set of $\omega_e$-holders, so $m$ is unchanged and (i′)'s comparison happens at fixed $m$ — the invariance the proof uses. With the current single elite-firm type in $G$, both generalizations have zero effect on any existing result; but they touch existing definitions and therefore require sign-off under the editorial covenant before integration.

## 6. What the theorem licenses (front-end preview)

The contribution sentence the revised abstract can defend:

> Competition eliminates organizations dominated in the space of complete products — memberships included — but not organizations dominated only in material production; when status is an institutionally produced membership, a school–firm complex that consumes more resources per unit of output than its rivals can therefore survive in the strong core, its shortfall financed at market prices by status-valuing members.

Guard-rail from the Phase-1 discussion: the statement is at the **complex** level. Elite *firms* remain materially superior firm-for-firm in the central configuration ($\alpha>1$); the report's own draft sentence ("materially inferior firms survive") must not be adopted, or the empirical recalibration of 2026-07-20 (gross premium requires $\alpha>1$) is undone.

Claims retired by the theorem: "no entrant offering status without waste" (lines 77, 429) is replaced by the exact statement (i)/(ii); the caveat paragraph (lines 433–438) is replaced by Remarks 1–2.

## 7. Decision gate: is the result trivial?

Honest assessment, per roadmap Phase 2, now informed by the adversarial pass. The proofs are short: (i) is a replacement block, (i′) is arbitrage, the corollary is a rearrangement. The referee's strategic read, which I share: part (i) alone would be called immediate by any EGSZ-literate reader. What survives hostile reading as content:

1. **The pair is the theorem.** (i) alone is the folk displacement argument made exact; (ii) alone is the paper's example. Stated *together* as a single two-part theorem, they characterize the boundary — and part (ii)(a) now exhibits the boundary in (i)'s exact sense inside the paper's own technology set: the serious school is the status-without-waste entrant, vector-dominating the elite school and failing only at the qualification clause. Neither half should be stated separately.
2. **The definition is the contribution.** (E1)–(E2) formalize what "the same product" means when products include memberships, and Remark 1 shows the definition doing real work. The manuscript version should let the definition and the school-pair instance carry the interpretation.
3. **(i′) is the only technically non-inherited piece.** It does not pass through the EGSZ welfare theorem and survives where that theorem fails (the positional regime, after the Section 5 generalizations). It is elementary, but it is ours, and it directly rebuts "the deepest result is inherited." Its two load-bearing conditions — break-even pricing of inactive types, and the interiority proviso — are exactly the pre-sign-off verification items in Section 8.

**Gate recommendation:** proceed, with the framing discipline above (one two-part theorem, remarks carrying the interpretation, financing corollary at one paragraph). One caution from the referee that I adopt: the defensive argument "a referee who calls the theorem trivial thereby concedes the paper's thesis" is for internal use only — it must not appear in the manuscript. If either coauthor reads Section 3 and still judges the content thin, the fallback in roadmap §6.6 (augmented-technology proposition for linked school–firm economies) is strictly weaker and both the referee and I recommend against it.

## 8. Scope limits and pre-sign-off verification items

What we do not claim:

- No theory of which status-equivalent technologies are feasible (reputation, credibility, incumbency): the feasible set $G$ remains a primitive, as in any production economy.
- No claim that prestige can never be copied cheaply — only that copying requires (E1)–(E2), which are economic restrictions, not labels.
- The common-profile requirement means the theorem compares like-for-like staffing; replacements that also economize on members (smaller profiles) are a genuine extension, not covered.
- Remark 2 makes no existence claim for augmented economies.

Verification items — **both CLOSED against the source (2026-07-21)**. Source: Ellickson–Grodal–Scotchmer–Zame, "The Organization of Production, Consumption and Learning," ch. 9 of *Institutions, Equilibria and Efficiency* (Springer 2006), pp. 149–185; PDF in `literature/` (file named "Ellickson et al 2007.pdf" — same chapter, misnamed).

1. **EGSZ budget-balance convention: CONFIRMED.** Section 9.3.6 (p. 159–160) states: "(1) Budget balance for group types. For each $(\pi,\gamma,y)\in G$: $\sum_\omega \pi(\omega)\,q(\omega,(\pi,\gamma,y)) + p\cdot y = 0$." Equality, quantified over all of $G$, no activity qualifier anywhere in the definition. (i′)'s Step 2 stands as written. Bonus support for Step 1: the same subsection remarks "Because utility functions are assumed monotone in private goods, private goods prices will be positive in equilibrium" — EGSZ's own assertion under their maintained monotonicity; our axis caveat means we keep the proviso-based one-line argument rather than citing this.
2. **Strong core definition: SOURCED** (p. 161–162): $(x,\mu)$ is in the strong core if no positive-measure $B\subset A$ and $B$-feasible state exist with $u'\geq u$ a.e. in $B$ and $u'>u$ on a positive-measure $C\subset B$ — exactly the blocking notion (i)'s proof uses. Also available: EGSZ Proposition 1 (p. 162): under desirable endowments the strong core *coincides with* the core. Integration item: the manuscript must state this definition in Section 3 so (i)'s proof is self-contained.

---

*Prepared by MDR/Claude, 2026-07-21; repaired same day after adversarial round 1 (`referee-reports/2026-07-21-memo-r1.md`). Verification: `analysis/displacement_theorem.py` — openness sweep for part (ii); aggregate-saving identity for the school example (arithmetic identity check only: (i′) is a proof, not a computation). Next step on approval: close the two verification items, then Phase 3 front-end rewrite against Section 6's contribution sentence.*
