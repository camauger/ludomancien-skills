# 5e to OSR Translation

OSR sub-systems compared (B/X, OSE, Shadowdark, Dolmenwood,
generic old-school), HP scaling, save categories, encounter
philosophy, treasure-as-XP, dungeon time tracking, spell
conversion.

Converting 5e to OSR is **not just a math change** — it's a
philosophy change. OSR play prioritizes player skill over
character builds, GM rulings over rules, exploration over
narrative pacing, and lethality over heroism.

---

## OSR Sub-Systems

Pick one before converting. Each has different defaults.

### B/X (1981 Basic / Expert) and OSE (Old-School Essentials)

- **Most classic.** Direct descendant of original D&D.
- **Descending AC** (AC 9 default; AC 0 = good plate).
- **Saving throw categories:** Death/Poison, Wands, Paralysis/
  Petrification, Breath, Spells.
- **HD = level.** Classes capped (often at 14).
- **Race-as-class** option in B/X (Halfling, Elf, Dwarf are classes).
- **OSE** is a clean modern restatement of B/X — recommended target.

### Shadowdark (2023, Kelsey Dionne)

- **Modern OSR.** Ascending AC, ability-modifier-based.
- **Five saving throws:** STR, DEX, CON, INT, WIS, CHA (each
  ability as a save).
- **Real-time torch tracking** (1 hour real-time = 1 hour torch).
- **Streamlined spells:** spellcasters roll to cast, can lose
  spell on failure.
- **Modern compatibility** with 5e fans wanting OSR feel.

### Dolmenwood (2024, Necrotic Gnome)

- **OSE-based** with rich setting integration.
- Same mechanics as OSE.

### Generic Old-School

- Used when target is unspecified. Apply B/X assumptions: descending
  AC, save categories, race-as-class optional.

---

## Stat Block Comparison

### 5e Stat Block

```
Goblin
Small Humanoid, Neutral Evil
Armor Class 15
Hit Points 7 (2d6)
Speed 30 ft

STR 8 (-1) DEX 14 (+2) CON 10 (+0) INT 10 (+0) WIS 8 (-1) CHA 8 (-1)
Skills Stealth +6
Senses Darkvision 60 ft, passive Perception 9
Languages Common, Goblin
Challenge 1/4 (50 XP)
Proficiency Bonus +2

Nimble Escape. The goblin can take the Disengage or Hide action
as a bonus action on each of its turns.

ACTIONS
Scimitar. Melee Weapon Attack: +4 to hit, reach 5 ft., one target.
Hit: 5 (1d6+2) slashing damage.

Shortbow. Ranged Weapon Attack: +4 to hit, range 80/320 ft.,
one target. Hit: 5 (1d6+2) piercing damage.
```

### B/X / OSE Equivalent

```
Goblin
AC 6 [13]    HD 1-1    Att 1 weapon (1d6)    THAC0 20 [+0]
MV 60' (20')    SV D14 W15 P16 B17 S18 (NH)    ML 7
AL Chaotic    XP 5    NA 2d4 (6d10)    TT (R)
- Nimble: -1 to hit them in melee with surprise
- Surprise: 1-3 on d6 (vs 1-2 standard)
- Hate light, lurk in darkness
```

Notes:
- **AC 6 [13]** = descending AC 6 (with ascending equivalent 13 in
  brackets for OSE).
- **HD 1-1** = 1 hit die, -1 HP (= about 3-4 HP avg).
- **THAC0** = "To Hit Armor Class 0" — old-school attack
  resolution.
- **SV** = saving throws across five categories.
- **ML** = morale (when does the monster flee).
- **XP 5** = treasure-and-fight XP awarded.
- **NA** = Number Appearing (in dungeon, in wilderness).
- **TT (R)** = Treasure Type (varies by table).

### Shadowdark Equivalent

```
Goblin
AC 12, HP 5, ATK 1 weapon +1 (1d6), MV near, S -1, D +2, C +0,
I -1, W -1, Ch -1, AL Chaotic, LV 1

- Stealthy: +5 advantage on Hide checks
- Lurk: hates bright light
```

