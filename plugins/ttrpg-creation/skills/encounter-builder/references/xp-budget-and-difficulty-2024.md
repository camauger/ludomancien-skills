# XP Budget and Difficulty — D&D 5e 2024

The numerical anchors for calibrating combat encounter difficulty in
D&D 5e 2024.

**Honest note on sources:** the 2024 Dungeon Master's Guide revised
the encounter-building chapter, simplifying the 2014 "Easy / Medium /
Hard / Deadly" tiers into "Low / Moderate / High" and adjusting the
group multiplier approach. The benchmarks below derive from the 2014
DMG table preserved with minor adjustments. Use as **design targets**
— verify against the 2024 DMG before publishing commercial content.

---

## 1. The Three Difficulty Tiers (DMG 2024)

| Tier | What it means | Resource consumption | Risk of PC death |
|---|---|---|---|
| Low | Easy encounter; obstacle, not crisis | ~25% of daily resources | Negligible |
| Moderate | Standard encounter | ~50% of daily resources | Low but real |
| High | Hard encounter; party tested | ~75% of daily resources | Significant; PCs may go down |

The 2024 "High" subsumes the 2014 "Hard" and the lower band of
"Deadly." For genuinely punishing encounters that risk TPK, push
above the High threshold by 25–50% with explicit GM warning.

### "Deadly" doesn't disappear

The 2024 system removed "Deadly" as a separate tier but acknowledges
that High encounters can be designed to be deadlier by:

- Hitting the upper end of the High XP budget
- Adding terrain hazards
- Stacking environmental pressure (time, witnesses, escape blocked)
- Selecting monsters whose abilities counter the party (anti-caster
  for caster-heavy parties, ranged for melee parties)

---

## 2. XP Budget per Character per Level

This table gives the XP budget *per PC* at each level for each
difficulty tier. Multiply by party size for the total budget.

| Level | Low (per PC) | Moderate (per PC) | High (per PC) |
|---|---|---|---|
| 1 | 50 | 75 | 100 |
| 2 | 100 | 150 | 200 |
| 3 | 150 | 225 | 400 |
| 4 | 250 | 375 | 500 |
| 5 | 500 | 750 | 1,100 |
| 6 | 600 | 1,000 | 1,400 |
| 7 | 750 | 1,300 | 1,700 |
| 8 | 1,000 | 1,700 | 2,100 |
| 9 | 1,300 | 2,000 | 2,400 |
| 10 | 1,600 | 2,300 | 2,800 |
| 11 | 1,900 | 2,900 | 3,600 |
| 12 | 2,200 | 3,700 | 4,500 |
| 13 | 2,600 | 4,200 | 5,100 |
| 14 | 2,900 | 4,900 | 5,700 |
| 15 | 3,300 | 5,400 | 6,400 |
| 16 | 3,800 | 6,100 | 7,200 |
| 17 | 4,500 | 7,200 | 8,800 |
| 18 | 4,900 | 7,500 | 9,500 |
| 19 | 5,700 | 8,500 | 10,900 |
| 20 | 6,400 | 9,500 | 12,700 |

### Reading the table

A party of 4 PCs at level 5:

- **Low encounter:** 4 × 500 = 2,000 XP total
- **Moderate encounter:** 4 × 750 = 3,000 XP total
- **High encounter:** 4 × 1,100 = 4,400 XP total

The XP budget is the *sum of monster XP values* you can spend on
the encounter.

### Cross-checking against monster XP

Monster XP by Challenge Rating (from `cr-design-protocol-2024.md`
in the `monster-creator` skill):

| CR | XP |
|---|---|
| 0 | 0 or 10 |
| 1/8 | 25 |
| 1/4 | 50 |
| 1/2 | 100 |
| 1 | 200 |
| 2 | 450 |
| 3 | 700 |
| 4 | 1,100 |
| 5 | 1,800 |
| 6 | 2,300 |
| 7 | 2,900 |
| 8 | 3,900 |
| 9 | 5,000 |
| 10 | 5,900 |
| 11 | 7,200 |
| 12 | 8,400 |
| 13 | 10,000 |
| 14 | 11,500 |
| 15 | 13,000 |
| 16 | 15,000 |
| 17 | 18,000 |
| 18 | 20,000 |
| 19 | 22,000 |
| 20 | 25,000 |

For the 4 PCs at level 5 with a 3,000 XP Moderate budget:
- 1 monster at CR 5 (1,800 XP) + 2 CR 1 (400 XP) = 2,200 → underbudget
- 1 monster at CR 6 (2,300 XP) + 2 CR 1/2 (200 XP) = 2,500 → slight under
- 1 monster at CR 7 (2,900 XP) → at budget, single-monster fight
- 4 monsters at CR 2 (1,800 XP) → significantly underbudget; need
  multiplier consideration (see below) or more monsters

