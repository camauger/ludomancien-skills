# Action Economy Audit (D&D 5e 2024)

Action economy budgets per CR tier: multiattack, recharge, reactions,
bonus actions, legendary actions, lair actions, regional effects,
mythic actions. Common patterns and anti-patterns.

A creature's action economy is **the rate at which it does
mechanical things per round.** Wrong action economy makes a
correctly-statted creature feel wrong at the table.

---

## Action Economy Budget per CR Tier

### Tier 1 (CR 0–4)

**Standard budget:** 1 attack per Multiattack (sometimes 2 at CR
3+), 0 recharge abilities, 0-1 Reactions, 0 Bonus Actions, 0
legendary actions.

| Element | Standard | Notes |
|---|---|---|
| Multiattack | 1 attack at CR 0-1; 2 at CR 2-4 | Single high-damage strike often replaces multiattack |
| Recharge | None typical | Maybe one at CR 4 |
| Reactions | 0-1 | Standard creatures have at most one |
| Bonus Actions | None typical | Maybe one specific (Goblin Nimble Escape) |
| Legendary Actions | None | |
| Lair Actions | None | |

### Tier 2 (CR 5–10)

**Standard budget:** 2 attacks per Multiattack, sometimes 3 at CR
9-10; 0-1 recharge abilities; 1-2 Reactions; often a Bonus Action
option; no legendary actions.

| Element | Standard | Notes |
|---|---|---|
| Multiattack | 2 attacks typical, 3 at CR 9-10 | Some monsters use single big-strike |
| Recharge | 0-1 | Standard Recharge 5-6 |
| Reactions | 1-2 | Most have 1 |
| Bonus Actions | 0-1 | Common for spellcasters and dexterous monsters |
| Legendary Actions | Rare, sometimes for CR 9-10 boss types | |
| Lair Actions | Rare | |

### Tier 3 (CR 11–16)

**Standard budget:** 2-3 attacks per Multiattack; 1 recharge
ability; 1-2 Reactions; often a Bonus Action; some have legendary
actions starting CR 13+.

| Element | Standard | Notes |
|---|---|---|
| Multiattack | 2-3 attacks | Or one signature ability + a strike |
| Recharge | 1 | Standard recharge |
| Reactions | 1-2 | |
| Bonus Actions | 0-1 | More common |
| Legendary Actions | Often at CR 13+, sometimes earlier | 3 actions per round; boss types |
| Lair Actions | At CR 13+ if boss-tier | |
| Regional Effects | At CR 13+ if boss-tier | |

### Tier 4 (CR 17+)

**Standard budget:** 3-4 attacks per Multiattack OR 2 attacks +
signature ability; 1-2 recharge abilities; 2-3 Reactions; multiple
Bonus Action options; legendary actions standard.

| Element | Standard | Notes |
|---|---|---|
| Multiattack | 3-4 attacks or 2 + signature | Highest action economy |
| Recharge | 1-2 | More frequent |
| Reactions | 2-3 | Multiple options |
| Bonus Actions | 1-2 options | |
| Legendary Actions | Standard | 3 actions per round |
| Lair Actions | Standard for major bosses | |
| Regional Effects | Standard for major bosses | |
| Mythic Actions | For named bosses; trigger at HP threshold | "Phase 2" mechanic |

---

## Multiattack Patterns

### Standard Multiattack Format

```
***Multiattack.*** The [creature] makes two attacks: one with its
[weapon 1] and one with its [weapon 2].
```

### Common Variants

**Two attacks same weapon:**
```
***Multiattack.*** The creature makes two scimitar attacks.
```

**Mixed weapon + spell:**
```
***Multiattack.*** The creature makes three weapon attacks or casts
a spell, but not both. (Note: 2024 has unified this; check specific
creature.)
```

**Conditional multiattack:**
```
***Multiattack.*** If the creature is in fox form, it makes two
bite attacks. If in human form, it makes two longsword attacks.
```

### Multiattack Pitfalls

| Pitfall | Why |
|---|---|
| Multiattack with no attacks specified | Ambiguous; players don't know what to roll |
| Same attack repeated without specifying "twice" | Confusing; players may think multiple targets |
| Multiattack with mixed save/attack mechanics without grouping | Hard to track |
| Multiattack count too high for CR | Action economy inflation |
| Multiattack count too low for CR | Creature feels weak |

---

## Recharge Mechanics

### Standard Recharge Patterns

| Recharge | When usable | Notes |
|---|---|---|
| Recharge 5-6 | 33% per round | Standard "use rarely" |
| Recharge 6 | 17% per round | Use very rarely (Tier 4) |
| Recharge after a Long Rest | Once per day | Major signature ability |
| 1/Day | Once per day | Often replaces "Recharge after a Long Rest" |

