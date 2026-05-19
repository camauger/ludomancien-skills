# Chase and Downtime Encounter Protocols

Protocols for the two dynamic encounter types where calibration
depends on time-based or movement-based variables.

---

## Part I — Chase Encounter Protocol

### 1. Chase Anatomy

A chase has these structural elements:

| Element | What it represents |
|---|---|
| Quarry | The fleeing party / NPC |
| Pursuer | The chasing party / NPC |
| Lead distance | The gap between quarry and pursuer |
| Catch threshold | The lead distance at which quarry is caught |
| Escape threshold | The lead distance at which quarry is permanently free |
| Segments | Discrete "zones" of the chase route with their own complications |
| Complications | Per-round or per-segment obstacles |
| Resolution | What happens when caught / escaped |

### 2. Chase Scales

Pick the scale that matches the chase context:

| Scale | Route example | Duration | Lead distances |
|---|---|---|---|
| Foot chase (street level) | Urban alleys, marketplaces | 3–8 rounds | Lead 0–60 ft. |
| Building chase (multi-floor) | Rooftops, stairwells, sewers | 4–10 rounds | Lead 0–80 ft. |
| District chase (urban scale) | Multi-block sprint | 6–12 rounds | Lead 0–200 ft. (abstracted) |
| Mounted chase (regional) | Roads, fields, hills | 10–20 rounds | Lead 0–600 ft. (abstracted) |
| Vehicle chase (carriage, ship) | Sea, road | 15–30 rounds | Highly abstracted; segment-based |

### 3. Starting Lead Distance

The initial gap when the chase begins. Three patterns:

| Pattern | Initial lead | Notes |
|---|---|---|
| Close chase | 10–30 ft. | Quarry surprised; pursuit imminent |
| Mid chase | 30–80 ft. | Quarry got a head start; tense |
| Long chase | 80–200 ft. | Quarry well ahead; pursuit needs sustained effort |

Initial lead drives the chase's *texture*. Close chases are
desperate sprints; long chases are sustained efforts.

### 4. Catch and Escape Thresholds

- **Catch threshold:** typically 5 ft. (engagement range) or 0 ft.
  (squares overlap). At this distance, the pursuer can take an
  attack action or grapple action.
- **Escape threshold:** typically 100–200 ft. or "off the map / out
  of line of sight." At this distance, the quarry breaks free for
  good.

Both thresholds should be visible to the players from the start
("you're 40 ft. behind; if they get 150 ft. ahead, they escape").

### 5. Complication Tables

The signature mechanic of a chase: per-segment or per-round, a
complication forces a check or imposes a cost.

#### Complication design

A good complication:
- Forces a check (Athletics, Acrobatics, Stealth, Perception, etc.)
- Has 3 outcomes: success (no cost), partial success (small cost),
  failure (significant cost)
- Costs lead distance, action economy, HP, or alerts witnesses

#### Sample complication: urban street

| Roll d6 | Complication | Check | Success / Failure |
|---|---|---|---|
| 1 | A market stall blocks the way | DEX (Acrobatics) 12 | Success: no cost. Failure: −10 ft. movement this turn. |
| 2 | A loud commotion ahead | WIS (Perception) 14 | Success: spot the route around. Failure: enter alley with bystanders. |
| 3 | Sudden crowd of bystanders | STR (Athletics) 13 | Success: push through. Failure: knocked prone. |
| 4 | A passing wagon | DEX (Acrobatics) 14 | Success: vault over. Failure: take 1d6 + −10 ft. |
| 5 | Slippery cobblestones | DEX save 12 | Success: stay upright. Failure: fall prone, lose 1 move action. |
| 6 | A pursuer attempts to grab | Quarry's WIS save vs grabber's DC | Save: free. Fail: grappled briefly, lose 10 ft. lead. |

#### Sample complication: forest / outdoors

