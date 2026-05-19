---
name: encounter-builder
description: >
  Build single encounters for D&D 5e 2024 across all five types: Combat, Social,
  Exploration, Chase, and Downtime. For each: calibrate difficulty against the
  specific party (size, level, composition), design terrain and objectives
  including alternative win/loss conditions, and produce table-ready
  deliverables (read-aloud for entrance and resolution + GM cheat sheet with
  pre-calculated initiative or key DCs). Use on "build an encounter", "balance
  this combat", "design a social encounter", "create a chase", "downtime
  scene", "encounter for 4 PCs level 5", "calibrate XP budget", "fabrique-moi
  une rencontre", "design un combat pour mon groupe", "rencontre sociale avec
  enjeux", "poursuite", "scène de tension non-combat", "encounter with
  objectives beyond TPK", "alternative win conditions", "encounter terrain
  with hazards". Boundary: this skill produces ONE encounter at a time. For
  scenario-length chains of linked scenes (three-clue rule, node-based
  structure) use scenario-writer. For monster stat blocks and per-monster
  tactics use monster-creator. For random encounter tables use
  random-encounter-creator or urban-d100-encounters. This skill focuses on
  static calibration and table-ready delivery, not runtime AI.
---

# Encounter Builder

Build single encounters for D&D 5e 2024, table-ready, across the five
encounter types the rules support: Combat, Social, Exploration, Chase, and
Downtime. The output is what a publisher's encounter designer would deliver
for a scenario's key scene, or what a busy GM would prepare the night before
a session.

The skill calibrates difficulty against the specific party, designs terrain
and objectives that go beyond TPK-vs-kill-all, and produces table-ready
deliverables — entrance read-aloud, GM cheat sheet, and resolution branches.

---

## Boundary with Other Skills

This skill produces **one encounter at a time**, focused on calibration and
table delivery. The frontiers with adjacent skills:

| Brief | Use |
|---|---|
| "I need 6 linked scenes for a one-shot" | `scenario-writer` (scenario chain) |
| "I need this one fight balanced and ready" | this skill |
| "I need the gnoll stat block" | `monster-creator` |
| "I need the gnolls to behave intelligently in combat" | `monster-creator` (tactics section) |
| "I need a d100 table of urban encounters" | `urban-d100-encounters` |
| "I need a one-shot adventure" | `scenario-writer` |
| "I need the read-aloud for this dungeon room" | `read-aloud-crafter` |
| "I need this combat's entrance read-aloud" | this skill (delivered with the encounter) |

**Rule of thumb:** if the brief is about *a single scene that has a beginning
and an end*, it belongs here. If the brief is about *multiple scenes that
form an arc*, it's `scenario-writer`. If the brief is about *a creature in
isolation*, it's `monster-creator`.

---

## Before You Begin

1. **Identify the encounter type.** One of five:
   - **Combat** — tactical confrontation that resolves in HP/save
     mechanics
   - **Social** — negotiation, persuasion, interrogation, debate
   - **Exploration** — traversal, navigation, environmental discovery
   - **Chase** — pursuit with directional movement and complications
   - **Downtime** — between-adventure activities with time-based outcomes

   If the encounter is hybrid (a combat that can be avoided through
   negotiation; a chase that becomes a fight), pick the *primary* type and
   build the secondary as a branch.

2. **Identify the party.** Get the minimum viable data:
   - **Size** (number of PCs)
   - **Level** (and party-level if mixed; use the average)
   - **Composition** (rough class mix: 2 martial + 2 caster typical; all
     casters and all martial are edge cases that change difficulty)

   If the user doesn't specify, ask. Difficulty calibration without party
   data is guesswork.

3. **Determine the difficulty target.** D&D 5e 2024 uses three tiers:
   - **Low** — easy encounter; party uses ~25% of daily resources
   - **Moderate** — standard encounter; party uses ~50% of daily resources
   - **High** — hard encounter; party uses ~75% of daily resources, may
     suffer significant losses; risk of PC death exists

   "Deadly" from 2014 is now subsumed within High (with notes about extra
   challenge). Load `references/xp-budget-and-difficulty-2024.md` for the
   precise budget thresholds.

4. **Determine the narrative context.** What's happening, what's at stake,
   why is this encounter happening *now*?
   - Does the party expect it (planned confrontation) or stumble into it
     (ambush)?
   - What do the PCs lose if they fail? What do they gain if they succeed?
   - Are there witnesses, ongoing time pressure, or ambient stakes (a
     spreading fire, a captured ally, an approaching deadline)?

   Without narrative context, encounters become mechanical exercises rather
   than memorable scenes.

