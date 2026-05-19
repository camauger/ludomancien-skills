# Magic Item Property Library

A library of recurring magic-item property patterns in D&D 5e 2024.
Use these as building blocks when designing custom items — most strong
items combine 1–3 patterns from this library.

---

## 1. Static Bonuses

The simplest properties: a flat number gets added to something.

### +X to Attack and Damage (Weapons)

```
You gain a +[1 / 2 / 3] bonus to attack rolls and damage rolls made
with this weapon.
```

Rarity by bonus:
- +1: Uncommon
- +2: Rare
- +3: Very Rare

### +X to AC (Armor / Shield)

```
You have a +[1 / 2 / 3] bonus to AC while wearing this [armor/shield].
```

Rarity by bonus:
- +1: Uncommon
- +2: Rare
- +3: Very Rare

### +X to Specific Save

```
You gain a +[1 / 2 / 3] bonus to [Charisma / Wisdom / specific] saving
throws while attuned to this item.
```

Rarity scales similarly to AC bonus but typically appears as one part
of a multi-property item.

### +X to Spell Attack / Save DC

```
You gain a +[1 / 2 / 3] bonus to spell attack rolls and a +[1 / 2 / 3]
bonus to the saving throw DCs of your spells.
```

Rarity:
- +1: Rare
- +2: Very Rare
- +3: Legendary

Powerful — affects every spell the caster uses. Reserve for casters'
identity items.

### Ability Score Setting

```
Your [Strength / Dexterity / Constitution / etc.] score is [21 / 23 /
25 / 27 / 29] while you wear/wield this item.
```

Rarity by score:
- 21: Rare (Giant Strength: Hill Giant)
- 23: Very Rare (Stone Giant, Frost Giant)
- 25: Very Rare (Fire Giant)
- 27: Legendary (Cloud Giant)
- 29: Legendary (Storm Giant)

The exact number matters less than the *category* (giant tiers).

---

## 2. Conditional Triggers

Properties that activate only under specific circumstances.

### Damage Type Bonus

```
Whenever you hit a creature with this weapon, the target takes an
extra [1d4 / 1d6 / 1d8] [damage type] damage.
```

Rarity:
- 1d4 of one type: Uncommon (added rider)
- 1d6 of one type: Rare
- 1d8 of one type: Very Rare

### Bane Property

```
This [weapon] deals an extra [2d6] damage when used against
[creature type or specific creature, e.g., dragons, fiends, undead,
giants].
```

Rarity:
- +2d6 bonus damage against one creature type: Rare
- +2d6 against multiple types or all evil-aligned: Very Rare

### Critical Hit Modification

```
When you score a critical hit with this weapon, the target takes an
additional [Xd6] damage.
```

OR

```
This weapon's critical hits ignore the target's resistance to
[damage type].
```

OR

```
This weapon scores a critical hit on a roll of 19 or 20.
```

Rarity:
- Critical hit damage rider (+2d6 to crits): Uncommon to Rare
- Crit-range expansion (19–20): Rare
- Crit ignores resistance: Rare to Very Rare

### Range Extension

```
When wielded, your spells with a range of [60+ feet] have their
range doubled.
```

Rarity:
- Doubled range for specific spell list: Rare
- Doubled range for all spells: Very Rare

### Conditional Advantage

```
You have advantage on attack rolls when attacking [specific creature
type] / [in specific conditions like dim light] / [while at less than
half HP].
```

Rarity:
- Conditional advantage on attacks against one type: Uncommon to Rare
- Conditional advantage in specific conditions: Rare

---

## 3. Charge-Based Properties

Items with charges expend them for effects. Standard format:

```
This item has [X] charges. While holding it, you can use an action
to expend [N] charges to cast [spell] (save DC [Y]).

The item regains [1d6 + N] charges daily at dawn. If you expend the
last charge, roll a d20. On a 1, the item crumbles into dust.
```

### Standard charge counts by rarity

| Rarity | Charges | Daily recharge |
|---|---|---|
| Uncommon | 3 | 1d3 |
| Rare | 5–7 | 1d4+1 |
| Very Rare | 7–10 | 1d4+2 to 1d6+4 |
| Legendary | 10–20 | 1d4+6 to 1d10+5 |

### Spell-as-charges scaling

