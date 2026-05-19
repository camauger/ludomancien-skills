---
name: monster-creator
description: >
  Create complete monsters for D&D 5e 2024, Monster Manual format. Produces a
  full stat block (type, size, alignment, AC, HP, speeds, abilities, saves,
  skills, resistances, senses, languages, CR, traits, multiattack, actions,
  bonus actions, reactions) plus lair actions + regional effects + variants
  for CR 5+, legendary and mythic actions for CR 11+, ecology and habitat,
  signs of presence, GM tactics, and 3–5 plot hooks per creature. Single-
  monster mode, publication-ready. Use on "crée un monstre", "create a
  monster", "stat block 5e 2024", "custom monster", "design a creature",
  "monstre custom", "bestiaire D&D", "fabrique-moi un monstre", "stat block
  CR 7", "monster manual style", "boss for my campaign", "mini-boss level 5",
  "homebrew creature", "balance this monster", "creature with lair actions".
  Boundary with npc-creator: humanoid NPCs with personality and secrets stay
  in npc-creator; non-humanoid creatures or species treated as ecological
  entities (a hag coven as a species, a goblin warband as a stat block) live
  here. NOT for encounter balance vs a specific party, stat block validation
  only (use ttrpg-supplement-reviewer), or D&D 2014 monsters.
---

# Monster Creator

Create publication-ready monsters for D&D 5e (2024 rules), formatted to match
the 2024 Monster Manual style. The output is what a publisher's monster
designer would deliver for a bestiary entry or an adventure mid-boss.

The skill is mechanical *and* narrative: stat block balance is non-negotiable,
but a creature without ecology, signs, and plot hooks is half a monster.

---

## Boundary with Other Creation Skills

This is the most common point of confusion. Use this guide:

| Brief | Use |
|---|---|
| "I need the village priest with secrets and motivations" | `npc-creator` (named humanoid with persona) |
| "I need the corrupted priest's wraith form when she dies" | `monster-creator` (creature emerging from NPC death) |
| "I need a goblin warband leader, a specific named goblin" | `npc-creator` (named individual) |
| "I need the **goblin species** for my setting, ecology + variants" | `monster-creator` (species as ecological entity) |
| "I need a hag with a personality and a coven role" | Both: persona via `npc-creator`, statistics via this skill |
| "I need a dragon, no specific name yet" | `monster-creator` |
| "I need the named ancient dragon Velnaris-the-Mourning" | This skill for stats + ecology, `npc-creator` for the named persona layer |
| "I need a faction's stat-block grunts (cult fanatics, knights)" | `monster-creator` (the species/type), `faction-creator` for the org |

**Rule of thumb:** if the brief includes *a name and a personality*, an
NPC layer is needed. If the brief includes *an ecology, a habitat, and
signs*, a monster layer is needed. Many briefs need both — run the two
skills and stitch the outputs.

---

## Before You Begin

1. **Identify the concept.** What is this creature in one sentence?
   - Inspiration (mythology, real animal, folklore, original)
   - Niche (apex predator, ambush hunter, scavenger, parasite, sentient
     collective, undead echo, fiend bargain, etc.)
   - Setting and biome (forest, deep sea, urban sewers, blasted plain,
     Underdark, planar)
   - Narrative function (random encounter, mid-boss, recurring threat,
     campaign antagonist, ecological flavor)

2. **Determine the target CR.** Anchor on the party that will face it.
   - Random encounter for a level 3 party → CR 1–4
   - Mid-boss for level 5 party → CR 5–8
   - Capstone boss for level 10 party → CR 10–14
   - Tier 4 threat → CR 18+
   If unspecified, ask. Default fallback: CR 3 (broadest utility).
   Load `references/cr-design-protocol-2024.md` for benchmarks by CR.

3. **Determine the combat role.** Same CR creatures play very
   differently. Load `references/combat-roles.md` and pick one:
   Skirmisher, Brute, Artillery, Lurker, Soldier, Controller, Leader,
   or Spoiler. The role drives stat distribution and action design.

4. **Determine the creature type.** Aberration, Beast, Celestial,
   Construct, Dragon, Elemental, Fey, Fiend, Giant, Humanoid,
   Monstrosity, Ooze, Plant, or Undead. Load
   `references/creature-types-and-tags-2024.md` for tag conventions
   and type implications.

5. **Decide on tier features.**
   - **CR 0–4:** Stat block + brief lore + 1–2 hooks. No lair actions.
   - **CR 5–10:** + Lair actions + regional effects + 1–2 variants +
     full tactics section.
   - **CR 11–20:** + Legendary actions + signature traits + multi-phase
     if narratively appropriate.
   - **CR 21+:** + Mythic actions + cosmic-scale ecology.

