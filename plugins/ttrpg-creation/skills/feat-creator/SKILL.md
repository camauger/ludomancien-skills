---
name: feat-creator
description: >
  Create complete custom feats for D&D 5e 2024, formatted to match the
  2024 Player's Handbook style. Covers all four feat categories: Origin
  feats (level 1, no prerequisite, no ASI), General feats (level 4+,
  +1 Ability Score Increase included — the 2024 half-feat structure),
  Fighting Style feats (Fighting Style feature prerequisite), and Epic
  Boons (level 19+, ASI up to 30). Each feat ships with a PHB-format
  entry (name, category, prerequisite, repeatable flag, named benefits),
  calibration against named official feats, a lore paragraph and 1–2
  plot hooks. Produces ONE feat per call or a small thematic set of
  2–4 linked feats (e.g. a knightly order chain: 1 Origin + 2 General +
  1 Epic Boon). Use on "crée un don", "create a feat", "custom feat",
  "homebrew feat", "origin feat custom", "epic boon for my barbarian",
  "half-feat homebrew", "feat chain", "don pour mon paladin", "fighting
  style homebrew", "feat for my campaign", "balance this feat idea".
  Boundary: class and subclass features (Eldritch Invocations, Battle
  Master maneuvers, Metamagic, monk techniques) are NOT feats — out of
  scope. Backgrounds referencing an Origin feat are built by the
  backgrounds skill; when that background needs a CUSTOM Origin feat,
  this skill is the authority. Spells use spell-creator; magic items
  use magic-item-creator; validating an existing supplement uses
  ttrpg-supplement-reviewer. Targets 2024 rules only.
---

# Feat Creator

Create publication-ready custom feats for D&D 5e (2024 rules), formatted
to match the 2024 Player's Handbook style. The output is what a
publisher's mechanical designer would deliver for a player-options
supplement, a campaign primer, or an adventure's signature reward.

The skill is mechanical *and* narrative: category discipline and
calibration against named official feats are non-negotiable, but a feat
without an identity, an origin, and a notable practitioner is just a
stat bump with a label.

---

## Scope and Boundary

This skill covers **standard 5e 2024 feats** across all four categories.

| In scope | Out of scope |
|---|---|
| Origin feats (level 1, via background, no ASI) | Class/subclass features (Eldritch Invocations, Battle Master maneuvers, Metamagic, monk techniques) |
| General feats (level 4+, +1 ASI included) | 2014-format feats and 2014 → 2024 feat conversion (use adventure-converter for module-wide conversion) |
| Fighting Style feats (Fighting Style feature prerequisite) | New class or subclass design |
| Epic Boon feats (level 19+, ASI up to 30) | Spells (use spell-creator) |
| One feat per call, or a thematic set of 2–4 linked feats | Magic items, including charged effects (use magic-item-creator) |
| Repeatable flag where the structure makes it safe | Editorial review of an existing supplement (use ttrpg-supplement-reviewer) |

**Boundary with `backgrounds`:** that skill builds complete backgrounds,
which *reference* an Origin feat. When the background calls for a custom
Origin feat, this skill designs the feat (mechanics, calibration, lore);
the background then references it by name.

**Boundary with monster design:** creature abilities are never feats —
use `monster-creator`.

---

## Before You Begin

Five things to settle before designing:

1. **Concept.** What is this feat *about*? "The reflexes of someone who
   grew up dodging dockside cranes" beats "a Dexterity feat." Without a
   concept, you build a stat bump.

2. **Category.** The category fixes the template, the access point, and
   the power band:

   | Category | Access | ASI | Power position |
   |---|---|---|---|
   | Origin | Level 1, via background | none | Floor — never must-pick |
   | General | Level 4+ feat slots | +1 (max 20) | The homebrew reference |
   | Fighting Style | Fighting Style feature | none | Narrow, combat-only |
   | Epic Boon | Level 19+ | +1 (max 30) | Capstone, rule-breaking |

   Load `references/feat-categories-2024.md` for the full anatomy of
   each category, official examples dissected, and the routing decision
   tree when a concept straddles two categories.

