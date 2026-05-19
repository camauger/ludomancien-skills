# Common Stat Block Errors

Catalogue of recurring errors found in homebrew and conversion
stat blocks. Use this as the validator's pattern library.

For each error: how to detect, why it matters, how to correct.

---

## Arithmetic Errors

### Error A1: Ability Modifier Mismatch

The stated modifier doesn't equal `(score - 10) / 2`, rounded down.

**Examples:**
- STR 15 stated as +3 (should be +2).
- DEX 14 stated as +3 (should be +2).
- CON 17 stated as +2 (should be +3).

**Detection:** Check each ability score's modifier.

**Why it matters:** Cascades into attack bonus, save bonus,
skill bonus, AC (Dex contribution). Wrong modifier propagates
throughout the stat block.

**Correction:** Recompute correctly. Use formula `floor((score-10)/2)`.

### Error A2: Save Bonus Mismatch

A proficient save's bonus doesn't equal `ability mod + PB`.

**Examples:**
- Wis save stated as +4 with Wis mod +2 and PB +2 (should be
  +4, but actually 2+2=4, this is correct — example error
  would be +3 with same data).
- Con save stated as +6 with Con mod +3 and PB +2 (should be
  +5).

**Detection:** For each proficient save, compute `Ability mod +
PB` and compare.

**Why it matters:** Proficient saves are core to mechanical
identity (a high-Wisdom monster should be hard to charm).

**Correction:** Recompute correctly.

### Error A3: Skill Bonus Mismatch

A proficient skill's bonus doesn't equal `ability mod + PB`.

**Examples:**
- Stealth +5 with Dex mod +3 and PB +2 (should be +5, correct;
  example error: Stealth +6 with same data).
- Perception +4 with Wis mod +1 and PB +2 (should be +3).

**Detection:** For each proficient skill, compute `Ability mod +
PB` and compare. Expertise grants `+2 × PB`.

**Why it matters:** Direct impact on Stealth, Perception, and
other check-driven mechanics.

**Correction:** Recompute correctly.

### Error A4: Attack Bonus Mismatch

An attack's to-hit bonus doesn't equal `ability mod + PB + magic
bonus`.

**Examples:**
- Greatsword attack +4 with Str mod +3 and PB +2 (should be
  +5).
- Bow attack +3 with Dex mod +2 and PB +2 (should be +4).

**Detection:** For each attack, identify governing ability (Str
for melee default; Dex for ranged or Finesse; spellcasting
ability for spell attacks). Compute `mod + PB + magic` and compare.

**Why it matters:** Affects encounter difficulty calibration.

**Correction:** Recompute.

### Error A5: Damage Average Mismatch