### Format

```
***[Ability Name] (Recharge 5–6).*** [Description.]
```

Or:

```
***[Ability Name] (Recharge after a Long Rest).*** [Description.]
```

Or:

```
***[Ability Name] (1/Day).*** [Description.]
```

### Recharge Pitfalls

| Pitfall | Why |
|---|---|
| Recharge 4-6 on Tier 1-2 monster | Too generous; over-uses |
| Recharge 3-6 anywhere | Almost-always-on, not really a recharge |
| Recharge X-6 outside standard ranges (e.g., Recharge 5-7) | Format error |
| Recharge without specifying the trigger value | Ambiguous |
| Multiple recharge abilities on a non-boss monster | Action economy inflation |
| Recharge ability that's strictly inferior to a base attack | Why have it? |

---

## Reactions

### Standard Reactions

| Reaction | Examples |
|---|---|
| Parry / Riposte | Add to AC or counter-attack |
| Counterspell-like | Spellcasters |
| Defensive reactions | Shield, Disengage when struck |
| Opportunity attacks | Standard for all creatures |

### Format

```
REACTIONS

***[Reaction Name].*** [When the trigger occurs, the creature takes
this action.]
```

Trigger formula: `"When [event]:"` then the reaction.

### Reaction Pitfalls

| Pitfall | Why |
|---|---|
| Reaction with no trigger | Ambiguous |
| Reaction trigger that's always-on (e.g., "When the creature is hit") with massive reactive effect | Too strong |
| Multiple reactions per round without specifying | Action economy inflation |
| Reaction with no cost (most reactions are 1 per round) | Format error |

---

## Bonus Actions

### Standard Bonus Actions

| Bonus Action | Examples |
|---|---|
| Cunning Action (Dash/Disengage/Hide) | Rogue, Goblin, similar agile creatures |
| Misty Step / teleport | Spellcasters with focus on mobility |
| Bonus attack from feature | Two-weapon fighting, Battle Master maneuvers |
| Self-buff | Spellcaster Bonus Action buffs |
| Healing word / minor heal | Cleric, Bard |

### Format

```
BONUS ACTIONS

***[Bonus Action Name].*** [Description.]
```

### Bonus Action Pitfalls

| Pitfall | Why |
|---|---|
| Bonus Action that's Action-strength | Major balance error |
| Bonus Action that allows an extra leveled spell | Violates one-leveled-spell-per-turn rule |
| Multiple Bonus Action options where one is strictly better | Why have alternatives? |
| Bonus Action without clear use case | Filler |

---

## Legendary Actions

### Standard Budget

| Tier | Legendary Action Budget |
|---|---|
| CR 11-12 (rare) | 3 actions per round, but with limited options |
| CR 13-16 | 3 actions per round, 3-4 sub-options, costs vary |
| CR 17+ | 3 actions per round, 4-5 sub-options, costs include 2-3 action cost specials |

### Standard Legendary Action Cost

Most legendary actions cost **1 action**. The "premium" options
cost 2-3 actions.

| Cost | Typical Use |
|---|---|
| 1 action | Standard option (detect, basic attack, minor effect) |
| 2 actions | Stronger option (Wing Attack, Tail Sweep) |
| 3 actions | Major or terrain-affecting effect (Frightful Presence, Lair Modification) |

### Format

```
LEGENDARY ACTIONS

The [creature] can take 3 legendary actions, choosing from the
options below. Only one legendary action option can be used at a
time and only at the end of another creature's turn. The
[creature] regains spent legendary actions at the start of its
turn.

***Detect.*** The [creature] makes a Wisdom (Perception) check.

***[Basic Attack].*** The [creature] makes one [type] attack.

***[Major Action] (Costs 2 Actions).*** [Description of stronger
effect.]
```

### Legendary Action Pitfalls

