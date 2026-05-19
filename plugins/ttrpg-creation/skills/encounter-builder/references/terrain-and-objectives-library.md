# Terrain and Objectives Library

Patterns for combat-encounter terrain (cover, elevation, hazards,
points of interest) and alternative-objective patterns (capture,
rescue, escape, protection, time pressure, negotiation,
exfiltration).

A combat encounter without terrain interest plays in an empty 30×30
square. A combat encounter without alternative objectives reduces
every fight to "kill everything." Both shortcuts cost the encounter
its memory.

---

## 1. Terrain Pattern: Cover

Cover gives positioning meaning. PCs and monsters can break line of
sight, gain AC bonuses, or interrupt area-effect spells.

### Cover types

| Type | Mechanical effect | Examples |
|---|---|---|
| Half cover | +2 AC, +2 Dex saves | Low wall, large furniture, dense crowd |
| Three-quarters cover | +5 AC, +5 Dex saves | Arrow slit, partial wall, narrow door |
| Full cover | Can't be targeted directly | Full wall, closed door, behind a corner |

### Cover-rich layouts

- **Pillared hall:** rows of columns provide half cover throughout;
  movement around columns is the tactical game
- **Ruined courtyard:** half-collapsed walls give three-quarters
  cover at intervals
- **Forest clearing:** trees provide three-quarters cover; PCs and
  enemies maneuver to flank
- **Crowded marketplace:** stalls and crates give half cover; ranged
  attackers must move to maintain line of sight

### Cover design discipline

- At least 2–3 cover features per 30×30 ft. of combat space
- Cover should be **breakable / movable** in some cases (a crate
  can be tipped, a wall has a weak section)
- Avoid making cover too convenient — a column that conveniently
  blocks the wizard from being seen by 4 enemies is poor design

---

## 2. Terrain Pattern: Elevation

Height advantage is a powerful tactical lever in 5e: +5% to hit
ranged attacks (advantage on attacks from above per some interpretations,
or just the practical benefit of line-of-sight).

### Elevation types

| Type | Tactical effect |
|---|---|
| Low ledge (5–10 ft.) | Climb action required; range advantage |
| Mid ledge (10–30 ft.) | Climbing requires checks; ranged attackers exploit |
| High platform (30+ ft.) | Significant climb investment; flying enemies dominate |
| Pit / drop (below party level) | Restraint, falling damage, isolation |
| Multi-tier (stairs, ladders) | Movement-cost variations |

### Elevation-rich layouts

- **Cathedral with balcony:** ground-floor combat + archers on
  balcony 20 ft. up
- **Cliff face:** combat occurs on rock outcropping; characters can
  be pushed off
- **Multi-level dungeon room:** stairs, pit, raised dais — three
  distinct elevations in one space
- **Rooftop chase / fight:** combat occurs across rooftops with
  drops between

### Elevation design discipline

- Elevation rewards positioning AND penalizes positioning errors
- Don't make all elevations identical — vary height and access cost
- Consider what flying creatures do; if monsters fly, the elevation
  question changes

---

## 3. Terrain Pattern: Hazards

Environmental dangers that impose damage or conditions.

### Hazard types

| Hazard | Effect | Activation |
|---|---|---|
| Fire (open flame) | 1d6 to 3d6 fire damage on contact | Move into the square |
| Spreading fire | 1d6+ damage, spreads each round | Initiative count 20 |
| Acid pool | 2d6 acid + ongoing 1d4 acid until cleaned | Standing in pool |
| Lightning rod / arcane field | 2d6 lightning on triggered conditions | Triggered |
| Cold zone | Constitution save or exhaustion | Spend X rounds in zone |
| Magical zone (silence, antimagic) | Suppresses spellcasting | Inside the zone |
| Collapsing terrain | Dex save or fall through floor | Triggered or per-turn |
| Quicksand / mud | Restraint, Strength check to escape | Move into the square |
| Drowning water | Suffocation rules engage | Submerged |
| Toxic gas | 1d8+ poison damage, poisoned condition | Inside gas cloud |

### Hazard placement principles

- **Hazards should be visible** before combat starts (the PCs see
  the fire, see the pit, see the magical glow). Hidden hazards
  feel cheap.
- **Hazards apply to all sides** — monsters can also fall in pits,
  burn in fire, be silenced in antimagic. Hazards that only hurt
  PCs feel unfair.
- **Hazards interact with the encounter narrative** — fire in a
  burning library; acid in an alchemist's workshop; cold in a
  northern tomb.
- **One major hazard per encounter** typically; multiple hazards
  overwhelm.

### Hazard scaling by tier

| Party tier | Hazard damage |
|---|---|
| Tier 1 (1–4) | 1d6 to 2d6 |
| Tier 2 (5–10) | 2d6 to 4d6 |
| Tier 3 (11–16) | 4d6 to 8d6 |
| Tier 4 (17–20) | 8d6 to 12d6+ |

---

## 4. Terrain Pattern: Points of Interest

