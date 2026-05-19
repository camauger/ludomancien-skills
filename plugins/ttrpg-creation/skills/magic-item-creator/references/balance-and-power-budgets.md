# Balance and Power Budgets

How to allocate "design points" to a magic item to keep it within its
rarity tier. This file provides the structural discipline that prevents
power creep when designing custom items.

The system below is an *informal* framework. The 2024 DMG does not
publish an explicit point-budget system, but veteran designers
internalize equivalent intuitions. Use this as scaffolding while
developing that intuition.

---

## 1. The Power Budget Concept

Every magic item carries a **power budget** determined by its rarity.
Adding properties costs from this budget. Stacking too many properties
exceeds the budget, and the item should jump rarity.

The opposite is also true: an item with cheap properties below its
budget feels *underwhelming* for its rarity. Players will be
disappointed by a "Rare" item that just gives +1 to Stealth.

---

## 2. Budget by Rarity

Each rarity provides a budget in "design points." This is a heuristic
— not all properties cost the same, but it gives a useful first-pass
balance check.

| Rarity | Total budget | Typical use |
|---|---|---|
| Common | 1 point | One simple effect |
| Uncommon | 2–3 points | One major effect OR two minor |
| Rare | 4–5 points | One major + two minor, OR signature ability |
| Very Rare | 6–8 points | Signature ability + 2–3 supporting properties |
| Legendary | 10+ points | Identity-defining ability + multi-property suite |

### Property cost reference table

This table assigns approximate point costs to common property types.
Adjust to taste; use as starting reference.

| Property | Approximate cost |
|---|---|
| Cosmetic effect (changes color, emits light, no mechanical impact) | 0–1 |
| +1 to single skill (advantage on one specific check type) | 1 |
| +1 to attack and damage (weapon) | 2 |
| +2 to attack and damage | 4 |
| +3 to attack and damage | 6 |
| +1 to AC | 2 |
| +2 to AC | 4 |
| +3 to AC | 6 |
| +1 to one save type | 1 |
| +1 to all saves | 3 |
| Set ability score to 21 (Hill Giant) | 2 |
| Set ability score to 25 (Fire Giant) | 5 |
| Set ability score to 29 (Storm Giant) | 8 |
| One damage type rider (+1d6 of one type) | 2 |
| Bane property against one creature type (+2d6) | 3 |
| Damage resistance to one common type | 2 |
| Damage resistance to one rare type (force, radiant) | 3 |
| Damage immunity to one type | 4–5 |
| Charge-based spellcasting (3rd-level spell, 1/day) | 3 |
| Charge-based spellcasting (5th-level spell, 1/day) | 5 |
| Spell-storing (any spell up to 5th level) | 4 |
| At-will cantrip casting | 1 |
| At-will 1st-level spell | 2 |
| At-will 2nd-level spell | 4 |
| At-will 3rd-level spell | 6 |
| Flying speed (30 ft.) | 3 |
| Flying speed (60 ft.) | 5 |
| Truesight (60 ft.) | 4 |
| Truesight (120 ft.) | 6 |
| Darkvision (60 ft.) | 1 |
| Darkvision (120 ft.) | 2 |
| Reaction-based defensive (parry, deflect crit 1/day) | 2 |
| Signature ability (Recharge 5–6, identity-defining) | 4–6 |
| Mythic / phase-shift (HP-threshold-triggered) | 6+ |

### Budget composition examples

**Common item** (budget 1):
- A candle that doesn't go out (1 pt cosmetic + 1 pt minor utility = 2)

  → Slightly over; reduce to "a candle that doesn't go out unless
  immersed in water" (1 pt). Or accept as 2-pt Uncommon.

**Uncommon item** (budget 2–3):
- +1 longsword (2 pts) + minor flavor (changes color when wielded) (0 pts) = 2

  → Standard Uncommon weapon.

- Cloak of Elvenkind: advantage on Stealth (1 pt) + disadvantage on
  attempts to see you (1 pt) + attunement (free) = 2

  → Standard Uncommon Wondrous.

**Rare item** (budget 4–5):
- +2 mace (4 pts) + minor flavor = 4

  → Standard Rare weapon.

- Boots of Flying: 30 ft. fly speed (3 pts) + 4-hour daily limit (–1 pt
  for limit) = 2 — too cheap for Rare.

  → Bump effect: 50 ft. fly speed (4 pts) + 4-hour daily limit (–1) = 3,
  closer to Rare.