The average damage shown doesn't equal `(die average) + ability
mod`.

**Examples:**
- 1d6+3 damage shown as 7 (should be 6.5 → 6).
- 2d8+2 damage shown as 9 (should be 11).

**Detection:** For each damage formula, compute `(die count ×
average per die) + modifier` and compare. Round down to nearest
integer.

**Average per die:**
- d4: 2.5
- d6: 3.5
- d8: 4.5
- d10: 5.5
- d12: 6.5

**Why it matters:** Quick-reference for GM; consistency with
formulae.

**Correction:** Recompute. Round down.

### Error A6: AC Computation Wrong

The AC doesn't match armor + Dex (capped) + bonuses.

**Examples:**
- AC 16 stated, with chain shirt (13) + Dex +2 cap = 15.
- AC 17 stated, with leather armor (11) + Dex +3 = 14.

**Detection:** Identify armor type from notation; apply Dex cap;
add shield (+2) if present; add magic / natural armor bonus.

**Armor base AC by type:**
- Leather: 11 + Dex (no cap)
- Studded leather: 12 + Dex (no cap)
- Hide: 12 + Dex (max +2)
- Chain shirt: 13 + Dex (max +2)
- Scale mail: 14 + Dex (max +2)
- Breastplate: 14 + Dex (max +2)
- Half plate: 15 + Dex (max +2)
- Ring mail: 14 (no Dex)
- Chain mail: 16 (no Dex)
- Splint: 17 (no Dex)
- Plate: 18 (no Dex)
- Natural armor: typically 12-22 base, depends on creature

**Why it matters:** AC drives defensive CR.

**Correction:** Recompute correctly.

### Error A7: HP Formula Wrong

HP doesn't equal `(HD × HD average) + (HD count × Con mod)`.

**Examples:**
- HP 30 (5d6+10): average = 5×3.5 + 10 = 17.5 + 10 = 27.5, round
  to 27. Stated 30 is too high.
- HP 13 (3d6): average = 3×3.5 = 10.5, round to 10. Stated 13
  is too high.

**Detection:** For each HD formula, compute average HP and
compare.

**Why it matters:** HP drives defensive CR.

**Correction:** Either:
- Update HP to match formula (preferred for consistency).
- Adjust formula to match HP (if HP is target value).

---

## CR Math Errors

### Error C1: CR / PB Mismatch

PB doesn't match the CR tier.

**Examples:**
- CR 5 monster with PB +2 (should be +3).
- CR 10 monster with +3 (should be +4).
- CR 17 monster with +5 (should be +6).

**Detection:** Look up expected PB by CR tier and compare.

**Why it matters:** PB cascades into save bonus, skill bonus,
attack bonus. Wrong PB invalidates downstream math.

**Correction:** Recompute everything with correct PB OR adjust CR
to match PB.

### Error C2: Offensive Math Doesn't Support CR

DPR (averaged over 3 rounds) is significantly under or over the
expected range for stated CR.

**Examples:**
- CR 5 monster doing 12 DPR (expected: 33-38 DPR; this is CR 2
  output).
- CR 3 monster doing 50 DPR (expected: 21-26; this is CR 7
  output).

**Detection:** Compute DPR considering multiattack + recharge +
save-half. Compare to expected.

**Why it matters:** Encounter difficulty calibration is wrong.

**Correction:** Either:
- Adjust DPR (multiattack count, weapon damage, recharge
  frequency) to match stated CR.
- Adjust stated CR to match the math.

### Error C3: Defensive Math Doesn't Support CR

HP (with multipliers) is significantly under or over expected for
stated CR.

**Examples:**
- CR 5 monster with HP 50 (expected 131-145; this is CR 1 HP).
- CR 3 monster with HP 200 (expected 101-115; this is CR 9 HP).

**Detection:** Look up expected HP range for stated CR. Compare.

**Why it matters:** Defensive CR mismatch.

**Correction:** Either adjust HP or stated CR.

### Error C4: AC Doesn't Support CR

AC is significantly different from expected for stated HP range.

**Examples:**
- CR 5 monster with AC 11 (expected 15).
- CR 2 monster with AC 20 (expected 13).

**Detection:** Look up expected AC for CR / HP range. Compare.

**Why it matters:** AC drives defensive CR; outside range
indicates miscalibration.

**Correction:** Adjust AC, or adjust stated CR.

---

## Action Economy Errors

### Error E1: Multiattack Count Inflation

Multiattack count exceeds expected for CR tier.

**Examples:**
- CR 1 monster with Multiattack 2 attacks (acceptable but high).
- CR 5 monster with Multiattack 3 attacks (acceptable).
- CR 3 monster with Multiattack 4 attacks (out of range — should
  be 2 at CR 3).

**Detection:** Compare multiattack count to expected range for
stated CR.

**Why it matters:** Each extra multiattack adds damage; an extra
attack is roughly +50% damage at same hit rate.

**Correction:** Reduce multiattack count or scale up other
elements.

### Error E2: Recharge Frequency Out of Standard

Recharge value outside the standard 5-6 or special "6" range.

**Examples:**
- Recharge 4-6 on a Tier 2+ creature (should be 5-6).
- Recharge 3-6 anywhere (essentially always-on; not a recharge).
- Recharge 5-7 (impossible roll outcome).
- Recharge 1-6 (always on).

**Detection:** Check recharge values against expected 5-6 baseline.

**Why it matters:** Frequency inflation; ability is used too
often.

**Correction:** Adjust to 5-6 or specify justification.

### Error E3: Legendary Actions on Sub-Boss

Legendary actions present on a creature CR < 10.

**Examples:**
- CR 5 villain with 3 legendary actions.
- CR 8 mini-boss with legendary actions.

**Detection:** Check if creature has legendary actions and CR < 10.

**Why it matters:** Legendary actions multiply action economy by
~3, inflating effective CR.

**Correction:** Either remove legendary actions OR scale stat
block up to CR 10+.

### Error E4: Missing Multiattack on High-CR Monster

CR 5+ creature with no Multiattack action.

**Examples:**
- CR 7 creature with only a single Greatsword Attack action.

**Detection:** Check if CR ≥ 5 and Multiattack is absent.

**Why it matters:** DPR will be far too low for CR; the creature
under-performs.

**Correction:** Add Multiattack with appropriate count.

### Error E5: Reaction Without Trigger

Reaction listed without an explicit trigger condition.

**Examples:**
- "***Parry.*** The creature can add to its AC." (When? Always?)

**Detection:** Look for Reactions section; verify each Reaction
has "When [event]:" clause.

**Why it matters:** Ambiguous; impossible to run at table.

**Correction:** Add trigger clause.

### Error E6: Bonus Action Strength Inflation

Bonus Action ability equivalent to an Action-strength ability.

**Examples:**
- "***Bone Spike (Bonus Action).*** The undead creates a spike
  doing 3d6 damage." (As a Bonus Action, this is Action-level
  damage.)

**Detection:** Compare Bonus Action effects to similar Actions.

**Why it matters:** Action economy abuse; creature gets double
output.

**Correction:** Reduce Bonus Action effect, OR move to Action.

---

## Vocabulary Errors

### Error V1: Lowercase Condition Names

Conditions written in lowercase.

**Examples:**
- "the target is paralyzed for 1 minute" (should be "Paralyzed").
- "advantage against frightened creatures" (should be
  "Frightened").

**Detection:** Search for lowercase usage of canonical conditions.

**Why it matters:** 2024 convention is to capitalize official
conditions; consistency.

**Correction:** Capitalize.

### Error V2: Lowercase Action Types

"bonus action", "reaction", "action" lowercased.

**Detection:** Search for lowercase versions of these terms.

**Why it matters:** 2024 standard is capitalized.

**Correction:** Capitalize.

### Error V3: Wisdom (Perception) Style

Old 2014 phrasing like "Wisdom (Perception) check" in 2024
context.

**Detection:** Search for "(Perception)", "(Stealth)", etc.

**Why it matters:** 2024 streamlined to just "Perception check".

**Correction:** Update to streamlined form.

### Error V4: Missing Damage Type

Damage formula without damage type specification.

**Examples:**
- "Hit: 5 (1d6+2) damage." (No damage type.)
- "Hit: 1d10+3." (No "damage" word; no type.)

**Detection:** Search for damage formulae and verify type follows.

**Why it matters:** Damage type matters for resistances /
immunities / vulnerabilities.

**Correction:** Add damage type. Default to weapon type if from
weapon attack.

### Error V5: Damage Type Lowercase

Damage type written in lowercase.

**Examples:**
- "5 (1d6+2) slashing damage" (should be "Slashing").
- "8 (2d6) fire damage" (should be "Fire").

**Detection:** Search for damage type words.

**Why it matters:** 2024 convention is capitalized.

**Correction:** Capitalize.

### Error V6: Non-Standard Recharge Format

Recharge format outside standard parenthetical form.

**Examples:**
- "Recharge 5-6" (no parens, OK informally; need parens in stat
  block).
- "Recharge 5/6" (slash instead of dash).
- "Recharge after a rest" (vague).
- "Once per long rest" (acceptable but verify format consistency
  with rest of stat block).

**Detection:** Look for "Recharge" usage.

**Why it matters:** Format consistency.

**Correction:** Standardize to canonical forms.

### Error V7: "Race" Instead of "Species"

In creature lore or description, "race" used to mean species.

**Detection:** Search for "race" in flavor text.

**Why it matters:** 2024 vocabulary update; not strictly stat
block but flagged for full publication consistency.

**Correction:** Replace with "species" or "ancestry" or similar.

### Error V8: Alignment Without Optional Qualifier

Alignment stated as fixed (e.g., "Chaotic Evil") in 2024 context
where optional/typical alignment is the norm.

**Detection:** Compare alignment to MM 2024 conventions.

**Why it matters:** 2024 explicitly relaxed alignment from
mandatory; using fixed alignment without "Typically" is a 2014
pattern.

**Correction:** Add "Typically" or use "Any alignment", per
2024 conventions.

---

## Format Errors

### Error F1: Missing Required Field

A required stat block field is missing.

**Examples:**
- No AC line.
- No HP line.
- No Senses line (or no Passive Perception).
- No Languages line.
- No CR line.

**Detection:** Verify presence of all required fields.

**Why it matters:** Stat block is incomplete; unusable.

**Correction:** Add the missing field with appropriate value.

### Error F2: Habitat / Treasure Missing (2024)

Habitat or Treasure field missing.

**Detection:** Verify Habitat and Treasure are present.

**Why it matters:** New 2024 standard fields; their absence is
incomplete-to-2024 format.

**Correction:** Add Habitat and Treasure.

### Error F3: Field Order Wrong

Fields out of canonical order.

**Examples:**
- Senses listed before Languages.
- Saves listed before AC.

**Detection:** Compare field order to canonical 2024 format.

**Why it matters:** Format consistency; readers expect order.

**Correction:** Reorder.

### Error F4: Inconsistent Italics on Trait Names

Some traits italicized, others not.

**Detection:** Compare all trait/action names; verify all are
italicized.

**Why it matters:** Format consistency.

**Correction:** Apply italics consistently.

### Error F5: Hit Points Formula Format

HP formula not in `XdY + Z` form, or formula doesn't show in
parentheses.

**Examples:**
- "HP 22" (missing formula).
- "HP 22 5d6+5" (formula without parens).
- "HP 22 (5xd6+5)" (typo).

**Detection:** Verify HP shows both average and formula in
parens.

**Why it matters:** Standard format.

**Correction:** Format correctly.

---

## Audit Priority Ranking

When reporting multiple errors, rank by impact:

| Priority | Error Types |
|---|---|
| **Critical** | C1 (PB mismatch), C2/C3/C4 (CR math significantly off by 2+), F1 (missing required field), F2 (missing 2024 Habitat/Treasure) |
| **High** | A4-A6 (wrong attack/AC/HP), E1 (multiattack inflation), E3 (legendary actions wrong tier), V4-V5 (damage type errors) |
| **Medium** | A1-A3 (mod/save/skill arithmetic), E2/E5/E6 (recharge/reaction/bonus action format), V1-V3 (vocabulary drift) |
| **Low** | F3-F5 (format consistency), V6-V8 (style polish) |