If the brief is ambiguous on any of these, ask before designing. Do
not invent CR or role — these are the load-bearing choices.

---

## The Six-Step Creation Workflow

Every creature passes through these steps in order. The output assembles
them into a Monster Manual-style entry.

### Step 1 — Concept and Identity

- **Name.** Distinctive, evocative, not generic ("Forgekin Sentinel"
  not "Iron Golem"). Avoid noun-soup ("Ancient Lost Shadowkeeper of
  Tears"). One distinctive word + a category word usually beats three
  poetic words.
- **One-line pitch.** What is this creature, in 15 words or fewer?
- **Visual.** 2–4 sentences of physical description that a GM can read
  aloud. Concrete sensory details, not abstract atmosphere.
- **Signature behavior.** The one thing this creature *does* that
  distinguishes it (hunts at dawn, builds nests from skulls, whispers
  the names of its victims, etc.).

### Step 2 — Stat Block (5e 2024 Format)

Build the stat block using the 2024 Monster Manual format. Load
`references/cr-design-protocol-2024.md` for HP/AC/damage benchmarks
by CR. Load `references/trait-and-action-library.md` for trait and
action patterns.

The stat block sections, in order:

```
[Name]
[Size] [Type] ([Tags]), [Alignment]

AC      [value]
HP      [average] ([dice formula])
Speed   [walk] ft., [other modes as relevant]

         STR     DEX     CON     INT     WIS     CHA
        XX (+X) XX (+X) XX (+X) XX (+X) XX (+X) XX (+X)

Saving Throws   [list]
Skills          [list with bonuses]
Damage Resistances/Immunities/Vulnerabilities    [as relevant]
Condition Immunities                              [as relevant]
Senses          [special senses] passive Perception [value]
Languages       [list, or —]
CR              [value] (XP [value]); PB +[value]

Traits
[Trait Name]. [Description]
...

Actions
Multiattack. [Description]
[Action Name]. [Attack roll or save, range/reach, target, damage, effect]
...

Bonus Actions (if any)
[Action Name]. [Description]

Reactions (if any)
[Reaction Name]. [Description]

Legendary Actions (CR 11+ if applicable)
[Costs X actions per turn description]
[Action 1] (Cost X)
[Action 2] (Cost X)
...
```

**Balance discipline:**
- Use the CR benchmarks (see references) as anchors, not as rigid
  rules. Adjust ±10% for creature role (Brute trades AC for HP and
  damage; Lurker trades HP for stealth and burst).
- Damage per round (DPR) is the **single most important number**.
  Multiattack must produce roughly the DPR for the CR.
- Saving throw DCs and attack bonuses follow proficiency bonus +
  relevant modifier; check `cr-design-protocol-2024.md` for the
  expected ranges.
- Resistances and immunities are powerful — each one effectively
  bumps the defensive CR. Don't stack three resistances on a CR 2
  creature.
- Recharge abilities (Recharge 5–6) are the standard 5e device for
  signature spike damage; use them for the creature's defining
  attack.

### Step 3 — Lair Actions, Regional Effects, Variants (CR 5+)

For creatures CR 5+ with a permanent dwelling, include:

**Lair Actions.** Up to 3 actions the lair takes on initiative count
20 (losing initiative ties). Pick from a recurring menu thematically
linked to the creature. Example for a swamp hag:

> On initiative count 20 (losing initiative ties), the hag takes a
> lair action to cause one of the following effects; the hag can't
> use the same effect two rounds in a row:
> 
> - *Roots and reeds erupt from the muddy ground...*
> - *Mist thickens in a 30-foot radius...*
> - *The hag whispers a victim's secret aloud, audible everywhere in
>   the lair...*

**Regional Effects.** 2–4 environmental phenomena within ~1 mile of
the lair that signal the creature's presence and warp the world
around it. Effects persist while the creature lives and fade 1d10
days after its death.

**Variants.** 1–2 sub-types of the creature that share the base
stat block with tweaks (e.g., Coastal Swamp Hag with swim speed +
amphibious; Crone-Stage Swamp Hag with extra legendary action).
Each variant has a 1-paragraph description and a stat delta.

### Step 4 — Lore and Ecology

This section is the Monster Manual narrative half. Cover, in this
order:

- **Origin / Nature.** Where did this creature come from? Created by
  a divine curse? Evolved from a mundane animal? Bargained into
  existence? Native species?
- **Habitat.** Where it lives, in concrete terms. "Coastal salt
  marshes within 30 miles of the open sea" beats "wetlands".
- **Behavior.** Hunting / mating / social / reproductive patterns.
  Hierarchy if relevant.
- **Diet.** What it eats and how it acquires food. (Important for
  ecology and for player problem-solving.)
- **Signs of Presence.** What a tracker or alert party notices before
  the creature shows itself. Physical traces (scat, prints, kills),
  sounds, smells, environmental shifts, weather omens. **3–5 signs
  minimum.**
- **Relationships.** Predators, prey, rivals, symbiotes, cults. If
  the creature has known interactions with other Monster Manual
  entries, note them.
- **Treasure (if any).** What the creature collects, hoards, or
  carries.

Load `references/lore-templates.md` for category-specific patterns
(apex predator template, swarm template, scavenger template,
intelligent collective template, etc.).

### Step 5 — GM Combat Tactics

How to actually play this creature at the table. Cover:

- **Opening move.** What the creature does on round 1 if it acts first.
- **Round-by-round behavior.** How it adapts to damage, party
  positioning, lost allies.
- **Retreat conditions.** At what HP threshold does the creature
  flee, surrender, or transform? Most creatures are not suicidal;
  the smart ones especially flee when below 25% HP.
- **Special tactics.** Use of terrain, recharge ability timing,
  legendary action prioritization, lair action sequencing.
- **What this creature does NOT do.** Common GM mistakes to avoid
  (e.g., "doesn't engage in melee while it has artillery
  positioning", "doesn't waste recharge on minions when boss is
  alive").

This section is 4–8 sentences, not a chapter. Practical, table-ready.

### Step 6 — Plot Hooks

3–5 plot hooks that put the creature into a story. Each hook is one
to three sentences and answers: who hires the party, what's at
stake, what the creature is doing right now.

Cover variety:
- A bounty / threat scenario
- A mystery / investigation scenario
- A moral-gray scenario (the creature is suffering, not just
  hostile)
- A faction-tied scenario (someone benefits from the creature's
  existence or removal)
- An environmental / ecological scenario (the creature's role
  in the biome is the actual problem)

Hooks should make the creature *usable* across campaign types, not
just "fight it for XP".

---

## Output Format

Assemble all six steps into a single document formatted like a
Monster Manual 2024 entry. Use this structure:

```markdown
# [Creature Name]

*[One-line pitch in italics.]*

[Visual description, 2–4 sentences, read-aloud-able prose.]

## Stat Block

[The full stat block in the format shown in Step 2. Use a code block
or table for readability.]

## Lair Actions, Regional Effects, and Variants
*(CR 5+ only; omit for lower CRs)*

### Lair Actions
[3 actions, formatted as above.]

### Regional Effects
[2–4 effects with persistence note.]

### Variants

**[Variant Name].** [Description and stat delta.]

## Ecology

### Origin and Nature
[Paragraph.]

### Habitat
[Paragraph.]

### Behavior
[Paragraph.]

### Diet
[Paragraph or sentence.]

### Signs of Presence
- [Sign 1]
- [Sign 2]
- [Sign 3]
- [Sign 4 if applicable]
- [Sign 5 if applicable]

### Relationships
[Paragraph.]

### Treasure
[Sentence or paragraph, or "None."]

## Running [Creature Name] at the Table

[GM tactics, 4–8 sentences.]

## Plot Hooks

1. **[Hook Title].** [1–3 sentences.]
2. **[Hook Title].** [1–3 sentences.]
3. **[Hook Title].** [1–3 sentences.]
4. [Optional 4th]
5. [Optional 5th]
```

**Language:** Match the language of the user's brief. If the brief is
in French, write the entire entry in French (including the stat block
labels: PV instead of HP, CA instead of AC, etc. — see
`references/creature-types-and-tags-2024.md` for the FR vocabulary).

**Tone:** Monster Manual professional. Evocative but precise. Avoid
purple prose; favor concrete sensory detail.

---

## Tier-Specific Adjustments

### CR 0–4 (Encounter fodder, mooks, low-tier mid-bosses)

- Skip Step 3 (Lair Actions and Regional Effects)
- Variants are optional
- Lore section is shorter: 2–3 paragraphs total
- Plot hooks: 1–2 sufficient
- Focus polish on: stat block balance, signature trait, 2–3 signs of
  presence

### CR 5–10 (Mid-tier threats, mini-bosses)

- Include all six steps
- Lair Actions if the creature has a permanent dwelling
- Variants: 1 alternative form
- Legendary actions: rarely; only if creature is a tier-defining
  threat
- Full ecology section

### CR 11–17 (Tier 3 bosses, campaign threats)

- Legendary actions become standard
- Multi-phase combat optional (if narratively appropriate)
- Signature traits become more pronounced (recharge abilities, lair
  actions with stronger effects)
- Variants: 2 alternative forms
- Plot hooks: at least 4

### CR 18–20 (Tier 4 capstones)

- All of the above, polished
- Mythic actions (a second "phase" of legendary actions triggered
  by HP threshold) become available
- Cosmic-scale ecology and regional effects

### CR 21+ (Demigod-tier, cosmic threats)

- Mythic actions standard
- Cosmic regional effects (extending 10+ miles, planar bleed-through)
- The creature *changes the world* by existing; ecology section
  becomes a small worldbuilding piece
- Plot hooks become campaign-scale, not session-scale

---

## Interaction with Other Skills

- **Named individual layer** (this creature is a *specific named
  character*) → run `npc-creator` for the persona; use this skill's
  output for the mechanical layer; stitch them.
- **Faction context** (this creature is faction-tied — cultists,
  knights of an order) → run `faction-creator` for the organization;
  reference faction membership in this creature's ecology and hooks.
- **Settlement context** (this creature haunts / threatens / inhabits
  a specific village or city) → run `settlement-toolkit-creator` for
  the place; reference the place in this creature's habitat.
- **Scenario integration** (using this creature in a specific
  adventure) → run `scenario-writer`; pass this creature as one of
  the antagonists.
- **Read-aloud for combat narration** → run `read-aloud-crafter`
  on this creature's signature attacks and entrance.
- **Originality audit** (is my "ancient lich" too cliché?) → run
  `ttrpg-cliche-buster` on the creature concept before designing.
- **Pre-publication review** (this creature is going into a
  bestiary I'm publishing) → run `ttrpg-supplement-reviewer` after
  designing for editorial validation.
- **Mechanical stress test** (does this creature work in actual
  combat?) → run `ttrpg-playtest-orchestrator` for simulation.

---

## Edge Cases

**Creature is a humanoid species, not an individual:** Use this
skill. The stat block represents a *typical member* of the species;
the lore section describes the species as a whole. Named individuals
of the species use `npc-creator` for persona layered on this stat
block.

**Creature is a hybrid of two existing monsters:** Build from
scratch using the role and CR target, then explicitly note the
"parent" creatures in the lore section. Don't average two stat
blocks numerically — that produces messy results.

**Creature is a swarm:** Use the Swarm template in
`references/lore-templates.md` and the swarm mechanics from the
2024 Monster Manual (swarm of Tiny / Small creatures functioning as
a single Medium / Large creature). HP is the *collective* HP; the
swarm has resistance to many damage types.

**Creature is an environmental hazard, not really a creature:** This
is a different skill (trap / hazard creator, not yet in the
marketplace). Tell the user the skill produces *living creatures*;
if they want a hazard, suggest reframing or wait for a dedicated
skill.

**Creature is for adult content (Fantasy Vixens niche, etc.):**
The skill produces standard mechanical content. Adult layer
(seductive abilities, charm-based attacks framed in adult terms,
etc.) is added via the Fantasy Vixens-specific erotica skills
afterward. The skill itself stays SFW in output by default.

**Brief is vague ("I need a forest monster"):** Ask for: target CR,
party level, combat role, and tone (heroic / dark / horror). Without
these, the design becomes generic.

**Brief asks for "the same as [Monster Manual creature] but X":**
Don't reproduce copyrighted stat blocks. Build from scratch with
the requested twist as the differentiator. Cite the inspiration
publicly only if the user is creating non-published / personal
content.

---

## Reference Files

Load these as needed — not all at once.

- `references/cr-design-protocol-2024.md` — D&D 5e 2024 Challenge
  Rating design protocol. HP / AC / DPR / attack bonus / save DC
  benchmarks by CR. Adjustment guidance for resistances, immunities,
  legendary creatures, and recharge abilities.
- `references/creature-types-and-tags-2024.md` — The 14 official
  creature types of 2024, with tag conventions (Shapechanger,
  Demon, Devil, Titan, etc.) and type-specific implications
  (immunities, vulnerabilities, behaviors). Includes the FR
  vocabulary for stat blocks (PV, CA, etc.).
- `references/combat-roles.md` — The 8 combat roles (Skirmisher,
  Brute, Artillery, Lurker, Soldier, Controller, Leader, Spoiler)
  with stat distribution patterns, signature trait suggestions,
  and CR-by-role examples.
- `references/trait-and-action-library.md` — Recurring 5e trait and
  action patterns: Pack Tactics, Magic Resistance, Charge, Recharge
  X-X, Multiattack templates, Reaction patterns (Parry, Riposte,
  Mage Slayer), Legendary Action menus, Lair Action templates.
- `references/lore-templates.md` — Category-specific ecology
  templates: apex predator, ambush hunter, swarm, scavenger,
  parasite, sentient collective, undead echo, fiendish bargain,
  fey trickster, elemental embodiment, planar exile.
