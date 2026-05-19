---
name: magic-item-creator
description: >
  Create complete custom magic items for D&D 5e 2024, formatted to match the
  2024 DMG style. Covers the eight standard categories (Armor, Weapons,
  Potions, Rings, Rods, Scrolls, Staves, Wands, Wondrous Items) at all five
  rarities (Common, Uncommon, Rare, Very Rare, Legendary). Each item gets a
  stat block with category / rarity / attunement / properties / charges plus
  lore and origin paragraph, 1–2 variants, and 2–3 plot hooks. Use on "crée
  un objet magique", "create a magic item", "épée magique custom", "magic
  weapon for level 5", "wand of X", "homebrew ring", "Uncommon potion",
  "Rare wondrous item", "custom legendary item", "fabrique-moi un objet
  magique", "potion custom", "objet merveilleux", "anneau magique homebrew",
  "+1 sword with a twist", "magic item with a story". Boundary: cursed
  flavor and minor sentience can be added as options to standard items, but
  full Sentient items, full Cursed items, and Artifacts (unique campaign-tier)
  are deferred to dedicated future skills. NOT for non-magical equipment,
  potion-as-spell-component crafting rules (use DMG crafting chapter), or
  monster stat blocks (use monster-creator). Targets 2024 rules only.
---

# Magic Item Creator

Create publication-ready custom magic items for D&D 5e (2024 rules), formatted
to match the 2024 Dungeon Master's Guide style. The output is what a
publisher's mechanical designer would deliver for a treasure entry, a
supplement chapter, or an adventure's signature reward.

The skill is mechanical *and* narrative: balance discipline is non-negotiable,
but an item without an origin, a journey, and a hook is just a number bonus.

---

## Scope and Boundary

This skill covers the **eight standard categories** of D&D 5e 2024 magic
items at all five rarities. Deferred categories will get their own skills
when added:

| In scope | Out of scope (for now) |
|---|---|
| Armor, Weapons, Potions, Rings, Rods, Scrolls, Staves, Wands, Wondrous Items | Artifacts (unique campaign-tier items) |
| Common → Legendary rarity | Sentient items (full personality + alignment conflict) |
| Optional "cursed flavor" toggle | Full cursed items with reveal/removal mechanics |
| Attunement: yes / no, with prereqs | Crafting rules / time / cost |

