# Encounter Types — D&D 5e 2024

The five encounter types the rules formally support, with their
defining features, primary mechanics, common pitfalls, and output
emphasis. Plus the decision tree for picking a type when the brief
is ambiguous.

---

## 1. Combat Encounter

Tactical confrontation resolved primarily through HP, save mechanics,
and round-by-round action economy.

### Defining features

- Initiative is rolled (or pre-calculated by the encounter builder)
- Damage and HP track progress toward resolution
- Saving throws and conditions impose ongoing effects
- Action economy (action / bonus action / reaction) shapes
  round-by-round play
- Spatial positioning matters (cover, elevation, line of sight,
  range)

### Primary mechanics

- **XP budget calibration** — see
  `xp-budget-and-difficulty-2024.md`
- **Monster selection** — within XP budget, with role distribution
- **Multiattack / Recharge / Legendary actions** govern enemy
  output
- **Damage types** interact with resistances and vulnerabilities
- **Condition application** (frightened, restrained, charmed,
  paralyzed, etc.) shifts party tactics
- **Terrain and hazards** add environmental damage and tactical
  constraint

### Common pitfalls

- **DPR overload:** a CR-appropriate monster with too many attacks
  drops a single PC per round, turning the fight into a roll-for-stabilize
  exercise.
- **Solo boss vs party action economy:** one CR 11 monster against
  4 PCs at level 7 produces a feel-bad fight because the boss is
  stunlocked while the party fires 4-to-1 actions per round.
  Solution: add legendary actions, add minions, or escalate the
  monster's complexity.
- **No alternate win conditions:** every combat is "reduce enemies
  to 0 HP." Adds combat fatigue across a session of 4+ fights.
  Solution: every other combat should have an alternative objective.
- **Terrain ignored:** the fight occurs in a "10x10 empty room"
  with no environmental features. Solution: every combat encounter
  needs at least 2 tactical features (cover, elevation, hazard).
- **Boss fight with no escalation:** the boss does the same thing
  every turn from full HP to 0. Solution: at 50% HP, the boss
  changes behavior — second phase, lair activation, new ability,
  retreat path.

### Output emphasis

For combat, the encounter document must emphasize:

- Pre-calculated initiative (or initiative-roll-once protocol)
- Monster placement on map
- Round 1 setup (positions, environmental cues)
- Round 2+ adaptive triggers
- Resolution branches that differ meaningfully

---

## 2. Social Encounter

Negotiation, persuasion, interrogation, debate, or any interpersonal
challenge resolved primarily through dialogue and ability checks.

### Defining features

- Initiative is typically not used; conversation flows
- Attitude ladder governs success (Hostile → Indifferent → Friendly
  → Helpful)
- Ability checks (Persuasion, Deception, Intimidation, Insight) drive
  outcomes
- Information exchange is the primary "damage type"
- NPCs have motivations and leverage — not HP

### Primary mechanics

- **NPC attitude** as a tracked state across the encounter
- **Persuasion DCs** scaled by stakes and NPC investment
- **Levers** that shift attitude (evidence presented, social
  reputation, favors owed)