| Roll d6 | Complication | Check | Success / Failure |
|---|---|---|---|
| 1 | A tangled root | DEX (Acrobatics) 13 | Success: pass. Failure: prone. |
| 2 | A narrow ravine to cross | STR (Athletics) or DEX (Acrobatics) 13 | Success: across. Failure: drop into ravine, 2d6 damage. |
| 3 | A patch of brambles | CON 12 or take 1d4 piercing | Success: minor cuts. Failure: 1d4 + reduced speed. |
| 4 | An overhanging branch (low) | DEX (Acrobatics) 14 | Success: duck under. Failure: knocked off mount or prone. |
| 5 | A muddy slope | DEX (Acrobatics) 14 | Success: maintain footing. Failure: slide downhill, lose 15 ft. |
| 6 | A wildlife alarm (birds startled) | Stealth check vs Perception | Failure: alerts other creatures in area. |

#### Sample complication: rooftops

| Roll d6 | Complication | Check | Success / Failure |
|---|---|---|---|
| 1 | A loose tile | DEX (Acrobatics) 14 | Success: balance. Failure: prone or slide 10 ft. |
| 2 | A long jump | STR (Athletics) 12 | Success: clear. Failure: half distance + fall damage. |
| 3 | A clothesline / cable | DEX 12 | Success: duck or use. Failure: 1d4 damage. |
| 4 | A guard on a balcony | Stealth check | Failure: alert the guard. |
| 5 | A weak section of roof | CON save 14 (or fall through) | Failure: fall into building (2d6 damage; encounter inside) |
| 6 | A flock of pigeons | WIS (Perception) 12 | Success: navigate. Failure: disadvantage on attacks for 1 round. |

### 6. Chase Movement Rules

Each round, all chase participants:

1. **Dash by default** (double movement). Costs 0 for human-scaled
   creatures; tracks exhaustion at the bottom of the chase.
2. **Take a complication check** if triggered (per the table)
3. **Movement difference applies** — the faster mover gains lead
   distance; the slower loses ground
4. **Optional action:** can sacrifice a Dash for an action (cast a
   spell, throw an object, force a check on the pursuer / quarry)

### 7. Exhaustion Tracking

The 2024 DMG simplified exhaustion. In a chase:

- Each round of Dashing, the participant accumulates "chase
  exhaustion" (a tracked counter, not full exhaustion levels)
- Every 3 rounds of Dashing, the participant must make a CON save
  (DC starts at 10, increases by 1 each subsequent check) or gain
  1 level of exhaustion
- Mounted creatures gain exhaustion at half the rate (every 6
  rounds)
- Some classes have features that reduce exhaustion (rangers, monks
  with specific subclasses)

### 8. Resolution of a Chase

The chase resolves when:

- **Quarry caught:** combat begins or grapple action triggered
- **Quarry escapes:** lead distance exceeds escape threshold; quarry
  goes off-map or out of sight
- **Quarry surrenders:** voluntary stop (taking damage, witnessing
  ally captured, etc.)
- **Chase ends due to environment:** entering a sealed area, joining
  reinforcements, hitting impassable terrain

Each resolution should have a *named narrative outcome* — not just
"you escape" but "you escape into the slums of the Iron Rats, who
will not be pleased to see you."

### 9. Chase Encounter Output Structure

```
**Quarry:** [Description, motivation]
**Pursuer:** [Description, motivation]
**Initial Lead:** [N feet]
**Catch Threshold:** [5 ft. typical]
**Escape Threshold:** [N feet]

### Route Segments
1. [Segment 1 — terrain, mood, complications]
2. [Segment 2 — terrain, mood, complications]
3. [Segment 3 — terrain, mood, complications]
[3–5 segments typically]

### Complication Table (per segment OR per round)
[d6 or d8 table with checks and outcomes]

### Catch Outcomes
- [On catch: what happens — combat? capture? negotiation?]

### Escape Outcomes
- [On escape: where does the quarry go? what's the cost of pursuing
  further?]
- [On giving up the chase: what does the party gain or lose?]
```

### 10. Common Chase Pitfalls

#### "Everyone Dashes Every Round"

The chase has no tactical decisions. Every round is just movement
math.

**Fix:** complications force checks; check failures cost lead or
actions; choices matter (Stealth to evade vs Athletics to vault).

