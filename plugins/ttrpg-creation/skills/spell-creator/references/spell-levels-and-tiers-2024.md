# Spell Levels and Tiers (D&D 5e 2024)

Expected magnitude per spell level, slot economy, choosing the
right level, anti-patterns.

---

## Spell Slot Economy (PHB 2024 Full Caster)

A full caster (Wizard, Cleric, Druid, Sorcerer, Bard, Warlock with
caveats) gains slots at this approximate cadence:

| Char Level | 1st | 2nd | 3rd | 4th | 5th | 6th | 7th | 8th | 9th |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 2 | — | — | — | — | — | — | — | — |
| 3 | 4 | 2 | — | — | — | — | — | — | — |
| 5 | 4 | 3 | 2 | — | — | — | — | — | — |
| 7 | 4 | 3 | 3 | 1 | — | — | — | — | — |
| 9 | 4 | 3 | 3 | 3 | 1 | — | — | — | — |
| 11 | 4 | 3 | 3 | 3 | 2 | 1 | — | — | — |
| 13 | 4 | 3 | 3 | 3 | 2 | 1 | 1 | — | — |
| 15 | 4 | 3 | 3 | 3 | 2 | 1 | 1 | 1 | — |
| 17 | 4 | 3 | 3 | 3 | 2 | 1 | 1 | 1 | 1 |
| 19 | 4 | 3 | 3 | 3 | 3 | 2 | 1 | 1 | 1 |
| 20 | 4 | 3 | 3 | 3 | 3 | 2 | 2 | 1 | 1 |

Half-casters (Paladin, Ranger) start spellcasting at level 2 and
max at 5th level. Pact magic (Warlock) uses a different slot model
(few slots, all at max known level, short-rest recovery).

**Design implication:** A 9th-level spell can be cast **once** per
long rest by a level-17 character. A 1st-level spell can be cast
**4 times** plus every higher slot expended down. Power curves
must reflect this — a 9th-level spell is a one-shot signature; a
1st-level spell is a workhorse.

---

## Power-Level Benchmarks by Spell Level

These are the expected magnitudes a same-level spell competes
against in PHB 2024. Anchor your design to the column for the
spell's level.

### Damage Benchmarks (single-target attack / save AoE)

| Level | Single-target attack | AoE save-half |
|---|---|---|
| Cantrip (L1) | 1d8–1d10 | 1d6 (sm AoE) |
| 1st | 3d6–4d6 | 3d6 |
| 2nd | 3d8–4d8 | 4d6 |
| 3rd | 6d6–8d6 | 8d6 (Fireball) |
| 4th | 6d10 (single target) | 6d8 (AoE) |
| 5th | 8d8 | 9d6 (Cone of Cold) |
| 6th | 10d6+40 (Disintegrate) | 8d6 (multi-fire chain) |
| 7th | 7d8+30 (Finger of Death) | 10d6 (Plane Shift damage) |
| 8th | 12d6 (Sunburst-tier) | 12d6 (AoE) |
| 9th | 14d6+ (Meteor Swarm 40d6 total split 4 AoE) | Variable |

**Anti-pattern: under-leveled bloater.** A 2nd-level spell doing
6d6 damage is a 3rd-level spell mis-labeled. Re-level it.

**Anti-pattern: over-leveled trinket.** A 5th-level spell doing
4d6 damage and a minor utility is a 2nd-level spell mis-labeled.
Re-level or amplify the effect.

### Condition Benchmarks

| Level | Condition examples |
|---|---|
| 1st | Charmed (single-target, end-on-harm), Frightened (single-target), Hold Person prep |
| 2nd | Hold Person (single-target Paralyzed, save end-of-turn), Web area, Suggestion |
| 3rd | Hypnotic Pattern (mass Incapacitated, save end-on-harm), Slow (mass debuff) |
| 4th | Polymorph (single-target transform), Banishment (single-target removal) |
| 5th | Hold Monster (any creature Paralyzed), Modify Memory, Geas |
| 6th | Mass Suggestion, Eyebite (multi-condition) |
| 7th | Force Cage (no-save trap), Power Word Pain (save with stages) |
| 8th | Dominate Monster, Power Word Stun |
| 9th | Imprisonment (long-term), Power Word Kill |

### Utility Benchmarks

