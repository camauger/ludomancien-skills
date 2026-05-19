# Social and Exploration Encounter Protocols

Protocols for designing the two non-combat encounter types where
calibration is static (the encounter's parameters are set in
advance, not driven by round-by-round movement).

---

## Part I — Social Encounter Protocol

### 1. The NPC Attitude Ladder

NPCs have a tracked attitude toward the PCs. The DMG 2024 preserves
the basic 5-state ladder:

| Attitude | What it means | Default action |
|---|---|---|
| Hostile | Wants to harm the PCs | Attack or call for help |
| Indifferent | No interest, possibly resentful | Refuse to help; minimal engagement |
| Friendly | Sympathetic but not committed | Offer minor help if convenient |
| Helpful | Actively wants PCs to succeed | Offer substantive aid |
| Allied | Personal stake in PC success | Coordinate, share intel, sacrifice |

### Attitude shifts during the encounter

Attitude is not static. Each "move" in the conversation can shift
it up or down:

| PC move | Effect on attitude |
|---|---|
| Strong persuasion check + relevant offer | +1 tier |
| Strong persuasion check + nothing offered | +0 to +1 tier |
| Threat / intimidation succeeding | +1 tier toward "Helpful through fear" |
| Threat failing | −1 to −2 tiers |
| Insult / disrespect | −1 to −2 tiers |
| Demonstrating shared values / common ground | +1 tier |
| Presenting evidence the NPC must accept | +1 tier or unlock new content |
| Revealing the PCs' true motives | depends; can be +1 or −2 |

### Walk-away threshold

Every NPC has a point where they leave the conversation. Define it
explicitly:

- "The merchant walks away if openly insulted or if the conversation
  takes more than 20 minutes of his time."
- "The cultist walks away the moment her god is invoked
  disrespectfully."
- "The lord walks away if his honor is questioned in front of his
  retainers."

The walk-away threshold is a hard "fail" state for the encounter.

### Information graph

For information-gathering social encounters, define what the NPC
*knows* and what they *reveal* at each attitude tier:

```
The Court Wizard knows:
1. The Queen's location (known to all)
2. The Queen's daily schedule (known to courtiers)
3. The Queen's secret meetings (known to inner circle)
4. The Queen's plans (known only to the Wizard)

Reveal at:
- Indifferent: 1 only
- Friendly: 1 and 2
- Helpful: 1, 2, and 3
- Allied: All four
```

This makes the social encounter feel *progressive* — each level of
trust unlocks more.

### 2. Persuasion DCs

Scale DCs by stakes and what the PCs offer:

