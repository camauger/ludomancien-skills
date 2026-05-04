---
name: ttrpg-supplement-reviewer
description: >
  Review TTRPG supplements for publication readiness: villain supplements, adventure modules,
  setting toolkits, bestiaries, player options, zines. Structured 6-axis editorial audit
  (writing, mechanics, table utility, structure, brand alignment, publication verdict) with
  multi-system validation (D&D 5e 2014/2024, PF2e, OSR, narrative) and configurable brand
  scoring (Fantasy Vixens, Ludomancien, custom). Use on "review my supplement", "is this
  publishable", "critique this", "editorial feedback", "check this stat block", "ready for
  DriveThruRPG", "what needs fixing", "act as editor", "review like a publisher", or any
  TTRPG manuscript quality/completeness assessment. Also triggers on "honest feedback",
  "what's wrong with this", "improve before release". NOT for listings/sales strategy
  (digital-product-evaluator), prose tics (editorial-tic-auditor), or cliché audits
  (ttrpg-cliche-buster). This evaluates the whole product as a publication.
---

# TTRPG Supplement Reviewer

Produce structured, actionable editorial reviews of TTRPG supplements at manuscript stage.
The review reads like a professional editorial report — the kind a publisher's editor would
deliver before greenlighting production. Honest, specific, constructive.

---

## Before You Begin

1. **Identify the game system.** Load `references/system-mechanics.md` for the relevant
   system section. If the system is not specified, infer from stat blocks, terminology, or ask.
2. **Identify the product type.** The audit axes adapt weight based on product type (see below).
3. **Check for brand context.** If the supplement is for a known brand (Fantasy Vixens,
   Ludomancien, etc.) or the user specifies brand expectations, load `references/brand-profiles.md`.
   If no brand context exists, skip Axis 6 or run it as generic market-fit.
4. **Check for stat blocks.** If the supplement contains stat blocks with CR/level ratings,
   load `references/stat-block-validation.md` for the calculation protocol.

---

## Product Types and Axis Weighting

Not every axis matters equally for every product. Use this weighting guide to calibrate
depth and emphasis. The axis always appears in the report; the weight determines how much
space and scrutiny it receives.

| Product Type | Writing | Mechanics | Table Utility | Structure | Brand | Examples |
|---|---|---|---|---|---|---|
| Villain supplement | ●●●○ | ●●●● | ●●●● | ●●●○ | ●●●● | Maren, Yrsa Kett |
| Adventure module | ●●●○ | ●●●○ | ●●●●● | ●●●●● | ●●○○ | One-shots, campaigns |
| Setting toolkit | ●●●●● | ●●○○ | ●●●● | ●●●○ | ●●●○ | Settlement books, region guides |
| Bestiary / monsters | ●●○○ | ●●●●● | ●●●○ | ●●●○ | ●●○○ | Monster collections |
| Player options | ●●○○ | ●●●●● | ●●○○ | ●●●● | ●●○○ | Subclasses, backgrounds, feats |
| Zine / anthology | ●●●●● | ●●○○ | ●●●○ | ●●●●● | ●●●● | Zarathar zines, essay collections |
| System-agnostic | ●●●●● | — | ●●●● | ●●●○ | ●●●○ | GM advice, random tables |

●= minimal attention  ●●●●●= maximum scrutiny  —= skip axis

---

## The Six Axes

Every review covers all applicable axes in order. Each axis produces:
- A **diagnostic** (what's working, what isn't, with specific citations from the text)
- A **verdict** (Strong / Adequate / Needs Work / Blocking Issue)
- **Actionable recommendations** (not vague directions — concrete edits or additions)

### Axis 1 — Writing Quality

Assess the prose at document level, not line level (line-level tics are the domain of
`editorial-tic-auditor`).

**Evaluate:**

- **Voice consistency.** Does the document maintain a coherent authorial voice? Are there
  jarring register shifts between sections (e.g., literary monologue → dry game text → casual
  advice) without intentional transitions?
- **Redundancy.** Are the same ideas repeated across sections without deepening them? Count
  the restatements. If a theme is stated >3 times without new information or new angle, flag
  as redundant.
