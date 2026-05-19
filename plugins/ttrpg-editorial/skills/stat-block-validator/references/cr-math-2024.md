# CR Math (D&D 5e 2024)

Offensive CR table (DPR → CR), defensive CR table (HP + AC → CR),
expected save DC by CR, expected attack bonus by CR, expected AC,
PB by CR, multiplier rules, worked examples.

CR is the **average** of offensive CR and defensive CR. Each is
derived independently from the stat block.

---

## Defensive CR Table

Determine effective HP and AC, then read the CR.

### Effective HP Calculation

```
Effective HP = HP × resistance/immunity multiplier
```

- **No resistances / immunities:** 1× HP.
- **Common resistance** (e.g., resistance to nonmagical
  bludgeoning/piercing/slashing): 1.5× HP.
- **Common immunity** (e.g., immunity to one common damage type
  like fire): 1.5× HP.
- **Multiple resistances/immunities:** Cap at 2× total unless
  the creature has extreme defenses (e.g., a stone golem with
  multiple immunities).

### Defensive CR Table

| Effective HP | Expected AC | Defensive CR |
|---|---|---|
| 1–6 | 13 | 0 |
| 7–35 | 13 | 1/8 |
| 36–49 | 13 | 1/4 |
| 50–70 | 13 | 1/2 |
| 71–85 | 13 | 1 |
| 86–100 | 13 | 2 |
| 101–115 | 13 | 3 |
| 116–130 | 14 | 4 |
| 131–145 | 15 | 5 |
| 146–160 | 15 | 6 |
| 161–175 | 15 | 7 |
| 176–190 | 16 | 8 |
| 191–205 | 16 | 9 |
| 206–220 | 17 | 10 |
| 221–235 | 17 | 11 |
| 236–250 | 18 | 12 |
| 251–265 | 18 | 13 |
| 266–280 | 18 | 14 |
| 281–295 | 18 | 15 |
| 296–310 | 18 | 16 |
| 311–325 | 19 | 17 |
| 326–340 | 19 | 18 |
| 341–355 | 19 | 19 |
| 356–400 | 19 | 20 |
| 401–445 | 19 | 21 |
| 446–490 | 19 | 22 |
| 491–535 | 19 | 23 |
| 536–580 | 19 | 24 |
| 581–625 | 19 | 25 |
| 626–670 | 19 | 26 |
| 671–715 | 19 | 27 |
| 716–760 | 19 | 28 |
| 761–805 | 19 | 29 |
| 806+ | 19 | 30 |

### AC Adjustment

If the AC of a stat block differs from the expected AC for its HP
range, adjust the defensive CR by 1 per 2 points of AC difference.

- **AC 2 higher than expected:** +1 to defensive CR.
- **AC 4 higher than expected:** +2 to defensive CR.
- **AC 2 lower than expected:** -1 to defensive CR.

---

## Offensive CR Table

Determine DPR (damage per round, averaged over 3 rounds), then
read the CR.

### DPR Calculation

```
DPR = average damage that the monster expects to deal per round,
       considering:
       - Multiattack (sum all attack damage)
       - Recharge probability (average expected use)
       - Save-half effects (assume target with average save:
         half damage in 50% of cases, full in 50%)
       - Attack hit rate (assume average to-hit vs expected AC)
```

For the recharge: a Recharge 5-6 ability has 33% probability per
round. Over 3 rounds, expect roughly 1 use of a 5-6 recharge in
the average fight (sometimes 0, sometimes 2). Conservative
estimate: 1 use over 3 rounds.

### Offensive CR Table

| DPR | Expected Attack Bonus / Save DC | Offensive CR |
|---|---|---|
| 0 | n/a | 0 |
| 1–3 | +3 / DC 13 | 1/8 |
| 4–5 | +3 / DC 13 | 1/4 |
| 6–8 | +3 / DC 13 | 1/2 |
| 9–14 | +3 / DC 13 | 1 |
| 15–20 | +3 / DC 13 | 2 |
| 21–26 | +4 / DC 13 | 3 |
| 27–32 | +5 / DC 14 | 4 |
| 33–38 | +6 / DC 15 | 5 |
| 39–44 | +6 / DC 15 | 6 |
| 45–50 | +6 / DC 15 | 7 |
| 51–56 | +7 / DC 16 | 8 |
| 57–62 | +7 / DC 16 | 9 |
| 63–68 | +7 / DC 16 | 10 |
| 69–74 | +8 / DC 17 | 11 |
| 75–80 | +8 / DC 17 | 12 |
| 81–86 | +8 / DC 18 | 13 |
| 87–92 | +9 / DC 18 | 14 |
| 93–98 | +9 / DC 18 | 15 |
| 99–104 | +10 / DC 18 | 16 |
| 105–110 | +10 / DC 19 | 17 |
| 111–116 | +10 / DC 19 | 18 |
| 117–122 | +11 / DC 19 | 19 |
| 123–140 | +11 / DC 19 | 20 |
| 141–158 | +12 / DC 20 | 21 |
| 159–176 | +12 / DC 20 | 22 |
| 177–194 | +13 / DC 21 | 23 |
| 195–212 | +13 / DC 21 | 24 |
| 213–230 | +14 / DC 21 | 25 |
| 231–248 | +14 / DC 22 | 26 |
| 249–266 | +15 / DC 22 | 27 |
| 267–284 | +15 / DC 22 | 28 |
| 285–302 | +16 / DC 23 | 29 |
| 303+ | +16 / DC 23 | 30 |

