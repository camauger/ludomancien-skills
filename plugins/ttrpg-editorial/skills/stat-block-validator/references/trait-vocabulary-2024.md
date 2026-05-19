# Trait Vocabulary (D&D 5e 2024)

Canonical 2024 vocabulary: condition names, action types,
recharge syntax, save syntax, damage syntax, targeting syntax,
sense format, French vocabulary, conditions reference.

A stat block's prose should match official MM 2024 conventions.
This document defines the canonical phrasing.

---

## Conditions (Official 2024 List)

These are the official conditions. Use these exact terms — no
synonyms, no invented conditions.

| Condition | Capitalization | Notes |
|---|---|---|
| **Blinded** | Always capitalized | "the creature is Blinded" |
| **Charmed** | Always capitalized | "the target is Charmed by the [creature]" |
| **Deafened** | Always capitalized | |
| **Frightened** | Always capitalized | (Was "Frightened" in 2014 too; 2024 unchanged) |
| **Grappled** | Always capitalized | |
| **Incapacitated** | Always capitalized | |
| **Invisible** | Always capitalized | (Visibility rules updated in 2024) |
| **Paralyzed** | Always capitalized | |
| **Petrified** | Always capitalized | |
| **Poisoned** | Always capitalized | |
| **Prone** | Always capitalized | |
| **Restrained** | Always capitalized | |
| **Stunned** | Always capitalized | |
| **Unconscious** | Always capitalized | |
| **Exhaustion 1-6** | Capitalized; specify level | "Exhaustion 1", "Exhaustion 6" |

