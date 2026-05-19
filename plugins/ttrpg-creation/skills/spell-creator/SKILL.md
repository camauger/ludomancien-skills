---
name: spell-creator
description: >
  Create complete custom spells for D&D 5e 2024, formatted to match the
  2024 Player's Handbook style. Covers all 10 spell levels (Cantrip → 9th),
  the eight schools (Abjuration, Conjuration, Divination, Enchantment,
  Evocation, Illusion, Necromancy, Transmutation), every standard class
  spell list, and all casting frames (Action, Bonus Action, Reaction,
  ritual, minutes / hours / 24 hours). Each spell ships with PHB-format
  stat block (level, school, casting time, range, components, duration,
  classes), description text, scaling at higher levels (or cantrip
  scaling), and 1–2 plot hooks tied to origin or notable users. Use on
  "crée un sort", "create a spell", "cantrip homebrew", "3rd-level
  evocation", "wizard spell for X", "concentration spell that does Y",
  "ritual spell", "fabrique-moi un sort", "sort original", "homebrew
  spell with twist", "spell for a Storm Sorcerer", "necromancy at 5th
  level", "BBEG signature spell". Boundary: this skill produces ONE spell
  per call (or a small thematic set of 2–3 related spells). Class feature
  design — subclass abilities, monk forms, warlock invocations, fighter
  maneuvers, Eldritch Invocations, ki/focus features — is out of scope;
  those are class features, not spells. Magic item charged effects are
  handled by magic-item-creator. Monster spell-like abilities and innate
  spellcasting use monster-creator. Epic / 10th+ level / Mythic spells
  defer to a future skill. Targets 2024 rules only (PHB 2024 / DMG 2024
  conventions).
---

# Spell Creator

Create publication-ready custom spells for D&D 5e (2024 rules), formatted
to match the 2024 Player's Handbook style. The output is what a
publisher's mechanical designer would deliver for a class supplement, a
spellbook product, or an adventure's signature spell.

The skill is mechanical *and* narrative: balance discipline is
non-negotiable, but a spell without an identity, an origin, and a
notable user is just a damage formula with a name.

---

## Scope and Boundary

This skill covers **standard 5e 2024 spells** at all levels and schools.