#### "Single Check Ends It"

A failed Athletics roll = caught. The party feels cheated.

**Fix:** failures cost lead distance or actions, not the whole
chase. Multiple failures are needed.

#### "Featureless Route"

"You chase through the city for 6 rounds." No texture. Players
disengage.

**Fix:** 3–5 named segments with distinct terrain and complication
tables. Each segment has a memorable feature.

#### "Speed Advantage Trivializes"

The quarry has +10 ft. speed; they always pull ahead. The chase
is forgone.

**Fix:** terrain transitions reset the speed advantage. Some
terrains (water, rope ladders, ice) favor the slow, not the fast.

#### "No Witnesses or Consequences"

The chase is in a vacuum. Damage to bystanders doesn't matter.

**Fix:** for urban chases, every collateral choice has narrative
weight. The market vendor whose stall got knocked over remembers.

---

## Part II — Downtime Encounter Protocol

### 1. Downtime Activity Catalog

Downtime encounters cover activities that span days, weeks, or
months. Common activities:

| Activity | Time cost | Gold cost | Primary check / metric |
|---|---|---|---|
| Carousing (gather info) | 1 week | Lifestyle expense | Charisma check, info gained |
| Training (gain proficiency) | 250 days, 1 gp/day | Cumulative time | Pass with no check; mastered |
| Crafting (make item) | 1 day per 5 gp value | 50% of item value | Tool proficiency check |
| Research (gain info / spell) | 1 week minimum | 10–50 gp/week | Cumulative Intelligence checks |
| Practicing a profession | 1 week | None | Earn 1d6 sp/day or equivalent |
| Recuperation (heal injury) | 3 days | None | Recover from a lingering injury |
| Pit fighting | 1 week | Earnings or wager | Combat-related skill checks |
| Sowing rumors | 1 week | 1 gp/day per +1 DC | Persuasion or Deception |
| Building relationships | Variable | Lifestyle expense | Persuasion check per week |
| Religious devotion | 1 week | Donation | Religion check, deity favor |
| Scribing scrolls / brewing potions | Days per item | Material cost | Class-specific feature |

### 2. Downtime Activity Output Structure

```
**Activity:** [Name]
**Time Cost:** [Days, weeks, months]
**Gold Cost:** [If applicable; lifestyle expense for the duration]
**Success Metric:** [Single check / cumulative / resource trade-off]
**Modifier sources:** [Skills, tool proficiencies, class features]

### Mechanical Resolution
[How the check or accumulation is determined]

### Outcome Branches
- **Full success:** [The intended outcome]
- **Partial success:** [Lesser outcome — useful but incomplete]
- **Failure:** [No outcome; resources still spent]
- **Critical failure:** [Negative side effect beyond losing resources]

### World Reaction
[What happens in the wider campaign while the PC is engaged in this
activity. Even a 1-week downtime means 1 week of other events:
NPC X moves; faction Y recruits; opportunity Z closes; rumor R
spreads.]

### Narrative Payoff
[A 1-paragraph description of the experience — what the PC sees,
does, learns, becomes. This is the "read-aloud equivalent" for
downtime.]
```

### 3. Downtime DCs and Metrics

Downtime DCs scale less by character level and more by *what is
being attempted*:

| Difficulty of activity | DC |
|---|---|
| Trivial / well-resourced | 10 |
| Standard (most activities) | 15 |
| Hard (researching obscure topics) | 18 |
| Very Hard (creating new spell, mastering rare proficiency) | 20 |
| Nearly Impossible (cure a unique curse, reverse a death) | 25 |

For cumulative metrics (research, training):

| Threshold | Effort accumulated |
|---|---|
| Light learning | 1 week of effort |
| Standard mastery | 1 month of effort |
| Deep specialization | 6 months of effort |
| Mastery / unique knowledge | 1+ year of effort |

### 4. The World Continues — Time Pressure

The defining mechanic of downtime is that *time passes for everyone*.
While the PCs spend 2 months training, NPCs do things, factions move,
opportunities open and close.

For each downtime period:

