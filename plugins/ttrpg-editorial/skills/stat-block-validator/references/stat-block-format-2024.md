# Stat Block Format (D&D 5e 2024)

Canonical MM 2024 stat block layout, field order, vocabulary,
syntax conventions. Plus French Manuel des Monstres mapping.

---

## Field Order (Required)

A 2024 stat block reads top-to-bottom in this order:

```
[Name]
[Size + Type + (Tag) + Alignment]

AC [value] ([armor type if applicable])
HP [value] ([HD formula])
Speed [value], [other speeds if any]

[Ability score block — 6-column with score + modifier]

[Saves — if proficient saves exist]
[Skills — if proficient skills exist]
[Damage Resistances / Immunities / Vulnerabilities — if any]
[Condition Immunities — if any]
[Senses — always includes Passive Perception]
[Languages — always; "—" if none]
CR [value] (XP [value]; PB +[value])
PB +[value]

[Habitat — biome list, comma-separated]
[Treasure — tier label]

[Traits — italicized name. period. body text.]

ACTIONS
[Actions — italicized name. period. body text.]

[BONUS ACTIONS — header if any bonus actions exist]
[Bonus action entries]

[REACTIONS — header if any reactions exist]
[Reaction entries]

LEGENDARY ACTIONS — [if creature has legendary actions]
[Legendary actions header text]
[Sub-action 1]
[Sub-action 2]
[Sub-action 3]

LAIR ACTIONS — [if creature has lair actions]
[Lair actions header text]
[Sub-actions]

REGIONAL EFFECTS — [if creature has regional effects]
[Regional effects header text]
[Effect entries]

MYTHIC ACTIONS — [Tier 4 only, if applicable]
[Header text + trigger condition]
[Sub-actions]
```

---

## Field Syntax

### Name

The creature's name. Plural form not used in the stat block —
even if "Goblins" appear in a group, the stat block is "Goblin".

### Size + Type + Tag + Alignment

Format: `[Size] [Type] ([Tag]), [Alignment]`

| Size | Examples |
|---|---|
| Tiny | Faerie dragon |
| Small | Goblin, Kobold |
| Medium | Orc, Human |
| Large | Ogre, Horse |
| Huge | Stone giant, Adult dragon |
| Gargantuan | Ancient dragon, Tarrasque |

| Type | Examples |
|---|---|
| Aberration | Mind flayer |
| Beast | Wolf, Dire wolf |
| Celestial | Solar |
| Construct | Animated armor, Golem |
| Dragon | Adult red dragon |
| Elemental | Fire elemental |
| Fey | Pixie, Dryad |
| Fiend | Demon (Type, often with tag), Devil |
| Giant | Hill giant, Stone giant |
| Humanoid | Goblin (Tag: Goblinoid), Orc (Tag: Orc) |
| Monstrosity | Owlbear, Bulette |
| Ooze | Black pudding |
| Plant | Treant, Awakened shrub |
| Undead | Skeleton, Vampire |

| Tag | Used for |
|---|---|
| (Goblinoid) | Goblins, hobgoblins, bugbears |
| (Orc) | Orcs |
| (Elf) | Elf-tagged creatures |
| (Demon) | Demons within Fiend type |
| (Devil) | Devils within Fiend type |
| (Lawful) / (Chaotic) | Sometimes used for Outsider alignment |
| (Shapechanger) | Werewolves, mimic, etc. |
| (Titan) | Tarrasque, Empyrean |

Alignment is now **optional** in 2024 ("Typically [alignment]"
or "Any alignment" or "Unaligned"). When stated, use the
9-alignment grid:

- Lawful Good, Neutral Good, Chaotic Good
- Lawful Neutral, Neutral, Chaotic Neutral (or "True Neutral")
- Lawful Evil, Neutral Evil, Chaotic Evil
- Unaligned (for non-sentient beasts)
- Any alignment
- Typically [alignment] (suggested baseline)

### AC

Format: `AC [value] ([armor source if applicable])`