Notes:
- **AC 12** = ascending AC (5e-like math).
- **MV near** = simple range bands (close, near, far).
- **Abilities as modifiers** (5e-like).
- **LV 1** = creature level (used for encounter XP).

---

## HP Scaling

This is the biggest mechanical shift.

### 5e HP

A 5e Goblin: 7 HP. A 5e Dragon: 200+ HP. Players are heroes who
survive multiple hits.

### OSR HP

A B/X Goblin: 3-4 HP. A B/X Dragon: 30-50 HP. Players die fast,
even at higher levels.

### Conversion Protocol

| 5e CR | OSR HD |
|---|---|
| 0 | 1-1 (1d6 -1 HP, ~3 HP) |
| 1/8 | 1d6 (1 HD) |
| 1/4 | 1d8 |
| 1/2 | 1d10 or 2d6 |
| 1 | 2 HD (2d8, ~10 HP) |
| 2 | 3 HD |
| 3 | 4 HD |
| 5 | 6 HD |
| 10 | 12 HD |
| 17 | 17-20 HD |

OSR HP totals are dramatically lower than 5e equivalents.
**Calibrate encounter difficulty accordingly.**

---

## AC and Attack Resolution

### 5e

- **Ascending AC:** higher is better. Typical range 10-22.
- **Attack roll:** d20 + bonus, beat AC.

### B/X / OSE (Descending AC)

- **Descending AC:** lower is better. AC 9 = no armor, AC 0 = good
  plate.
- **THAC0 system:** subtract THAC0 from AC to determine roll
  needed.
- Some OSR products provide both descending and ascending notations
  (OSE does this).

### Shadowdark (Ascending AC)

- **Ascending AC:** like 5e.
- **Attack roll:** d20 + bonus, beat AC.

### Conversion Protocol

| 5e AC | B/X AC (descending) | Ascending equivalent |
|---|---|---|
| 10 (no armor) | 9 | 10 |
| 12 (leather) | 7 | 12 |
| 14 (chain shirt) | 5 | 14 |
| 16 (chain mail) | 4 | 15 |
| 18 (plate) | 3 | 16 |
| 20 (plate + shield) | 1 | 18 |

OSR AC peaks lower than 5e because attacks are simpler and HP
is lower.

---

## Saving Throws

### 5e (six ability-based saves)

STR, DEX, CON, INT, WIS, CHA saves. d20 + ability mod + prof bonus.

### B/X / OSE (five categories)

| Category | What |
|---|---|
| Death/Poison (D) | Toxic effects, death magic |
| Wands (W) | Ray/wand effects |
| Paralysis/Petrification (P) | Paralyzing or stoning effects |
| Breath weapon (B) | Dragon breath, AoE attacks |
| Spells (S) | General spell effects not in others |

Each class has fixed save targets per level (no roll formulas —
just "did you roll equal to or higher than your save score").

### Shadowdark (six ability saves)

Like 5e (STR/DEX/CON/INT/WIS/CHA saves), simpler.

### Conversion Protocol

| 5e Save | B/X Save | Shadowdark Save |
|---|---|---|
| Con save vs poison | Death/Poison | Con save |
| Dex save vs trap dart | Death/Poison or Paralysis | Dex save |
| Wis save vs charm | Spells | Wis save |
| Dex save vs fireball | Breath | Dex save |
| Cha save vs banishment | Spells | Cha save |
| Int save vs psychic | Spells | Int save |

For B/X conversions, pick the most-applicable save category. For
Shadowdark, use the same ability save.

---

## Skill Checks

### 5e

- 18 skills, each tied to an ability.
- Roll d20 + ability mod + proficiency.

### OSR (B/X, OSE, classical)

- **No skill system in classic OSR.** All non-combat resolution
  is GM-fiat ability check or saving throw.
- Specific systems: Thief skills (% chance per level: Open Locks
  20%, Find Traps 15%, etc.) — only Thieves get these.
- Other classes: GM rules. "Roll under your STR on d20" or "succeeds
  automatically."

### Shadowdark

- Ability checks (5e-style) for most resolution.
- Some streamlined skill mechanics for specific classes.

### Conversion Protocol