5. **Decide what type of victory matters.** Combat win conditions are not
   always "reduce enemies to 0 HP." Map to the encounter's narrative:
   - Defeat all enemies (default)
   - Capture / interrogate one specific enemy
   - Survive N rounds until reinforcements / escape
   - Rescue a captive
   - Recover an object
   - Force enemy surrender through damage threshold
   - Force enemy surrender through social pressure mid-combat

   Type-specific variants apply (social encounters have negotiation win,
   exploration has discovery win, chase has reaching the goal, downtime
   has completed activity).

If any of these is unclear, ask before designing. Building without these
inputs produces generic encounters.

---

## The Five-Step Build Workflow

Every encounter passes through five steps. The output combines them into a
table-ready document.

### Step 1 — Encounter Setup

- **Encounter name** (distinctive and evocative, not "Combat 3")
- **Type** (Combat / Social / Exploration / Chase / Downtime)
- **Party assumed** (size, level, composition)
- **Difficulty target** (Low / Moderate / High)
- **Stakes** (1–2 sentences: what's at risk on either side)
- **Narrative context** (1–3 sentences: where, when, why now)

### Step 2 — Calibration

Load `references/xp-budget-and-difficulty-2024.md`.

**For Combat encounters:**
- Calculate XP budget for the party at target difficulty
- Select monsters whose XP totals fit the budget
- Note encounter multiplier rules if applicable (DMG 2024 has
  simplified the 2014 multiplier system; see the reference for the
  current approach)
- Validate against monster role distribution (don't put 4 Brutes in
  one fight; mix roles for tactical interest)
- Confirm action economy parity (party turns vs enemy turns per
  round)

**For Social encounters:**
- Determine the NPC's starting attitude (Hostile / Indifferent /
  Friendly)
- Set initial DC for the desired persuasion outcome (typically
  scaled by level: 10 for low-stakes, 15 for standard, 20+ for
  high-stakes)
- Define what evidence or leverage shifts attitude (each lever
  reduces DC by 2–5)

**For Exploration encounters:**
- Identify the navigation/survival challenge type (traverse hazard,
  find concealed passage, recognize environmental danger)
- Set DCs for the relevant skills (Survival, Perception,
  Investigation, Athletics, Acrobatics)
- Determine consequences of failure (damage, lost time, alert
  enemies, take a worse path)

**For Chase encounters:**
- Choose the chase scale (street-level, district-level, regional)
- Determine pursuer and quarry initial positions (lead distance)
- Set the goal distance / duration (rounds until quarry escapes or
  is caught)
- Layer in complication frequency (every round, every other round)

**For Downtime encounters:**
- Identify the downtime activity (research, crafting, training,
  carousing, building influence)
- Set the time investment required (days, weeks)
- Set the gold investment if applicable
- Set the success metric (single check, accumulated successes,
  resource trade-off)

### Step 3 — Terrain and Setting

For all encounter types, the *physical setting* shapes how the encounter
plays. Load `references/terrain-and-objectives-library.md` for patterns.

**For Combat encounters, describe:**
- **Layout:** size of the engagement area, shape, key features
- **Cover and elevation:** where can PCs and enemies break line of
  sight, gain height advantage
- **Hazards:** environmental dangers (fire, drop, water, magical
  zones, traps)
- **Points of interest:** levers, doors, altars, brazier — things
  that can be interacted with mid-combat
- **Lighting:** bright / dim / dark, with implications for
  darkvision-having characters

Provide a numbered legend if a tactical map is implied. The output
should give a GM enough to draw a battlemap quickly.

**For Social encounters, describe:**
- **The space** (a throne room, a tavern back-room, a prison cell,
  a battlefield parley tent)
- **Who else is present** (allies, hostile witnesses, neutral
  observers)
- **Physical props** (the evidence the PCs brought, the document
  being signed, the corpse being discussed)
- **Implicit constraints** (the NPC can't leave a chair; the meeting
  is timed; weapons are forbidden)

**For Exploration encounters, describe:**
- **The environment** (cliff face, swamp at dusk, underground river,
  burning library)
- **Distances and orientations** (how far is the goal, in which
  direction)
- **Visible vs hidden features** (what the party sees first vs what
  requires investigation)

**For Chase encounters, describe:**
- **The route** (street network, sewer tunnels, forest paths,
  rooftop chains)
- **Terrain transitions** (open street → narrow alley → bridge →
  marketplace)
- **Each segment's complications** (1–3 obstacles per segment)

**For Downtime encounters, describe:**
- **The location** (workshop, library, training yard, social venue)
- **NPC contacts** present and relevant
- **Resources available** (tools, materials, references)

### Step 4 — Objectives and Outcomes

Define what success and failure look like, and (critical) what alternatives
exist beyond binary win/lose.