| Spell level cast from charges | Charge cost |
|---|---|
| Cantrip | 0 (at-will) |
| 1st-level | 1 charge |
| 2nd-level | 2 charges |
| 3rd-level | 3 charges |
| 4th-level | 4 charges |
| 5th-level | 5 charges |

Some items invert this and let the user "choose the level" by
expending the matching charge count.

### Spell choice patterns

- **Single fixed spell:** "Cast *fireball* by expending 3 charges."
- **Limited list:** "Choose one: *fireball, lightning bolt, fly* —
  spend matching charges."
- **Variable list:** "Cast any 1st through 3rd level spell by
  expending matching charges, provided the spell is on the wizard
  spell list."

---

## 4. Daily / Per-Rest Uses

Properties that recharge on rest rather than via charges.

### Once Per Day (Daily Use)

```
Once per day, you can use an action to [effect].
```

OR

```
You can use this property once per day at dawn.
```

### Per Short Rest

```
You can use this property once per short rest.
```

### Per Long Rest

```
You can use this property once per long rest.
```

### Per-Rest vs Charges

- **Charges** suit items with multiple uses per day at varying
  costs.
- **Per-rest** suits items with a single high-impact effect that
  shouldn't be spammed.

---

## 5. Spell-Like Abilities

The item lets the user cast a specific spell or set of spells.

### At-Will (typical Cantrip or 1st-level)

```
While attuned to this item, you can cast [cantrip] at will, using
[ability score] as your spellcasting ability.
```

### Limited Daily Casts

```
You can cast [spell] using this item once per day at dawn.
```

Rarity scales with spell level:
- Cantrip at will: Common
- 1st level once per day: Uncommon
- 2nd level once per day: Uncommon-Rare
- 3rd level once per day: Rare
- 4th level once per day: Rare-Very Rare
- 5th level once per day: Very Rare
- 6th+ level once per day: Very Rare-Legendary

### Empowered Spell Casting

```
When you cast [specific spell] while attuned to this item, you can
choose to cast it as if upcast at [N+] level.
```

OR

```
Your [specific spell] deals 1 extra damage die when cast while attuned
to this item.
```

---

## 6. Resistance and Immunity

### Damage Resistance (one type)

```
While attuned to this item, you have resistance to [damage type].
```

Rarity:
- One common type (fire, cold, lightning): Uncommon
- One uncommon type (force, radiant, psychic): Rare
- One rare type (necrotic with specific use, etc.): Rare

### Multiple Damage Resistances

```
You have resistance to [damage type 1] and [damage type 2] damage
while attuned to this item.
```

Rarity:
- Two types: Rare
- Three types: Very Rare
- Four+ types or "all damage from a source" (Mantle of Spell Resistance):
  Very Rare to Legendary

### Damage Immunity

Much rarer. Reserved for Very Rare and Legendary items.

```
You have immunity to [damage type] damage while attuned to this item.
```

### Condition Immunity / Resistance

```
You can't be [condition: charmed / frightened / paralyzed / etc.]
while attuned to this item.
```

Rarity:
- Resistance / advantage on saves vs one condition: Uncommon
- Immunity to one common condition: Rare
- Immunity to multiple conditions: Very Rare

---

## 7. Sense Grants

### Darkvision

```
You have darkvision out to a range of [60 / 120] feet while attuned
to this item.
```

Rarity:
- 60 feet: Common-Uncommon
- 120 feet: Uncommon

### Blindsight / Tremorsense / Truesight

```
You have [blindsight / tremorsense / truesight] out to a range of
[X] feet while attuned to this item.
```

Rarity:
- Blindsight 30 ft.: Rare
- Truesight 60 ft.: Very Rare
- Truesight 120 ft.: Legendary
- Tremorsense 30 ft.: Rare

### Detect Spells

```
You can cast [detect magic / detect evil and good / detect thoughts]
at will while attuned to this item.
```

Rarity:
- Detect magic at will: Uncommon
- Detect thoughts at will: Rare
- True seeing at will: Legendary

---

## 8. Movement Grants

### Speed Increase

```
Your walking speed increases by [10 / 15 / 20] feet while attuned
to this item.
```

Rarity:
- +10 ft.: Uncommon (Boots of Speed style without the doubling)
- +15 ft.: Rare
- +20 ft.: Very Rare

### Fly Speed

```
You gain a flying speed of [30 / 60] feet while attuned to this item.
```