**Anti-pattern:** Lowercase ("the creature is paralyzed"), or
non-official ("the creature is fascinated", "the target is
shaken").

### Condition Interactions

Multiple conditions can apply simultaneously. List them as:
"Charmed and Stunned", "Frightened, Poisoned, and Prone".

### Condition Removal

State the removal condition explicitly:
- "until the end of its next turn"
- "until the [creature] is destroyed"
- "as long as the [creature] is concentrating on this effect"
- "until the target succeeds on a DC X Wisdom saving throw at
  the end of each of its turns"

---

## Action Types (Capitalization)

| Term | Capitalization |
|---|---|
| Action | "the creature takes the Attack Action" |
| Bonus Action | "as a Bonus Action on each of its turns" |
| Reaction | "When a creature... the [X] can use its Reaction to..." |
| Free Action / Free | Lowercase generally; not a standard 5e concept |
| Movement | Lowercase; specific actions use capitals |

**Anti-pattern:** Lowercase ("bonus action", "reaction"). 2024
explicitly capitalizes these.

---

## Recharge Syntax

### Standard Format

```
(Recharge 5–6)
```

Parentheses, en-dash (not hyphen). Use Unicode en-dash (–) where
typography supports it; hyphen (-) acceptable when typography is
limited.

### Variants

```
(Recharge 6)              — 17% per round
(Recharge 4–6)            — 50% per round (rare, mostly Tier 1)
(Recharge after a Long Rest) — once per day
(Recharge after a Short Rest) — between short rests
(Recharges after [trigger]) — conditional
(1/Day)                    — once per day
(3/Day)                    — three times per day
```

**Anti-pattern:** "Recharge 5/6" (slash instead of dash), "Recharge
5 to 6" (verbose), "Recharge after rest" (unspecific).

---

## Saving Throw Syntax

### Standard Format

```
DC [X] [Ability] saving throw
```

Or in alternative form:

```
[Ability] saving throw (DC [X])
```

Examples:
```
The target must succeed on a DC 14 Wisdom saving throw or be
charmed for 1 minute.

Each creature in the area makes a DC 16 Constitution saving throw,
taking 8d6 Fire damage on a failed save, or half as much damage
on a successful one.
```

### Save Outcome Patterns

- **Save vs effect:** "or be [Condition]" / "or take [X] damage"
- **Half on save:** "taking X damage on a failed save, or half
  as much damage on a successful one"
- **Save end-of-turn:** "at the end of each of its turns,
  succeeding on a DC X saving throw to end the effect"
- **Save with stages:** "save again at end of next turn; if
  failed twice, [worse effect]"

**Anti-pattern:** "DC 14 save" (missing ability), "Wisdom saving
throw at DC 14" (verbose).

---

## Damage Syntax

### Standard Format

```
[average] ([die roll]) [damage type] damage
```

Examples:
```
5 (1d6+2) Slashing damage
14 (2d6+7) Bludgeoning damage
28 (8d6) Fire damage
1d10+3 Necrotic damage
```

The average is the rounded-down value of `(die roll average) +
modifier`. Always show both average and dice formula.

### Damage Type Capitalization

Damage types are **capitalized** in 2024:

| English | French |
|---|---|
| Acid | Acide |
| Bludgeoning | Contondant |
| Cold | Froid |
| Fire | Feu |
| Force | Force |
| Lightning | Foudre |
| Necrotic | Nécrotique |
| Piercing | Perforant |
| Poison | Poison |
| Psychic | Psychique |
| Radiant | Radiant |
| Slashing | Tranchant |
| Thunder | Tonnerre |

**Anti-pattern:** Lowercase damage types ("piercing", "fire"),
missing damage type, "damage" without specification.

---

## Attack Syntax

### Melee Weapon Attack

```
[Weapon Name]. Melee Weapon Attack: +X to hit, reach 5 ft., one
target. Hit: [average] ([die roll]) [damage type] damage.
```

### Ranged Weapon Attack

```
[Weapon Name]. Ranged Weapon Attack: +X to hit, range 80/320 ft.,
one target. Hit: [average] ([die roll]) [damage type] damage.
```

### Spell Attack

```
[Spell Name]. Spell Attack: +X to hit, range 60 ft., one target.
Hit: [average] ([die roll]) [damage type] damage.
```

### Targeting Conventions

- "one target you can see within range"
- "each creature within X feet"
- "all targets within a 30-foot cone"
- "one creature within reach"
- "two targets within 5 feet of the creature"

---

## Targeting Vocabulary

| Term | Use |
|---|---|
| "one target" | Single creature, attacked or chosen |
| "one target you can see" | Restrict to visible targets |
| "each creature within X ft" | AoE; affects all |
| "any creature of your choice within X ft" | AoE with selection |
| "the nearest creature within X ft" | Range-limited |
| "a creature you can see within range" | Spell-friendly |

---

## Sense Format

```
Senses [sense list], Passive Perception [value]
```

Senses:
- **Blindsight X ft.** — perceives without sight within X ft.
- **Darkvision X ft.** — sees in dim light as if bright; in
  darkness as if dim.
- **Tremorsense X ft.** — feels vibrations through the ground.
- **Truesight X ft.** — sees through magical darkness, invisibility,
  illusions; perceives shapechangers' true forms.

Examples:
```
Senses Darkvision 60 ft., Passive Perception 11
Senses Blindsight 30 ft. (blind beyond this radius), Passive Perception 13
Senses Truesight 120 ft., Passive Perception 18
Senses Darkvision 60 ft., Tremorsense 30 ft., Passive Perception 13
```

---

## Spellcasting Vocabulary

### Innate / Spell-like Abilities

```
***Spellcasting.*** The [creature] casts the following spells, using
[Ability] as the spellcasting ability (spell save DC [X]):

At will: [spell 1], [spell 2]
3/day each: [spell 3], [spell 4]
1/day each: [spell 5], [spell 6]
1/long rest each: [spell 7]
```

### Spell Slot Casting

```
***Spellcasting.*** The [creature] is a Xth-level spellcaster. Its
spellcasting ability is [Ability] (spell save DC X, +X to hit with
spell attacks). The [creature] has the following spells prepared:

Cantrips (at will): [list]
1st level (X slots): [list]
2nd level (X slots): [list]
...
```

---

## Anti-Patterns to Flag

### Vocabulary Drift from 2014 to 2024

| 2014 (old) | 2024 (correct) | Reason |
|---|---|---|
| race | species | 2024 vocabulary update |
| Lawful Good (mandatory) | Typically Lawful Good (optional) | 2024 alignment is suggestive |
| Wisdom (Perception) check | Perception check | 2024 streamlined |
| bonus action (lowercase) | Bonus Action | 2024 capitalization |
| "advantage on Wisdom (Perception) checks" | "advantage on Perception checks" | Streamlined |
| "Speed 30 ft" | "Speed 30 ft." (with period) | Format standard |
| Damage type lowercase | Damage type Capitalized | 2024 standard |

### Vocabulary Drift from Free-Form to MM-Standard

| Casual prose | MM standard | Reason |
|---|---|---|
| "the creature is paralyzed" | "the creature is Paralyzed" | Capitalize conditions |
| "the orc bites for 8 damage" | "8 (2d6+1) Piercing damage" | Standard damage syntax |
| "rolls a save vs poison" | "succeeds on a DC X Constitution saving throw" | Standard save syntax |
| "uses its trick once a battle" | "(Recharge 5–6)" or "(1/Day)" | Standard recharge |
| "10-feet flat AC bonus" | "+2 AC" then describe trigger | Mechanical clarity |

### Format Inconsistencies

| Inconsistency | Fix |
|---|---|
| Inconsistent capitalization across actions | Pick one convention; apply throughout |
| Italic / bold mixing in trait names | Action names italicized; conditions capitalized |
| Mixed en-dash and hyphen in recharge | Use en-dash (–) consistently |
| Mixed singular / plural in targets | "one target" (singular) unless AoE |

---

## French Vocabulary (Manuel des Monstres FR)

### Action and condition vocabulary in French

| English | French |
|---|---|
| Action | Action |
| Bonus Action | Action bonus |
| Reaction | Réaction |
| Action légendaire | Action légendaire |
| Recharge | Recharge |
| Recharge after a Long Rest | Recharge après un Repos long |
| Saving Throw | Jet de sauvegarde |
| Damage | Dégâts |
| Damage Resistance | Résistance aux dégâts |
| Damage Immunity | Immunité aux dégâts |
| Condition | État |
| Senses | Sens |

### Conditions in French (alphabetical)

| English | French |
|---|---|
| Blinded | Aveuglé |
| Charmed | Charmé |
| Deafened | Assourdi |
| Exhaustion | Épuisement |
| Frightened | Terrorisé (or Effrayé) |
| Grappled | Empoigné |
| Incapacitated | Neutralisé |
| Invisible | Invisible |
| Paralyzed | Paralysé |
| Petrified | Pétrifié |
| Poisoned | Empoisonné |
| Prone | À terre |
| Restrained | Entravé |
| Stunned | Étourdi |
| Unconscious | Inconscient |

### Damage type vocabulary in French (in stat block)

| English | French |
|---|---|
| Acid damage | Dégâts d'acide |
| Bludgeoning damage | Dégâts contondants |
| Cold damage | Dégâts de froid |
| Fire damage | Dégâts de feu |
| Force damage | Dégâts de force |
| Lightning damage | Dégâts de foudre |
| Necrotic damage | Dégâts nécrotiques |
| Piercing damage | Dégâts perforants |
| Poison damage | Dégâts de poison |
| Psychic damage | Dégâts psychiques |
| Radiant damage | Dégâts radiants |
| Slashing damage | Dégâts tranchants |
| Thunder damage | Dégâts de tonnerre |

### Attack syntax in French

```
[Nom de l'arme]. Attaque d'arme au corps à corps : +X au toucher,
allonge 1,5 m, une cible. Touché : Y (Zd6+W) dégâts tranchants.
```

(Allonge = reach; au toucher = to hit; touché = hit)