- 5e skill checks → **OSR GM-fiat call** with ability check OR
  saving throw OR procedure (open lock = Thief % roll). Don't
  preserve 5e's "DC 15 Investigation" — convert to "the trapdoor
  is found by anyone who declares they're carefully examining the
  floor; players who rush are surprised."
- Document **what you converted** (the procedural OSR call) vs
  what you kept (5e-style ability check).

---

## Encounter Calibration

### 5e Encounter Budget

Numerical XP budget. Targeting Medium-to-Deadly difficulty.

### OSR Encounter Philosophy

- **Lethality is the design.** A 1st-level B/X PC has 1-6 HP
  (often 3-4). A goblin does 1d6 damage. **Two hits often = dead.**
- Encounters often resolved by:
  - **Reaction roll** (2d6 vs monster reaction table: Hostile,
    Unfriendly, Cautious, Indifferent, Friendly, Helpful).
  - **Morale check** (will the monster keep fighting? Roll ≤ Morale
    score on 2d6).
  - **Random encounter rolls** (per turn or per watch).
- Combat is a choice, often not the optimal one.

### Conversion Protocol

For a 5e encounter to feel right in OSR:

1. **Reduce monster count** to 1-2 of party-HD-level, or many low-
   HD monsters.
2. **Add reaction-roll context.** The monster has a goal; reaction
   is its initial disposition. Combat is one possible outcome.
3. **Include morale.** Monsters flee on bad morale rolls. Most
   fights don't go to the death.
4. **Include random encounter rolls** in dungeon procedure.
5. **Recalibrate "Hard encounter"** to **2-3 HD per PC** total.
   "Deadly" in 5e becomes "TPK risk" in OSR.

### XP Source

- **5e:** XP from defeating monsters.
- **OSR:** XP from monster *defeat* + XP from **recovering
  treasure** (often 1 XP per 1 GP recovered from a dungeon to a
  safe place).

This is the key OSR design move: **adventurers risk for gold,
gold = XP**. Treasure is *gameplay*, not a side reward.

---

## Dungeon Time Tracking

### 5e

Loose tracking. Long rests recover everything; short rests recover
some. Most dungeons playable in one session.

### OSR (classic)

- **Turn = 10 minutes** in dungeon time.
- **Watch = 4 hours** in wilderness time.
- **Torch burns 6 turns** (60 minutes real-time of dungeon time).
- **Random encounter roll every 2-3 turns** in dungeon.
- **Spell duration:** turns or rounds, not minutes/hours of real
  time.
- **Rest mechanics:** require safe shelter; long rests dangerous in
  the wild.

### Shadowdark

- **Real-time torch tracking** (every 1 hour of real play time =
  1 hour of in-fiction torch burn). Aggressive.
- **Encounter rolls every 1 hour** real-time.

### Conversion Protocol

- Document expected turn count for the dungeon.
- Add random encounter table (d6 or d8) for the dungeon.
- Specify torch / light tracking expectations.
- Adjust spell durations to dungeon-turns where applicable.

---

## Spells

### 5e Spells in OSR

Most fantasy staples exist in OSR systems. But OSR spells are:
- **Coarser** (less granular).
- **Per-day**, not per-spell-slot (e.g., 1 spell per day at level 1
  for Magic-User).
- **Vancian** (memorized spell, cast and gone — classic OSR; some
  systems modernized).

| 5e Spell | B/X Equivalent | Shadowdark Equivalent |
|---|---|---|
| Magic Missile | Magic Missile (1 missile per 5 caster levels) | Magic Missile (1d4 damage + scaling) |
| Fireball | Fireball (1d6 per caster level, max 10d6) | Fireball (5d6 in a 20-ft sphere) |
| Cure Light Wounds | Cure Light Wounds (1d6+1 healing) | Heal (1d8 healing) |
| Sleep | Sleep (creatures with 4 HD or less; 2d8 HD total affected) | Sleep |
| Charm Person | Charm Person | Charm Person |
| Invisibility | Invisibility | Invisibility |
| Detect Magic | Detect Magic | Detect Magic |
| Lightning Bolt | Lightning Bolt (1d6/level) | Lightning Bolt |
| Polymorph | Polymorph (Self / Other) | Polymorph |
| Wish | Wish (or "no Wish-tier" in some OSR) | Wish |

