# Balance and Anti-Patterns

Damage benchmarks, scaling math, condition cadence, Concentration
discipline, anti-patterns catalogue.

---

## Damage-by-Level Benchmarks

Anchor your damage to the spell level's standard PHB 2024
comparable. Deviating by more than ~20% requires a justifying
tradeoff (longer casting time, costly material, smaller area,
no scaling, etc.).

### Single-target damage (Attack roll)

| Level | Damage | Reference |
|---|---|---|
| Cantrip | 1d10 (scales to 4d10) | Fire Bolt |
| 1st | 4d6 piercing (Magic Missile = 3 × 1d4+1) | Magic Missile |
| 2nd | 4d6 (Scorching Ray pattern) | Scorching Ray (3 × 2d6) |
| 3rd | 6d6 in line | Lightning Bolt single targets in line |
| 4th | 6d10 to one target (Greater Invisibility is utility) | Phantasmal Killer |
| 5th | 8d8 single target | Destructive Wave-tier |
| 6th | 10d6+40 force damage | Disintegrate |
| 7th | 7d8+30 necrotic | Finger of Death |
| 8th | 12d6 | Sunburst single-target potential |
| 9th | varies — capstone-tier | Meteor Swarm |

### Area damage (Save half)

| Level | Damage | Reference |
|---|---|---|
| Cantrip | 1d6–1d8 small AoE | Acid Splash |
| 1st | 3d6 in 15-ft cube | Thunderwave |
| 2nd | 4d6 in 15-ft cube | Shatter |
| 3rd | 8d6 in 20-ft sphere | Fireball |
| 4th | 6d8 in 20-ft cylinder | Ice Storm |
| 5th | 8d8 in 60-ft cone | Cone of Cold |
| 6th | 8d6 chain | Chain Lightning |
| 7th | 10d6+ in 30-ft sphere | Delayed Blast Fireball |
| 8th | 12d6 radiant | Sunburst |
| 9th | 40d6 total split across 4 AoE | Meteor Swarm |

**Calibration formula (rough):**
- AoE = roughly 1.5× single-target damage at same level (because
  AoE hits multiple targets).
- Save-half halves damage on save (so expected damage = 0.75×
  full damage at typical save success rates).

---

## Scaling Math

### Cantrip Scaling (Character Level)

Cantrips gain a damage die or major effect upgrade at character
levels 5, 11, and 17.

**Linear damage cantrip:**
- Level 1: 1d8.
- Level 5: 2d8.
- Level 11: 3d8.
- Level 17: 4d8.

Pattern: doubles → triples → quadruples the initial dice count.

**Non-damage cantrip:**
- Level 1: base effect.
- Level 5: range +X, or duration +X, or one extra target.
- Level 11: another increment.
- Level 17: full-strength version.

### Leveled Spell Scaling (Higher Slot)

A spell cast from a slot above its base level gains:

**+1 die per slot above base** (most common):
- Magic Missile (1st): +1 missile per slot above 1st.
- Fireball (3rd): +1d6 per slot above 3rd.
- Cure Wounds (1st): +1d8 per slot above 1st.

**Larger area per slot:**
- Some spells expand size (e.g., a Wall variant: +10 ft length per
  slot above base).

**Longer duration per slot:**
- Some buffs gain +1 minute or +10 min per slot above base.

**More targets per slot:**
- Single-target spells: +1 creature per slot above base.

**Effect step-up:**
- Some spells *change* at higher slots (Spiritual Weapon: damage
  step up at 4th, 6th, 8th).

**Non-scaling spells:**
- Some 5th+ level spells don't scale (Hold Monster, Modify
  Memory, Wish). They're already powerful at base level.

---

## Condition Cadence

How often does the target get to throw off the condition?

### Save end-of-turn
The target re-saves at the **end of each of their turns**. On
success, the condition ends.

**Use for:** Most ongoing conditions of 2nd level and up (Hold
Person, Hold Monster, Charmed via Suggestion).

### Save end-of-source's-turn
The target re-saves at the **end of the source caster's turn**.

**Use for:** Rare; usually for spells with very specific timing
considerations.

### Save end-of-spell-duration
The condition runs until the spell's duration expires. No re-saves.

**Use for:** Powerful low-level spells with short durations
(Sleep — no save, just unconscious for 1 minute until damage or
shake).

### No-save permanent (until dispel/cure)
The condition is permanent until a specific cure or Greater
Restoration / Wish.

**Use for:** Severe high-level effects (Petrified, Imprisonment).

### Save with stages
Each failed save advances a stage; final stage is severe.

**Use for:** Powerful save-or-die effects (Power Word Pain,
Eyebite, Flesh to Stone).

**Anti-pattern: missing save cadence.** A spell that imposes a
condition must say *when* (or *whether*) the target gets to save
again. Forgotten cadence = unclear rules.

---

## Concentration Discipline

### Concentration Anti-Patterns

**1. Concentration leak**
A spell with ongoing impact but no Concentration. Example: A
1-minute summon that doesn't require Concentration would let
the caster stack it with Bless or Haste.
**Fix:** Add Concentration. Almost all ongoing impact = Concentration.

**2. Multi-Concentration spell**
A spell that requires Concentration for one effect AND has
*another* effect that ought to require Concentration. This
violates the one-spell-one-Concentration rule.
**Fix:** Pick one effect as the Concentration-anchor; make the
secondary effect Instantaneous or duration-tied.

**3. Concentration on Instantaneous**
A logic error: Instantaneous spells happen and end. There's
nothing to Concentrate on.
**Fix:** Either change duration to Concentration, up to X *or*
remove Concentration.

---

## Action Economy Anti-Patterns

