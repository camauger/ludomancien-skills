# 5e to PF2e Mapping

System architecture comparison, action economy, DCs, traits,
critical success/failure, conditions, ancestry/heritage, encounter
budget, spell heightening.

The most important fact: **PF2e is not a re-skin of 5e.** It's a
mathematically different system with different design priorities.
Converting requires more than swapping stat blocks.

---

## Action Economy: 5e vs PF2e

### 5e (2014/2024)

- On your turn:
  - **One Action** (Attack, Cast a Spell, Dash, Dodge, Disengage,
    Help, Hide, Ready, Search, etc.)
  - **One Bonus Action** (limited to specific abilities/spells)
  - **One Reaction** (per round, off-turn)
  - **Movement** (up to speed, split as you like)
- One leveled spell per turn (the bonus-action spell + cantrip rule
  unchanged in 2024).

### PF2e

- On your turn:
  - **Three Actions** per turn (✦). Use each for any action that
    costs 1 action.
  - Some actions cost 2 actions (e.g., casting most spells), some
    cost 3 (rare).
  - **One Reaction** per round (off-turn).
  - **Free actions** exist (limited, conditional).

### Conversion Impact

| 5e Action | PF2e Equivalent |
|---|---|
| Attack | Strike (1 action), with **Multiple Attack Penalty (MAP)** |
| Cast a Spell | Cast a Spell (usually 2 actions; cantrips often 2; some 1 or 3) |
| Dash | Stride (1 action) × 1, 2, or 3 |
| Dodge | Raise a Shield (if shield); else there's no direct equivalent. PF2e doesn't have a "Dodge action." |
| Disengage | Step (1 action — move 5 ft without triggering reactions) |
| Help | Aid (1 action) |
| Hide | Hide (1 action) |
| Ready | Ready (2 actions to set up trigger; reaction uses 0 actions on trigger) |
| Search | Seek (1 action) |
| Bonus Action (cast Bless) | Cast a Spell (2 actions) — Bless in PF2e is 1 action though |
| Reaction (Shield, Counterspell) | Reaction (different specific reactions per class) |

### Multiple Attack Penalty (MAP)

A core PF2e mechanic that radically reshapes combat:

- **First attack on turn:** no penalty.
- **Second attack on turn:** -5 to hit.
- **Third attack on turn:** -10 to hit.

(With Agile weapons: -4 / -8 instead of -5 / -10.)

**Impact:** A character with a +10 Strike at level 5 has
effectively +10 / +5 / 0 across three attacks. Most encounters
have PCs choosing one Strike + utility actions, not three Strikes.

**Conversion implication:** A 5e encounter calibrated for one
attack per PC per turn may be too easy in PF2e (PCs have more
options) or too hard if it relies on 3-Strikes-per-turn math.
Calibrate via PF2e encounter budget.

---

## DC System

### 5e

- Flat DCs: Easy (10), Medium (15), Hard (20), Very Hard (25),
  Nearly Impossible (30).
- Same DCs apply across levels.
- Skill check = d20 + ability mod + proficiency bonus.

### PF2e

- **Level-based DCs.** A DC is set by the *level of the task*
  (often equal to the level of the creature/character providing
  the challenge).
- Standard DCs by level:

| Level | DC |
|---|---|
| 0 | 14 |
| 1 | 15 |
| 2 | 16 |
| 3 | 18 |
| 4 | 19 |
| 5 | 20 |
| 6 | 22 |
| 7 | 23 |
| 8 | 24 |
| 9 | 26 |
| 10 | 27 |

(Continues +1.5 per level on average.)

- Adjusted by **rarity / difficulty steps:** Trivial (-2), Easy
  (-2), Hard (+2), Very Hard (+5), Incredibly Hard (+10).
- Skill check = d20 + level + ability mod + proficiency rank.

### Conversion Impact

A 5e "DC 15 Perception" check converts to PF2e as a level-based
DC. For a level-3 PC group facing a typical Perception task,
that's DC 18 (level 3 baseline). For a level-1 group, DC 15.

**Conversion rule of thumb:**

| 5e DC | PF2e equivalent (assuming party level matches) |
|---|---|
| DC 10 (Easy) | Trivial — PF2e baseline -2 or -5 |
| DC 15 (Medium) | Level-baseline DC for the party level |
| DC 20 (Hard) | Level-baseline +2 (Hard) |
| DC 25 (Very Hard) | Level-baseline +5 (Very Hard) |

---

## Critical Success / Critical Failure

### 5e

- Natural 20: critical hit on attacks (doubled damage dice).
- Natural 1: critical miss on attacks (auto-miss).
- Otherwise: success or failure based on meeting target value.