---

## 3. Multi-Monster Adjustment (2024 Approach)

The 2014 DMG used an explicit multiplier table to account for the
action economy advantage of multiple monsters against a single
party. The 2024 DMG simplified this — in many cases, the multiplier
is implicit (just sum monster XP) or applied through *encounter
intensity* notes rather than strict multipliers.

**Practical recommendation:** when designing encounters with
multiple monsters, mentally apply a 1.5× to 2× multiplier on the
monster XP for the effective difficulty:

| Number of monsters | Effective XP multiplier (informal) |
|---|---|
| 1 | ×1 |
| 2 | ×1.25 |
| 3–6 | ×1.5 |
| 7–10 | ×2 |
| 11+ | ×2.5+ |

A swarm of 4 CR 2 monsters at 1,800 raw XP plays like ~2,700 XP
effective in combat — closer to Moderate against the 3,000 budget.

### Why this matters

The single-monster vs multi-monster distinction is the most
important balance variable. A solo monster, even at high CR, can
be focused down by a coordinated party. Multi-monster encounters
force the party to spread attention and consume more spell slots
per round.

---

## 4. Party Composition Adjustments

The default XP budget assumes a "typical" party: 2 martial + 1
caster + 1 hybrid, or similar balanced mix. Adjust for outliers:

### All-Martial Parties (4 PCs, all fighters/barbarians/paladins)

- **Strong against**: solo high-HP bosses (focused fire)
- **Weak against**: ranged-heavy enemies, save-or-suck spells from
  enemies, environments where movement matters
- **Adjustment**: encounters with strong AoE or save-based threats
  hit harder; bump High threshold by 10%

### All-Caster Parties (4 PCs, all wizards/sorcerers/druids)

- **Strong against**: groups of low-HP monsters (AoE), monsters
  with low save bonuses
- **Weak against**: solo high-HP bosses, anti-magic creatures,
  long combats (slot depletion)
- **Adjustment**: solo boss fights hit harder; reduce High threshold
  by 10% for solo bosses

### Mixed but Specialized (4 PCs, all rogues / all clerics)

- Adjust based on the specialization's strengths and weaknesses
- Generally, mono-class parties have a tighter "win window" — they
  excel at one thing and struggle with the inverse

### Party Size Adjustments

| Party size | Budget adjustment |
|---|---|
| 1 PC | XP per character × 1.5 (solo play; per-PC harder) |
| 2 PCs | XP per character × 1.25 |
| 3 PCs | XP per character × 1.1 |
| 4 PCs | Standard (×1.0) |
| 5 PCs | XP per character × 0.9 |
| 6 PCs | XP per character × 0.8 |
| 7+ PCs | XP per character × 0.7; consider splitting encounters |

Smaller parties benefit per-PC; larger parties spread the load.

---

## 5. Adventuring Day Budget

The DMG suggests a "Daily XP Budget" — the total XP of all
encounters in a single adventuring day before the party needs a
long rest. This concept is preserved (with adjustments) in 2024.

### Daily XP budget per character per level

| Level | Daily budget per PC |
|---|---|
| 1 | 300 |
| 2 | 600 |
| 3 | 1,200 |
| 4 | 1,700 |
| 5 | 3,500 |
| 6 | 4,000 |
| 7 | 5,000 |
| 8 | 6,000 |
| 9 | 7,500 |
| 10 | 9,000 |
| 11 | 10,500 |
| 12 | 11,500 |
| 13 | 13,500 |
| 14 | 15,000 |
| 15 | 18,000 |
| 16 | 20,000 |
| 17 | 25,000 |
| 18 | 27,000 |
| 19 | 30,000 |
| 20 | 40,000 |

### Pacing implication

For a party of 4 at level 5:
- Daily budget: 4 × 3,500 = 14,000 XP
- That's roughly 4–7 Moderate encounters per day before long rest
- Or 2–4 High encounters per day
- Or 1 High + 2 Moderate + 1 Low

If the brief is a single encounter, the daily budget is just
context. If the brief is a chain (use `scenario-writer`), the
daily budget shapes the pacing.

---

## 6. Adjustment Levers Within the XP Budget

Two encounters with the same XP can feel very different. Use these
levers to shape *feel* without changing *difficulty*:

### Action economy lever

- **Solo monster** = boss fight feel, focused attention
- **2–3 monsters** = mid-CR ensemble, role variety
- **4+ monsters** = horde feel, spread attention, AoE-favoring

Same XP, different texture. Match the lever to the narrative beat.

### Power-level lever

- **One high-CR monster** = threat through a single dominant
  presence
- **Many low-CR monsters** = threat through quantity and chaos
- **Mixed CR (one high + several low)** = threat with hierarchy; the
  leader and the lieutenants

### Environment lever

Same monsters in different environments feel different:

