# Challenge Rating Design Protocol — D&D 5e 2024

This reference gives the numerical anchors for designing balanced
monsters at any Challenge Rating in D&D 5e 2024.

**Honest note on sources:** the 2024 Dungeon Master's Guide includes a
chapter on *Creating a Monster* with its own simplified protocol and
stat block templates by CR. The benchmarks in this file derive from the
2014 DMG table (Monster Statistics by CR) which the 2024 version
preserves with light adjustments. Use these as **design targets** that
will produce correctly-felt monsters at any given CR; verify against the
2024 DMG before publishing if the product targets official tournament
or commercial play.

---

## 1. Master CR Table

Each row shows the expected values for a creature *at* that CR. A
monster designed for CR X should fall close to these numbers; deviation
in one stat is offset by adjustment in another (see Section 4).

| CR | Prof Bonus | AC | HP | Attack Bonus | DPR | Save DC | XP |
|---|---|---|---|---|---|---|---|
| 0 | +2 | ≤13 | 1–6 | +3 | 0–1 | 13 | 0 or 10 |
| 1/8 | +2 | 13 | 7–35 | +3 | 2–3 | 13 | 25 |
| 1/4 | +2 | 13 | 36–49 | +3 | 4–5 | 13 | 50 |
| 1/2 | +2 | 13 | 50–70 | +3 | 6–8 | 13 | 100 |
| 1 | +2 | 13 | 71–85 | +3 | 9–14 | 13 | 200 |
| 2 | +2 | 13 | 86–100 | +3 | 15–20 | 13 | 450 |
| 3 | +2 | 13 | 101–115 | +4 | 21–26 | 13 | 700 |
| 4 | +2 | 14 | 116–130 | +5 | 27–32 | 14 | 1,100 |
| 5 | +3 | 15 | 131–145 | +6 | 33–38 | 15 | 1,800 |
| 6 | +3 | 15 | 146–160 | +6 | 39–44 | 15 | 2,300 |
| 7 | +3 | 15 | 161–175 | +6 | 45–50 | 15 | 2,900 |
| 8 | +3 | 16 | 176–190 | +7 | 51–56 | 16 | 3,900 |
| 9 | +4 | 16 | 191–205 | +7 | 57–62 | 16 | 5,000 |
| 10 | +4 | 17 | 206–220 | +7 | 63–68 | 16 | 5,900 |
| 11 | +4 | 17 | 221–235 | +8 | 69–74 | 17 | 7,200 |
| 12 | +4 | 17 | 236–250 | +8 | 75–80 | 17 | 8,400 |
| 13 | +5 | 18 | 251–265 | +8 | 81–86 | 18 | 10,000 |
| 14 | +5 | 18 | 266–280 | +8 | 87–92 | 18 | 11,500 |
| 15 | +5 | 18 | 281–295 | +8 | 93–98 | 18 | 13,000 |
| 16 | +5 | 18 | 296–310 | +9 | 99–104 | 18 | 15,000 |
| 17 | +6 | 19 | 311–325 | +10 | 105–110 | 19 | 18,000 |
| 18 | +6 | 19 | 326–340 | +10 | 111–116 | 19 | 20,000 |
| 19 | +6 | 19 | 341–355 | +10 | 117–122 | 19 | 22,000 |
| 20 | +6 | 19 | 356–400 | +10 | 123–140 | 19 | 25,000 |
| 21 | +7 | 19 | 401–445 | +11 | 141–158 | 20 | 33,000 |
| 22 | +7 | 19 | 446–490 | +11 | 159–176 | 20 | 41,000 |
| 23 | +7 | 19 | 491–535 | +11 | 177–194 | 20 | 50,000 |
| 24 | +7 | 19 | 536–580 | +11 | 195–212 | 21 | 62,000 |
| 25 | +8 | 19 | 581–625 | +12 | 213–230 | 21 | 75,000 |
| 26 | +8 | 19 | 626–670 | +12 | 231–248 | 21 | 90,000 |
| 27 | +8 | 19 | 671–715 | +12 | 249–266 | 22 | 105,000 |
| 28 | +8 | 19 | 716–760 | +12 | 267–284 | 22 | 120,000 |
| 29 | +9 | 19 | 761–805 | +13 | 285–302 | 22 | 135,000 |
| 30 | +9 | 19 | 806–850 | +13 | 303–320 | 23 | 155,000 |

**Reading the table:**