Rarity:
- 30 ft.: Rare (Cloak of the Bat, Winged Boots-style with charge limit)
- 60 ft.: Very Rare to Legendary

Flying speed without limitations is very powerful — usually have
duration limits or charge requirements.

### Swim / Climb / Burrow Speed

```
You gain a [swimming / climbing / burrowing] speed of [30 / 40] feet
while attuned to this item.
```

Rarity:
- Climb 30 ft.: Uncommon
- Swim 40 ft.: Uncommon-Rare
- Burrow 30 ft.: Rare

### Teleportation

```
As an action, you can teleport up to [30 / 60] feet to a location you
can see, [Y] times per day.
```

Rarity:
- Short teleport once per day: Rare
- Multiple teleports per day: Very Rare
- Long-range teleport (planar): Legendary

---

## 9. Action Economy Options

### Bonus Action Use

```
As a bonus action, you can [effect]. Once you use this property, you
can't use it again until [next dawn / X charges expended].
```

Strong because bonus actions are usually free of normal action costs.

### Reaction Use

```
As a reaction when [trigger], you can [effect].
```

Reaction-based properties are powerful because they trigger
opportunistically.

### Free Action (No Action Required)

```
You can [effect] at any time without using an action.
```

Reserved for passive abilities or very-low-cost activations
(e.g., light a flame, change item color).

---

## 10. Defensive / Passive Bonuses

### Damage Reduction

```
Reduce damage you take by [N] from one source per turn.
```

Niche but powerful at any rarity. The Cap matters:
- Reduce 1 per turn: Common (cosmetic)
- Reduce 3 per turn: Uncommon
- Reduce 5 per turn: Rare
- Reduce 10 per turn: Very Rare

### Lucky Reroll

```
Once per day, you can reroll a saving throw and take the better roll.
```

OR

```
You have advantage on saving throws against [type] effects.
```

Strong defensive bonus.

### Temporary HP Source

```
When you start a combat, you gain [N] temporary HP.
```

OR

```
Once per day, you can use an action to gain [Nd6+N] temporary HP.
```

### Critical Hit Resistance

```
Critical hits against you become normal hits.
```

OR

```
You have advantage on the saving throw to avoid being knocked
unconscious from massive damage.
```

Very Rare to Legendary properties.

---

## 11. Communication / Metaphysical

### Telepathy

```
While attuned to this item, you can communicate telepathically with any
creature within [30 / 60 / 120] feet of you that you can see and that
has a language.
```

Rarity:
- 30 ft.: Uncommon
- 60 ft.: Rare
- 120 ft.: Very Rare

### Tongues

```
While attuned, you can speak, read, and understand [specific languages
/ any language].
```

### Speak with Plants / Animals / Dead

```
You can cast [speak with plants / speak with animals / speak with dead]
at will.
```

Rarity:
- Speak with animals at will: Uncommon-Rare
- Speak with plants at will: Rare
- Speak with dead at will: Very Rare

### Planar Awareness

```
While attuned, you know your exact location relative to [specific
plane / planar landmark / artifact location].
```

Unique narrative property. Rarity depends on what's tracked.

---

## 12. Stacked Property Patterns

How to combine properties into a coherent item.

### Pattern: Combat Anchor + Utility Flavor

Best for: weapons, armor.

- One static combat bonus (+1 to +3)
- One small utility property (advantage on a specific skill, minor
  sense)
- One small flavor effect (changes color, emits sound, attracts
  certain creatures)

### Pattern: Spell Library + Charges

Best for: staves, wands, rods.

- One spellcasting property granting charges
- A specific spell list of 3–5 spells castable from charges
- One minor passive property (item glows, can be used as quarterstaff,
  detects magic)

### Pattern: Signature Ability + Supporting Properties

Best for: Very Rare and Legendary items.

- One identity-defining signature ability (Recharge-based or per-day)
- 2–3 supporting properties that flesh out the item's character
- Often a "set bonus" if part of a paired or matched item

### Pattern: Identity Toggle

Best for: items with multi-form mechanics (Rod of Lordly Might-style).

- The item has 3+ "modes" the user can switch between
- Each mode provides different mechanical effects
- Switching is a bonus action or reaction

### Anti-Pattern: Stacked Bonuses

Avoid: +1 to all attacks + +1 to all damage + +1 AC + advantage on
saves + spell list + charges + signature ability. That's a Legendary
item described as Uncommon. Pick a focus and let it carry the item.