| Example | Notes |
|---|---|
| AC 12 | No armor source listed; comes from natural/Dex |
| AC 14 (leather armor) | Light armor source |
| AC 17 (chain mail, shield) | Multiple sources |
| AC 18 (natural armor) | Natural armor monster |
| AC 16 (Shield) | Magical/dexterous shield |

### HP

Format: `HP [average] ([HD formula])`

The average is shown; the HD formula is in parentheses.

Examples:
- `HP 7 (2d6)` — 2 hit dice of d6, with average 7 (= 2 × 3.5)
- `HP 22 (5d8)` — 5 hit dice of d8, average 22.5 → 22
- `HP 38 (7d6 + 14)` — 7d6 + Con mod × HD = 14
- `HP 144 (16d10 + 56)` — 16d10 + Con +7 (avg 16 × 5.5 + 56 = 144)

### Speed

Format: `Speed [walking ft.], [other speeds if any]`

Examples:
- `Speed 30 ft.`
- `Speed 25 ft., Fly 50 ft.`
- `Speed 30 ft., Swim 40 ft.`
- `Speed 30 ft., Climb 30 ft.`
- `Speed 30 ft., Burrow 20 ft.`

### Ability Score Block

Six columns:

```
| STR    | DEX    | CON    | INT    | WIS    | CHA    |
| 16 +3  | 14 +2  | 12 +1  | 10 +0  | 12 +1  | 8 -1   |
```

Or inline:
```
STR 16 (+3) DEX 14 (+2) CON 12 (+1) INT 10 (+0) WIS 12 (+1) CHA 8 (-1)
```

Modifier is in parentheses next to score, OR shown as a tighter
grid. The 2024 MM uses both formats.

### Saving Throws

Format: `Saves [Ability] [bonus], [Ability] [bonus]`

Examples:
- `Saves Wis +5, Dex +4`
- `Saves Con +6, Int +6, Wis +6`

Only proficient saves are listed. Non-proficient ability mods are
calculated as ability mod alone if needed elsewhere.

### Skills

Format: `Skills [Skill] +[bonus], [Skill] +[bonus]`

Examples:
- `Skills Perception +5, Stealth +6`
- `Skills Athletics +5, Survival +5`

### Resistances / Immunities / Vulnerabilities

Three separate lines if any apply:

- `Resistances [damage types]`
- `Immunities [damage types]`
- `Vulnerabilities [damage types]`

Damage types: Acid, Bludgeoning, Cold, Fire, Force, Lightning,
Necrotic, Piercing, Poison, Psychic, Radiant, Slashing, Thunder.

Examples:
- `Resistances Bludgeoning, Piercing, Slashing from Nonmagical Attacks`
- `Immunities Fire, Poison`
- `Vulnerabilities Cold`

### Condition Immunities

Format: `Condition Immunities [list]`

Examples:
- `Condition Immunities Charmed, Frightened, Poisoned`
- `Condition Immunities Exhaustion`

### Senses

Format: `Senses [sense list], Passive Perception [value]`

Senses: Blindsight, Darkvision, Tremorsense, Truesight (each
followed by range).

Examples:
- `Senses Darkvision 60 ft., Passive Perception 9`
- `Senses Blindsight 30 ft. (blind beyond this radius), Passive Perception 13`
- `Senses Truesight 120 ft., Passive Perception 18`

### Languages

Format: `Languages [list]`

Examples:
- `Languages Common, Goblin`
- `Languages —` (if no languages spoken)
- `Languages Infernal, Telepathy 60 ft.`

### Challenge Rating

Format: `CR [value] (XP [value]; PB +[value])`

Examples:
- `CR 1/4 (XP 50; PB +2)`
- `CR 1 (XP 200; PB +2)`
- `CR 5 (XP 1,800; PB +3)`
- `CR 20 (XP 25,000; PB +6)`

CR values: 0, 1/8, 1/4, 1/2, 1, 2, 3, ... 30.

### Habitat (2024 NEW)

Format: `Habitat [biome list]`