| In scope | Out of scope (for now) |
|---|---|
| Cantrips (level 0) → 9th-level spells | 10th+ level / Mythic / Epic spells |
| All 8 schools (Abjuration, Conjuration, Divination, Enchantment, Evocation, Illusion, Necromancy, Transmutation) | Class features that look like spells (Monk's Step of the Wind, Warlock invocations, Fighter Battle Master maneuvers) |
| All 13 standard PHB 2024 classes' spell lists (Artificer is 2024 reprint) | New class design |
| All casting times (Action, Bonus Action, Reaction, ritual, X minutes, X hours, 24h) | Crafting cost / time rules (use DMG crafting chapter) |
| All durations (Instantaneous, Concentration up to X, fixed duration, Until dispelled) | Spell scroll pricing (use magic-item-creator) |
| All effect types: damage, save, attack roll, control, buff/debuff, utility, summon, divination | Innate spellcasting on monsters (use monster-creator) |
| Ritual tag (when appropriate) | Magic item charged spells (use magic-item-creator) |

For **subclass features that resemble spells** (a Stormwrack Sorcerer's
"Tempest Sting"), build them via the dedicated class-feature design
skill once it exists. This skill produces spells callable from a
spell slot, not class-specific resources.

For **iconic monster abilities** (a Beholder's eye rays, a Dragon's
breath weapon), these are not spells — use `monster-creator`.

---

## Before You Begin

Six things to settle before designing:

1. **Concept.** What is this spell *about*? "A pulse of cold that
   binds the target's heart" beats "a spell that does cold damage
   and slows." Without a concept, you build a generic formula.

2. **Level.** Cantrip / 1st / 2nd / 3rd / ... / 9th. Anchor on the
   **expected tier of use**:
   - **Cantrip:** any tier; scales with character level.
   - **1st–2nd:** Tier 1 (levels 1–4) baseline.
   - **3rd–4th:** Tier 2 (levels 5–10) baseline.
   - **5th–6th:** Tier 3 (levels 11–16) baseline.
   - **7th–8th:** Tier 4 (levels 17–20) baseline.
   - **9th:** capstone, identity-defining.

   Load `references/spell-levels-and-tiers-2024.md` for power-level
   benchmarks per level.

3. **School.** Pick one of eight. The school encodes the spell's
   conceptual flavor *and* certain mechanical tendencies (Evocation
   damages, Enchantment controls minds, Abjuration protects).

   Load `references/schools-and-tradition-2024.md` for school
   conventions and pitfalls.

4. **Effect type.** Damage / control / buff/debuff / utility /
   movement / divination / summon / battlefield-shape. Most spells
   do one primary thing well. A spell that does five things at
   once is a balance failure.

5. **Class list.** Which classes can cast this spell? PHB 2024
   spell lists: Bard, Cleric, Druid, Paladin, Ranger, Sorcerer,
   Warlock, Wizard. (Artificer if using the 2024 reprint.) Spell
   identity often hints at the right list — a Cleric spell evokes
   the divine; a Wizard spell often involves studied geometry; a
   Druid spell ties to nature.

6. **Identity hook.** The one thing that makes this spell *itself*
   and not interchangeable with another spell of the same level and
   school. The hook is usually in the *delivery*, the *secondary
   effect*, or the *narrative consequence*.

If any of these is unclear, ask before designing.

---

## The Six-Step Creation Workflow

Every spell passes through these steps. Output assembles them into a
PHB-style entry.

### Step 1 — Concept and Identity

- **Name.** Distinctive, evocative, not generic. "Veilcall" beats
  "Summon Friend." "Hollowing Touch" beats "Necrotic Touch." A
  pattern often is `[Single Distinctive Word]` or `[Adjective + Body
  Part / Element]` or `[Noun's / Maker's] [Effect]`.
- **One-line pitch.** What is this spell, in 15 words or fewer?
- **Visual.** 1–2 sentences of how the spell *manifests* — the
  caster's gesture, the visible effect, the sensory signature.
  Concrete: color, sound, smell, motion. Avoid generic "a magical
  effect occurs."
- **Identity hook.** The one feature that distinguishes this spell
  from same-level same-school neighbors. Examples:
  - *Hollowing Touch* (Necromancy 2): not just damage — the target's
    next healing fails.
  - *Veilcall* (Illusion 1): not just a sound illusion — the sound
    comes from a *specific named source* the caster designates.

### Step 2 — Level, School, and Class List

- **Level** (Cantrip / 1 / 2 / 3 / 4 / 5 / 6 / 7 / 8 / 9).
- **School** (Abjuration / Conjuration / Divination / Enchantment /
  Evocation / Illusion / Necromancy / Transmutation).
- **Class list.** Pick from PHB 2024: Bard, Cleric, Druid, Paladin,
  Ranger, Sorcerer, Warlock, Wizard, Artificer.
- **Ritual?** Eligible spells (most non-combat utility spells of
  any level) can be cast as a ritual, taking 10 extra minutes and
  consuming no slot. Combat spells (damage, control in combat) are
  *not* eligible for ritual. Use sparingly.

Match the level/school to the lore. A 1st-level Necromancy spell
should not deliver 7th-level effect magnitude. A 6th-level
Divination should not be a glorified Insight check.

### Step 3 — Casting Frame

Build the casting envelope. Load
`references/casting-time-and-components-2024.md` for details.

- **Casting time.** Action (default for offensive spells), Bonus
  Action (specialized, usually one-target buffs or self-buffs),
  Reaction (defensive or counter-spells, with explicit trigger
  condition), X minutes / hours (ritual-eligible, out-of-combat),
  1 hour for elaborate effects, 8 hours for binding rituals, 24
  hours for once-per-day major spells.
- **Range.** Self / Touch / 5 ft – 500 ft / Sight / Unlimited (rare).
  Most combat spells: 30–120 ft. Most defensive: Self or Touch.
- **Components.** V, S, M (with cost if consumed). Material
  components without listed cost are often handled by a spellcasting
  focus. Consumed materials (Diamond worth 300+ gp consumed) make
  a spell expensive and rare-to-use; reserve for powerful effects
  like Revivify, Raise Dead.
- **Duration.** Instantaneous (effect happens, no upkeep), fixed
  duration (1 round / 1 minute / 10 minutes / 1 hour / 8 hours /
  24 hours / 7 days), Concentration (up to X), Until dispelled.

**Concentration discipline:**
- A caster can only Concentrate on one spell at a time.
- Most ongoing battlefield-control or duration-buff effects
  REQUIRE Concentration. This is the primary balance lever — it
  prevents stacking.
- Avoid creating high-impact ongoing effects *without*
  Concentration. That's a balance leak that lets a caster stack
  the spell with a second Concentration spell.

### Step 4 — Effect Design

Build the mechanical body of the spell. Load
`references/spell-effect-library.md` for recurring patterns and
`references/balance-and-anti-patterns.md` for benchmarks.

Core mechanical elements (pick the primary, add 0–1 secondaries):

**Damage effects:**
- Saving throw vs damage (typically Dex / Con / Wis)
- Attack roll vs AC (spell attack)
- Area shapes: Cube (X ft), Sphere (X ft), Cone (X ft), Line (X ft
  long × 5 ft wide), Cylinder (X ft radius × Y ft tall)
- Damage type (acid, cold, fire, force, lightning, necrotic,
  poison, psychic, radiant, thunder, bludgeoning/piercing/slashing)
- Half on save (standard for AoE saves)

**Control / Condition effects:**
- Saving throw vs condition (Charmed, Frightened, Grappled,
  Restrained, Prone, Blinded, Deafened, Paralyzed, Stunned,
  Incapacitated, Petrified, Poisoned)
- Save end-of-turn vs permanent until dispel
- Concentration usually required

**Buff effects:**
- Self-buff or single-target buff (AC, attack, save, speed,
  resistance, advantage on X, temp HP, hit point boost)
- Duration usually Concentration or 1 minute / 10 minutes / 1
  hour

**Debuff effects:**
- Saving throw vs disadvantage / vulnerability / penalty
- Often Concentration

**Utility effects:**
- Movement (teleport, flight, climb, swim, phase-shift)
- Sensing (see invisibility, detect, scry, divine)
- Communication (telepathy, animal speech, tongues)
- Object manipulation (mage hand, telekinesis, animate)

**Summon effects:**
- A creature appears under caster's control
- 2024 design: use *one* statblock per spell with scaling per slot
  (e.g., *Summon Beast* casts a Beast Spirit; higher slots scale
  its CR)
- Duration usually Concentration

**Battlefield-shape effects:**
- Persistent area: Wall of X, Cloud of X, Sphere of X
- Damages, blocks, controls, or alters terrain in the area
- Concentration usually required

**Divination effects:**
- Yes/no answers, locations, futures, identities
- Often 1+ minute casting time; often ritual-eligible
- High-level: Wish-tier scope

Design discipline:
- **One primary effect.** A spell that *both* damages an AoE *and*
  imposes a condition on each target *and* persists for a turn is
  three spells at once.
- **Secondary effects scale to ½ primary's power budget.** A
  damage spell can have a 1-round debuff rider; a debuff spell
  can have a token damage rider.
- **Saves vs Attacks.** AoE → save (you can't roll attack against
  multiple targets). Single target → attack roll *or* save (your
  choice based on flavor; saves favor martial casters, attacks
  favor archetypal magic-blasters).

### Step 5 — Scaling

Two scaling modes:

**Cantrip scaling (character level):**
At character level 5, 11, and 17, cantrip damage / effect increases
by one die or one step. Use this protocol:
- Cantrip with a damage die: starts at 1d**X**; gains another 1d**X**
  at levels 5, 11, 17 (final = 4d**X**).
- Cantrip with a non-damage effect: adds a secondary effect or
  doubles a numeric value at one of the scaling points.

Examples (PHB 2024):
- *Fire Bolt:* 1d10 → 2d10 → 3d10 → 4d10.
- *Mage Hand:* range/weight expand at character levels.

**Leveled spell scaling (higher slot):**
A spell cast at a slot *higher* than its base level gains an
"At Higher Levels" effect. Standard patterns:
- **+1d/slot:** Damage spells gain extra damage die per slot above
  base. Most common pattern.
- **+1 target/slot:** Single-target spells affect one extra
  creature per slot.
- **+10/+5 ft/slot:** Range or area expand per slot.
- **+10 min/slot:** Duration extends.
- **Effect upgrade:** Some spells *change* at higher slots
  (Spiritual Weapon: bigger weapon / more damage at 4th+).

Some spells (Wish, Resurrection-tier, Time Stop, divinations of
specific knowledge) *do not scale* — they are level-locked.

### Step 6 — Class Assignment, Lore, and Plot Hooks

**Class assignment:**
Which classes get this spell? PHB 2024 lists are thematic:
- **Bard:** charm, illusion, knowledge, healing-light.
- **Cleric:** divine, healing, light, undead-rebuking, command.
- **Druid:** nature, animal, weather, healing, shape, plant.
- **Paladin:** smite, oath-flavored, divine.
- **Ranger:** nature, hunting, terrain, beast-bond.
- **Sorcerer:** elemental, damage, manipulation, blood-lineage.
- **Warlock:** patron-themed, eldritch, dark utility.
- **Wizard:** broad, often scholarly / studied; the default
  generalist arcane list.
- **Artificer (2024 reprint):** invention, contraption, brief
  utility, support.

A signature spell can be **exclusive** to one class (rare, like
*Eldritch Blast* to Warlock) or **shared** across 2–4 classes.
Default to shared with thematic logic.

**Lore (paragraph):**
- **Maker / Discoverer.** Who developed this spell? Named caster?
  Lineage? Forgotten archive? Accidental discovery?
- **Cultural significance.** Who currently uses it? Is it well-
  known, faction-locked, forbidden, sacred?
- **Notable historical uses.** What has the spell done in the
  world's history? Famous battle, infamous murder, miracle of
  healing, sealing of a great evil.

**Plot hooks (1–2):**
Each hook is 1–3 sentences and answers: who knows this spell, who
wants it, what's at stake. Examples:
- **Bounty.** A scholar wants the only surviving spellbook
  containing this spell; the spellbook is held by a hostile cult.
- **Forbidden.** This spell is banned in the kingdom; possession
  is a capital offense. The party finds it scribed in a noble's
  diary.
- **Mentor.** A retired caster will teach this spell — for a
  service.
- **Trap.** This spell appears in tomes, but the version preserved
  is subtly altered; casting it draws an entity's attention.

---

## Output Format

Assemble all six steps into a single document formatted like a PHB
2024 entry. Use this structure:

```markdown
# [Spell Name]

*[One-line pitch in italics.]*

[Visual description, 1–2 sentences, evocative prose.]

## Spell Entry

> **[Spell Name]**
>
> *[Level] [School] [(ritual)]*
>
> **Casting Time:** [Action / Bonus Action / Reaction (trigger:) / X
> minutes / X hours]
> **Range:** [Self / Touch / X ft / Sight]
> **Components:** [V, S, M ([material description, with cost if
> consumed])]
> **Duration:** [Instantaneous / fixed duration / Concentration, up
> to X / Until dispelled]
> **Classes:** [list]
>
> [Description: 1–4 paragraphs of mechanical and flavor text. Lead
> with what happens, then conditions, then exceptions.]
>
> ***Using a Higher-Level Spell Slot.*** [Scaling rule, 1–2
> sentences.]
>
> *(For cantrips, replace the scaling block with:)*
> ***Cantrip Upgrade.*** [Scaling at character levels 5, 11, 17.]

## Origin and Lore

### Maker / Discoverer
[Paragraph.]

### Cultural Significance
[Paragraph.]

### Notable Uses
[Paragraph.]

## Plot Hooks

1. **[Hook Title].** [1–3 sentences.]
2. **[Hook Title].** [1–3 sentences, optional second hook.]
```

**Language:** Match the language of the brief. If the brief is in
French, write the entire entry in French (including stat block
labels: *Temps d'incantation*, *Portée*, *Composantes*, *Durée*,
*Classes*). See `references/schools-and-tradition-2024.md` for
French school names and vocabulary.

**Tone:** PHB 2024 professional. Mechanical text precise, flavor
text evocative but concise. Names should reflect identity, not
generic fantasy. Avoid noun-soup ("Sword of Holy Burning Light").

---

## Level-Specific Adjustments

### Cantrip (Level 0)

- **Damage cantrip:** 1d8–1d10 single-target attack-roll, or
  1d6 AoE save-half. Scales with character level.
- **Utility cantrip:** Persistent or repeatable minor effect.
  Examples: Mage Hand, Light, Mending, Prestidigitation.
- **Identity test:** Is this useful at level 1 and *still*
  useful at level 17? If not, it's a 1st-level spell with no
  scaling.
- **Components:** Often V, S; M only for utility cantrips.
- **Lore:** Brief, often a common-knowledge magical effect.

### 1st–2nd Level (Tier 1 baseline)

- **1st level:** 2d8–3d8 damage, or 1 condition with save end-of-
  turn, or a major utility (Detect, Identify, Comprehend, Cure
  Wounds basic).
- **2nd level:** 3d6 AoE, 4d8 single-target, mid-tier condition
  (Hold Person, Web), or expanded utility (Misty Step, Mirror
  Image).
- Plot hooks: usually local-scale.

### 3rd–4th Level (Tier 2 baseline)

- **3rd level:** AoE damage (Fireball 8d6 baseline), powerful
  control (Counterspell, Hypnotic Pattern, Slow), or signature
  utility (Fly, Haste, Major Image).
- **4th level:** Heavy battlefield effects (Polymorph, Banishment,
  Wall of Fire), major buffs (Greater Invisibility), or potent
  divination (Divination, Locate Creature).
- Plot hooks: regional-scale.

### 5th–6th Level (Tier 3 baseline)

- **5th level:** Reality-bending (Hold Monster, Telekinesis,
  Animate Objects), major heals (Raise Dead), strong shape spells
  (Wall of Stone / Force, Cone of Cold).
- **6th level:** Major control of large foes (Disintegrate at
  10d6+40), powerful battlefield reshapes (Move Earth, Wall of
  Ice), strong divination (True Seeing).
- Plot hooks: kingdom-scale.

### 7th–8th Level (Tier 4 baseline)

- **7th level:** Reality manipulation (Teleport, Mirage Arcane,
  Plane Shift), powerful instakill-with-save (Finger of Death,
  Power Word Pain).
- **8th level:** Capstone control (Dominate Monster), powerful
  shape-spells (Sunburst, Earthquake), major battlefield (Maze).
- Plot hooks: continent-scale, planar implications.

### 9th Level (Tier 4 capstone)

- World-changing or campaign-defining: Wish, Time Stop, True
  Polymorph, Imprisonment, Mass Heal, Power Word Kill.
- Each 9th-level spell should be **identity-defining** for its
  class or for the campaign.
- Lore section: deep history, cosmic implications.
- Plot hooks: multi-planar, civilization-scale.

---

## Interaction with Other Skills

- **Spell is tied to a specific NPC** (signature spell of a
  named caster) → run `npc-creator` for the caster, reference in
  lore. If the NPC is a major BBEG, this is their *signature
  move*.
- **Spell is tied to a faction** (the order's secret rite, the
  cult's forbidden incantation) → run `faction-creator`, reference
  in lore.
- **Spell appears in a magic item** (the staff casts X) →
  run `magic-item-creator`; that skill references the spell.
  Don't double-design.
- **Spell appears in a monster stat block** (innate spellcasting,
  spell-like ability) → run `monster-creator`; that skill handles
  the spell as a monster ability, often with slight modifications.
- **Spell defines a unique scenario / event** (the wizard is going
  to cast Ritual of X at midnight) → run `scenario-writer`; this
  spell is the McGuffin or the climax.
- **Originality check** (is my "Fire Bolt" too cliché?) → run
  `ttrpg-cliche-buster` on the spell concept before designing.
- **Read-aloud for the spell's first appearance** → run
  `read-aloud-crafter` on the dramatic casting moment.
- **Pre-publication review** (this spell is going into a class
  supplement) → run `ttrpg-supplement-reviewer` after designing.

---

## Edge Cases

**Brief is "create a spell"** with no specifics: ask for level,
school, intended effect (damage / control / utility / buff), and
class list. Without these, you build a generic spell.

**Brief asks for "the same as [PHB spell] but X":** Don't reproduce
copyrighted entries. Build from scratch with the requested twist
as the differentiator. Don't write the new entry as a "modification
of Fireball" — write it as its own spell that happens to share
the genre with Fireball.

**Brief asks for a spell that's actually a class feature** (a
Monk's quick-step, a Warlock invocation, a Bard's inspiration
upgrade): defer. Class features don't consume spell slots and
have different design constraints. Defer to a future class-
feature design skill, or rebrand the request as a spell that
happens to fit the theme.

**Brief asks for a 10th-level / Epic / Mythic spell:** defer.
This skill targets PHB 2024 standard slots only. Either re-frame
as 9th-level (the highest standard slot) or wait for the Epic
Spells skill.

**Brief asks for a "save-or-die" effect:** carefully. A
save-or-die at 5th level is acceptable on a creature with low Hit
Dice (Power Word Kill targets ≤100 HP). A save-or-die at lower
levels needs *failure consequence with degree*. Better design:
"on a fail, save *again* at end of next turn — if fail again,
unconscious — if fail third time, die." Saves with stages
preserve drama without one-shot lethality.

**Brief asks for a spell that consumes a specific costly
material:** good design when balance demands it. Consumed-component
spells limit casting frequency naturally. Use for: Revivify (300
gp diamond), Raise Dead (500 gp diamond), Resurrection (1,000 gp
diamond), Wish-tier effects. Components should be
*available-but-significant*, not arbitrary.

**Brief asks for a ritual spell:** check eligibility. Ritual-
tagged spells are non-combat, often utility / divination /
binding spells. Most damage and combat-control spells are *not*
ritual-eligible. Ritual lets the spell be cast for free outside
combat, at the cost of 10 extra minutes.

**Brief asks for a Concentration-free big-effect spell:**
carefully. The lack of Concentration lets a caster stack it with
another Concentration spell — that's a balance leak. Most
big-effect persistent spells SHOULD require Concentration. Only
*Instantaneous* effects, *very short* fixed durations (1 round),
or *self-only buffs* should escape Concentration.

**Brief asks for a spell exclusive to one class:** acceptable when
identity warrants it (Eldritch Blast = Warlock signature). For
most spells, share across 2–4 classes. Exclusive spells are
rare in PHB 2024 — most class-uniqueness comes from class
features, not spell lists.

**Adult content:** standard 5e produces SFW spells by default.
Adult-themed flavor can be layered after this skill produces the
mechanical baseline.

---

## Publication Checklist

Before considering a spell complete:

- [ ] Name (distinctive, evocative).
- [ ] One-line pitch.
- [ ] Visual / manifestation paragraph.
- [ ] Spell entry block: level + school (+ ritual), casting time,
      range, components, duration, classes.
- [ ] Description: lead with effect, then conditions, then
      exceptions. 1–4 paragraphs.
- [ ] Scaling (cantrip upgrade *or* "At Higher Levels").
- [ ] Identity hook visible (the spell isn't interchangeable with
      a same-level same-school neighbor).
- [ ] Power budget appropriate to level (load
      `balance-and-anti-patterns.md`).
- [ ] Concentration assigned correctly (ongoing impact → yes).
- [ ] Save / attack chosen with reason (AoE → save; single ranged
      → attack possible).
- [ ] Components reasonable (V, S default; M only if needed).
- [ ] Ritual tag only if eligible (non-combat utility).
- [ ] Class list thematic.
- [ ] Lore: maker, significance, notable uses.
- [ ] At least 1 plot hook.

---

## Reference Files

Load these as needed — not all at once.

- `references/spell-levels-and-tiers-2024.md` — Cantrip → 9th-level
  scaling. Expected magnitude per level (damage curves, condition
  cadence, utility scope). Spell slot economy by character level
  (how many slots of each level a caster has). Choosing the right
  level for a given concept. Anti-patterns ("under-leveled
  bloater," "over-leveled trinket").
- `references/schools-and-tradition-2024.md` — The 8 schools
  (Abjuration, Conjuration, Divination, Enchantment, Evocation,
  Illusion, Necromancy, Transmutation) detailed: thematic
  conventions, mechanical tendencies, pitfalls, anti-patterns
  ("damage-spell-mislabeled-as-Necromancy"), classic spells by
  school. French school names and vocabulary.
- `references/casting-time-and-components-2024.md` — Action /
  Bonus Action / Reaction / minute / hour / 24h. Reaction trigger
  syntax. Components (V, S, M with vs without cost). Ritual rules.
  Concentration discipline (when required, anti-patterns).
- `references/spell-effect-library.md` — Recurring effect patterns:
  damage shapes (cube, sphere, cone, line, cylinder), saves vs
  attacks, condition imposers, control effects, utility, buffs /
  debuffs, summons (2024 design pattern), battlefield-shape spells,
  divinations. With example formulae per level tier.
- `references/balance-and-anti-patterns.md` — Damage-by-level
  benchmarks (per PHB 2024 reference points). Save vs attack
  choice rules. AoE shape budgets. Scaling math (+1d / slot,
  variants). Condition cadence (save-end vs permanent-until-
  dispelled). Concentration vs no-Concentration discipline. Common
  anti-patterns: save-or-die at low level, no-save high damage,
  action-economy abuse (Bonus Action that's an Action-level
  effect), must-have-or-die (universal anti-everything spell),
  Concentration leak, ritual abuse, ceiling-buster (spell breaks
  encounter design).