**Very Rare item** (budget 6–8):
- Mantle of the Storm: +1 AC (2 pts) + resistance to lightning (2 pts)
  + 5/day lightning bolt (5 pts) = 9

  → Slightly above Very Rare; consider trimming or bump to Legendary.
  Try: +1 AC + resistance to lightning + 3/day lightning bolt (5 → 4)
  = 8 → Very Rare.

**Legendary item** (budget 10+):
- Sword of Inevitability: +3 attack and damage (6 pts) + crit on 19–20
  (2 pts) + once per day, target a creature within 60 ft. that takes
  10d10 force damage on failed Wis save (6 pts) + signature ability
  recharge (–2 pt for recharge limit) = 12

  → Legendary territory.

---

## 3. Tiering by Character Level

A character's experience tier shapes what magic items they can
actually *use* effectively.

### Tier 1 (Levels 1–4)

- Common items are everywhere.
- Uncommon items appear at level 3–4.
- Rare items rare; Very Rare and Legendary essentially absent.
- **Don't give Tier 1 characters Very Rare items.** They can't use
  them yet, and the item dominates their identity.

### Tier 2 (Levels 5–10)

- Common refresh.
- Uncommon staple.
- Rare items appear regularly.
- One Very Rare by level 10 is a milestone reward.
- Legendary items are rare exceptions tied to milestone moments.

### Tier 3 (Levels 11–16)

- Uncommon and Rare flood in.
- Very Rare becomes regular.
- Legendary items appear, especially as quest goals.
- Single Common items lose significance.

### Tier 4 (Levels 17–20)

- Rare and Very Rare are common.
- Legendary items define identity.
- Some campaigns introduce Artifacts here.

### Implication for design

If designing a Rare item, ask: *which tier will encounter this?*

- Tier 2 character finding their first Rare → significant moment;
  design accordingly with care
- Tier 4 character finding a Rare → ordinary; can be more utilitarian

---

## 4. The "Three Magic Items at a Time" Constraint

Most characters can attune to **3 items maximum**. This is the hidden
constraint that shapes item design:

- Players will retire one attuned item to slot a new one in.
- Items that don't require attunement compete for slot rules (rings,
  cloaks) but don't compete for attunement.
- Powerful non-attunement items (Bag of Holding, Decanter of Endless
  Water, etc.) are *valuable* because they don't compete for
  attunement.

### Design implication

When evaluating an item's power:
- **Attunement-required:** the item must justify its slot. Compare
  against the *best* item the character could otherwise attune.
- **Non-attunement:** the item is "free" in attunement terms; it can
  be slightly weaker per-effect but still useful.

### Common pitfall

Designing 5+ Rare items that all require attunement floods the
player's attunement slots, forcing tough choices and feeling
punishing. Mix attunement and non-attunement items in any
campaign's treasure budget.

---

## 5. Property Synergies and Anti-Synergies

Some properties compound when combined; some negate each other.

### Synergies (combining these multiplies effective power)

- **Advantage on attack rolls + Bonus damage rider** — both apply on
  the same hit
- **Critical hit expansion + Critical hit damage bonus** — more
  crits, each crits harder
- **Flying speed + Ranged weapon bonus** — kite at will, untouchable
- **Resistance to one type + Vulnerability immunity on the same type**
  — effective immunity-like behavior
- **Bonus to one save + Lucky reroll on that save** — practical
  immunity to saved-against effects

### Anti-synergies (combining these wastes a property)

- **Two damage-type-rider properties on the same weapon** — only one
  applies per hit unless explicitly stacked
- **AC bonus + Mage Armor spell** — mage armor doesn't stack with
  worn armor
- **Multiple resistances to the same damage type** — resistance
  doesn't stack
- **Charge-based spellcasting + spell-storing** on the same item —
  unclear which mechanic governs each spell

When designing, check for accidental anti-synergies and remove or
clarify.

---

## 6. Comparing to Existing Official Items

Cross-checking your design against published items is the fastest
sanity check.

### For weapons

| Rarity | Reference Item | Why it matters |
|---|---|---|
| Uncommon | +1 Longsword | Establishes the baseline +1 cost |
| Rare | Sun Blade | +2 weapon + daylight emission + radiant damage rider |
| Very Rare | Hammer of Thunderbolts | +3 hammer + 3d10 thunder damage + giant-bane |
| Legendary | Vorpal Sword | +3 weapon + decapitates on natural 20 |

### For armor