| Stakes | Base DC (NPC neutral or Indifferent) |
|---|---|
| Trivial (move aside, give directions) | 10 |
| Minor (share gossip, deliver a message) | 12 |
| Standard (perform a favor at no cost) | 15 |
| Significant (risk reputation, cost gold) | 17 |
| Major (betray a faction, risk life) | 20 |
| Massive (sacrifice a loved one's safety) | 25 |

Adjustments:

| Lever | DC modifier |
|---|---|
| NPC owes the PCs a favor | −2 to −5 |
| NPC's faction approves | −2 |
| PCs offer commensurate reward | −2 to −5 |
| PCs present compelling evidence | −5 (or unlock new attitude) |
| NPC has reason to distrust PCs | +2 to +5 |
| NPC's faction opposes | +2 |
| Multiple PCs witness the conversation | −1 (social pressure) |
| Private conversation | usually +0 |

### 3. Action Economy of a Social Encounter

A social encounter is not round-by-round but has structural beats:

- **Opening:** initial attitude established, stakes named
- **Exchange:** 2–4 "moves" where PCs offer, ask, threaten, or
  reveal
- **Climax:** the decisive check or revelation
- **Resolution:** outcome stated; what the NPC does next

Each "move" is approximately one minute of in-fiction conversation.
A typical social encounter spans 5–15 minutes of fiction and 15–30
minutes of table time.

### 4. Social Encounter Output Structure

```
**NPC:** [Name, role]
**Starting Attitude:** [Hostile / Indifferent / Friendly / Helpful / Allied]
**Goal:** [What the NPC wants from the PCs, or wants for themselves]
**Walk-Away Threshold:** [Specific trigger]
**Persuasion DC (base):** [Number]

### Levers (each shifts DC or attitude)
- [Lever 1]: [effect]
- [Lever 2]: [effect]
- [Lever 3]: [effect]
- [Lever 4]: [effect]

### Information Graph
- Indifferent: [what NPC reveals]
- Friendly: [what NPC adds]
- Helpful: [what NPC adds]
- Allied: [what NPC adds — usually the deepest info]

### Outcome Branches
- Allied: [consequence]
- Helpful: [consequence]
- Friendly: [consequence]
- Indifferent: [consequence]
- Hostile (downward shift): [consequence — combat? expulsion? rumor?]
```

### 5. Common Social Encounter Subtypes

#### Interrogation

The captured enemy must reveal information. Levers include
intimidation, leverage (threats to family / faction), trade (the
PC offers something), and Insight reads.

#### Persuasion of a Hostile NPC

The PC must convince an opponent to take an action they would not
naturally take. Levers include appeals to shared values, demonstrations
of competence, evidence presentation, and personal cost on the PC's
side.

#### Political Negotiation

Multiple factions or NPCs with overlapping and conflicting interests.
The PCs broker outcomes. Often involves multiple consecutive checks
(persuade A, then leverage A's agreement to persuade B).

#### Debate

The PCs argue a position in a formal or public setting. Audience
opinion is the tracked variable. Each rhetorical move shifts audience
opinion; the final check determines the verdict.

#### Romance / Seduction

Building emotional connection rather than transactional negotiation.
Levers are different: shared experiences, vulnerability, charisma
displays, demonstrations of care. Long-arc rather than single-scene.

---

## Part II — Exploration Encounter Protocol

### 1. The Exploration Challenge Types

Exploration encounters are about traversal, navigation, or discovery.
Six common challenge types:

| Type | Primary skill | Failure cost |
|---|---|---|
| Traverse hazard | Athletics, Acrobatics | Damage, time |
| Find concealed | Investigation, Perception | Wrong path, alert enemies |
| Navigate unknown | Survival, Nature | Lost, time, exhaustion |
| Identify danger | Perception, Insight | Surprise, damage |
| Avoid notice | Stealth | Combat encounter triggered |
| Decode / interpret | Investigation, Arcana, History | Misunderstand, take wrong action |

### 2. Skill DC Scaling for Exploration

| Difficulty | DC | Failure cost |
|---|---|---|
| Trivial | 10 | Minor delay, no real cost |
| Easy | 12 | 1d4 minutes lost or minor damage |
| Standard | 15 | Time loss, conditional damage |
| Hard | 18 | Significant cost (exhaustion, alerting enemies) |
| Very Hard | 20 | Major setback (lose path entirely, take real damage) |
| Nearly Impossible | 25 | Catastrophic (full encounter trigger, severe damage) |

DCs scale somewhat with party level — a "Standard" DC for a level
5 party is 15, but for a level 17 party it's effectively trivial
(the party's modifier is +8 to +10 reliably).

For higher-level parties, adjust:

| Party tier | Standard DC adjustment |
|---|---|
| Tier 1 (1–4) | DCs 10–18 standard |
| Tier 2 (5–10) | DCs 12–20 standard |
| Tier 3 (11–16) | DCs 15–22 standard |
| Tier 4 (17–20) | DCs 18–25 standard |

### 3. Multi-Path Design

Strong exploration encounters offer multiple paths to success.
Three primary patterns:

#### Skill alternative

The same goal achievable by different skills.
Example: cross a chasm by Athletics (climb), Acrobatics (jump), or
Survival (find a path around).

Each skill has its own DC and cost; the party chooses based on
their strengths.

#### Spell alternative

The same goal achievable through magical means.
Example: cross a chasm by climbing (no spell), or by misty step (1
spell slot), or by fly (1 spell slot, longer duration).

Spell alternatives let casters spend resources for advantage; this
is a core 5e currency.

#### Patience / time alternative

The same goal achievable with more time investment but no risk.
Example: solve a puzzle by spending 1 hour searching (no check), or
by Investigation DC 18 (1 minute, partial info), or by Arcana DC
22 (1 minute, full info).

Patience alternatives give the party an option that doesn't require
checks but consumes their long-rest opportunities.

### 4. Environmental Hazards in Exploration

Hazards in exploration encounters are typically *passive*:

| Hazard | Activation | Effect |
|---|---|---|
| Cold environment | Per hour | Constitution save, exhaustion on fail |
| Heat | Per hour | Constitution save, exhaustion on fail |
| Altitude | After 4 hours of climbing | Save or take exhaustion |
| Suffocation (closed space, swimming) | After holding breath limit | Damage and consciousness loss |
| Magical environment (silence, antimagic) | While inside | Suppresses spellcasting |
| Cursed terrain | Per hour spent | Charisma or Wisdom save against effects |
| Patrolled area | Periodic | Stealth check or encounter triggered |

Hazard interaction is the tax for traversal. Exploration encounters
with no hazards become walk-throughs; encounters with too many
hazards become drudgery.

### 5. Exploration Encounter Output Structure

```
**Environment:** [Specific place, time of day, atmosphere]
**Challenge Type:** [Traverse / Find / Navigate / Identify / Avoid / Decode]
**Primary Goal:** [What success unlocks]

### Paths to Success
1. [Path A] — DC [N] [skill], cost [time / resource]
2. [Path B] — DC [N] [skill], cost [time / resource]
3. [Spell alternative] — [spell name], cost [slot level]
4. [Patience alternative] — [time investment], no check

### Hazards
- [Hazard 1]: [activation], [effect]
- [Hazard 2]: [activation], [effect]

### Partial Success Outcomes
[What the PCs learn or gain even on partial failure — never let
failure be informationally empty]

### Failure Outcomes
- [Outcome 1]: time lost, damage
- [Outcome 2]: alert enemies, alternative encounter triggered
- [Outcome 3]: take a worse path; new exploration encounter

### Discovery Payoff
[What the PCs see / feel / gain on success — sensory and narrative]
```

### 6. Common Exploration Encounter Subtypes

#### The Climb / Traverse

A physical obstacle: cliff, chasm, river, collapsed bridge. Tests
Athletics or Acrobatics; spell alternatives are climbing, jumping,
gas, fly.

#### The Maze / Labyrinth

Navigation through complex paths. Tests Survival, Investigation, or
memory. Spell alternatives are scrying, divinations, teleportation
to known locations.

#### The Sealed Chamber

A space with a hidden entry. Tests Perception and Investigation.
Spell alternatives are detect magic, knock, find traps. Time
alternative is exhaustive search.

#### The Stalking Predator

The party must avoid being detected by a roaming threat. Tests
Stealth, Perception (to spot the predator first), Survival (to
read tracks). Failure triggers a combat encounter — design that
encounter as a follow-up.

#### The Ancient Library

Decoding ancient texts, paintings, or relics. Tests Investigation,
Arcana, History, Religion. Reveals lore and clues. Spell alternatives
are comprehend languages, legend lore, divinations.

---

## Part III — Combining Social and Exploration

Some encounters blend social and exploration. Three patterns:

### Social-Driven Exploration

The party must convince an NPC to *lead them* through an unknown
area. The exploration challenge is gated by social success first.

Example: convince the dragon's former mate to lead you through the
mountain's hidden tunnels.

### Exploration-Driven Social

The party finds something during exploration that changes a social
encounter. The exploration is what creates social leverage.

Example: searching a noble's library reveals love letters; these
become leverage in the later negotiation.

### Hybrid Resolution

The encounter has both a social path and an exploration path to
the same goal. The party picks based on their strengths.

Example: get into the sealed temple by (a) convincing the priest
to open it, or (b) finding the hidden side passage.

---

## Part IV — Encounter Memory and Engagement

### Why social and exploration encounters fail at the table

Combat encounters have built-in stakes (PC death is possible) and
built-in tension (initiative, damage, save rolls). Social and
exploration encounters have to *manufacture* stakes and tension.

The most common reason these encounters fail:

- **Stakes are too low.** "Convince the merchant to sell you the
  goods" without consequences for failure becomes a roll-once-and-move-on.
  Add: the merchant has limited stock; rivals are bidding; the goods
  have moral cost to acquire.
- **Resolution is too fast.** A 30-second roll resolution. Add
  multiple beats: the merchant has a wife who hates outsiders; she
  intervenes after the first persuasion attempt; the merchant's
  guard is suspicious.
- **No alternative paths.** The PCs realize they need persuasion
  and the rogue is mute. Provide skill alternatives, spell
  alternatives, or patience alternatives.
- **No payoff variation.** Success and failure feel similar. Make
  success feel *won*; make failure leave traces that affect future
  encounters.

### Designing engagement

- **Multiple beats:** social and exploration encounters should
  produce *3–5 distinct moments* of player attention, not a single
  check.
- **Branching outcomes:** the encounter's resolution shapes the next
  encounter or the campaign's direction.
- **Memorable details:** an NPC's tic, a specific quote, a vivid
  environmental feature. Players remember encounters by their
  texture.
- **Cost to engage:** every check, every minute, every spell slot
  spent has cost. Don't make engagement free.

---

## Part V — Common Pitfalls

### Social pitfall: "One Roll to Rule Them All"

A single Persuasion check resolves the whole encounter. The
encounter becomes a roll-vs-DC exchange, not a roleplay scene.

**Fix:** require multiple checks or beats. Build the encounter as a
sequence of escalating reveals.

### Exploration pitfall: "Skill Check Tax"

Every step of the journey requires a Survival roll, but the rolls
have no narrative weight. The party rolls dice for no reason.

**Fix:** reserve checks for moments where failure has real
consequences. Replace some checks with passive scores or with
investigation that *informs* rather than gates.

### Social pitfall: "The NPC Has No Goal"

The PCs ask the NPC for something, and the NPC has nothing they
want in return. Negotiation collapses into "yes / no."

**Fix:** every NPC in a social encounter must want something — even
if it's just "want to be left alone." That want becomes leverage.

### Exploration pitfall: "All Paths Lead to the Same Place"

The exploration "challenge" has three skill paths, but all three
arrive at the same outcome. The choice is illusory.

**Fix:** different paths produce different outcomes — different
information, different costs, different alerts to enemies. Make the
choice matter.