- **Tells** that the PCs can read for advantage (Insight against the
  NPC's Deception)
- **Walk-away thresholds** — what causes the NPC to abandon the
  conversation
- **Information bleed** — even on failed checks, partial info leaks

### Common pitfalls

- **One-roll resolution:** the player rolls Persuasion DC 15, hits
  it, and the social encounter is over in 30 seconds. Solution:
  social encounters should have multiple beats — at minimum 3
  meaningful exchanges.
- **NPC has no goal:** if the NPC doesn't want anything, the PCs
  can't negotiate. Define what the NPC wants before the PCs
  arrive.
- **Single-axis DC:** every persuasion check is "DC 15." Solution:
  scale DCs by attitude tier and by what the PCs offer.
- **No fail-state:** if "failure" is just "you don't get what you
  wanted," the stakes are too low. Add consequences: the NPC
  becomes hostile, the NPC summons reinforcements, the NPC reports
  to a rival.
- **No information bleed:** failing the persuasion means the PCs
  learn nothing. Solution: even on failure, the NPC reveals
  something (an emotional reaction, a slip of the tongue, a
  decision to leave).

### Output emphasis

For social encounters, the document must emphasize:

- NPC's starting attitude
- 2–4 levers the PCs can play (and what each costs in checks or
  resources)
- The information graph (what NPC knows, what they reveal at each
  tier)
- Multiple outcome branches (full success, partial success, failure,
  hostile turn)
- The "out" — if negotiations break down, what does the NPC do?

---

## 3. Exploration Encounter

Traversal, navigation, environmental discovery, or any spatial /
temporal challenge resolved primarily through skill checks and
resource management.

### Defining features

- Time and space are the primary axes
- Ability checks (Survival, Perception, Investigation, Athletics,
  Acrobatics, Nature) drive progress
- Environmental hazards impose damage or conditions
- Discovery (finding a hidden passage, identifying a relic, reading
  a map) is the primary reward
- Failure typically costs time, resources, or HP

### Primary mechanics

- **Skill DCs** for navigation challenges (Survival to track,
  Athletics to climb, Investigation to find concealed)
- **Environmental hazards** (cold damage, falling, drowning,
  suffocation, exhaustion)
- **Resource consumption** (rations, water, torches, spell slots
  for utility magic)
- **Multi-path design** (skill A or skill B both work, with
  different costs)
- **Partial discovery** (failing the primary check reveals a clue
  toward an alternative path)

### Common pitfalls

- **One skill, one check:** the dungeon is gated behind a single
  Perception DC 15 roll. Solution: provide 2–3 ways to discover
  the same information, each with different costs.
- **Skill check tax:** every step of the journey requires a check,
  but the checks have no narrative weight. Solution: reserve
  checks for moments where failure has consequences.
- **No environmental memory:** the party crosses the burning library
  but the burning library has no effect on later scenes. Solution:
  exploration encounters should leave traces (HP loss, items
  damaged, time pressure intensified, NPC reactions).
- **Failure spiral:** failing the first check makes the rest of the
  encounter impossible. Solution: failures should redirect, not
  block.

### Output emphasis

For exploration encounters, the document must emphasize:

- The environment in vivid sensory terms
- The skill DCs available (multiple paths to success)
- The hazards and their costs
- The discovery payoff (what success reveals)
- Multiple endings based on which path the party took

---

## 4. Chase Encounter

Pursuit with directional movement, complications, and a goal-distance
or goal-time metric. Resolved through movement, skill checks, and
resource expenditure.

### Defining features

- Directional movement on an abstracted scale (rounds, segments,
  zones)
- Lead distance is the tracked variable
- Complications interrupt the chase each round
- Speed and Dexterity are the primary stats
- Resolution = close to within X distance / escape to X distance

### Primary mechanics

- **Lead tracking** (the quarry's lead in feet or segments)
- **Movement allocations** per round
- **Complication rolls** every round or every other round
- **Dash actions** and exhaustion tracking
- **Terrain transitions** — each terrain has different complications
- **Witnesses and collateral** for urban chases

### Common pitfalls

- **No tactical decisions:** the chase is "everyone Dashes" for 6
  rounds. Solution: complications force choices — do you stop to
  help the bystander or push through?
- **Speed advantage trivializes:** if the quarry has +10 ft. speed,
  they always escape. Solution: terrain transitions reset the
  speed advantage; some terrains favor the slow.
- **Single failure ends:** one failed Athletics check = caught.
  Solution: failure costs an action or lead distance, not the
  whole chase.
- **Featureless route:** "you chase through the city" without
  defining the route. Solution: name 3–5 distinct segments with
  different complication tables.

### Output emphasis

For chase encounters, the document must emphasize:

- Initial lead distance
- The route as named segments (3–5)
- Per-segment complication tables (3–5 complications per segment)
- Catch and escape thresholds (numerical)
- The consequences of catching / escaping (not just "you escape" —
  but "you escape into the unfriendly territory of the Iron Rats
  guild")

---

## 5. Downtime Encounter

Between-adventure activities that occur over days, weeks, or months
of in-fiction time. Resolved through time investment, gold cost, and
success metrics.

### Defining features

- Time is measured in days / weeks / months
- Gold cost or resource cost is typically present
- Single checks OR cumulative successes determine outcome
- The world continues to evolve during downtime (rival NPCs act,
  factions move, opportunities close)
- The PC's identity and capabilities can shift (training, magical
  research, relationship building)

### Primary mechanics

- **Activity menu** (research, crafting, training, carousing,
  building influence, scribing scrolls, performing services)
- **Time cost** in days or weeks per activity
- **Gold cost** in lifestyle expenses + activity costs
- **Success metric** (single check, cumulative weekly progress,
  resource trade-off)
- **Side effects** — successful activities trigger consequences
  beyond the primary reward

### Common pitfalls

- **No opportunity cost:** the PC can do all the downtime
  activities simultaneously. Solution: time is the binding
  constraint; force trade-offs.
- **No world reaction:** the PC trains for 3 weeks and the world
  is unchanged when they return. Solution: every downtime week
  produces a small world-change (NPC X moved, faction Y started
  recruiting, etc.).
- **Single-check resolution:** "Roll Intelligence (Investigation),
  on a 15+ you finish your research." Solution: research takes
  weeks of progress; mistakes and breakthroughs along the way.
- **No narrative weight:** the downtime is mechanical. Solution:
  every downtime activity should have a 1-paragraph narrative
  outcome.

### Output emphasis

For downtime encounters, the document must emphasize:

- The activity being undertaken
- Time and gold cost
- Success metric (single, cumulative, or trade-off)
- 3–4 outcome branches (success / partial / failure / unintended
  side effect)
- The world-reaction (what happens elsewhere while the PC is
  doing this)
- Narrative payoff: a short read-aloud or summary that captures
  the experience

---

## 6. Type Selection — Decision Tree

When the brief is ambiguous, use this decision tree:

1. **Is HP / damage the primary stake?**
   - Yes → **Combat**
   - No → continue

2. **Is the encounter resolved through dialogue and persuasion?**
   - Yes → **Social**
   - No → continue

3. **Is the encounter primarily about movement toward / away from
   a goal?**
   - Yes → **Chase**
   - No → continue

4. **Does the encounter span days or longer in fiction time?**
   - Yes → **Downtime**
   - No → continue

5. **Default → Exploration** (skill-check-based, spatial / temporal
   challenge)

If the brief implies a hybrid, pick the primary and design the
secondary as a branch or alternative path.

---

## 7. Hybrid Encounters

Real campaigns often produce hybrid scenes that don't fit cleanly
into one type. Common hybrids:

### Combat → Social

A fight that the party can talk down. Build as Combat with a Social
alternative win condition. The social conversion requires:
- Demonstrating power (some damage dealt or maintained pressure)
- A persuasion check at a DC scaled by enemy commitment
- Acceptable terms offered (give us X, leave the area, etc.)

### Social → Combat

A negotiation that breaks down. Build as Social with a Combat fallout
state. If negotiations fail, the social participants become combat
participants — provide initiative order and stat blocks ready.

### Exploration → Combat

A dungeon room with both an environmental puzzle AND monsters who
defend it. Build as Combat with the exploration challenge as a
terrain feature.

### Chase → Combat

The quarry turns to fight when cornered. Build as Chase with the
combat encounter prepped for round X (when caught).

### Downtime → Crisis

A weekly downtime activity interrupted by an emergency. Build as
Downtime with the interruption as a separate encounter to drop in
at the chosen moment.

When the brief implies a hybrid, design **both** elements but mark
the primary type for the calibration and output emphasis.

---

## 8. Common Pitfalls Across All Types

### Pitfall: No stakes

If the encounter doesn't matter, neither will the resolution.
Every encounter needs:
- What the party loses on failure
- What the party gains on success
- What the world changes either way

### Pitfall: One-axis design

If success or failure pivots on a single check, the encounter is
fragile. Design at least two paths to success, two failure states,
and one unexpected outcome.

### Pitfall: GM fatigue

If the encounter requires the GM to invent 6 things on the fly at
the table, it's not table-ready. Pre-resolve as much as possible
in the document.

### Pitfall: Player passivity

If the encounter doesn't give the players choices, they won't be
invested. Every encounter should have 3+ meaningful decision points.

### Pitfall: No memory hook

If the encounter is mechanically fine but forgettable, the players
won't remember it next session. Each encounter needs one memorable
detail — a vivid NPC line, a strange environmental feature, an
unexpected twist, a haunting visual.