### PF2e

- **Roll 10+ above DC: critical success.**
- **Roll 10+ below DC: critical failure.**
- **Roll natural 20: increase success by one step** (failure →
  success; success → critical success).
- **Roll natural 1: decrease success by one step** (success →
  failure; failure → critical failure).
- Most rolls have four outcomes: critical failure, failure, success,
  critical success — each with distinct results.

### Conversion Impact

This is the **biggest cognitive shift** in 5e → PF2e conversion.

- 5e: "On a successful save, the target takes half damage."
- PF2e: "On a critical success, target takes no damage. On a
  success, target takes half damage. On a failure, target takes
  full damage. On a critical failure, target takes double damage
  and is dazzled for 1 minute."

**Conversion rule:** every save / check in 5e needs four PF2e
outcomes. Lean on PF2e's published spells for the pattern.

---

## Conditions

### 5e Conditions (binary)

Blinded, Charmed, Deafened, Frightened, Grappled, Incapacitated,
Invisible, Paralyzed, Petrified, Poisoned, Prone, Restrained,
Stunned, Unconscious, Exhaustion (graded 1-6).

### PF2e Conditions (graded)

PF2e has more conditions, many graded:

- **Frightened 1, 2, 3, 4** — penalty to all checks
- **Stupefied 1, 2, 3, 4** — penalty to mental checks
- **Sickened 1, 2, 3, 4** — penalty to checks
- **Drained 1, 2, 3, 4** — HP and Fortitude penalty
- **Doomed 1, 2, 3, 4** — death threshold
- **Wounded 1, 2, 3, 4** — death threshold increment
- **Dying 1, 2, 3, 4** — at 4, you die
- **Flat-footed** — -2 to AC
- **Off-guard** — combat advantage equivalent
- **Concealed** — 20% miss chance
- **Hidden** — 50% miss chance
- **Undetected** — full Hide benefit
- Standard binary conditions: Blinded, Confused, Controlled,
  Deafened, etc.

### Conversion Impact

- 5e "Frightened" → PF2e "Frightened 2" (typical level mapping).
- 5e "Poisoned" → PF2e "Sickened X" or "Drained X" depending
  on flavor.
- Conditions that affect attack rolls in 5e (Poisoned grants
  disadvantage) → in PF2e you use the graded version with
  specific check penalties.

---

## Ancestry / Heritage vs Race / Subrace

### 5e

- Race (Human, Elf, Dwarf, etc.) grants traits.
- Subrace (Hill Dwarf, High Elf, etc.) grants additional traits.

### PF2e

- **Ancestry** = race (Human, Elf, Dwarf, Gnome, Goblin, etc.).
- **Heritage** = specific lineage / variant (e.g., for Human: Skilled
  Heritage, Versatile Heritage; for Elf: Whisper Elf, Woodland
  Elf, etc.).
- **Ancestry Feats** = additional traits chosen at level 1, 5, 9, 13,
  17 — like 5e racial feats but as a system.

### Conversion Impact

- An NPC built with a 5e race + subrace converts to PF2e ancestry
  + heritage + ancestry feats.
- Most fantasy ancestries exist in both systems. PF2e has more
  variety in heritages.

---

## Class Structure

### 5e

- 13 classes (PHB 2024): Barbarian, Bard, Cleric, Druid, Fighter,
  Monk, Paladin, Ranger, Rogue, Sorcerer, Warlock, Wizard,
  Artificer.
- Subclasses chosen at level 1, 2, or 3.
- Class features at every level (some passive, some active).

### PF2e

- 12 core classes (Player Core 2): Alchemist, Barbarian, Bard,
  Champion, Cleric, Druid, Fighter, Investigator, Monk, Ranger,
  Rogue, Sorcerer, Wizard. (Plus expansions: Witch, Magus,
  Inventor, etc.)
- Most classes have **subclass options** (mostly via class feats
  at specific levels).
- **Class feats** every 2 levels, **skill feats** at 2/4/6...,
  **ancestry feats** at 1/5/9/13/17.

### Conversion Impact

- A 5e PC build converts approximately by:
  1. Matching class.
  2. Matching subclass (cleric domain → cleric doctrine + deity).
  3. Choosing ancestry / heritage / ancestry feats.
  4. Choosing class feats that match the 5e PC's features.
  5. Adjusting for the action economy.

- A 5e NPC's class can be inferred → PF2e class. Most fantasy
  archetypes match.

---

## Encounter Budget

### 5e Encounter Calibration

- **Easy / Medium / Hard / Deadly** thresholds based on party
  level + size.
- XP budget per encounter; multiplied by encounter multiplier for
  multi-monster fights.

