# Casting Time and Components (D&D 5e 2024)

Casting time options, Reaction triggers, component rules,
ritual rules, Concentration discipline.

---

## Casting Time

### Action (default for combat spells)

The most common casting time. The caster uses their Action.

**Use for:**
- Offensive damage spells.
- Battlefield-control spells with ongoing effect.
- Most leveled spells of 2nd–8th level.
- Heals during combat.

**Limitation:** A character with one Action cannot cast another
leveled spell with Bonus Action the same turn (the 2024 "one
leveled spell per turn" rule applies).

### Bonus Action

The caster uses their Bonus Action. Frees up the Action for a
weapon attack or other action.

**Use for:**
- Self-buffs (Shield of Faith, Spiritual Weapon).
- Quick movement (Misty Step).
- Quick utility (Healing Word — controversial, lets healers
  attack-and-heal in same turn).
- Conditional triggers.

**Discipline:** A Bonus Action leveled spell *prevents* casting
a leveled spell as your Action that turn (you can cast a cantrip,
make a weapon attack, etc.). This is the 2024 "one leveled spell
per turn" balancing constraint.

**Anti-pattern:** Action-level effect at Bonus Action cost.
A 5th-level damage spell at Bonus Action is broken. Bonus Action
spells should have *small* effects or be *single-target / self*.

### Reaction (with explicit trigger)

The caster uses their Reaction (one per round).

**Required syntax:** Always specify the trigger:
- *"You can cast this spell as a Reaction when you take damage
  from a creature within 60 feet."*
- *"You can cast this spell as a Reaction when you see a creature
  within 60 feet cast a spell."*
- *"You can cast this spell as a Reaction when an ally within 30
  feet is targeted by an attack."*

**Use for:**
- Defensive responses (Shield, Counterspell, Absorb Elements).
- Opportunistic attacks (Hellish Rebuke).
- Triggered teleports (rare).

**Discipline:** Reaction spells should resolve *within* the
triggering event's timing — e.g., Shield applies before damage is
rolled. Make the timing explicit.

### Longer Casting Times

For non-combat spells:

| Casting Time | Use Case |
|---|---|
| 1 minute | Rest-time setup (Goodberry, Aid, Find Familiar) |
| 10 minutes | Mid-rest utility, divinations (Augury) |
| 1 hour | Major rituals, divinations (Divination, Commune, Find the Path) |
| 8 hours | Major bindings (Magic Circle expanded, Glyph of Warding setup) |
| 24 hours | Reality-changing (Wish-related, True Resurrection at cost) |

**Long casting times mean the spell *cannot* be cast in combat.**
That's a balance lever — high-impact effects with long casting
times can be more powerful than their slot suggests, because they
can't react to fast-moving threats.

---

## Ritual Tag

A spell with the `(ritual)` tag can be cast in two ways:

1. **Normal casting:** Use a spell slot, casting time as listed.
2. **Ritual casting:** Add 10 minutes to the casting time, **don't
   use a spell slot.**

**Eligibility:**
- The spell must be on the caster's spellcasting class's list **as
  a Ritual spell** (most non-combat utility spells).
- The caster must know / have prepared the spell (varies by class
  — Wizards can ritual from spellbook without prep, others must
  have it prepared).

**Combat-relevant spells are NOT ritual-eligible.** Damage spells,
combat-control spells, and battlefield-shape spells should not get
the ritual tag.

**Good ritual candidates:**
- Divination (Detect Magic, Augury, Divination).
- Long-duration buffs out of combat (Comprehend Languages, Tongues
  during exploration).
- Setup spells (Magic Circle, Glyph of Warding).
- Communication (Speak with Dead, Sending).

**Bad ritual candidates:**
- Damage spells (Fireball).
- Combat-control (Hold Person).
- Combat-summons (Summon Beast).
- Self-buffs intended for combat (Haste).

---

## Components

D&D 5e 2024 retains three component types:

### Verbal (V)

The caster speaks the spell — chant, command word, incantation.

**Restrictions:**
- A Silenced creature cannot cast V spells.
- A creature that cannot speak (Gagged, mute, in a Silence area)
  cannot cast V spells.
- Loud, magical chant — V spells reveal the caster's presence and
  rough position.

**When to omit V:** Subtle Spell (Sorcerer Metamagic) removes V.
For spell design, *most* spells use V. Subtle utility spells (a
silent ward) might omit V for thematic reasons; this is a *minor
power-up*, so consider whether to leave V in.

### Somatic (S)

The caster makes a gesture — hand sign, weave-pattern, traced
sigil.

**Restrictions:**
- A creature with both hands occupied (carrying two items, hands
  tied) cannot cast S spells unless a free hand exists.
- A spellcasting focus can serve as the gesturing tool — holding
  a focus (wand, staff, holy symbol) lets you cast S spells.
- Heavy armor without proficiency causes spellcasting failure on
  S spells.

**When to omit S:** Subtle Spell removes S. Rarely omit S in
design unless the spell is purely mental.

### Material (M)

The caster needs a specific substance, focus, or component.

**Two sub-types:**

1. **Generic M (no listed cost):** Replaced by a spellcasting
   focus (orb, rod, staff, wand, holy symbol, druidic focus,
   arcane focus). The component is "in the spell" but not
   physically necessary if a focus is held.

2. **Specific M with cost (consumed or not):**
   - **Consumed components** (e.g., "a diamond worth at least 300
     gp, which the spell consumes"): the spell *requires* the
     material *and destroys it on casting*. Cannot be substituted.
   - **Non-consumed costly components** (e.g., "a sapphire worth
     at least 500 gp"): required at each casting but not destroyed.

**When to assign costly M:**
- The spell's power requires a balance throttle (Revivify: 300 gp
  consumed; Raise Dead: 500 gp consumed; True Resurrection: 25,000
  gp consumed).
- The spell is *replicable* but expensive (preventing daily use).
- The spell is *non-consumed costly* when you want to gate access
  to wealthy casters but not throttle frequency.

**Anti-pattern:** Cosmetic M with no cost on a high-power spell —
why is the cost there? Either make it cost or remove it.

---

## Concentration

**Concentration discipline is the primary spell-balance lever in
D&D 5e 2024.**

### Concentration Rules (PHB 2024 baseline)

- A character can only be concentrating on **one spell** at a time.
- Casting a new Concentration spell ends the prior concentration.
- Taking damage triggers a Concentration save (DC = 10 or half
  damage, whichever is higher).
- Being incapacitated, dying, or affected by certain conditions
  ends Concentration.
- Concentration can also be ended at will (no action required).

### When to Require Concentration

**Require Concentration if:**
- The spell has an ongoing effect that lasts more than 1 round.
- The spell controls the battlefield (Wall of Fire, Hold Person,
  Hypnotic Pattern).
- The spell buffs an ally for 1+ minute.
- The spell debuffs an enemy for 1+ minute.
- The spell summons a creature that fights for the caster.

**Don't require Concentration if:**
- The spell is Instantaneous (effect happens, no ongoing).
- The spell has a duration of 1 round only.
- The spell is a self-only minor buff (Shield is 1 round and
  Reaction-only, no Concentration needed).
- The spell creates a *delayed* but pre-determined effect (Delayed
  Blast Fireball: Concentration optional; Glyph of Warding: no
  Concentration after setup).

### Concentration Anti-Patterns

**Concentration leak:** A high-impact ongoing spell that doesn't
require Concentration. This lets the caster stack it with a second
Concentration spell. Always Concentration for ongoing impact.

**Concentration stack:** Two effects from the same spell, both
ongoing, requiring two Concentrations. Not allowed. One spell =
one Concentration.

**Concentration on Instantaneous:** A logic error. Instantaneous
spells happen and end; nothing to Concentrate on.

### Concentration Discipline by Spell Tier

| Spell Type | Concentration? |
|---|---|
| Instantaneous damage (Fireball, Magic Missile) | No |
| Single-round damage with rider | Usually no |
| 1-minute ongoing buff (Haste, Bless) | Yes |
| Long-duration buff (8h Aid) | Sometimes — case-by-case |
| Battlefield control (Wall of Fire, Hold Person) | Yes |
| Summon | Yes |
| Persistent area (Cloudkill) | Yes |
| Mental control (Charm Person duration) | Sometimes (Suggestion: yes; Charm Person 1h: no) |
| Divination (Scrying, Detect Magic) | Yes for active scrying; no for passive Detect |
| Defensive Reaction (Shield) | No (Instantaneous-equivalent) |

---

## Casting Time + Component Quick Reference

| Spell archetype | Casting Time | Components | Concentration? |
|---|---|---|---|
| Cantrip damage | Action | V, S | No |
| Cantrip utility (Mage Hand) | Action | V, S | Yes (sometimes) |
| Quick teleport (Misty Step) | Bonus Action | V | No |
| Single-target ranged blast | Action | V, S, M | No |
| AoE damage (Fireball) | Action | V, S, M (consumed: bat guano + sulfur) | No |
| Battlefield control | Action | V, S, M (sometimes) | Yes |
| Single-target buff | Bonus Action or Action | V, S | Yes |
| Mass buff (Bless, Aid) | Action | V, S, M | Yes |
| Counter (Shield, Counterspell) | Reaction | V, S | No |
| Divination | 1 action / 1 min / 10 min | V, S, M (sometimes costly) | Yes for active |
| Ritual | Normal + 10 min | V, S, M (no costly) | Varies |
| Major reality-bend | 1 minute / 1 hour | V, S, M (costly consumed) | Often |
| Wish-tier | 1 action | V (just "Wish" stated) | No |