### Casting Mechanics

- **B/X / OSE:** Memorized spell. Cast and forget. Prepare another
  on rest.
- **Shadowdark:** Spell roll. Roll vs DC; on success, cast and
  retain. On failure, spell lost for the day.
- **5e Concentration:** does NOT exist in OSR. Spells either run
  duration or end.

### Conversion Protocol

- Find OSR equivalent by name; use OSR mechanics (slot vs roll).
- Drop Concentration; OSR spells just run.
- Reduce duration if the OSR equivalent is shorter.

---

## Class Equivalents

| 5e Class | B/X / OSE Class | Shadowdark Class |
|---|---|---|
| Fighter | Fighter | Fighter |
| Barbarian | Fighter (or Berserker variant) | Fighter (Berserker option) |
| Rogue | Thief | Thief |
| Wizard / Sorcerer | Magic-User | Wizard |
| Warlock | Magic-User (or invent) | Wizard |
| Cleric | Cleric | Priest |
| Paladin | Cleric or Fighter | Priest / Fighter blend |
| Ranger | Fighter (or Ranger variant) | Ranger |
| Druid | Druid | Druid |
| Bard | Bard (variant) | Bard |
| Monk | Monk (variant) or invent | Not standard |

5e subclasses generally don't convert cleanly. Most OSR classes
are simpler "do one thing well." Convert by **role**, not
mechanically.

---

## Magic Item Conversion

5e magic items are richer than OSR equivalents.

| 5e Item | OSR Equivalent |
|---|---|
| +1 Sword | Sword +1 |
| Ring of Protection | Ring of Protection |
| Bag of Holding | Bag of Holding |
| Cape of Mountebank | Cloak of Displacement (functional analog) |
| Cloak of Elvenkind | Cloak of Elvenkind |
| Robe of the Archmagi | Robe of the Archmagi |
| Wand of Fireballs | Wand of Fireballs |
| Sentient items, complex magic items | Usually omitted; OSR keeps items simpler |
| Cursed items | Frequently used; OSR-style curses are nasty |

OSR items don't have:
- Attunement (usually)
- Charges that recharge daily
- Complex action-economy interactions

OSR items often have:
- "Cursed unless you do X" wrinkles
- "Costs Y to use" mechanics (sacrifice a hit point, etc.)
- Single-use scrolls

---

## Treasure-as-XP

A core OSR mechanic worth highlighting.

- **5e:** XP from monster kills.
- **OSR:** XP from monster defeat + XP from gold recovered.

In classical OSR: **1 GP recovered = 1 XP** (or higher rate).

**Conversion implication:**
- Treasure value in the source 5e adventure matters more in OSR.
- An OSR encounter "worth playing" is one where treasure pays out
  enough XP.
- A 5e adventure with $100 GP per encounter converts to OSR as
  XP-rich; one with $1000 GP per encounter as moderate.
- Some OSR systems halve or quarter the rate (1 GP = 1/4 XP) to
  prevent XP inflation; check the specific OSR system.

---

## Conversion Checklist (5e → OSR)

- [ ] OSR sub-system selected (B/X, OSE, Shadowdark, etc.).
- [ ] HP reduced to OSR HD-based formulas.
- [ ] AC converted (descending or ascending per sub-system).
- [ ] Saves converted (5 categories for B/X; 6 ability saves for
      Shadowdark).
- [ ] Skill checks converted to ability check / saving throw /
      class-skill (% Thief skills) / GM-fiat.
- [ ] Encounter counts reduced (1-2 HD-per-PC max; not 4+
      monsters of equivalent CR).
- [ ] Random encounter table added.
- [ ] Reaction roll context added.
- [ ] Morale documented for monsters.
- [ ] Spells converted to OSR list (or marked custom).
- [ ] Concentration dropped from converted spells.
- [ ] Treasure-as-XP rate documented.
- [ ] Dungeon procedure (turns, torches, encounters) explained.
- [ ] Lethality warning in GM notes ("OSR play kills PCs faster").