| Time | World reaction |
|---|---|
| 1 week | 1 minor event (rumor spreads, NPC visits town, news from afar) |
| 1 month | 1 moderate event (faction policy shifts, new opportunity, lost opportunity) |
| 3 months | 1 major event (NPC dies, war begins, magical convergence) |
| 1 year+ | Campaign-defining event (the world has changed substantially) |

The downtime encounter document should list these *plausible world
reactions* — what would happen while the PC is occupied?

### 5. Side Effects of Downtime

Beyond the primary reward, downtime activities should produce *side
effects* — for the PC, the campaign, or both.

| Activity | Common side effect |
|---|---|
| Carousing | Made a friend, but also a rival; alerted authorities |
| Training | New ability + a debt of gratitude to the trainer |
| Crafting | Item created + a workshop fire / supplier issue |
| Research | Knowledge gained + an academic rival takes interest |
| Pit fighting | Gold + a debt collector / a fan club / a scar |
| Sowing rumors | Rumor spread + a counter-rumor traceable to the PC |
| Religious devotion | Boon from deity + an obligation to the temple |

Side effects make downtime *consequential*. Without them, downtime
is just numerical changes — gain item, gain proficiency, gain gold.

### 6. Common Downtime Pitfalls

#### "Simultaneous activities"

The PC researches, trains, and crafts simultaneously during the
same 4 weeks.

**Fix:** time is the binding constraint. Force trade-offs. A PC
training in swordsmanship can't also research necromancy in the
same hours.

#### "No world reaction"

The PC returns from 6 months of training and the world is unchanged.

**Fix:** every downtime period produces at least 1 world reaction,
visible to the PC.

#### "Mechanical-only resolution"

Downtime is "roll Intelligence, you finish your research." No
narrative, no investment.

**Fix:** narrative payoff (the 1-paragraph experience). Side effects.
World reaction. Make downtime *feel* like the months they represent.

#### "Cost is too low"

The PC spends 1 month and 50 gp and masters a new tool proficiency.
But the PC has 10,000 gp; the cost is meaningless.

**Fix:** scale costs by tier. A Tier 4 PC paying 50 gp for training
is symbolic at best; the real cost should be time investment and
opportunity cost.

#### "All activities are equally accessible"

The desert nomad PC can carouse in the same way as the noble PC.

**Fix:** lifestyle and reputation gate activities. Carousing in
high society requires nobility or a strong introduction. Research
in an arcane library requires academic standing.

### 7. Sample Downtime Encounter

**Activity:** Sowing Rumors (the PC tries to spread a story about a
rival noble's secret debts)

**Time Cost:** 2 weeks
**Gold Cost:** Lifestyle expense + 1 gp/day per +1 to DC = 14 gp +
3 gp per +1 DC chosen
**Success Metric:** Persuasion or Deception DC 15 (base), +1 per
each additional gold spent boosting

### Mechanical Resolution
PC makes a check per week. Two successes plant the rumor.

### Outcome Branches
- **Full success (2 successes):** Rumor spreads; the rival's
  reputation suffers; faction relationships shift in PC's favor
- **Partial success (1 success):** Rumor partially spreads; some
  whispers; the rival becomes suspicious but cannot trace the source
- **Failure (0 successes after 2 weeks):** Rumor fails to take; PC
  has spent gold and time with no payoff
- **Critical failure (failed roll by 5+):** Rumor traced back to PC;
  the rival's faction now has the PC as a target

### World Reaction
- Week 1: A minor faction rep visits town; might cross paths with
  the rumor depending on outcome
- Week 2: News from afar — a related rumor (real or coincidental)
  spreads in another city
- The rival's faction holds a council in Week 3 to address (or
  ignore) the situation

### Narrative Payoff
> Two weeks of evenings in inns and parlor rooms, of leaning close
> to listen, of paying for rounds of cheap wine and waiting for the
> right moment to drop a story. By the end, your story has acquired
> the texture of overheard truth — passed mouth to mouth, embellished
> at each retelling. You don't know exactly who told it last, but you
> know it's no longer your story to control.