- **Economy.** Is the text *earning* its word count? Every paragraph should either (a) give
  the GM information they can use, (b) set tone the GM can channel, or (c) provide mechanical
  reference. Prose that does none of these is dead weight.
- **Monologue / flavor text quality.** If the supplement includes in-character text (villain
  monologues, read-alouds, journal entries), evaluate as *writing* — rhythm, specificity,
  emotional credibility. Generic fantasy prose is a product flaw.
- **Transition quality.** How does the document move between voice-of-character and
  voice-of-designer? Abrupt transitions without framing create reader disorientation.

**Verdict criteria:**
- Strong: Voice is distinctive, prose is economical, flavor text could stand alone as writing.
- Adequate: Competent but unremarkable. No major problems, no memorable passages.
- Needs Work: Redundancies, register shifts, or generic prose that weakens the product.
- Blocking: Writing quality would generate negative reviews.

---

### Axis 2 — Mechanical Coherence

Validate every game-mechanical element against the declared system. Load the relevant
section from `references/system-mechanics.md` before evaluating.

**Evaluate:**

- **Stat block accuracy.** For any creature with a CR/level, run the validation protocol
  from `references/stat-block-validation.md`. Check: AC calculation (armor + shield + Dex),
  HP calculation (hit dice formula vs. declared HP), ability score → modifier consistency,
  saving throw proficiency bonus, skill bonuses, attack bonus (proficiency + ability mod),
  damage dice (weapon base + ability mod + any declared bonuses — flag unexplained bonuses),
  spell save DCs.
- **CR / encounter balance.** Does the declared CR match the offensive and defensive profile?
  A CR that is off by >1 in either direction is a mechanical flaw that experienced GMs will catch.
- **Feature interactions.** Do the creature's features create unintended loops, exploits, or
  dead abilities? (Example: a frightened condition that the creature's own aura prevents allies
  from suffering — useful against PCs but makes the feature text confusing.)
- **System version compatibility.** If the product declares dual compatibility (e.g., 5e
  2014/2024), check for known breaking changes between versions (exhaustion rules, weapon
  mastery, revised conditions). Flag any mechanic that works in one version but is ambiguous
  or broken in the other.
- **Magic item formatting.** Items should follow the system's convention for type, rarity,
  attunement, and property description.