Things that can be *interacted with* mid-combat, beyond movement
and attacks.

### Interactive feature types

| Feature | Action cost | Effect |
|---|---|---|
| Lever / pulley | Action | Opens door, drops portcullis, lowers chandelier |
| Brazier / fire source | Action | Ignites weapon for 1d6 fire damage 1 turn |
| Altar / shrine | Action + religious check | Bless an ally (advantage on save), curse enemy |
| Lever-activated trap | Bonus action | Triggers a built-in trap on enemies |
| Symbol / glyph | Investigation check | Disables magical wards |
| Spell-storing item (one-charge) | Action | Releases a stored spell |
| Object (statue, painting) | Action | Pushes onto an enemy (Dex save or take damage) |
| Lighting source | Bonus action | Extinguishes lighting (everyone disadvantage) |
| Sound source (bell, horn) | Bonus action | Summons reinforcements or alerts witnesses |

### Interactive feature design

- Each feature gives the players a *choice* — use it now vs save
  it; sacrifice an action for terrain advantage.
- Features should be **dangerous if misused** — a brazier ignites
  weapons but also drops embers; a chandelier crushes whoever's
  underneath including allies who got out of the way too slowly.
- 2–3 interactive features per combat is the sweet spot.

---

## 5. Composite Terrain Layouts

Putting cover + elevation + hazards + points of interest together.
Five archetypal layouts:

### Layout: The Ruined Hall

- **Cover:** broken columns providing half cover at intervals
- **Elevation:** a raised dais at the back (5 ft. up); a collapsed
  section drops to 10 ft. below floor
- **Hazard:** a spreading fire from a fallen brazier (3d6 fire,
  expands 5 ft. each round)
- **Points of interest:** a damaged statue (can be pushed, Dex save
  6d6); an altar (action to cast bless on one ally 1/encounter)

### Layout: The Cliff Edge

- **Cover:** rock outcroppings provide three-quarters cover at
  ridge level
- **Elevation:** the path is 10 ft. wide on a 200 ft. drop; ranged
  attackers fire from above
- **Hazard:** the drop (fall damage 20d6 to base, but a 10-ft.
  ledge halfway down catches at 10d6); strong wind imposes
  disadvantage on ranged attacks
- **Points of interest:** loose boulders (action to push, Dex save
  4d6 + prone)

### Layout: The Burning Library

- **Cover:** bookshelves (half cover); some are toppled (full cover
  for one side)
- **Elevation:** ladders to upper gallery (10 ft. up); the gallery
  is unstable
- **Hazard:** fire spreading from books (1d6 fire on contact, 3d6
  if standing in fire); smoke imposing disadvantage on ranged
  attacks at long range; structural collapse triggered at round 5
- **Points of interest:** a magical book on a pedestal (releasing
  it casts dispel magic 1/encounter); a fire-control rune (DC 15
  Arcana to activate, halts spread)

### Layout: The Sewer Junction

- **Cover:** pipes and culverts (three-quarters cover for prone
  characters)
- **Elevation:** raised walkway 5 ft. above sewage; main flow at
  ground level
- **Hazard:** sewage water (move at half speed, Constitution save
  or contract disease at end of encounter); rusted spikes
  along walls
- **Points of interest:** sewer grate (Strength to lift, drops to
  lower level); flickering torch (extinguishing it darkens area
  to dim light)

### Layout: The Crowded Marketplace

- **Cover:** stalls and crates everywhere (half cover throughout)
- **Elevation:** flat terrain primarily; some second-story windows
  (10 ft. up)
- **Hazard:** crowd disadvantages (movement at half speed in crowd;
  bystanders panic and provide chaos); collateral damage rules
  apply to area attacks
- **Points of interest:** stall canopy (can be cut to drop on
  enemies, Dex save 2d6 + restrained); peddler's wagons (push to
  block paths)

---

## 6. Alternative Objectives — Beyond TPK

Every encounter should have at least one alternative objective.
Eight common patterns:

### Pattern A: Capture

The party must defeat enemies *without killing them all*. Often:
take the leader alive, capture a specific enemy for interrogation,
preserve the enemy as a hostage.

**Mechanical implementation:**
- Track non-lethal damage separately (or treat all reductions to 0
  HP as unconscious if PCs declare)
- A "capture success" requires the target to be at 0 HP without
  having taken a death save failure
- Magical capture options (sleep, hold person) become highly
  valuable

### Pattern B: Rescue

Save a captive / hostage from harm. The captive is in the encounter
space but has limited or no autonomy.

**Mechanical implementation:**
- The captive has HP and can be killed by enemies before the party
  reaches them
- The captive may be bound, blindfolded, or magically restrained
- Reaching the captive costs movement and turn investment
- Failure state: captive dies → emotional and narrative cost

### Pattern C: Escape

The party's goal is to *leave* the encounter area, not defeat
enemies. Often used when the encounter is too tough or when stealth
is the intent.

**Mechanical implementation:**
- Define an escape threshold (reach a specific square, exit a
  building, cross a boundary)