### Attack Bonus / Save DC Adjustment

If the attack bonus or save DC differs from expected for the DPR:

- **+2 above expected:** +1 to offensive CR.
- **+2 below expected:** -1 to offensive CR.
- Apply the same logic to save DC.

---

## Proficiency Bonus by CR

| CR | PB |
|---|---|
| 0–4 | +2 |
| 5–8 | +3 |
| 9–12 | +4 |
| 13–16 | +5 |
| 17–20 | +6 |
| 21–24 | +7 |
| 25–28 | +8 |
| 29+ | +9 |

A stat block's PB must match its stated CR.

---

## Final CR Calculation

```
Final CR = ceiling( (Offensive CR + Defensive CR) / 2 )
```

Standard CR values: 0, 1/8, 1/4, 1/2, 1, 2, 3, 4, ..., 30.

**Round to the nearest standard CR.** If offensive CR = 5 and
defensive CR = 4, average = 4.5 → round to 5 (closer to upper
end usually).

---

## CR Mismatch Detection

Compare stated CR with computed CR.

**Mismatch severity:**
- **Within 1 CR:** Minor; may be intentional (designed weak/strong
  for niche).
- **2 CR off:** Medium; flag for review.
- **3+ CR off:** Major; almost certainly an error.

**Common causes:**
- HP not scaled to CR (most common — HP too low for stated CR or
  vice versa).
- AC not scaled.
- Damage too low (multiattack count wrong, weapon die wrong).
- Saving throw / attack bonus mismatch with PB.
- Missing resistances / immunities for stated CR tier.

---

## Worked Examples

### Example 1: CR 1 Goblin Captain

Stat block summary:
- AC 15 (chain shirt)
- HP 38 (7d6 + 14)
- STR 12 (+1), DEX 16 (+3), CON 14 (+2), INT 12 (+1), WIS 12 (+1),
  CHA 12 (+1)
- Multiattack: 2 scimitar attacks
- Scimitar: +5 to hit (Dex +3, PB +2), 1d6+3 = 6.5 avg

**Offensive CR:**
- DPR = 2 × 6.5 = 13 → DPR 13 → CR 1 (target +3 attack)
- Attack bonus stated: +5. Expected for CR 1: +3.
  +2 above expected → +1 to CR → offensive CR = 2

**Defensive CR:**
- HP = 38. No multipliers.
- HP 38 → CR 1/4 to 1/2 range.
- AC = 15. Expected for HP 38 range: 13.
  +2 above expected → +1 to CR → defensive CR = 1

**Final CR:**
- (Offensive 2 + Defensive 1) / 2 = 1.5 → CR 1 or CR 2.

The Goblin Captain at CR 1 is borderline; possible refinement to
CR 2 if mechanics emphasize offense. Stated CR 1 is acceptable
within tolerance.

### Example 2: CR 5 Spellcaster

Stat block summary:
- AC 14 (no armor; Dex +2 + Bracers of Defense +2)
- HP 91 (14d8 + 28)
- INT 18 (+4), prof bonus +3
- Multiattack: 3 quarterstaff attacks @ 1d6+4 each, OR Cast a Spell
- Quarterstaff: +5 to hit (Str +1 + PB +3 + magic, etc.), 1d6+4
  avg 7.5
- Spellcasting: cast spells up to 3rd level, DC 16 spell save

**Offensive CR:**
- DPR (weapon mode) = 3 × 7.5 = 22.5
- Or DPR (Fireball cast at 3rd level: 8d6 = 28 avg; assume hits 4
  targets = 112... but 1/day, so distribute over the long fight)
- For 3-round avg: maybe one fireball + two weapon rounds.
  Round 1: Fireball 28 (assume 3 targets hit at half on save:
    28 × 2/4 + 28 × 1/4 = 21 avg)
  Round 2: 22.5 (multiattack)
  Round 3: 22.5
  Average DPR = (21 + 22.5 + 22.5) / 3 = 22.0
- DPR 22 → CR 3 (target +4 attack / DC 13)
- Save DC stated: 16. Expected for CR 3: DC 13. +3 above expected
  → +1.5 to CR → CR 4-5
- Attack bonus +5: expected for CR 3 = +4. +1 → ~+0.5 to CR.
- Offensive CR ≈ 5

**Defensive CR:**
- HP 91 → CR 1-2 range (101+ would be CR 3+).
- AC 14: expected for HP 91 range = 13. +1 above expected → ~+0.5
  to CR.
- Defensive CR ≈ 1-2

**Final CR:**
- (Offensive 5 + Defensive 1.5) / 2 = 3.25 → CR 3

Stated CR 5 with computed CR 3 = mismatch. This monster is
**underdefended for stated CR.** HP needs to be ~131-145 for CR
5 (or AC 15+).

---

## CR Math Quick Validation

For a CR X stat block, check that:

1. PB matches: CR 0-4 → PB +2; CR 5-8 → PB +3; etc.
2. HP is within the defensive CR range: see table.
3. AC is close to expected AC for HP range: ±1-2 acceptable.
4. DPR (averaged over 3 rounds, accounting for multiattack and
   recharge) is within ±20% of expected DPR for stated CR.
5. Attack bonus and save DC match expected values for stated CR.

If all match, CR is calibrated correctly.