- **AC** is the expected armor class. ±1 is normal variance; ±2 starts
  to shift the effective CR.
- **HP** is the *average* hit points. Use the midpoint of the range.
- **Attack Bonus** applies to weapon attacks. Add proficiency bonus +
  relevant ability modifier and check against this number.
- **DPR** is *damage per round* averaged over 3 rounds, assuming all
  attacks hit (or assuming standard hit rate for save-based effects).
  This is the single most important number for offensive balance.
- **Save DC** applies to abilities forcing saves. Calculated as
  `8 + proficiency bonus + relevant ability modifier`.

---

## 2. Offensive CR vs Defensive CR

A monster has **two effective CRs** that you average:

### Defensive CR (driven by HP and AC)

1. Find the CR row that matches the monster's HP.
2. If the actual AC is **2 or more above** the expected AC for that row,
   bump defensive CR by 1 (per 2 AC above).
3. If the actual AC is **2 or more below** the expected AC, drop
   defensive CR by 1 (per 2 AC below).
4. **HP adjustment for resistances and immunities** — a creature with
   resistance to most damage types effectively doubles its HP for CR
   calculation. Apply this multiplier *before* matching to the HP table:
   - Resistance to one common damage type (e.g., bludgeoning): ×1.0
     (cosmetic, doesn't change CR)
   - Resistance to non-magical weapon attacks (the classic "magic
     weapon required"): ×1.5 effective HP up to CR 10; ×1.25 above
   - Resistance to two or more common damage types: ×1.25
   - Immunity to one common damage type: equivalent to resistance,
     ×1.0 to ×1.25
   - Immunity to multiple common damage types: ×1.5
   - Immunity to most damage (golems, oozes with many immunities):
     ×2 effective HP for low CR, ×1.5 above CR 10

### Offensive CR (driven by DPR and Attack Bonus / DC)

1. Find the CR row that matches the monster's DPR.
2. If the actual attack bonus is **2 or more above** the expected
   value for that row, bump offensive CR by 1.
3. If the actual attack bonus is **2 or more below**, drop offensive
   CR by 1.
4. **Damage adjustment for save-or-suck** — a single-target attack that
   imposes a debilitating condition (paralysis, charm, banishment)
   effectively adds damage. Treat the condition as roughly equivalent
   to an extra attack's worth of damage for a few rounds.

### Final CR

Average the two effective CRs. If they differ by more than 2, the
creature is **lopsided** — it will feel unfair or trivial. Redesign
either the offense or the defense to bring them within 2 of each other.

### Worked example

A homebrew CR 5 creature:
- AC 17 (expected: 15, so +2 → defensive CR +1)
- HP 145 (in range for CR 5)
- Resistance to non-magical weapons (×1.5 effective HP → ~217 HP, in
  range for CR 10 → defensive CR jumps massively)
- Multiattack: 2 attacks at +6 attack bonus
- Average damage: 36 per round (in range for CR 5)

**Defensive CR:** the resistance to non-magical weapons is dominant.
Treating effective HP as 217 places it in the CR 10–11 range, but
this is misleading for a low-level party (they may not have magic
weapons yet). For a party expected to fight this at level 5–6, the
resistance is *very* punishing → defensive CR ~9.
**Offensive CR:** AC and attack bonus match CR 5. DPR matches CR 5 →
offensive CR 5.
**Average:** 7. The creature is lopsided (defense > offense by 4).
Either: (a) drop the resistance, (b) increase DPR significantly to
CR 8 levels, or (c) accept that this creature is meant to be a
sponge-defender rather than a damage threat.

---

## 3. Combat Length Calibration

DPR benchmarks assume the creature lives for **3 rounds**. If the
creature is designed to live longer or shorter, recalibrate:

- **Glass cannon** (designed to drop in 1–2 rounds): can have DPR
  one tier above its CR.
- **Sponge** (designed to live 4–5+ rounds): should have DPR one tier
  below its CR, with the extra HP making up the encounter math.
- **Marathon** (legendary creature that fights for 6+ rounds with
  multiple phases): DPR matches CR but reserve burst damage for
  late-phase activations.

---

## 4. Adjustment Levers (Without Changing CR)

You can shape *how a creature feels* without moving its CR:

| Lever | Effect on play feel | CR impact |
|---|---|---|
| ↑ AC by 2, ↓ HP by 15% | Spikier; relies on dodging | Neutral |
| ↓ AC by 2, ↑ HP by 15% | Brutish; eats damage | Neutral |
| Multiattack: 2× attacks at half damage each | Reliable damage, hard to miss | Neutral |
| Single high-damage attack | Swingy; can whiff round 1 | Neutral |
| Recharge 5–6 signature ability | Burst threat round 1, then waiting game | Neutral |
| Add a controlling rider (prone, restrained, frightened) | Tactical depth | +0 to +1 effective CR |
| Add reaction (Parry, Riposte, Mage Slayer) | Punishes specific party tactics | +0 to +1 effective CR |
| Legendary actions | Action economy parity vs party | +1 to +3 CR (built into base CR) |
| Lair actions | Environmental threat layer | Adds 1 to CR for that fight only |
| Multi-phase HP threshold | Reset action economy mid-fight | +1 to +2 effective CR |

---

## 5. Standard Stat Block Calibrations

Quick reference values for each CR's stat block. Use these as starting
points and adjust by role (see `combat-roles.md`).

### CR 1 baseline

```
AC 13 · HP 75 (10d8+30) · Speed 30 ft.
Ability scores: 14 / 12 / 14 / 10 / 12 / 10 (Brute slant)
Prof Bonus +2
Attack: +5 to hit (Str +2 + prof +2 + magic +1) — 1d8+3 (avg 7.5) ×1
DPR: ~11
```

### CR 5 baseline

```
AC 15 · HP 140 (16d10+48) · Speed 30 ft.
Ability scores: 18 / 14 / 16 / 10 / 14 / 12 (Soldier slant)
Prof Bonus +3
Attack: +7 to hit — 1d10+4 (avg 9.5) ×2 attacks
DPR: ~19 (under target)
Add: Recharge 5–6 ability dealing 4d8 (avg 18) → 3-round avg DPR ~25 (still low)
Solution: bump multiattack to 3 attacks, or give riders that add effective damage
Final target: ~35 DPR
```

### CR 10 baseline

```
AC 17 · HP 215 (23d10+92) · Speed 40 ft.
Ability scores: 20 / 16 / 18 / 14 / 16 / 14 (Soldier slant)
Prof Bonus +4
Attack: +9 to hit — 2d8+5 (avg 14) ×2 attacks
DPR: ~28
Add: Recharge 5–6 area ability for 8d6 (avg 28) on a DC 16 save
3-round avg DPR: ~50, above the 63–68 target
Solution: keep multiattack tight, or add a debuff rider that effectively adds damage
Final calibration: aim for 60–68 DPR over 3 rounds
```

### CR 15 baseline

```
AC 18 · HP 290 (28d10+112) · Speed 40 ft. (+ flying if applicable)
Ability scores: 22 / 14 / 22 / 18 / 16 / 18 (Soldier/Caster slant)
Prof Bonus +5
Attack: +11 to hit — 2d10+6 (avg 17) ×3 attacks
DPR: ~51
Add: Recharge ability for 14d6 (avg 49)
3-round DPR avg: ~85 (in CR 15 range of 93–98 — slightly under target)
Solution: bump recharge or add legendary actions (3/turn)
Legendary actions add: Attack action ×3/turn at ~17 each → +51 effective DPR distributed across turns
This pushes the encounter weight up correctly for CR 15
```

### CR 20 baseline (Tier 4 capstone)

```
AC 19 · HP 380 (30d12+180) · Speed 40 ft. (+ flying, swim, climb)
Ability scores: 26 / 16 / 26 / 24 / 22 / 24 (Capstone slant)
Prof Bonus +6
Attack: +13 to hit — 3d10+8 (avg 24.5) ×3 attacks
DPR: ~73
Add: Recharge ability dealing 18d6 (avg 63)
Legendary actions: 3/turn, with at least one Attack-equivalent (~25 damage)
Lair actions: contribute environmental damage and control
3-round combat DPR avg with all systems: ~125–140 (matches CR 20)
```

---

## 6. Saving Throw and Skill DCs

The Save DC column applies to monster abilities that force saves
against effects (breath weapons, charms, frightening presence, etc.).

For *skill DCs* the party must beat (Stealth vs the monster's Perception,
Athletics vs the monster's Strength save, etc.), use the monster's
passive Perception or save modifier directly.

### Conversion table

| Stat / Skill bonus | Implied Save DC |
|---|---|
| +0 | DC 10 |
| +2 | DC 12 |
| +4 | DC 14 |
| +6 | DC 16 |
| +8 | DC 18 |
| +10 | DC 20 |

---

## 7. Movement Speeds

| Mode | Standard | Notes |
|---|---|---|
| Walk | 30 ft. | Default for Medium / Small humanoids |
| Walk (heavy) | 20 ft. | Gnomes, dwarves, encumbered |
| Walk (fast) | 40 ft. | Beasts, elves, athletic creatures |
| Walk (very fast) | 50–60 ft. | Apex predators (cheetah-style) |
| Burrow | 10–30 ft. | Subterranean dwellers |
| Climb | 20–30 ft. | Arboreal, spider-like, agile |
| Fly | 40–60 ft. | Standard winged creatures |
| Fly (hover) | Yes/No | Hover requires no flapping mechanic; affects positioning |
| Swim | 30–60 ft. | Aquatic creatures; double for fast swimmers |

**Tactical note:** flying creatures with no other restriction quickly
break encounters. Modern 2024 design often gives flying creatures one
of: (a) restricted altitude (must stay within 60 ft. of ground), (b)
ranged attack only without melee multiattack, (c) a "swoop" action
that triggers opportunity attacks, or (d) clipped wings via a
specific party action.

---

## 8. Common Errors and How to Catch Them

### Error: "DPR feels too low at the table"

- Recharge abilities are statistically expected to fire ~once every
  3 rounds. If your creature's signature attack is on Recharge 5–6
  and the fight ends in 2 rounds, that damage never lands.
- **Fix:** if the creature is designed to die fast, make the signature
  attack non-recharge. Or add a "first turn" trigger that fires it
  automatically once.

### Error: "Multiattack feels like overkill"

- Multiattack of 3+ at-will attacks against a single PC can drop them
  in one round. This isn't a balance error (the DPR matches CR) but
  a *feel* error.
- **Fix:** require Multiattack to spread across different targets, OR
  give the multiattack pattern variety (1 weapon + 1 spell + 1
  ability instead of 3 identical weapon swings).

### Error: "AC is too high and the party never hits"

- AC above table by 3 or more turns a fight into a slog. Party
  damage drops 30% per +2 AC.
- **Fix:** check the AC against the table. If above, drop it, OR
  add a "vulnerability window" (e.g., the creature drops its AC by
  2 when using its signature attack).

### Error: "Resistance to non-magical weapons trivializes the encounter at low level"

- Parties below level 5 often lack magic weapons. The resistance
  effectively doubles HP and slows the fight to a halt.
- **Fix:** for CR ≤ 4 creatures, avoid resistance to non-magical
  weapons. Use specific damage type resistances instead (resistance
  to cold, lightning, etc.), or restrict resistance to a particular
  weapon material (silvered weapons, cold iron, adamantine).

### Error: "Legendary creature feels weaker than expected"

- Legendary actions are part of the creature's CR calculation. A CR
  17 dragon with no legendary actions is actually a CR 14–15 dragon.
- **Fix:** make sure legendary actions are real damage threats, not
  cosmetic moves. At minimum one legendary action option should be an
  Attack equivalent.

### Error: "Lair actions are forgotten in play"

- Lair actions trigger on initiative count 20, but GMs frequently
  skip them in the heat of combat.
- **Fix:** make at least one lair action *visible and atmospheric*
  even if it doesn't directly deal damage — players notice and
  remind the GM. Effects that change terrain or reveal information
  are particularly sticky.

---

## 9. Quick Design Checklist

Before declaring a stat block done:

- [ ] AC matches expected for CR (±1 acceptable)
- [ ] HP within range for CR (use midpoint)
- [ ] DPR (3-round average including recharge expectation) matches
      CR range
- [ ] Attack bonus matches CR
- [ ] Save DCs match CR
- [ ] Proficiency bonus matches CR
- [ ] Saving throws and skills include the creature's *signature*
      stats (Wisdom save for a focused mind; Stealth for a lurker)
- [ ] Resistances and immunities are intentional and balanced
- [ ] Multiattack pattern produces the target DPR without trivializing
      single PCs
- [ ] At least one signature trait or ability that makes the creature
      *feel like itself* in combat
- [ ] Reaction (if any) costs something or rewards the right tactic
- [ ] Legendary creature: 3 legendary action points; menu has at
      least one Attack equivalent
- [ ] Lair actions (if CR 5+): 3 thematic options, one offensive,
      one defensive, one environmental