- Pursuers continue if PCs flee — chase encounter rules engage
- Spell slots for movement (misty step, dimension door, fly) become
  encounter-defining

### Pattern D: Protection

The party must keep someone or something alive. The protected
entity is at risk; the encounter is "you vs the clock."

**Mechanical implementation:**
- The protected entity has HP and limited mobility
- Enemies prioritize the protected entity (rules: they target
  protected on initiative tie; they ignore PC threats to push for
  the protected; they move to ignore PC interception)
- Failure state: protected dies → encounter is over with bad
  consequence

### Pattern E: Time Pressure

The party must accomplish something *fast* — disable a ritual,
reach a location, prevent an event. Combat is the obstacle, not
the goal.

**Mechanical implementation:**
- Define round count: at round X, [bad thing] happens
- The party can spend turns on combat OR on the objective; choose
- Often combined with Capture, Rescue, or Protection

### Pattern F: Negotiation

The encounter can end in dialogue if the party plays it right.
Combat is the default, but social pressure can shift outcome.

**Mechanical implementation:**
- Enemies have a "willingness to negotiate" threshold (e.g.,
  "If reduced to 25% HP or less, the leader considers terms")
- Specific demonstrations or offers shift attitude (intimidating
  display, presenting evidence, naming an ally)
- Combat ends when negotiation succeeds AND both sides accept
  terms

### Pattern G: Exfiltration

The party has obtained something and now must *leave with it*.
Differs from Escape in that the *what they're taking* is the
encounter focus.

**Mechanical implementation:**
- The stolen item / freed prisoner / sacred relic has weight or
  encumbrance properties
- Carrying the item slows movement or restricts options
- Enemies may try to recapture the item rather than kill PCs
- Failure: PC drops the item → enemies recover

### Pattern H: Information Gathering

The party's goal is to learn something specific from the encounter
— a name, a location, a ritual word, a face. Combat may be
incidental.

**Mechanical implementation:**
- Define what knowledge is gained at each success state
- Capture is often required (the enemy is the source of info)
- Failure: enemies die before talking, OR PCs leave with wrong info

---

## 7. Multi-Objective Encounters

Most strong encounters layer 2+ objectives:

### Example: The Hostage Tower

- **Primary:** Rescue the kidnapped noble from the cult
- **Secondary:** Capture the cult leader for interrogation
- **Time pressure:** The ritual completes at round 8

The party can succeed at one objective, multiple, or all three.
Rescue is the most narrative-essential. Capture is a stretch goal
that opens later plot. Time pressure is the constraint.

### Example: The Forbidden Market

- **Primary:** Exfiltrate with the sealed package
- **Avoid:** Civilian casualties (each civilian death penalizes a
  faction relationship)
- **Optional:** Identify the mole supplying the cultists (information
  gathering)

The party balances speed (escape) with collateral damage (civilians)
and depth (information).

### Combining objectives — design principles

- **At most 3 objectives per encounter.** More than that becomes
  cognitive overhead at the table.
- **Make objectives competitive.** Achieving objective A makes
  objective B harder.
- **Make objectives optional.** The party can succeed by clearing
  just the primary; secondaries are stretch goals.
- **Make objectives memorable.** Players remember the encounter
  by the alternative objectives, not by the kill count.

---

## 8. Failure States — Beyond TPK

The opposite of "alternative victory" is "graduated failure." Not
every loss is a TPK.

### Failure types

- **Survived but failed:** PCs lived; the objective failed. The
  campaign continues with a setback.
- **Captured:** PCs are subdued, taken prisoner. New encounter:
  escape from captivity.
- **Forced retreat:** PCs are alive but driven from the area. The
  encounter location is now controlled by the enemy.
- **Pyrrhic victory:** PCs won but at significant cost (PC death,
  major resource loss, NPC ally killed, item destroyed).
- **Compromise:** PCs got partial success — captured one enemy but
  not the leader; rescued the hostage but they're injured.

### Designing graduated failures

- Specify what each failure state *looks like* in the encounter
  document
- Provide read-aloud for each failure state so the GM can deliver
  it cleanly at the table
- Connect failures to *next-step direction* — "On capture, the
  party wakes in [location]; the campaign's next encounter is
  prison-break"

---

## 9. Terrain and Objectives Combined — Encounter Recipe

The full combat-encounter design recipe:

1. **Pick an XP budget** (see `xp-budget-and-difficulty-2024.md`)
2. **Pick a terrain layout** (Section 5 of this file, or build
   custom from Sections 1–4)
3. **Pick a primary objective** (TPK or one of Patterns A–H from
   Section 6)
4. **Pick 1–2 secondary objectives** (Pattern from Section 6)
5. **Pick a time pressure** (none / soft / hard)
6. **Layer environmental detail** for atmosphere
7. **Document failure states** (Section 8)
8. **Validate against `xp-budget-and-difficulty-2024.md` checklist**

A well-designed encounter has all of these elements without feeling
overwrought. Restraint is part of the craft.