| Rarity | Reference Item |
|---|---|
| Uncommon | +1 Studded Leather |
| Rare | +2 Half Plate |
| Very Rare | +3 Plate (or +2 Plate of Resistance) |
| Legendary | Plate Armor of Etherealness |

### For wondrous items

| Rarity | Reference Item |
|---|---|
| Common | Wand of Pranks (utility, no combat impact) |
| Uncommon | Cloak of Elvenkind (Stealth advantage) |
| Rare | Cloak of Displacement (attacks have disadvantage) |
| Very Rare | Cloak of the Bat (flight + animal form 1/day) |
| Legendary | Robe of the Archmagi (multiple identity-defining bonuses) |

If your custom design is comparable to or stronger than an item at
its target rarity, the rarity is right. If it's significantly
stronger, bump the rarity.

---

## 7. Pricing Adjustments

Gold price tracks rarity but also internal power.

### When to price at the upper end

- Item has all of: attunement requirement, multiple notable
  properties, a signature ability.
- Item is in high demand for the campaign (matches the most-popular
  class, fills a slot players want).
- Setting has low magic availability (multiplier ×2 to ×5).

### When to price at the lower end

- Item has only one effect.
- Item has restrictions (only works in certain conditions, only at
  certain times of day, only with specific commands).
- Setting has high magic availability (lower competition).

### Bundle discounting

If multiple items of similar rarity are sold together, expect a 10–
20% discount per item beyond the first.

---

## 8. The Identity Test

A well-designed magic item passes the "identity test": you can
describe the item in one sentence that captures its mechanical *and*
narrative essence, and that sentence couldn't apply to any other item
of the same rarity.

### Examples that pass

- "*A frost greatsword that grows hungry when you draw blood — the
  hungrier it gets, the colder its bite.*" (signature trait: hunger
  mechanic; clear identity)
- "*An amulet that lets you remember a single fact perfectly, but you
  must forget another to learn anything new.*" (mechanical trade-off;
  identity in cost)
- "*Boots that double your speed in moonlight, but lock to the ground
  at noon.*" (conditional power; identity through limitation)

### Examples that fail

- "A +1 sword." (no identity)
- "A ring that grants +1 to all saves." (mechanical but no identity)
- "A cloak with multiple useful properties." (identity is unclear)

When a design feels generic, ask: *what would a buyer at a magic-item
fair brag about owning this?* If they'd only brag about the bonus
number, the item lacks identity.

---

## 9. Power Budget Checklist

Before declaring a magic item designed:

- [ ] Total property points are within budget for target rarity
- [ ] No property exceeds its rarity tier individually (a +3 weapon
      property doesn't appear on an Uncommon item)
- [ ] Attunement requirement matches power level
- [ ] Property synergies are intentional, not accidental
- [ ] Property anti-synergies are absent
- [ ] Item compares reasonably to the closest official item at the
      target rarity
- [ ] Identity test: one sentence captures the item, distinct from
      others at the same rarity
- [ ] Pricing aligns with rarity table and setting magic density
- [ ] If multi-property: each property is *intentional*, not added to
      pad the description
- [ ] If charges: charge count and recharge match power patterns from
      `property-library.md` Section 3

---

## 10. Anti-Patterns to Avoid

These design patterns produce unbalanced or unsatisfying items.

### "Swiss Army Knife"

The item does 6 different unrelated things. No identity, no focus,
exceeds budget through breadth not depth.

**Fix:** pick 1–2 themes and elaborate. Cut unrelated properties.

### "Quietly Best in Slot"

The item is mechanically optimal but boring. No story, no flavor,
no narrative weight.

**Fix:** add origin lore, an unusual visual, an aesthetic
property, a quirk.

### "Numeric Tax"

The item provides a +1 to numbers in 5 different places. No
identity, dull to play.

**Fix:** consolidate to a single bigger bonus + one identity-defining
property.

### "Save-or-Suck Spammer"

The item enables save-or-suck spam (banish at will, charm at will).
Trivializes encounter design.

**Fix:** limit by charges, by daily uses, or by requiring specific
preconditions.

### "Inflated Description"

The item's flavor describes cosmic power, but the mechanics deliver
a +1 bonus. Buyer disappointment.

**Fix:** scale mechanics to match flavor, OR scale flavor to match
mechanics.

### "Pattern-Breaker"

The item violates an established 5e mechanical pattern (e.g., "this
sword gives you proficiency in all skills" — that's not a magic-item
pattern, that's a class feature).

**Fix:** rework using established 5e patterns or accept the deliberate
weirdness as a Legendary-or-Artifact identity choice.