3. **Prerequisites.** Only for General feats (level, ability score 13+,
   class feature, or training) and the fixed gates of Fighting Style /
   Epic Boon. A prerequisite must gate something real — see
   `references/balance-and-anti-patterns.md`.

4. **Power budget.** Which 2–3 official feats occupy the nearest niche?
   If you cannot name them, the category is probably wrong. Load
   `references/power-budgets-and-benchmarks.md` for floor/ceiling
   benchmarks per category and quantified effect costs.

5. **Identity hook.** The one thing that makes this feat *itself* and
   not interchangeable with an official feat of the same niche. The
   hook is usually in the *trigger condition*, the *secondary effect*,
   or the *narrative texture* — not in bigger numbers.

If any of these is unclear, ask before designing. In non-interactive
contexts (batch generation, orchestrated calls), state your assumptions
explicitly in the deliverable and proceed.

---

## The Six-Step Creation Workflow

Every feat passes through these steps. Output assembles them into a
PHB-style entry.

### Step 1 — Concept and Name

- **Name.** Distinctive, evocative, not generic. "Lanternbearer's
  Vigil" beats "Improved Alertness." Epic Boons follow the official
  naming scheme: "Boon of [the] X."
- **One-sentence identity.** Write it before any mechanics: "the feat
  for characters who [fantasy]." Every benefit must serve this sentence.
