# Spell Effect Library

Recurring effect patterns: area shapes, saves vs attacks, damage,
conditions, buffs/debuffs, summons, utility, divination.

---

## Area-of-Effect Shapes

D&D 5e 2024 standardizes AoE shapes. Use these — don't invent new
shapes.

| Shape | Definition | Example spells |
|---|---|---|
| **Cube** | X-ft sides, anchored at chosen point | Thunderwave (15-ft cube) |
| **Sphere** | X-ft radius from chosen point | Fireball (20-ft sphere) |
| **Cone** | X-ft length, fanning from caster | Burning Hands (15-ft cone) |
| **Line** | X-ft length × 5-ft wide | Lightning Bolt (100-ft line) |
| **Cylinder** | X-ft radius × Y-ft height | Spike Growth (20-ft radius × 5-ft height area) |
| **Emanation** | X-ft radius from caster, moves with caster | Spirit Guardians |

**Shape choice by concept:**

- **Explosive / radial:** Sphere.
- **Breath-like / blast forward:** Cone.
- **Bolt-like / piercing line:** Line.
- **Localized chamber / room-sized:** Cube.
- **Pillar / falling / sky-down:** Cylinder.
- **Aura on caster:** Emanation.

**Shape sizes by spell level (rough guide):**

| Spell Level | Cube | Sphere | Cone | Line |
|---|---|---|---|---|
| 1st | 15 ft | 10 ft | 15 ft | 30 ft |
| 2nd | 20 ft | 15 ft | 20 ft | 40 ft |
| 3rd | 20 ft | 20 ft | 30 ft | 60 ft |
| 4th | 30 ft | 20 ft | 30 ft | 100 ft |
| 5th | 30 ft | 30 ft | 60 ft | 100 ft |
| 6th–8th | 40 ft | 40 ft | 60 ft | 150 ft |
| 9th | varies | 40 ft | 90 ft | 200 ft |

Larger shapes at lower spell levels skew toward overpower. Default
to the tabled sizes unless you have a balancing tradeoff.

---

## Save vs Attack Choice

A damage / harmful spell uses either a **saving throw** or a
**spell attack roll** — pick one per spell.