**For Combat encounters:**
- **Primary victory condition** (defeat enemies / survive / capture / etc.)
- **Alternative victory conditions** (force surrender via negotiation,
  achieve specific goal even if enemies aren't all defeated)
- **Failure conditions** (TPK; specific PC objective lost; secondary
  goal failed but PCs survive)
- **Escalation triggers** (round X reinforcements arrive; HP threshold
  reveals monster's second phase)
- **De-escalation possibilities** (enemy surrenders at < 20% HP; PCs
  can offer terms after demonstrating power)

**For Social encounters:**
- **Persuasion ladder** (Hostile → Indifferent → Friendly → Helpful
  → Allied) with what changes attitude per step
- **NPC walk-away threshold** (what causes the NPC to abandon the
  conversation entirely)
- **Compromise outcomes** (the PCs don't get full success but get
  something useful)
- **Information bleed** (even on failure, the NPC reveals some hint
  by accident)

**For Exploration encounters:**
- **Multiple paths** to the goal (skill A or skill B both work, with
  different costs)
- **Partial discovery** (failure reveals something useful, just not
  the primary goal)
- **Costs of routes** (faster route is more dangerous, safer route
  is slower)

**For Chase encounters:**
- **Catch / escape conditions** (close to within X spaces / open
  to X spaces gap)
- **Detour options** (the quarry can sacrifice speed for stealth,
  or vice versa)
- **Witness consequences** (chase through a market = collateral
  damage; chase through sewer = no witnesses but real dangers)

**For Downtime encounters:**
- **Success thresholds** (single check vs cumulative)
- **Resource costs** (gold, time, social capital)
- **Side effects** (success in carousing = info gained but enemy
  alerted; success in research = lead found but academic rival
  takes interest)

### Step 5 — Table-Ready Deliverables

The encounter must be playable from the document, not require the GM to
do additional prep at the table.

**Mandatory deliverables for every encounter:**

- **Entrance read-aloud** (1–2 paragraphs, 80–150 words). What the
  PCs see, hear, smell, feel as they enter. Sensory and immediate,
  not exposition-heavy. Load `references/read-aloud-protocols.md`
  for templates.

- **GM cheat sheet** (1 page maximum, scannable in 30 seconds at
  the table):
  - Initiative order pre-calculated (for combat) or attitude index
    (for social) or DC list (for exploration / chase / downtime)
  - Key reminders (a lair action that triggers on 20, an
    environmental hazard, the NPC's tell that the PCs can read
    for advantage)
  - Resolution branches (3–5 named outcomes the encounter can
    end on, with the next-step direction for each)

- **Resolution read-aloud options** (one per major outcome, 1
  paragraph each, 50–80 words). What the PCs see/feel as the
  encounter resolves.

---

## Output Format

Assemble the five steps into one document. Structure:

```markdown
# [Encounter Name]

**Type:** [Combat / Social / Exploration / Chase / Downtime]
**Party:** [N PCs at level L, composition]
**Difficulty:** [Low / Moderate / High]
**Stakes:** [What's at risk]

## Context

[1–3 sentences: where, when, why now.]

## Entrance — Read-Aloud

> [Read-aloud text, 1–2 paragraphs.]

## Calibration

[XP budget calculation OR DC scaffolding OR chase parameters OR
downtime metrics — depending on type.]

## Terrain / Setting

[Description of the physical space. Layout, cover, elevation,
hazards, points of interest, lighting (for combat) / participants,
props, constraints (for social) / etc.]

[Optional numbered legend if map is implied.]

## Objectives and Outcomes

### Primary Victory
[Description.]

### Alternative Victories
[Description.]

### Failure States
[Description.]

### Escalation / De-escalation Triggers
[Description.]

## GM Cheat Sheet

**Initiative / Attitude / DCs:** [pre-calculated or listed]
**Key Reminders:** [bulleted, 3–6 items]
**Resolution Branches:**
1. [Outcome 1] → [next step direction]
2. [Outcome 2] → [next step direction]
3. [Outcome 3] → [next step direction]
4. [Outcome 4 if applicable] → [next step direction]

## Resolution Read-Aloud

**On primary victory:**
> [1 paragraph.]

**On alternative victory:**
> [1 paragraph.]

**On failure (survived):**
> [1 paragraph.]

**On TPK / total failure:** (combat only)
> [1 paragraph.]
```

**Language:** Match the language of the user's brief. If the brief is
in French, write the entire encounter in French (including DC labels,
attitude tiers, etc.).

**Tone:** Practical, table-ready. The encounter is a tool, not a
short story. Read-aloud is evocative but precise; mechanics are
clear; resolution branches are *named* and *directed*.

---

## Type-Specific Protocols

Each encounter type follows the same 5-step workflow but with
type-specific protocols. Load the relevant reference file:

- **Combat:** `references/xp-budget-and-difficulty-2024.md` +
  `references/terrain-and-objectives-library.md`
- **Social:** `references/social-and-exploration-protocols.md`
- **Exploration:** `references/social-and-exploration-protocols.md`
- **Chase:** `references/chase-and-downtime-protocols.md`
- **Downtime:** `references/chase-and-downtime-protocols.md`

---

## Interaction with Other Skills

- **Multiple linked encounters** (a 4-hour scenario) → run
  `scenario-writer` for the chain, then this skill for individual key
  scenes that need extra polish.
- **Monster stat blocks** for the combat → run `monster-creator`
  before or after this skill; reference the monsters by name in the
  calibration section.
- **Monster runtime tactics** (round-by-round behavior) →
  `monster-creator` includes a "Running [Monster] at the Table"
  section; reference that, don't duplicate.
- **NPC personas** for social encounters → run `npc-creator` for the
  NPC's full character; this skill uses the NPC's persona to set
  attitude and levers.
- **Faction stakes** → run `faction-creator` for the org; this skill
  references faction context in stakes.
- **Settlement / dungeon context** → run
  `settlement-toolkit-creator`; this skill references the place in
  terrain.
- **Read-aloud polish** (the user wants more lyrical or specific
  read-aloud) → run `read-aloud-crafter` on the encounter's
  read-aloud sections; this skill produces functional read-aloud,
  read-aloud-crafter polishes for publication.
- **Pre-publication review** → run `ttrpg-supplement-reviewer` after
  designing for editorial validation.
- **Mechanical stress test** → run `ttrpg-playtest-orchestrator` for
  simulated play with 4–5 personas.
- **Cliché check** (this fight feels like every other dragon fight) →
  run `ttrpg-cliche-buster` on the concept before designing.

---

## Edge Cases

**Hybrid encounter (combat that can be talked down):** Build it as the
primary type (Combat if the default expectation is combat) and include
the secondary type's path as an Alternative Victory. Provide DCs and
attitude levers for the social path within the GM Cheat Sheet.

**Encounter at the wrong level for the party:** If the user's brief
implies a difficulty that exceeds the party's capacity (e.g., a CR 10
monster against level 3 PCs), build the encounter as requested but
flag the imbalance explicitly in the calibration section. Suggest
either: (a) reducing the threat, (b) adding alternative win paths so
the encounter doesn't require pure combat, or (c) running it as a
chase / escape encounter rather than combat.

**Encounter with no party data:** Ask. Building an encounter without
knowing the party is unreliable. The exception: a "generic" encounter
template for a published supplement; in that case, build for an
"average party of 4 at level X" and note the assumption.

**Encounter for adult content settings:** Standard mechanical content.
Adult layer (seductive social encounters, sensual exploration scenes,
intimate downtime activities) is added via Fantasy Vixens-specific
skills after this skill produces the baseline.

**Encounter that requires custom mechanics:** If the encounter calls
for unique subsystems (a specific puzzle, a magical trial, a custom
chase rule), build the core encounter and *flag* the subsystem
requirement. Custom subsystems are beyond the scope of this skill —
either inherit existing 5e systems (skill challenges, ability check
trees) or create the subsystem separately.

**Encounter that depends on previous encounter outcomes:** If the
brief is "the boss fight assuming the party rescued the prisoner in
the previous encounter," build the encounter with the assumption made
explicit. Note the dependency in the context section.

---

## Reference Files

Load these as needed — not all at once.

- `references/encounter-types-2024.md` — The five encounter types
  detailed: combat, social, exploration, chase, downtime. For each:
  defining features, primary mechanics, common pitfalls, output
  emphasis. The decision tree for picking a type when the brief is
  ambiguous.
- `references/xp-budget-and-difficulty-2024.md` — D&D 5e 2024
  difficulty thresholds (Low / Moderate / High) with XP budgets per
  PC by level. Monster XP table by CR. Group multiplier guidance.
  Adjustment for party composition (all-martial, all-caster mixes).
  Honest notes on the 2024 vs 2014 calibration changes.
- `references/terrain-and-objectives-library.md` — Combat-encounter
  terrain patterns (cover, elevation, hazards, points of interest)
  and alternative-objective patterns (capture, rescue, escape,
  protection, time pressure, negotiation, exfiltration).
- `references/social-and-exploration-protocols.md` — Social
  encounters: NPC attitude ladder, persuasion DCs, leverage system,
  walk-away thresholds. Exploration encounters: navigation
  challenges, perception/investigation gates, environmental hazards,
  multi-path design.
- `references/chase-and-downtime-protocols.md` — Chase encounters:
  DMG 2024 chase rules summary, complication tables by terrain,
  segment design. Downtime encounters: activities catalog, time and
  gold costs, success metrics, narrative side effects.
- `references/read-aloud-protocols.md` — Templates and patterns for
  encounter read-aloud: entrance hooks, sensory ladders, resolution
  branches. How to write read-aloud that supports rather than
  overrides the GM's voice.