### PF2e Encounter Calibration

- **Trivial / Low / Moderate / Severe / Extreme** thresholds.
- XP budget (party of 4): 40 (Trivial), 60 (Low), 80 (Moderate),
  120 (Severe), 160 (Extreme).
- Adjusted by party size.
- Per-creature XP set by **creature level vs party level:**

| Creature vs Party | XP |
|---|---|
| Lower by 4+ | 0 (trivial, no XP) |
| Lower by 3 | 10 |
| Lower by 2 | 20 |
| Lower by 1 | 30 |
| Equal | 40 |
| Higher by 1 | 60 |
| Higher by 2 | 80 |
| Higher by 3 | 120 |
| Higher by 4+ | 160 (boss) |

### Conversion Rule

| 5e | PF2e |
|---|---|
| Easy encounter | Low (mostly trivial in PF2e) |
| Medium encounter | Low to Moderate |
| Hard encounter | Moderate to Severe |
| Deadly encounter | Severe to Extreme |

Note: PF2e's "Moderate" encounter is a real challenge; PF2e's
"Severe" is genuinely dangerous; PF2e's "Extreme" is boss-vs-PCs
or near-TPK. Calibrate carefully.

---

## Spell Conversion

### 5e Spells → PF2e Spells

Most fantasy staple spells exist in both systems with similar
flavor, different mechanics.

| 5e Spell | PF2e Equivalent |
|---|---|
| Fireball (3rd lvl, 8d6) | Fireball (3rd lvl, 6d6, level-scaled) |
| Magic Missile | Magic Missile |
| Cure Wounds | Heal |
| Mage Hand | Telekinetic Hand |
| Shield (1st lvl reaction) | Shield (cantrip) |
| Bless (1st lvl) | Bless (1st lvl) |
| Hold Person | Paralyze |
| Polymorph | Animal Form / specific polymorph spells |
| Banishment | Banishment |
| Wish | Wish (still 9th lvl) |

### Heightening (PF2e) vs Higher-Level Slot (5e)

- **5e:** Cast a spell at a higher slot to gain "At Higher Levels"
  benefit.
- **PF2e:** Heighten a spell to a specific spell rank (1st through
  10th rank). Heightening rules per spell specify what changes
  per rank above base.

### Conversion Protocol

1. Match the spell by name + flavor.
2. Use PF2e's published version if it exists.
3. Adjust damage and effects to PF2e's scaling.
4. Document if "At Higher Levels" → "Heightened" conversion
   changes anything material.

---

## Spell Components / Casting

### 5e

- V (verbal), S (somatic), M (material with optional cost).
- Concentration (one at a time, save on damage).

### PF2e

- **Components:** verbal, somatic, material, focus.
- **Sustained spells** (similar to Concentration but explicitly
  sustained as an action each turn).
- **Concentrate trait** — many spells have this; sustain action
  needed; can be interrupted.

### Conversion Impact

- 5e Concentration → PF2e Sustain Action (1 action per turn to
  keep the spell going).
- Component changes are usually preserved for flavor; mechanically
  PF2e components mostly map (V, S, M).

---

## Healing and Death

### 5e

- HP recovery: short rest (1+ Hit Die), long rest (full HP).
- Death: at 0 HP, death saves (3 successes / 3 failures).

### PF2e

- HP recovery: rests of 8+ hours restore full HP; shorter rests
  with appropriate skills (Treat Wounds, Refocus).
- Death: **Wounded condition** stacks on each occasion you drop to
  0 HP. **Dying X** condition advances on failed Recovery saves.
  At Dying 4, you die.

### Conversion Impact

- 5e "death saves" → PF2e "Dying X with Recovery saves."
- The mechanics are different but flavor preserved.

---

## Conversion Checklist (5e → PF2e)

- [ ] Every stat block's AC re-baselined (PF2e AC ~2 higher at
      same level baseline).
- [ ] HP re-baselined (PF2e creatures often have higher HP at
      same level).
- [ ] Strike instead of Attack (with MAP awareness in tactics).
- [ ] Spells heightened/converted to PF2e rank.
- [ ] DCs level-scaled to PF2e DC table.
- [ ] Conditions graded (Frightened 1-4 etc.).
- [ ] Critical success / failure outcomes documented for saves and
      attacks.
- [ ] Ancestry / heritage assigned to NPCs.
- [ ] Class feats and skill feats outlined for NPC builds.
- [ ] Encounter XP recalibrated to PF2e budget.
- [ ] Action economy noted (PF2e characters have 3 actions; one
      Strike often + utility).
- [ ] Conversion notes flag major design-philosophy shifts.