- **DC calibration.** Flag if >60% of DCs in the document are the same value (the "DC 15
  problem" — AI-generated content anchors to 15 as a default "medium" difficulty). Varied
  DCs (10–18 range for CR 5–15 content) indicate intentional calibration.

**Verdict criteria:**
- Strong: All math checks out, CR is defensible, features are clean.
- Adequate: Minor arithmetic issues (1–2 errors) that don't affect play significantly.
- Needs Work: CR mismatch >1, multiple calculation errors, or version-ambiguous mechanics.
- Blocking: Stat blocks would not survive table play. Math is visibly wrong.

---

### Axis 3 — Table Utility

The most important axis for published TTRPG products. This answers: *can a GM pick this up
and run it without additional prep?*

**Evaluate:**

- **Playable scenes.** Does the supplement provide scenes a GM can run as-is? A scene needs:
  a situation (what's happening), a trigger (what brings PCs in), named NPCs with enough
  personality to improvise, a decision point (what must PCs choose), and consequences
  (what happens based on the choice). If the supplement describes *concepts* without providing
  *scenes*, that's a table utility failure.
- **Read-aloud text.** Are there read-aloud passages for key moments? Are they the right
  length (2–4 sentences for most situations, 4–6 for dramatic reveals)? Do they contain
  mechanics or meta-language that would break immersion?
- **GM guidance.** Does the text tell the GM *how* to use this material? Behavioral cues
  for NPCs (voice, mannerisms, tells), tactical notes for combat encounters, branching
  logic for social scenes.
- **Quick reference.** Can critical information be found in 10 seconds during play? Stat
  blocks should be near the scene that uses them. Key NPC motivations should be visible
  without flipping pages. Reference tables should be self-contained.
- **Reaction tables / branching.** For NPCs and villains: does the supplement provide
  "If the PCs do X, then Y" guidance? A villain supplement without situational reactions
  forces the GM to improvise the most critical interactions.
- **Maps and spatial information.** If the supplement describes locations, is there enough
  spatial information (map, description, dimensions) to run an encounter there? Even a
  schematic sketch beats a paragraph of room description.

**Verdict criteria:**
- Strong: A GM could run this at the table with zero additional prep.
- Adequate: Needs 15–30 minutes of GM prep to fill gaps.
- Needs Work: Major scenes are conceptual, not executable. GM must create content.
- Blocking: This is a lore document, not a game supplement.

---

### Axis 4 — Editorial Structure

The information architecture of the product as a document.

**Evaluate:**

- **Section order.** Does the document present information in the order a GM needs it?
  For villain supplements: identity → motivation → methods → mechanics → scenes → hooks.
  For adventures: overview → act structure → encounters → appendices.
  For setting toolkits: overview → locations → NPCs → hooks → random tables.
- **Page budget.** Is space allocated proportionally to utility? A 20-page villain supplement
  that spends 8 pages on backstory and 2 on playable scenes has an inverted budget. Content
  that the GM reads once (lore) should take less space than content the GM references
  repeatedly (stat blocks, reaction tables, scene frameworks).
- **Cross-references.** When the text mentions a stat block, NPC, item, or location defined
  elsewhere, is there a page reference or clear label? Missing cross-references force page-flipping.
- **Completeness.** Does the supplement contain everything it promises? Check: table of
  contents vs. actual sections, promised stat blocks vs. delivered stat blocks, campaign
  hooks vs. developed hooks. Incomplete products generate the most negative reviews.
- **Appendix / reference material.** Does the supplement consolidate reusable material
  (stat blocks, item cards, handout-ready documents, summary tables) in an appendix
  section? A GM preparing a session wants a "rip and use" section.
- **Conventions consistency.** Formatting: are stat blocks in the same format throughout?
  Are DC presentations consistent (DC 15 vs. DC15 vs. Difficulty 15)? Are bold/italic
  conventions stable?

**Verdict criteria:**
- Strong: Logical flow, good page budget, complete, well-referenced.
- Adequate: Minor structural issues. Some sections could be reordered.
- Needs Work: Page budget is inverted or sections are incomplete.
- Blocking: Missing promised content. Document structure fights the reader.

---

### Axis 5 — Brand Alignment

*Skip this axis if no brand context exists. Run as generic market-fit assessment if the
user hasn't specified a brand but wants market positioning feedback.*

Load `references/brand-profiles.md` for the relevant brand.

**Evaluate:**

- **Promise match.** Does the supplement deliver what the brand promises to its audience?
  (e.g., Fantasy Vixens promises dark fantasy + intimate tension + morally complex female
  antagonists. A villain supplement under that brand that lacks the intimate dimension fails
  brand alignment even if the villain is excellent.)
- **Register.** Does the prose hit the brand's register? (Literary noir vs. pulp action vs.
  academic analysis vs. zine-punk — each brand has a voice.)
- **Audience expectations.** Would the target audience *recognize* this as part of the brand?
  If a regular buyer would be surprised or disappointed, that's a brand-fit problem.
- **Differentiation.** Does this supplement do something the brand hasn't done before, or
  does it repeat existing products? New entries should expand the brand's range, not duplicate.
- **Cross-product coherence.** If the brand has a catalog, does this supplement fit the
  quality tier and content expectations set by previous releases?

**Verdict criteria:**
- Strong: Unmistakably on-brand. Expands the line.
- Adequate: On-brand but could be from any similar publisher.
- Needs Work: Brand identity is diluted. The product doesn't need this brand to exist.
- Blocking: Publishing this under the brand would confuse or disappoint the existing audience.

---

### Axis 6 — Publication Verdict

This is the synthesis. Not a separate evaluation — a judgment drawn from the five axes above.

**Produce:**

1. **A summary table** showing each axis verdict (Strong / Adequate / Needs Work / Blocking).
2. **A publication readiness rating:**
   - **Ready** — Publishable with minor copyediting.
   - **Almost** — One revision pass needed. Specific blocking issues identified.
   - **Not Yet** — Multiple structural or mechanical issues. Needs significant revision.
   - **Rethink** — Fundamental concept, scope, or brand-fit problems that copyediting won't fix.
3. **A prioritized action list** — Numbered, in order of impact. Each item specifies:
   what to change, why it matters, and how to do it. Maximum 7 items — force-rank if more exist.
4. **Estimated revision scope** — Rough time/effort to reach "Ready" status.

---

## Report Format

The report should read as a professional editorial document. Use this structure:

```
# Rapport Éditorial — [Product Title]

## Observation Liminaire
[1–3 sentences: what type of product, what system, what brand context if any.
Flag any fundamental misalignment before the detailed review begins.]

## Axe 1 — Qualité d'Écriture
[Diagnostic, citations, verdict]

## Axe 2 — Cohérence Mécanique
[Diagnostic, stat block validation results, verdict]

## Axe 3 — Utilité à la Table
[Diagnostic, scene-by-scene assessment, verdict]

## Axe 4 — Structure Éditoriale
[Diagnostic, page budget analysis, verdict]

## Axe 5 — Alignement Marque
[Diagnostic, brand-profile comparison, verdict — or skip if generic]

## Verdict de Publication
[Summary table + readiness rating + prioritized action list]

## Prochaines Étapes
[Ordered, concrete, with clear sense of direction]
```

**Language:** Match the language of the submitted document. If the supplement is in English,
review in English. If in French, review in French. If the user explicitly requests a different
language, comply.

**Tone:** Professional editor, not cheerleader. Honest about problems, specific about
solutions, respectful of the work already done. The goal is to make the product better,
not to demonstrate how clever the reviewer is.

---

## Comparative Review Mode

When the user submits **two versions** of the same supplement (v1 and v2, or draft and
revision), switch to comparative mode:

1. **Identify what changed** between versions. List additions, removals, and modifications.
2. **Evaluate each change** — did it improve, worsen, or leave the axis unchanged?
3. **Identify what was NOT addressed** — problems from v1 that persist in v2.
4. **Provide a delta verdict** — how the readiness rating has shifted.
5. **Update the action list** — reprioritize based on remaining issues.

This mode is important for iterative development. The user needs to see progress
and remaining distance, not a full re-review that ignores the work they just did.

---

## Interaction with Other Skills

This skill is the **whole-product reviewer**. It identifies problems but delegates
specialized fixes:

- **Prose-level tic detection** → hand off to `editorial-tic-auditor`
- **Originality / cliché audit** → hand off to `ttrpg-cliche-buster`
- **Product listing / pricing strategy** → hand off to `digital-product-evaluator`
- **Print layout / production design** → hand off to `ttrpg-print-design`
- **Stat block creation** (not just validation) → hand off to system-specific creation skills

When a problem falls squarely in another skill's domain, note it in the report and
recommend the handoff explicitly. Do not attempt to replicate another skill's protocol —
identify, flag, delegate.

---

## Edge Cases

**No stat blocks:** Skip Axis 2 mechanical validation. Focus on internal consistency
of whatever system-adjacent content exists (DCs, ability checks, skill references).

**System-agnostic supplements:** Skip Axis 2 entirely. Redistribute weight to Axes 1, 3, 4.

**Very short products (<10 pages):** Compress the report. Each axis gets 2–3 sentences
instead of full sections. The verdict and action list remain full-length.

**Multiple game systems in one product:** Validate each system separately in Axis 2.
Flag cross-system consistency issues (does the PF2e version of the creature feel like
the same threat as the 5e version?).

**User submits only a section, not a complete product:** Review what's provided. Note
clearly what can and cannot be evaluated from a partial submission. Do not invent context.

---

## Reference Files

Load these as needed — not all at once.

- `references/system-mechanics.md` — System-specific validation rules, version differences,
  common errors per system. Sections: D&D 5e 2014, D&D 5e 2024, Pathfinder 2e, OSR
  (B/X + OSE), narrative systems (PbtA, Blades, Fate).
- `references/brand-profiles.md` — Brand identity profiles with register, audience,
  promise, and red flags. Includes: Fantasy Vixens, Ludomancien, and a template for
  custom brand profiles the user can define.
- `references/stat-block-validation.md` — Step-by-step CR calculation protocol for D&D 5e
  (2014 and 2024 DMG methods), PF2e creature building benchmarks, and OSR HD-based
  validation. Includes damage-per-round benchmarks by CR, effective HP multipliers, and
  common AI errors in stat block generation.