- Open plains: full mobility, ranged advantage, no cover
- Dense forest: cover plentiful, melee favored
- Underground caves: tight spaces, terrain matters, no flight
- Urban alleyways: cover, witnesses, collateral
- Magical zones: terrain effects, save-based attrition

### Time pressure lever

- **No time pressure:** standard combat, full resource use possible
- **Soft time pressure:** the bell will ring in N rounds, alerting
  more enemies
- **Hard time pressure:** if you don't reach the goal in X rounds,
  the captured ally dies

Time pressure pushes the party to take risks they wouldn't otherwise
take — feels harder without changing XP.

### Resource-depletion lever

Where in the adventuring day does this encounter fall?

- **First encounter of the day:** party has full resources; high
  budget needed for High feel
- **Mid-day:** party is at 60% resources; standard budget
- **Late day, no long rest:** party is at 30% resources; reduce
  effective budget by ~25%

---

## 7. Calibration Worksheet

When designing an encounter, walk through:

1. **Party data**
   - Size: ___ PCs
   - Level: ___
   - Composition: ___

2. **Target difficulty**
   - Tier: ☐ Low ☐ Moderate ☐ High ☐ Above-High (warned)

3. **Budget calculation**
   - XP per PC at target tier: ___
   - Party size: ___
   - Composition adjustment: ___ (×__)
   - Resource-depletion adjustment: ___ (×__)
   - **Total budget: ___ XP**

4. **Monster selection**
   - Pick the action-economy lever (solo / ensemble / horde)
   - Choose monsters totaling target XP
   - Apply informal multiplier for multi-monster (×1.25 to ×2.5)
   - Validate role distribution (don't put all Brutes)

5. **Environment overlay**
   - Terrain features (cover, elevation, hazards)
   - Time pressure (none, soft, hard)
   - Witnesses / collateral

6. **Sanity check**
   - Does this match the narrative beat?
   - Does this serve the campaign's pacing?
   - Is there an alternative win path beyond TPK?

---

## 8. Common Calibration Errors

### "Too many monsters at low CR"

Building a "horde" encounter for level 1 PCs with 8 CR 1/2 monsters
(total 800 XP) sounds reasonable against an XP budget of 800.
But the action economy (8 vs 4 actions per round) makes this
deadly — and the low save DCs from CR 1/2 monsters mean PCs save
out of conditions easily, making the fight long and grindy.

**Better:** 4 CR 1/2 + 1 CR 2 for ~1,000 XP. The mid-CR monster is
the threat anchor; the low-CR monsters are the bodyguards.

### "Solo high-CR boss"

A CR 11 monster alone against 4 level 7 PCs has 7,200 XP — well
beyond High threshold (6,800). It looks deadly.

But: the action economy is 4-to-1. The party will focus fire.
Without legendary actions or escape mechanics, the boss dies in
round 2 of round 3.

**Better:** add legendary actions (already factored in for some
CR 11 monsters), add 2–3 CR 1 minions to absorb concentration-
breaking attacks, OR escalate to a CR 13 boss with legendary
actions and lair effects.

### "Wrong CR for the threat type"

A "Hard" encounter for level 5 PCs (1,100 XP per PC, 4,400 total)
populated by a CR 7 monster (2,900 XP) is technically under-budget
but the *single CR 7* threat in a single fight has the right feel.

A "Hard" 4,400 budget filled with 8 CR 1 monsters (1,600 raw XP,
~3,200 effective with multiplier) is under-budget AND the action
economy feels overwhelming for level 5 PCs without strong AoE.

**Better:** match the CR scale to the encounter intent (boss vs
horde) and let XP fall where it falls within the tier band.

### "Forgetting party composition"

The encounter passes all numerical checks but the party has 4
melee characters and the monster is a flying caster who breaks
line of sight. The fight is a frustrating chase.

**Better:** account for composition either by changing monsters
(grounded melee for melee parties) or by adding environment
features that mitigate the disadvantage (low ceilings, choke
points).

---

## 9. Two-Phase Calibration Check

After the initial design, validate:

### Phase 1: Math check

- [ ] Total monster XP within ±10% of target budget
- [ ] Multi-monster multiplier accounted for
- [ ] Composition adjustment applied
- [ ] Resource-depletion adjustment applied

### Phase 2: Texture check

- [ ] Action economy is reasonable (4 monsters vs 4 PCs, or 1 boss
      + 2 minions vs 4 PCs, etc.)
- [ ] Role distribution mixes Brutes / Soldiers / Artillery / etc.
- [ ] Environment supports rather than blocks party tactics
- [ ] Time pressure is intentional, not accidental
- [ ] An alternative win path exists beyond TPK
- [ ] The encounter serves the narrative beat (boss = identity-defining;
      ambush = surprise; defense = stakes)