| Pitfall | Why |
|---|---|
| Legendary actions on a non-boss low-CR monster | Action economy inflation |
| Legendary action budget != 3 | Standard is 3; deviation needs justification |
| Legendary action that costs 0 (i.e., free legendary actions) | Format error |
| Legendary action with no thematic connection to the boss | Generic / forgettable |
| Missing recovery clause (when do they refresh?) | Format error |
| Frequency tied to the wrong turn (legendary action on the boss's turn instead of off-turn) | Format error |

---

## Lair Actions

### Standard Lair Action Format

```
LAIR ACTIONS

On initiative count 20 (losing initiative ties), the [creature]
takes a lair action to cause one of the following effects; the
[creature] can't use the same effect two rounds in a row:

- [Lair effect 1]
- [Lair effect 2]
- [Lair effect 3]
```

### Lair Action Pitfalls

| Pitfall | Why |
|---|---|
| Lair action on a non-lair-bound creature | Conceptual error |
| Lair actions outside initiative count 20 | Format error |
| Lair actions that can repeat same effect | Violates standard rule |
| Lair actions that affect the boss (rather than the environment) | Conceptual error; lair actions affect terrain/area |
| Single lair action option | Should be 3+ options for variety |
| Lair actions that don't tie to the boss's identity | Generic; should reflect what the boss is |

---

## Regional Effects

### Standard Format

```
REGIONAL EFFECTS

The region containing a [creature]'s lair is warped by [the
creature's] magic, which creates one or more of the following
effects:

- [Effect 1]
- [Effect 2]
- [Effect 3]

If the [creature] dies, these effects fade over the course of
1d10 days.
```

### Regional Effect Pitfalls

| Pitfall | Why |
|---|---|
| Regional effects without lair actions | Conceptually they pair together |
| Regional effects with no fade clause | Format error |
| Regional effects that affect combat | They're meant to be narrative environmental, not combat-active |
| Generic regional effects (e.g., "things are darker") | Should be specific to the boss's identity |

---

## Mythic Actions (Tier 4 only)

### Standard Format

```
MYTHIC ACTIONS

If the [creature]'s [feature name] is available, it can use the
options below as legendary actions for 1 hour after [trigger]. It
regains spent mythic actions at the start of each of its turns.

***[Mythic Action 1].*** [Description.]
***[Mythic Action 2].*** [Description.]
***[Mythic Action 3 (Costs 2 Actions)].*** [Description.]
```

### Mythic Action Pitfalls

| Pitfall | Why |
|---|---|
| Mythic actions on Tier 1-3 monster | Out of tier |
| Mythic actions without HP trigger | Format error; trigger condition is required |
| Mythic actions that don't tie to "phase 2" identity | Pointless |
| Mythic actions that overlap with legendary actions | Why have both? |

---

## Common Action Economy Errors

### Error 1: Inflated Multiattack

Statting a CR 2 monster with 3 multiattack. The damage output is
CR 4+, but the HP and AC are CR 2.

**Fix:** Reduce multiattack count OR scale HP/AC up to match.

### Error 2: Missing Multiattack

A CR 5+ monster with only 1 attack per round. The creature is
under-offensive.

**Fix:** Add Multiattack with appropriate attack count.

### Error 3: Recharge Inflation

A CR 4 monster with Recharge 4-6 on a high-damage AoE ability.
The damage output is CR 6+, but the rest of the stat block is
CR 4.

**Fix:** Reduce recharge frequency to 5-6 OR scale rest of stat
block up.

### Error 4: Legendary Action on Wrong Tier

CR 8 monster with 3 legendary actions. Legendary actions are
designed for CR 10+ bosses; this monster is action-econ-inflated
for its tier.

**Fix:** Remove legendary actions and rebalance, OR scale stat
block to CR 10+ with appropriate HP and offensive math.

### Error 5: Action Economy Without Counter-Balance

A CR 6 monster with Reaction Parry that grants +5 AC. This
effectively raises AC to "monster level + 5" for the first attack
each round.

**Fix:** Either scale offensive output down or treat the Parry
as a balanced trade (e.g., costs an action use).

### Error 6: Bonus Action Spam

A CR 7 monster with multiple Bonus Action options, each providing
buffs or attacks. The action-economy density is CR 10+.

**Fix:** Limit Bonus Actions to 1 option, OR scale stat block up.

### Error 7: Lair Actions on Non-Lair Boss

A non-bound boss with lair actions. Conceptually wrong; lair
actions are for environment-bound bosses.

**Fix:** Remove lair actions OR redefine the boss as lair-bound
in the lore.

### Error 8: Reactions Without Triggers

A reaction listed without a clear trigger condition.

**Fix:** Add the trigger ("When a creature ends its turn within
5 feet of the X:").

---

## Quick Audit Checklist

For a stat block at CR X, verify:

- [ ] Multiattack count matches tier expectation.
- [ ] Recharge values are 5-6 (or 6 for very strong abilities).
- [ ] Reaction count is appropriate (1-2 standard; 2-3 for Tier 4
      boss).
- [ ] Bonus Action options are reasonable (0-1 standard; 1-2 for
      Tier 4).
- [ ] Legendary actions present only on CR 10+ bosses; budget is
      3 actions.
- [ ] Lair actions present only on lair-bound bosses; trigger on
      initiative count 20.
- [ ] Regional effects present only on lair-action bosses; fade
      clause documented.
- [ ] Mythic actions present only on Tier 4 named bosses;
      trigger condition documented.
- [ ] No action-economy inflation: stat block's total per-round
      damage and effects match CR.