- Avoid names that collide with official feats or imply a different
  category (don't name an Origin feat "Boon of…").

### Step 2 — Category and Prerequisites

- Confirm the category against the decision tree in
  `references/feat-categories-2024.md`, then apply its header template
  *exactly*:
  - `*Origin Feat*`
  - `*General Feat (Prerequisite: Level 4+[, …])*`
  - `*Fighting Style Feat (Prerequisite: Fighting Style Feature)*`
  - `*Epic Boon Feat (Prerequisite: Level 19+[, …])*`
- General feats: pick the ASI's short thematic list (1–3 scores).
- Add at most one substantive prerequisite beyond the level gate, and
  only if it shapes who benefits.

### Step 3 — Mechanical Design

- **2–3 named benefits maximum — not counting the Ability Score
  Increase — and exactly one signature.** The signature is the
  benefit the player will tell stories about; the others are support.
  All benefits serve the Step 1 identity sentence — a grab bag is a
  design failure.
- Build from the bricks in `references/feat-effect-library.md`: resource
  patterns (once per turn / 1 per Long Rest / PB per Long Rest /
  recharge), combat riders, exploration and social bricks, the Magic
  Initiate and Fey-Touched chassis for spell-granting feats.
- **Action economy is the danger zone.** Bonus Action attacks need a
  trigger (crit or kill — the Great Weapon Master pattern). Extra
  Reactions or extra turns: never below Epic Boon.

### Step 4 — Calibration

Run the 5-step protocol from
`references/power-budgets-and-benchmarks.md`:

1. Name 2–3 official feats of the same category and niche.
2. Compare benefit by benefit (stronger / equal / weaker) in a table.
3. Stronger on every axis → nerf (condition, once-per-turn, PB scaling).
4. Weaker on every axis → buff or narrow the niche.
5. Write the one-line verdict: "Comparable to X, narrower than Y."

Then run the **stacking audit** and the **anti-pattern scan** from
`references/balance-and-anti-patterns.md` — must-pick and trap-option
tests, the 10-point catalog, and the final checklist. A feat that fails
any Critical check goes back to Step 3.

### Step 5 — PHB 2024 Text

Write the entry in the official format:

```markdown
#### Feat Name
*General Feat (Prerequisite: Level 4+, Strength 13+)*

You gain the following benefits.

**Ability Score Increase.** Increase your Strength or Constitution
score by 1, to a maximum of 20.

**Named Benefit.** Benefit text.

**Repeatable.** (only if menu-shaped) You can take this feat more than
once, but you must choose a different [option] each time.
```

Vocabulary rules (2024 only):

- **Capitalized game terms:** Advantage, Disadvantage, Heroic
  Inspiration, Long Rest, Short Rest, Speed, the conditions
  (Prone, Grappled…), action names (the Attack action, the Dash
  action, Bonus Action, Reaction).
- **Resource phrasing:** "a number of times equal to your Proficiency
  Bonus, and you regain all expended uses when you finish a Long Rest."
- **Banned 2014 syntax:** "racial traits," uncapitalized
  advantage/disadvantage, "−5 to hit / +10 damage" mechanics, "one
  skill of your choice from your class list."

### Step 6 — Lore and Plot Hooks

- **Origin paragraph (3–6 sentences).** Where does this training,
  blessing, or knack come from? Who teaches it, what does practicing
  it look like, what does it cost?
- **Notable practitioner.** One named NPC (or order, or lineage) known
  for it — usable as patron, rival, or corpse.
- **1–2 plot hooks** tied to the origin or the practitioner. A feat is
  also an adventure seed: someone wants this technique taught,
  suppressed, or avenged.

---

## Output Format

Deliver each feat as:

```markdown
#### [Feat Name]
*[Category Feat (Prerequisite: …)]*

[PHB-format benefits, per Step 5]

---

**Design Notes** *(GM-facing)*
- **Calibration:** [one-line verdict naming the 2–3 reference feats;
  add the benefit-by-benefit comparison table only when the design is
  contested or the feat sits near a category ceiling — otherwise the
  table stays internal]
- **Watch for:** [any table-level interaction worth flagging, or "nothing unusual"]

**Origin.** [lore paragraph + notable practitioner]

**Hooks.**
1. [hook]
2. [hook]
```

The Design Notes block is what separates a publishable feat from a
forum post — never omit the calibration verdict.

---

## Thematic Set Mode (2–4 feats)

When the request is a linked set (a knightly order's training path, a
dragon cult's gifts, a campaign's regional feats):

- **One shared mechanical theme** expressed differently per category —
  use the scaling ladder in `references/feat-effect-library.md`
  (Origin → General: add ASI, remove a restriction; General → Epic
  Boon: remove the limit, make it permanent).
- **Naming coherence.** A shared lexical root or formula ("Vigil of…",
  "…of the Ember Court") so the set reads as one tradition.
- **Progression, not repetition.** The General feat should make the
  Origin feat's owner feel continuity, not obsolescence — upgrade the
  same fantasy.
- **Intra-set stacking audit.** A character may legally hold the whole
  set by level 19. Run the stacking audit on the *combination*, not
  just each feat alone.
- Shared lore: one origin paragraph for the tradition, then 1–2 lines
  per feat, and hooks that chain across the set.

---

## Common Requests

| Request | Routing decision |
|---|---|
| "A feat for my sailor background" | Origin — design the feat here, reference it from the `backgrounds` skill |
| "A level 4 feat for grapplers" | General — calibrate against Grappler and Tavern Brawler |
| "Something like Sharpshooter but for thrown weapons" | General — clone the niche, change the trigger, calibrate against Sharpshooter and Thrown Weapon Fighting |
| "A new stance for my Fighter" | Fighting Style if always-on and weapon-bound; General if it carries resources or an ASI |
| "A capstone reward for my level 19 warlock" | Epic Boon — calibrate against Boon of Spell Recall and Boon of Fate |
| "A feat that gives my cleric more spells" | The Magic Initiate / Fey-Touched chassis in the effect library |
| "Make my homebrew feat balanced" | Run Steps 4–5 only (calibration + rewrite); for a full supplement audit, hand off to ttrpg-supplement-reviewer |
| "Five feats for my dwarven clans" | Thematic Set Mode if 2–4 and mechanically linked; otherwise split into separate calls |