| Level | Utility scope |
|---|---|
| Cantrip | Trivial (Mage Hand, Light, Mending) |
| 1st | Short-range / 1-effect (Detect, Identify, Comprehend, Misty Step? no — that's 2nd) |
| 2nd | Short-distance teleport (Misty Step), illusions (Mirror Image), divination (Locate Object) |
| 3rd | Mid-range mobility (Fly), divination (Clairvoyance), wards (Magic Circle) |
| 4th | Greater divination, control (Banishment), shape (Wall of Fire) |
| 5th | Major utility (Teleportation Circle), divination (Scrying), revival (Raise Dead) |
| 6th | Reality manipulation (Move Earth), planar (Word of Recall), divination (True Seeing) |
| 7th | Long-distance teleport (Teleport), planar travel (Plane Shift), illusion (Mirage Arcane) |
| 8th | Greater shape (Antimagic Field), demiplane (Demiplane), enchanted barriers |
| 9th | Reality manipulation (Wish, Time Stop, True Polymorph) |

---

## Choosing the Right Level

Given a concept, ask:

1. **What's the comparable existing PHB 2024 spell?** If you can
   name 1–2 similar spells, use their level as anchor.
2. **What tier of party should access this?** Tier 1 → 1st–2nd
   level; Tier 2 → 3rd–4th; Tier 3 → 5th–6th; Tier 4 → 7th–9th.
3. **Is this a workhorse spell or a signature spell?** Workhorse =
   lower level (cast multiple times per day). Signature = higher
   level (cast 1–2 times).
4. **Does this spell solve a *whole problem* or contribute to a
   solution?** Whole-problem-solvers belong at 5th+. Contributors
   live at 1st–4th.

If unsure, **start one level higher than your gut says** and
playtest. It's easier to drop a spell's level after seeing it
break encounters than to raise it after seeing it ignored.

---

## Anti-Patterns by Level

### Cantrip Anti-Patterns
- **Cantrip with scaling = 1st-level effect.** Don't make a
  cantrip that, at level 5, hits as hard as a 1st-level spell
  cast from a slot. Cantrip scaling should reach Fire Bolt levels,
  not Magic Missile levels.
- **Cantrip with no scaling.** A cantrip should remain useful
  through Tier 4. Bake in *some* scaling or expansion.

### 1st–2nd Level Anti-Patterns
- **The "I-Win" 1st level.** A 1st-level Hypnotic Pattern is too
  much. Save the AoE Incapacitated effect for 3rd level.
- **The trap utility.** A 1st-level utility that *only* helps
  once in a campaign is wasted slot economy. Be sure utility
  spells are repeatable.

### 3rd–4th Level Anti-Patterns
- **Counterspell at 3rd: don't reinvent.** Counter-spell-like
  effects belong here (3rd) or higher. Don't put them at 2nd.
- **Polymorph at 3rd: don't reinvent.** Single-target form-change
  belongs at 4th+. Re-leveling existing PHB spells is fine; just
  don't *copy* the entry — design fresh.

### 5th–6th Level Anti-Patterns
- **The skipped tier.** A 5th-level spell that does 9d6 damage
  with no rider is *worse* than Fireball-upcast. Make 5th-level
  damage *do something else* — a condition rider, a battlefield
  shape, a delayed effect.

### 7th–9th Level Anti-Patterns
- **The non-signature 9th.** A 9th-level spell that just deals
  14d6 damage is a wasted slot. 9th-level spells must be
  *campaign-altering*, not just "more damage."
- **The save-or-die without save-with-stages.** At 7th+ levels,
  save-or-die is acceptable on creatures within a specific HP
  threshold (Power Word Kill: ≤100 HP). For everyone else, use
  save-with-stages.

---

## Spell-Level vs Class Resource Comparison

Some classes spend non-slot resources to mimic spell effects.
Calibrate spells so they're not strictly outclassed by:

- **Monk Ki / Focus features:** Generally 1st–3rd level magnitude.
- **Battle Master maneuvers:** 1st–2nd level rider effects.
- **Eldritch Invocations:** 1st–4th level magnitude (some at-will
  with daily limits).
- **Channel Divinity:** 2nd–5th level magnitude.

If your spell's effect is weaker than an equivalent-level
non-slot resource, the spell is wasted slot economy. Strengthen
the spell.

---

## Multi-Target Spell Calibration

For spells affecting multiple targets, calibrate by **expected
average target count.**

- **Tight AoE (10–15 ft sphere or 15-ft cone):** expects 1–2
  targets average → damage scales as if hitting 1.5 targets.
- **Standard AoE (20-ft cube, 20-ft sphere, 30-ft cone):**
  expects 3–4 targets → damage per target is reduced vs
  single-target.
- **Large AoE (40-ft cube, 40-ft sphere, 60-ft cone, 100-ft
  line):** expects 4–6 targets → damage per target reduced
  further; usually demands higher spell level.

Fireball (8d6 in 20-ft sphere) hits hard *per target* but expects
3+ targets — total damage potential is 24d6 against a tight
formation, which is why Fireball is a Tier-2-defining spell.