### Choose Saving Throw when:
- AoE (multiple targets — can't roll an attack for each).
- Effect is *avoidance-based* (the target dodges, resists, sees
  it coming).
- The spell imposes a condition (Hold Person → Wisdom save).
- Long-distance / unavoidable (line-of-sight ignored or sense-
  based).

### Choose Spell Attack when:
- Single target.
- Effect is *delivery-based* (the spell must hit — a magical
  bolt, ray, touch).
- The spell crits (attacks can crit; saves cannot).
- Touch-range spells (the caster must hit physically).

### Save type by effect:
- **Strength save:** physical force, push, knock prone.
- **Dexterity save:** projectile, AoE explosion, lightning, fire,
  acid splash.
- **Constitution save:** poison, disease, energy drain, fortitude.
- **Intelligence save:** psychic damage, mind invasion, illusion
  disbelief.
- **Wisdom save:** charm, fear, sleep, willpower, dominate.
- **Charisma save:** banishment, planar shifting, possession.

### Save outcome standard:

- **Half on save** (standard for AoE damage): full damage on
  fail, half on save.
- **Save end-of-turn** (standard for ongoing conditions): the
  target saves at the end of each of their turns to shake off
  the condition.
- **Save vs effect**: fail = effect applies, save = no effect.
- **Save with stages** (for save-or-die at 7th+): each fail
  advances a stage; final stage = severe.

---

## Damage Patterns

### Standard damage shapes by spell level

| Level | Pattern | Example |
|---|---|---|
| Cantrip | 1d8 / 1d10 attack; 1d6 AoE save-half | Fire Bolt, Sacred Flame |
| 1st | 3d6 single (Magic Missile-style); 3d6 AoE save-half | Burning Hands |
| 2nd | 4d6–4d8 single; 4d6 AoE | Scorching Ray, Shatter |
| 3rd | 8d6 AoE; 6d6 single | Fireball, Lightning Bolt |
| 4th | 6d10 single; 6d8 AoE | Wall of Fire, Ice Storm |
| 5th | 8d8 single; 9d6 AoE | Cone of Cold |
| 6th+ | varies; signature scaling | Disintegrate 10d6+40 |

### Multi-hit / Damage-distribution patterns

- **Single big roll:** 8d6 to all in area (Fireball).
- **Multiple smaller rays:** Each ray is a separate attack roll
  (Scorching Ray, Eldritch Blast).
- **Per-round damage:** X damage per round to creatures in area
  (Wall of Fire, Cloudkill).
- **Repeating damage:** Save each round in the area; damage on
  fail (Insect Plague).

### Damage Type Choice

- **Acid:** sticky, lingering, corrodes objects.
- **Cold:** slowing, freezing, brittleness.
- **Fire:** burning, ignites flammables.
- **Force:** raw arcane, ignores resistance.
- **Lightning:** bolts, chains, electricity.
- **Necrotic:** death-energy, withers.
- **Poison:** organic, slows / sickens.
- **Psychic:** mind, ignores physical resistance.
- **Radiant:** divine, anti-undead.
- **Thunder:** sonic, audible, knocks down.
- **Bludgeoning / Piercing / Slashing:** physical (rare for
  spells; usually for Force spells like Magic Stone or Eldritch
  blasts).

---

## Condition-Imposing Spells

The 2024 PHB conditions and their typical spell-imposing form:

| Condition | Mechanism | Save end-of-turn? | Typical spell level |
|---|---|---|---|
| Blinded | Save vs effect; ends after duration | Often yes | 2nd–4th |
| Charmed | Wis save (Enchantment); end on harm or duration | Often no (Charm Person 1h) | 1st–6th |
| Deafened | Save vs effect; duration | Sometimes | 1st–2nd |
| Frightened | Wis save (Enchantment); end on out-of-sight or save | Yes | 1st–4th |
| Grappled | Effect-based; Str/Dex save to escape | Strength check | 1st–3rd |
| Incapacitated | Often a stage of broader effect | Yes | 3rd–6th |
| Invisible | Self-buff or area; duration | No | 2nd–6th |
| Paralyzed | Wis or Con save (Hold Person, Hold Monster) | Yes | 2nd–5th |
| Petrified | Con save (Flesh to Stone); save with stages | Save with stages | 6th+ |
| Poisoned | Con save; effect duration | Sometimes | 1st–4th |
| Prone | Str save (Earth Tremor); end of effect | N/A (one-time) | 1st–3rd |
| Restrained | Str/Dex save (Web, Entangle); end of effect | Yes | 1st–4th |
| Stunned | Wis or Con save (Power Word Stun); end of duration | Yes | 5th–8th |
| Unconscious | Wis save (Sleep); end on damage or duration | Yes (or specific) | 1st–3rd |

**Designing condition spells:**
- Lower-level conditions are *short-duration* or *easily ended*
  (Charmed ends if charmer harms; Frightened ends if no line of
  sight).
- Higher-level conditions are *severe* or *resist-removable*
  (Petrified requires Greater Restoration to remove).

---

## Buff and Debuff Patterns

### Common buffs

| Buff | Pattern | Spell level |
|---|---|---|
| Temporary HP | X temp HP | Cantrip–3rd |
| AC bonus | +1 / +2 / +3 / +5 | 1st–4th |
| Attack bonus | +1d4 (Bless), Advantage, +X | 1st–3rd |
| Save bonus | +1d4, Advantage on specific saves | 1st–4th |
| Speed | +10 / +20 ft (Longstrider, Haste) | 1st–3rd |
| Resistance | One damage type, all damage types | 3rd–6th |
| Extra Action | Haste +1 action | 3rd |
| Spell-attack bonus | Bigby's Hand variants | 5th |
| Damage rider | +1d4 / +1d8 / +1d10 per attack | 1st–3rd |

### Common debuffs

| Debuff | Pattern | Spell level |
|---|---|---|
| Penalty to attack | -1d4 (Bane) | 1st |
| Disadvantage | On specific roll type | 1st–4th |
| Vulnerability | To specific damage type | 4th–6th |
| Reduced speed | Half / -10 ft (Slow) | 1st–3rd |
| Action restrictions | Slow (1 action, no reactions) | 3rd |
| Concentration-breaker | Forced save / round | 4th+ |
| Save penalty | -X to specific save | 2nd–5th |

---

## Summon Spells (2024 Design Pattern)

The 2024 PHB unified summon spells into a clear pattern. **Do not
use the legacy "pick from a list" pattern.**

### 2024 Summon spell template

```
Summon [Type]
Xth-level Conjuration

Casting Time: Action
Range: 90 feet
Components: V, S, M (a [theme]-themed material component worth Y gp)
Duration: Concentration, up to 1 hour
Classes: [...]

You call forth a [Type] Spirit. It appears in an unoccupied space
you can see within range. The spirit uses the [Type] Spirit stat
block (below). The stat block scales with the spell slot used.

***Using a Higher-Level Spell Slot.*** Use the spell slot's level
for [HP / damage / DC scaling].
```

**Stat block design:**
- HP scales with spell slot (e.g., 30 + 10 × slot level above
  base).
- Damage scales with spell slot.
- AC, attack bonus, save DC scale modestly.
- Special abilities are flavor-driven (a Beast Spirit has a Beast
  Form choice; a Fey Spirit has a Fey Manner choice).

**Anti-pattern:** Summon spell that lists multiple stat blocks
to choose from (Conjure Animals classic). 2024 unified to one
scaling stat block per spell.

---

## Utility Spell Patterns

### Movement utility
- **Misty Step** pattern: short-range teleport, Bonus Action,
  2nd level.
- **Dimension Door** pattern: longer teleport, Action, 4th level.
- **Teleport** pattern: hyper-range, Action, 7th level.
- **Plane Shift** pattern: planar travel, 7th level.
- **Fly:** Concentration; 60 ft fly speed; 3rd level.

### Information utility
- **Detect [X]:** Detection at 30 ft for 10 min; 1st level.
- **Locate [X]:** Find specific within 1 mile; 2nd level.
- **Comprehend Languages:** Read written, hear spoken; 1st level.
- **Scrying:** Remote viewing; 5th level.

### Creation utility
- **Create Food and Water:** Tier 1 baseline; 3rd level.
- **Mage's Magnificent Mansion:** Extra-dimensional shelter;
  7th level.
- **Wish:** Anything; 9th level.

### Communication utility
- **Sending:** 25-word message anywhere on same plane; 3rd level.
- **Telepathy:** Two-way for 24 hours; 8th level.

---

## Divination Patterns

### Yes/No
- **Augury:** 30-minute future, yes/no/woe/weal; 2nd level.
- **Divination:** Specific question, 1-week future; 4th level.

### Direct knowledge
- **Identify:** Properties of an item; 1st level.
- **Speak with Dead:** 5 questions of corpse; 3rd level.
- **Legend Lore:** Lore on a specific known person/place/object;
  5th level.

### Remote sensing
- **Clairvoyance:** Stationary remote view at 1 mile; 3rd level.
- **Arcane Eye:** Mobile invisible sensor; 4th level.
- **Scrying:** Remote view of a known creature; 5th level.

### Prediction
- **Foresight:** Personal precognition for 8 hours; 9th level.

---

## Battlefield-Shape Spells

Persistent area spells:

| Spell archetype | Effect | Spell level |
|---|---|---|
| Wall of [X] | Linear or curved barrier | 3rd–6th |
| Cloud of [X] | Persistent gas / area | 3rd–6th |
| Sphere of [X] | Persistent globe | 5th–7th |
| Pit / Hole | Floor disruption | 4th–6th |
| Field of [X] | Wide-area difficult terrain or effect | 3rd–5th |

**Design discipline:**
- Specify the dimensions.
- Specify what happens to a creature inside.
- Specify what happens when entering / leaving (often save).
- Specify whether the spell blocks line of sight, line of effect,
  or movement.
- Specify Concentration (almost always yes for ongoing area).