For items that are *flavored* as cursed (e.g., a sword that occasionally
whispers in the wielder's ear without imposing mechanical drawbacks), this
skill handles them. For items where the curse is the central mechanic
(removal challenge, save-or-stay-attuned, alignment shift), wait for a
dedicated Cursed Items skill or run this skill and add the curse layer
manually.

For artifacts (single-of-a-kind items central to a campaign — the One
Ring, the Hand of Vecna), this skill produces the mechanical layer but
defers the campaign-scaffolding layer (destruction quest, minor and major
properties tied to identity, etc.) to a future Artifact skill.

---

## Before You Begin

1. **Identify the category.** Which of the 8 standard categories does the
   item fall into? Load `references/item-categories-2024.md` for the
   conventions of each category.

2. **Determine the rarity.** Common, Uncommon, Rare, Very Rare, or
   Legendary. Anchor on the **party tier** that should access it:
   - **Common:** Tier 1 baseline, accessible early
   - **Uncommon:** Tier 1 late / Tier 2 standard
   - **Rare:** Tier 2 late / Tier 3 standard
   - **Very Rare:** Tier 3 late / Tier 4 standard
   - **Legendary:** Tier 4 capstone, unique-feeling
   Load `references/rarity-and-attunement-guide.md` for power-level
   expectations and reward cadence.

3. **Decide attunement.** Most powerful items require attunement (max
   3 attuned per character). Common items rarely require it; Legendary
   items almost always do. Attunement prerequisites (class, alignment,
   ancestry, level, ability score) sharpen identity.

4. **Identify the concept.** What is this item *about*? Origin story,
   the function it serves at the table, the personality it brings to
   play. An item without a concept ends up as a number bonus with a
   name.

5. **Identify campaign context.** A standalone item or part of a series
   (matched pieces, set bonuses, themed collection)? An item tied to a
   specific faction, location, or NPC? Context informs the lore section
   and plot hooks.

If any of these is unclear from the brief, ask before designing.

---

## The Six-Step Creation Workflow

Every item passes through these steps. Output assembles them into a DMG-style
entry.

### Step 1 — Concept and Identity

- **Name.** Distinctive, evocative, not generic. "Verglas, Shard of the
  Drowned Pact" beats "Frost Sword +2." Avoid noun-soup names. Pattern
  often is `[Distinctive Single Word], [The Role / Origin Cue]`.
- **One-line pitch.** What is this item, in 15 words or fewer?
- **Visual.** 2–4 sentences of physical description. Concrete sensory
  details: material, color, scale, wear, sound, smell, weight. Avoid
  generic "ancient and glowing" descriptions.
- **Identity hook.** The one feature that makes this item *itself* and
  not interchangeable with another item of the same category and rarity.

### Step 2 — Category and Mechanical Frame

- **Category** (1 of 8 — see Step 1 of Before You Begin).
- **Sub-type within the category** (longsword vs greataxe vs rapier;
  potion vs oil; wand vs staff).
- **Rarity** (Common / Uncommon / Rare / Very Rare / Legendary).
- **Attunement** (yes / no; prerequisite if yes).
- **Slot** (for wondrous items: head, neck, shoulders, arms, hands,
  body, waist, feet, OR slotless for held / pocket items).

Match the mechanical frame to the lore. A Legendary helm should not
behave like a Common cantrip-on-demand item. A Common potion should
not deliver Rare-tier mechanical impact.

### Step 3 — Mechanical Design

Build the mechanical body of the item. Load
`references/balance-and-power-budgets.md` for the power budget per
rarity and `references/property-library.md` for the recurring property
patterns.

Core mechanical elements (mix as appropriate to category):

- **Static bonuses** (+1 / +2 / +3 to attack and damage; +X to AC; +X
  to specific saves)
- **Ability score effects** (set Strength to 21, advantage on Cha
  checks)
- **Conditional triggers** (when wielder is below half HP, when target
  has more HP than wielder, when in dim light)
- **Charge-based effects** (X charges per day, regain Y on dawn, expend
  N to cast spell Z at level W)
- **Daily / per-rest uses** (once per long rest, 3/day, recharge on dawn)
- **Action economy** (action / bonus action / reaction / no action)
- **Spell-like abilities** (cast specific spells from the item, with
  the item providing slots and DCs)
- **Resistance / immunity / vulnerability**
- **Senses bestowed** (darkvision, truesight, detect magic, see
  invisibility)
- **Movement effects** (fly speed, swim speed, climb speed, ignore
  difficult terrain)
- **Defensive effects** (advantage on saves vs certain types,
  proficiency in saves, expertise)
- **Communication / metaphysical** (telepathy, tongues, speak with
  X, planar awareness)

**Design discipline:**
- A Common item has **one** simple mechanical effect, often utility
  (a candle that doesn't go out, a cup that purifies water).
- An Uncommon item has **one** combat-relevant effect OR **2** utility
  effects.
- A Rare item has **2** notable effects OR **1** strong combat effect
  + lore-flavor minor effects.
- A Very Rare item has **2–3** notable effects, often including one
  signature ability.
- A Legendary item has **3–5** notable effects, with a signature
  identity-defining ability.

Don't pile mechanics on a low-rarity item to make it "interesting" —
that's how power-creep happens.

### Step 4 — Properties (DMG Format)

Format the mechanics into the DMG 2024 entry structure. Use this
template:

```
Item Name
[Category, Rarity (Attunement requirement if any)]

[1-paragraph flavor lead, 2–4 sentences.]

[If charges:] The item has [X] charges and regains [Y] daily at [time].

[Property 1, named and described in 1–3 sentences.]
[Property 2, named and described.]
[Property 3...]

[If signature/major ability:] [Name (Recharges after [trigger]).]
[Description of the signature ability, 2–4 sentences.]
```

Each property gets a **bold name** in the final output (e.g., **Frost
Hunger**, **Coldsteel Edge**, **Drowned Pact**). The names should
reflect the item's identity, not be generic ("Magic Bonus", "Special
Ability").

### Step 5 — Lore and Origin

The narrative half. Cover, in this order:

- **Maker.** Who created the item? (Artificer-mage of a fallen order?
  Divine forge? Accidental fusion during a planar incursion?
  Monster-bound spirit? Cursed pact? Ancient ritual?) Be specific.
- **Origin Story.** The circumstances of creation. 2–4 sentences.
- **Journey.** What has happened to the item since? (Passed through
  three owners; lost in a battle; sealed in a tomb; smuggled across
  borders; inherited.) 1–3 sentences.
- **Current State.** Where is the item now, and what condition is it
  in? (Intact in a vault; damaged and dormant; partial — half of a
  paired set; drained of charges and awakening; bound to a guardian.)
- **Cultural Significance.** Who knows of this item and what do they
  believe about it? (Forgotten by all; legend among a specific faction;
  actively sought by a sect; mistaken for something else.)

Load `references/lore-and-hook-templates.md` for category templates
(divine forge, monster-bound, accidental creation, etc.) and the
journey pattern catalog.

### Step 6 — Variants and Plot Hooks

**Variants (1–2):** Alternative forms of the same item that share the
mechanical frame with tweaks.
- Functional variants (this item exists in matched pairs, with the
  paired item having complementary properties)
- Tier variants (a Common cousin, an Uncommon sibling, a Rare
  ancestor)
- Cultural variants (the same item as made by different cultures,
  with cosmetic and minor mechanical differences)

Each variant: 1-paragraph description + a property delta.

**Plot Hooks (2–3):** Stories that put the item into a campaign.
Each hook is one to three sentences and answers: who has it now, who
wants it, what's at stake.

Cover variety:
- A bounty or recovery hook (someone wants the item retrieved)
- A maker-tied hook (the maker or the maker's faction has unfinished
  business with the item)
- A rival-claim hook (multiple parties want the item)
- An item-demands-something hook (the item itself imposes a cost or
  task on the wielder)
- An item-attracts-trouble hook (carrying the item draws specific
  threats)

Hooks should make the item *usable* across campaign types, not just
"loot it from a boss."

---

## Output Format

Assemble all six steps into a single document formatted like a DMG 2024
entry. Use this structure:

```markdown
# [Item Name]

*[One-line pitch in italics.]*

[Visual description, 2–4 sentences, read-aloud-able prose.]

## Mechanical Entry

> **[Item Name]**
> *[Category], [Rarity] (Requires Attunement [by X])*
>
> [Flavor lead, 2–4 sentences integrated into mechanics.]
>
> [If charges:] The [item] has [X] charges and regains [Y] expended
> charges daily at [time].
>
> ***[Property 1 Name].*** [Description.]
>
> ***[Property 2 Name].*** [Description.]
>
> ***[Signature Ability Name] (Recharges after [trigger]).*** [Description.]

## Origin and Lore

### Maker
[Paragraph.]

### Origin
[Paragraph.]

### Journey
[Paragraph.]

### Current State
[Paragraph.]

### Cultural Significance
[Paragraph.]

## Variants

**[Variant Name].** [Description and property delta.]

[Optional second variant.]

## Plot Hooks

1. **[Hook Title].** [1–3 sentences.]
2. **[Hook Title].** [1–3 sentences.]
3. [Optional 3rd hook.]
```

**Language:** Match the language of the user's brief. If the brief is in
French, write the entire entry in French (including stat block labels:
*Arme, peu commun (harmonisation requise)* instead of *Weapon, Uncommon
(Requires Attunement)*). See `references/item-categories-2024.md` for FR
vocabulary.

**Tone:** DMG professional. Evocative but precise. Names and properties
should reflect identity, not generic fantasy. Avoid purple prose; favor
concrete sensory detail and specific mechanical effect.

---

## Tier-Specific Adjustments

### Common (Tier 1 baseline)

- One simple mechanical effect, often utility (light at will, candle
  burns underwater, mug refills with chosen beverage once per day)
- Attunement: usually no
- Lore section: shorter, 2–3 paragraphs total
- Variants: optional, often a single one
- Plot hooks: 1–2 sufficient

### Uncommon (Tier 1 late / Tier 2 standard)

- One combat-relevant effect OR 2 utility effects
- Attunement: sometimes (50/50 ratio)
- Lore section: standard, 3–4 paragraphs
- Variants: 1 standard
- Plot hooks: 2 sufficient

### Rare (Tier 2 late / Tier 3 standard)

- 2 notable effects OR 1 strong combat effect + flavor minors
- Attunement: usually yes
- Lore section: full, 4–5 paragraphs
- Variants: 1–2
- Plot hooks: 2–3

### Very Rare (Tier 3 late / Tier 4 standard)

- 2–3 notable effects, often with a signature ability on Recharge
- Attunement: yes, often with prerequisite
- Lore section: full + cultural significance
- Variants: 2 (often a matched pair)
- Plot hooks: 3

### Legendary (Tier 4 capstone)

- 3–5 notable effects with identity-defining signature ability
- Attunement: yes, usually with specific prerequisite
- Lore section: full, with deeper history and cosmic-tier
  significance where appropriate
- Variants: 2 (paired set or paired forms)
- Plot hooks: 3+ campaign-scale

---

## Interaction with Other Skills

- **Item is tied to a specific NPC** (made by, owned by, sought by)
  → run `npc-creator` for the persona; reference in lore section.
- **Item is tied to a faction** (the holy order's relic, the cult's
  weapon, the guild's signet) → run `faction-creator` for the
  organization; reference in lore.
- **Item is housed in a settlement / dungeon** (the temple vault, the
  collapsed forge, the noble's manor) → run
  `settlement-toolkit-creator` for the place.
- **Item appears in a scenario** as a reward, a quest target, or a
  central object → run `scenario-writer`; pass this item as a key
  treasure or McGuffin.
- **Item is wielded by a monster** (the dragon's hoard sword, the
  lich's staff) → run `monster-creator` for the wielder; reference
  this item in the wielder's stat block under treasure.
- **Originality check** (is my "Sword of Truth" too cliché?) → run
  `ttrpg-cliche-buster` on the item concept before designing.
- **Read-aloud for discovery scene** → run `read-aloud-crafter` on
  the moment the party finds the item.
- **Pre-publication review** (this item is going into a supplement) →
  run `ttrpg-supplement-reviewer` after designing for editorial
  validation.

---

## Edge Cases

**Cursed flavor (not full curse):** A sword that whispers without
imposing mechanical penalties; armor that bleeds slightly when worn
but doesn't damage the wearer. This skill handles cursed *flavor* in
the lore and visual sections. If the curse needs full mechanical
implementation (alignment shift, can't be removed without ritual),
defer to a future Cursed Items skill or layer the mechanics manually.

**Item with minor sentience:** An item that occasionally speaks one
word, that pulses warmer near specific creatures, that prefers certain
wielders. Minor sentience is a flavor layer this skill handles. Full
sentient items (personality, goals, alignment conflict, control
challenge) defer to a future Sentient Items skill.

**Item that's actually a kit / set:** A matched pair (sword + sheath,
amulet + ring) or a themed collection (the Five Reliquaries) — each
piece is a separate item. Build each piece via this skill and define
the *set bonus* (what happens when all are attuned simultaneously) in
the variants section of the most-important piece.

**Item for adult content:** Standard 5e mechanics produce SFW output
by default. Adult-themed flavor (sensual properties, intimate
contexts) can be layered via Fantasy Vixens-specific skills after
this skill produces the mechanical baseline.

**Brief is vague ("I need a magic sword"):** Ask for: target rarity,
attunement preference, theme/flavor, intended owner / party tier.
Without these, the design becomes generic.

**Brief asks for "the same as [DMG item] but X":** Don't reproduce
copyrighted entries. Build from scratch with the requested twist as
the differentiator. Cite the inspiration publicly only if the user is
creating non-published / personal content.

**Brief asks for an artifact:** The skill produces standard items.
Artifacts (one-of-a-kind, campaign-defining items with minor +
major + destruction property structure) are deferred to a future
skill. Either reframe as Legendary, or wait for the Artifact skill.

---

## Reference Files

Load these as needed — not all at once.

- `references/rarity-and-attunement-guide.md` — The 5 rarity tiers with
  power-level expectations, gold price ranges (DMG 2024), reward
  cadence by tier, attunement rules, attunement-prerequisite patterns,
  slot rules for wondrous items.
- `references/item-categories-2024.md` — The 8 standard categories
  detailed: Armor, Weapons, Potions, Rings, Rods, Scrolls, Staves,
  Wands, Wondrous Items. For each: format conventions, naming
  patterns, sub-types, balance considerations, common pitfalls.
  Includes FR vocabulary for stat-block labels.
- `references/property-library.md` — Library of recurring magic-item
  property patterns: bonus types, conditional triggers, charge
  mechanics, spell-like abilities, resistance grants, sense grants,
  movement grants, action-economy options.
- `references/balance-and-power-budgets.md` — Power budgets by rarity
  (how many effects, what magnitude). Calibration by tier. Cap
  guidelines (items per PC by tier). Comparative examples (when is
  +1 vs +2 vs +3 appropriate; how Belt of Hill Giant Strength is
  balanced vs Belt of Storm Giant).
- `references/lore-and-hook-templates.md` — Maker categories (divine
  forge, monster-bound, accidental creation, etc.), journey patterns
  (passed down, lost-and-recovered, etc.), current-state options
  (intact, damaged, drained, awakening), and a hook library (bounty,
  maker-tied, rival-claim, item-demands, attracts-trouble) with
  examples by rarity tier.