### Bonus Action that's Action-strength
A Bonus Action spell with effect equal to an Action spell of
the same level.

Example: A 3rd-level Bonus Action spell dealing 6d6 damage. The
caster casts this + a cantrip + a weapon attack. That's three
"things" in one turn.

**Why bad:** Action economy is the limit on caster damage per
turn. Bonus Action high-impact is a balance breach.

**Fix:** Either:
- Reduce Bonus Action spell to ~1/2 the damage of an equivalent
  Action spell.
- Make the Bonus Action spell *Self*-targeted only (a buff to
  yourself).
- Move it to Action.

### Reaction that's not Reactive
A Reaction spell with a trigger that's "any time" or "as a free
reaction to nothing."

**Why bad:** Reactions are limited to one per round, and the
trigger should *react* to a specific event.

**Fix:** Always specify the trigger event (creature attacks me;
spell cast within range; ally damaged).

### Cantrip with leveled-spell impact
A cantrip whose at-level-1 effect is equivalent to a leveled
spell.

**Why bad:** Cantrips are at-will and unlimited; leveled spells
are slot-bound. A leveled-spell-cantrip lets a caster cast it
all day at zero cost.

**Fix:** Reduce cantrip impact to PHB 2024 cantrip benchmarks.

---

## Save-or-Die Anti-Patterns

### Save-or-die at low level
A 1st or 2nd level spell that deals death or near-death on a
failed save.

**Why bad:** Tier 1 PCs have low HP and might fail a single save
on bad luck. Save-or-die at this tier is unfair.

**Fix:** Use save with stages, or rename as a serious condition
(unconscious for X rounds) with damage on later saves.

### Save-or-die without HP cap
A high-level save-or-die that affects any creature regardless of
HP / hit dice.

**Why bad:** Power Word Kill *only* targets creatures with 100 HP
or fewer. This is intentional. A save-or-die without the cap is
broken at any level.

**Fix:** Add an HP cap (≤100, ≤200) or rename as save-with-stages.

### Save-or-die with no save
A spell that says "creature dies" with no save mentioned.

**Why bad:** No agency for the target. Cannot be balanced.

**Fix:** Add a save (Constitution at minimum for energy-based;
Wisdom for mental death).

---

## "Universal Anti-Everything" Anti-Pattern

A spell that solves *every* possible problem in its scope. Example:

> *"You speak the spell. Any chosen creature within 1 mile takes
> 6d6 damage of your chosen type, then must make a Wisdom save
> or be Charmed. The target's spellcasting is suppressed for 1
> minute."*

**Why bad:** Damage + condition + utility + counter-spell all in
one. There's no choice; this spell is always the right answer.

**Fix:** Pick *one* primary effect. Secondary effects must scale
to half the primary's impact.

---

## "Must-Have-or-Die" Anti-Pattern

A spell so powerful at its level that the entire party must have
access to a counter, or they lose.

Examples (in design space):
- A 3rd-level spell that auto-Banishes one creature for 1 hour
  with no save. Boss is removed; party wins.
- A 1st-level spell that grants Truesight at 120 ft for 1 hour.
  Renders entire genres of stealth and illusion useless.

**Why bad:** Forces other game elements (encounter design, NPC
design) to revolve around either having or countering this spell.

**Fix:** Add saves, reduce duration, raise spell level, or scope
the effect.

---

## "Ceiling-Buster" Anti-Pattern

A spell that breaks the standard encounter design assumptions of
its tier.

Examples:
- A 2nd-level spell that scouts 1 mile around the caster for 1
  hour. Renders Tier 1 hex-crawl meaningless.
- A 4th-level spell that creates a permanent 24-hour Wall of
  Force. Renders Tier 2 sieges trivial.

**Why bad:** Trivializes higher-tier challenges with lower-tier
slots.

**Fix:** Restrict scope, add Concentration, raise level, or
require costly material.

---

## "Subtle Spell Tax" Anti-Pattern

A spell that's only useful if you have Sorcerer Subtle Spell or
similar (no V components, no S components by design).

**Why bad:** Suboptimal for non-Sorcerer casters and forces
"feature tax."

**Fix:** Most spells should use V and S components. Subtle-via-
design should be rare and intentional.

---

## "Ritual Loophole" Anti-Pattern

A combat-relevant spell with the ritual tag.

Example: A 3rd-level Fireball-tier spell marked ritual. Caster
spends 10 minutes between fights and casts Fireball-equivalent
for free.

**Why bad:** Combat damage / control / battlefield-shape spells
should consume slots, *not* be ritual-eligible.

**Fix:** Remove ritual tag from combat spells. Ritual is for
non-combat utility, divination, and binding only.

---

## Pre-Publication Balance Audit

Before considering a spell complete, audit:

- [ ] Damage / impact within ±20% of same-level PHB 2024 benchmark.
- [ ] Save vs Attack matches effect (AoE → save; single-target →
      attack OR save based on flavor).
- [ ] Save type matches damage / effect (Dex for projectile, Wis
      for mental, etc.).
- [ ] Concentration applied if ongoing impact > 1 round.
- [ ] Casting time appropriate (Bonus Action spells aren't
      Action-strength).
- [ ] Components reasonable (costly M only if balance demands).
- [ ] Ritual tag only on non-combat spells.
- [ ] Scaling defined (cantrip or higher-slot).
- [ ] One primary effect; secondaries are ≤ 50% primary impact.
- [ ] Spell can't trivialize a tier's challenges.
- [ ] Spell has clear save cadence (end-of-turn, end-of-duration,
      save-with-stages).
- [ ] Spell has identity hook (not interchangeable with a same-
      level same-school neighbor).