Standard biomes:
- Arctic, Coastal, Desert, Forest, Grassland, Hill, Mountain,
  Swamp, Tundra, Underdark, Underwater, Urban
- Planar (with sub-plane): Plane of Air, Plane of Earth, Plane of
  Fire, Plane of Water, Astral, Ethereal, Feywild, Shadowfell,
  Plane of Faerie, Plane of Avernus, etc.

Examples:
- `Habitat Forest, Mountain, Grassland`
- `Habitat Underdark`
- `Habitat Astral, Plane of Fire`

### Treasure (2024 NEW)

Format: `Treasure [tier]`

Standard tiers:
- None
- Individual (single creature treasure)
- Hoard (lair treasure for boss creatures)

Examples:
- `Treasure None`
- `Treasure Individual`
- `Treasure Hoard`

---

## Traits (Italicized Name, Bold Pattern)

```
***[Trait Name].*** [Trait description as a paragraph.]
```

Examples:

```
***Nimble Escape.*** The goblin can take the Disengage or Hide
action as a Bonus Action on each of its turns.

***Pack Tactics.*** The creature has Advantage on an attack roll
against a creature if at least one of the creature's allies is
within 5 feet of the target and the ally has the Incapacitated
condition or is otherwise not Surprised.
```

---

## Actions

Header: `ACTIONS` (all caps, no bold).

Action entries:
```
***[Action Name].*** [Action description.]
```

**Attack format example:**
```
***Scimitar.*** Melee Weapon Attack: +4 to hit, reach 5 ft., one
target. Hit: 5 (1d6+2) Slashing damage.
```

Components of an attack action:
- Action name (italicized).
- Attack type: "Melee Weapon Attack" / "Ranged Weapon Attack" /
  "Spell Attack" / etc.
- To-hit bonus.
- Reach or range (and target description).
- "Hit:" prefix to damage.
- Average damage with formula in parentheses.
- Damage type.

**Multiattack format:**
```
***Multiattack.*** The orc makes two attacks: one with its
greataxe and one with its javelin.
```

Or:
```
***Multiattack.*** The wizard makes three attacks with its staff.
```

**Spellcasting (innate spellcasting) format:**
```
***Spellcasting.*** The wizard casts one of the following spells,
using Intelligence as the spellcasting ability (spell save DC 14,
+6 to hit with spell attacks):

At will: detect magic, light, mage hand
3/day: misty step, scorching ray
1/day: animate objects, lightning bolt
```

Or in the more recent unified 2024 syntax:
```
***Spellcasting.*** The creature casts the following spells, using
Intelligence as the spellcasting ability (spell save DC 14):

At will: prestidigitation, fire bolt, mage hand
1/day each: invisibility, hold person
1/week each: fly, scorching ray
```

---

## Bonus Actions, Reactions

### Bonus Actions

Header: `BONUS ACTIONS` (if any exist).

```
BONUS ACTIONS

***Cunning Action.*** The rogue takes the Dash, Disengage, or Hide
action as a Bonus Action on each of its turns.
```

### Reactions

Header: `REACTIONS` (if any exist).

```
REACTIONS

***Parry.*** When a creature the spy can see hits the spy with a
melee attack, the spy adds 2 to its AC for that attack only,
potentially causing the attack to miss.
```

---

## Legendary Actions

```
LEGENDARY ACTIONS

The dragon can take 3 legendary actions, choosing from the options
below. Only one legendary action option can be used at a time and
only at the end of another creature's turn. The dragon regains
spent legendary actions at the start of its turn.

***Detect.*** The dragon makes a Perception check.

***Tail Attack.*** The dragon makes one tail attack.

***Wing Attack (Costs 2 Actions).*** The dragon beats its wings.
Each creature within 10 feet of the dragon must succeed on a DC 19
Dexterity saving throw or take 14 (2d6 + 7) Bludgeoning damage
and be knocked prone. The dragon can then fly up to half its
flying speed.
```

Legendary actions:
- Specify the action budget (typically 3).
- Indicate cost per action (1 unless otherwise specified;
  expensive actions specify cost in parentheses).
- Used at the end of another creature's turn.
- Regained at the start of the legendary creature's turn.

---

## Lair Actions

```
LAIR ACTIONS

On initiative count 20 (losing initiative ties), the dragon takes
a lair action to cause one of the following effects; the dragon
can't use the same effect two rounds in a row:

- Magma erupts from a point in the lair within 120 feet of the
  dragon. Each creature within 20 feet of that point must succeed
  on a DC 15 Dexterity saving throw or take 7 (2d6) Fire damage.

- A tremor shakes the lair within 60 feet of the dragon. Each
  creature on the ground within that area must succeed on a DC 15
  Dexterity saving throw or be knocked prone.

- Volcanic gases form a sphere of poisonous gas with a 20-foot
  radius centered on a point the dragon chooses within the lair.
  The sphere spreads around corners and the area is lightly
  obscured. Each creature in the gas at the start of its turn
  must succeed on a DC 13 Constitution saving throw or be
  poisoned for 1 minute.
```

Lair actions:
- Trigger on initiative count 20 (lose ties).
- Affect the environment, not the boss directly.
- Are typically environmental effects keyed to the boss's
  identity.

---

## Regional Effects

```
REGIONAL EFFECTS

The region containing a legendary red dragon's lair is warped by
the dragon's magic, which creates one or more of the following
effects:

- Small earthquakes are common within 6 miles of the dragon's
  lair.

- Volcanic openings appear within 1 mile of the dragon's lair,
  many of these spitting magma or filling caves with poisonous
  gas.

- The dragon can choose for water to be hot at all times within
  1 mile of its lair.

If the dragon dies, these effects fade over the course of 1d10
days.
```

Regional effects:
- Narrative-level environmental changes.
- Visible *outside* the lair.
- Apply continuously while the boss is alive.
- Fade after the boss dies.

---

## Mythic Actions (Tier 4 only)

```
MYTHIC ACTIONS

If the dragon's [Mythic Action] feature is available, it can use
the options below as legendary actions for 1 hour after using
[trigger feature]. It regains spent mythic actions at the start
of each of its turns.

***[Mythic Action 1].*** [Description.]
***[Mythic Action 2].*** [Description.]
***[Mythic Action 3 (Costs 2 Actions)].*** [Description.]
```

Mythic actions trigger when the boss reaches a specific condition
(usually 50% HP). They replace legendary actions for the duration.

---

## French Vocabulary (Manuel des Monstres FR)

| English | French |
|---|---|
| Name | Nom |
| Size | Taille |
| Type | Type |
| Alignment | Alignement |
| Armor Class | Classe d'armure |
| Hit Points | Points de vie |
| Speed | Vitesse |
| STR DEX CON INT WIS CHA | FOR DEX CON INT SAG CHA |
| Saving Throws | Jets de sauvegarde |
| Skills | Compétences |
| Damage Resistances | Résistances aux dégâts |
| Damage Immunities | Immunités aux dégâts |
| Vulnerabilities | Vulnérabilités |
| Condition Immunities | Immunités aux états |
| Senses | Sens |
| Languages | Langues |
| Challenge | Facteur de puissance |
| Proficiency Bonus | Bonus de maîtrise |
| Habitat | Habitat |
| Treasure | Trésor |
| Actions | Actions |
| Bonus Actions | Actions bonus |
| Reactions | Réactions |
| Legendary Actions | Actions légendaires |
| Lair Actions | Actions de repaire |
| Regional Effects | Effets régionaux |
| Mythic Actions | Actions mythiques |
| Damage | Dégâts |
| Melee Weapon Attack | Attaque d'arme au corps à corps |
| Ranged Weapon Attack | Attaque d'arme à distance |
| Spell Attack | Attaque magique |

Conditions in FR:

| English | French |
|---|---|
| Blinded | Aveuglé |
| Charmed | Charmé |
| Deafened | Assourdi |
| Frightened | Terrorisé / Effrayé |
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
| Exhaustion | Épuisement |
