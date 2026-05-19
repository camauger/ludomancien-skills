---
name: dungeon-creator
description: >
  Create complete dungeons and adventure sites for D&D 5e 2024 — multi-room
  sites with room functions, encounter mix across the three pillars
  (combat / exploration / interaction), faction occupancy, traps, treasure
  placement, navigation logic and theme. Each dungeon ships with a numbered
  key, ASCII map sketch, GM-facing flow notes, and table-ready room entries.
  Covers 5-room dungeons (one-shot ready), small sites (10–15 rooms / one
  session), and full sites (16–25 rooms / multi-session). Use on "crée un
  donjon", "build a dungeon", "design a crypt", "temple ruin map", "tomb
  of X", "mine dungeon for level 4", "jaquaying this dungeon", "fabrique-moi
  un complexe souterrain", "donjon thématique", "5-room dungeon", "complexe
  pour 4 PJ niveau 6", "dungeon with factions", "sandbox dungeon". Boundary:
  this skill produces ONE dungeon as a site. For scenario-length narrative
  chains (3-act, three-clue redundancy, NPC web) wrapping the dungeon, use
  scenario-writer. For settlements (villages / towns / city districts) use
  settlement-toolkit-creator. For a single encounter inside a dungeon (one
  fight, one social scene, one chase) use encounter-builder. For monster
  stat blocks use monster-creator. For magic items found inside, use
  magic-item-creator. For random encounter tables to layer onto the dungeon,
  use random-encounter-creator. This skill produces the static site:
  geography, room functions, occupancy, hazards, treasure, theme — table-ready.
---

# Dungeon Creator

Create publication-ready dungeons and adventure sites for D&D 5e (2024 rules),
formatted as a numbered key with a navigable layout and a GM-facing flow.
The output is what a publisher's adventure-site designer would deliver for a
classic crawl, a one-shot site, or the dungeon module inside a larger
scenario.

The skill is structural *and* atmospheric: navigation logic and encounter
mix are non-negotiable, but a dungeon without a theme, a faction story,
and secrets is just a room sequence.

---

## Scope and Boundary

This skill covers **single dungeons / sites** at three scales:

| In scope | Out of scope |
|---|---|
| 5-room dungeons (one-shot, ~3 hours) | Mega-dungeons (50+ rooms, multi-level campaign sites — different scale, needs dedicated skill) |
| Small sites (10–15 rooms, one session) | Hex crawls, wilderness maps (use a wilderness skill once it exists) |
| Full sites (16–25 rooms, 2–3 sessions) | Settlements / villages / cities (use `settlement-toolkit-creator`) |
| Classic structures: crypt, ruin, mine, temple, tomb, fortress, lair, sewer, planar incursion | Pure narrative scenarios with no site (use `scenario-writer`) |
| Faction occupancy and dynamic inhabitants | One-off encounters (use `encounter-builder`) |
| Static layout + numbered key + ASCII map sketch | Visual/illustrated maps (use `midjourney-prompt-generator` for AI prompts) |

For a dungeon **inside a published scenario** (the dungeon module is the
climax of a 4-act adventure): build the scenario via `scenario-writer`,
then run this skill on the dungeon leg.

For **mega-dungeons** (Stonehell-scale, Castle Greyhawk-scale): this
skill produces *one level* of a mega-dungeon at a time. A 30-level
mega-dungeon is 30 runs of this skill plus a separate cross-level
overview document.

---

## Before You Begin

Six things to settle before laying out rooms:

1. **Concept.** What is this dungeon *about*? A drowned vault under a
   lighthouse? A cult temple still bleeding from a recent ritual? A
   noble family's tomb where the dead don't stay dead? Without a
   concept, rooms become generic.

2. **Scale.** Pick one:
   - **5-room dungeon** (3-hour one-shot) — Entrance, Roleplay/Puzzle,
     Setback/Twist, Climax, Reward/Revelation. Tight, single arc.
   - **Small site** (10–15 rooms, one session) — Section-and-section
     structure with at least one optional branch.
   - **Full site** (16–25 rooms, 2–3 sessions) — Multiple zones,
     factions, hidden levels, side objectives.

3. **Party tier and size.** XP budget, expected DC range, treasure
   level. A Tier 1 (levels 1–4) party gets different traps, monsters,
   and rewards than a Tier 3 party. Use 4 PCs as the default unless
   specified.

4. **Theme.** The atmospheric and sensory through-line. Drives room
   dressing, monster choice, treasure flavor, and trap design. Examples:
   *drowned*, *necrotic*, *fey-twisted*, *industrial*, *bureaucratic
   afterlife*, *living wood*, *infested machine*, *ash and slag*.

5. **Faction occupancy.** Who lives here *now*? Original builders are
   often long gone. The current occupants are what the party will
   actually meet — and they have their own goals (defending a relic,
   excavating treasure, running a smuggling route, hunting an
   intruder).

6. **Stakes / objective.** Why does the party enter? Recovery, rescue,
   sabotage, investigation, sealing, escape. Drives victory conditions
   and alternative win paths.

If any of these is unclear, ask before designing. Themes especially —
"a dungeon" is not enough.

---

## Layout Patterns

Pick a layout *before* writing rooms. The pattern shapes pacing and
player agency. Load `references/dungeon-structures.md` for full
patterns with diagrams.

| Pattern | Player agency | Best for |
|---|---|---|
| **Linear** | Low | Tightly-paced one-shots (5-room dungeon) |
| **Branching** | Medium | Small sites with a few optional rooms |
| **Loop** | Medium-high | Investigation, escape, faction patrol routes |
| **Hub-and-spoke** | High | Faction-heavy sites where the hub is contested |
| **Jaquayed** (multi-loop with shortcuts, secret connections, vertical layering) | Highest | Full sites and replayable dungeons |

**Default rule of thumb:** 5-room → linear; 10–15 rooms → branching or
loop; 16+ rooms → Jaquayed.

Jaquaying is the practice (named after Jennell Jaquays) of making
dungeons non-linear via loops, secret passages, alternate entries,
vertical layering, and shortcuts. Jaquayed dungeons reward exploration,
make navigation a meaningful choice, and let factions move independently
of the party.

---

## The Six-Step Creation Workflow

Every dungeon passes through these steps. Output assembles them into a
publishable dungeon document.

### Step 1 — Concept and Site Identity

- **Name.** Distinctive, evocative. "The Drowned Bell of Saint Mire"
  beats "Ancient Crypt." Pattern often is
  `[Distinctive Feature], [Place / Origin Cue]`.
- **One-line pitch.** What is this site, in 15 words or fewer?
- **Visual signature.** 2–4 sentences describing what the party sees
  on approach and at the threshold. Concrete sensory detail. Avoid
  generic "ancient and crumbling."
- **Origin.** Who built this? When? Why? In 2–3 sentences. Builders
  are usually gone — but their architectural choices, defenses, and
  iconography linger.
- **Current state.** What has happened since? Collapsed? Flooded?
  Repurposed by a new faction? Re-consecrated by a cult? Sealed?
  Looted? The *current state* drives most of the encounters.

### Step 2 — Layout Pattern and Scale

- **Scale** (5-room / small / full — see Before You Begin).
- **Layout pattern** (linear / branching / loop / hub-and-spoke /
  Jaquayed).
- **Zones.** Group rooms into 2–4 zones with shared theme or function:
  e.g., *Entry Halls*, *Inner Sanctum*, *Sealed Crypt*, *Flooded
  Lower*. Zones help the GM keep their bearings.
- **Vertical layering** (optional). For full sites, add levels:
  *Surface*, *Upper Vault*, *Lower Vault*, *Sealed Sub-level*. Each
  level should feel mechanically different (different occupants,
  different threats, different stakes).
- **Map sketch.** Provide an ASCII or text map with numbered rooms
  and labeled connections. Indicate:
  - Doors (open / locked / secret / one-way / barred)
  - Traversal hazards (collapsed, flooded, rope-only, climbable wall)
  - Vertical changes (stairs, shaft, ladder, ramp)
  - Visibility (dark / dim / bright / line-of-sight blocks)

### Step 3 — Room Key and Functions

Build each room from a **function**, not a theme. Load
`references/room-types-and-functions-2024.md` for the catalogue. The
ten standard functions:

1. **Entrance / Threshold** — sets tone, may include warning, trial,
   or first taste of the theme.
2. **Combat** — hostile encounter, terrain-driven.
3. **Puzzle / Lock** — gates progress, rewards investigation.
4. **Trap** — punishes carelessness, telegraphs danger.
5. **Treasure / Reward** — payoff, often guarded or trapped.
6. **Transition** — connective tissue, may include atmosphere or hint.
7. **Social / NPC** — talking encounter (faction representative,
   ghost, captive, rival adventurer).
8. **Rest / Safe** — short-rest or long-rest viable, replenishes
   resources.
9. **Lair / Boss** — the climax encounter, theme-defining.
10. **Ritual / Set-piece** — interactive multi-turn scene with
    objective beyond combat (close the rift, free the prisoner,
    decipher the slab while monsters arrive).

**Mix ratio by scale:**

- **5-room dungeon:** 1 entrance / 1 puzzle or social / 1 combat or
  trap (setback) / 1 lair / 1 treasure-revelation. (See Five Room
  Dungeon model in references.)
- **10–15 room site:** ~30% combat, ~25% exploration (transition +
  puzzle), ~15% trap, ~15% social/ritual, ~10% rest/treasure, ~5%
  hidden/optional. One lair.
- **16–25 room site:** Same ratio but with 2 lairs (one mini-boss in
  each major zone), more hidden rooms (10–15%), more social
  encounters with the occupying faction.

**Room entry template** (each room in the key uses this):

```
### [Room Number]. [Room Name]
*[One-sentence sensory hook — what hits first when the door opens]*

**Read-Aloud** (2–4 sentences of evocative description for the GM to
deliver; concrete sensory detail; no mechanics or DCs).

**Features**
- [Notable physical feature 1]
- [Notable physical feature 2]
- [Cover / elevation / hazards / interactive elements]

**Occupants** *(if any)*
- [Creature / NPC + count + reference to stat block]
- [Their current activity — what they're doing when the party arrives]

**Mechanics** *(if any)*
- [Perception DC X to notice Y]
- [Investigation DC X to discover Z]
- [Specific check or saving throw with consequence]

**Secrets** *(if any)*
- [Hidden detail and how to find it]

**Connections**
- North: Room [N] via [door type / passage type]
- East: Room [N] via [...]
- Hidden: Room [N] via [secret door, DC X to find]
```

### Step 4 — Encounter Mix, Faction Occupancy, and Pacing

- **Three-pillar balance.** Across the dungeon, the party should
  encounter all three pillars (combat / exploration / interaction).
  A dungeon that's 90% combat is exhausting. A dungeon that's 90%
  social is lifeless. Aim for the ratios in Step 3.

- **Encounter chains.** Load
  `references/encounter-mix-and-pillars.md`. Chain encounters so
  consequences in one room ripple to the next: alarms summon
  reinforcements, broken pillars destabilize the next room,
  questioned guards betray patrol patterns.

- **Faction occupancy.** Who's here *now*, and what are they doing?
  - **Static defenders** (the cult tending the relic, the lich's
    bound servants)
  - **Active intruders** (a rival adventuring party also looting,
    a slaver crew using the site as a holding pen)
  - **Wandering monsters** (the site's natural fauna — vermin, oozes,
    ferals)
  - **Boss / patron** (the entity at the lair)

  Map factional rooms vs neutral rooms. Factions react to disturbance
  — sounding alarms, fortifying choke points, fleeing, parlaying.
  Map the factional response chain in GM notes.

- **Pacing.** Alternate intensity. After a hard fight, an exploration
  room. After a puzzle, a tense social encounter. After three rooms
  of pressure, a safe rest opportunity. The rhythm matters.

- **Optional / hidden rooms** (Jaquayed sites): 10–15% of rooms should
  be optional — secret doors, hidden levels, alternate paths.
  Optional rooms reward thoroughness without punishing speed.

### Step 5 — Traps, Hazards, Treasure, Secrets

- **Traps.** Load `references/trap-and-hazard-library.md` for
  categories, DCs, and telegraphing rules. Every trap should:
  1. Be **telegraphed** (a clue, a stain, a sound, a damaged
     predecessor's remains) — Perception DC scales with party tier.
  2. Have a **disable / bypass / suffer** path — Thieves' Tools DC,
     Athletics DC, alternative route.
  3. Have **proportionate consequence** — a Tier 1 trap shouldn't
     instakill, a Tier 4 trap shouldn't tickle.

  Avoid trap density above 1 per 4 rooms in casual dungeons. Trap-
  heavy dungeons (haunted tomb, paranoid mage's tower) can go higher
  but should be telegraphed early as such.

- **Hazards.** Environmental conditions that persist (slippery floor,
  poisonous mist, magical darkness, gravity reversal, time slip).
  Hazards differ from traps: they affect everyone in the area, often
  for the duration of the room or zone. Use saving throws over
  surprise damage.

- **Treasure placement.** Load DMG 2024 treasure tables. Distribute:
  - **~30% in the lair / boss room** (signature treasure)
  - **~30% in side rooms or hidden rooms** (rewards exploration)
  - **~20% on enemy occupants** (loot from defeated)
  - **~20% as set dressing / mundane** (vault, hoard, library)

  Include at least one **signature treasure** that ties to the
  dungeon's theme — not just "gold and gems." See
  `magic-item-creator` for signature item design.

- **Secrets.** Information the players can uncover that recontextualizes
  the dungeon. Examples:
  - The "captives" the cult is sacrificing are actually the cult's
    rivals, not innocents.
  - The relic was placed here to *contain* the entity, not summon it.
  - The dungeon's builder is still alive in the lowest level,
    bargaining with PCs against their current occupants.

  Secrets should be **findable** (via Investigation, Perception,
  History, Religion checks, or by interrogating NPCs) and **stakes-
  altering** when found.

### Step 6 — Theme, Dressing, and GM Deliverables

Theme work makes a dungeon memorable. Load
`references/dungeon-themes-and-dressing.md` for archetypal themes,
sensory layering, and lore seeds.

- **Sensory through-line.** Pick 2–3 recurring sensory elements
  (e.g., for a drowned vault: *constant dripping*, *salt smell*,
  *brine-stained walls*). Drop them into multiple rooms to build
  cohesion.

- **Iconography.** What images, sigils, symbols, statues appear?
  Recurring iconography teaches the players to read the dungeon
  ("we keep seeing the bell motif…").

- **Recurring NPCs / signs of faction.** If a faction occupies the
  dungeon, leave traces in non-occupant rooms: graffiti, broken
  patrol gear, food leavings, recent damage.

- **Lore seeds.** 3–5 in-fiction lore fragments scattered through
  the dungeon (carved inscriptions, journal pages, ghostly
  monologues, rival adventurer's notes) that build the dungeon's
  backstory if assembled.

- **GM flow notes.** A 1-page (or shorter) GM-facing section with:
  - **Recommended approach order** if a default exists (e.g., "The
    direct path runs 1 → 4 → 7 → 12; the back-door path runs
    1 → 2 → 9 → 12. The cult patrols the direct path; the back
    door is unguarded but trapped.")
  - **Faction response chain** — if PCs trigger alarms in Room X,
    reinforcements arrive from Rooms Y and Z within N rounds.
  - **Time-pressure events** (if applicable) — what happens if PCs
    rest too long, what happens if a ritual completes.
  - **Victory and failure conditions** — what counts as success,
    what happens if PCs flee or fail.

---

## Output Format

Assemble all six steps into a single dungeon document. Use this
structure:

```markdown
# [Dungeon Name]

*[One-line pitch in italics.]*

## Overview

**Scale:** [5-room / Small (10–15) / Full (16–25)]
**Party Tier:** [Tier X, levels Y–Z]
**Theme:** [One-line theme]
**Faction Occupancy:** [Who's here now]
**Stakes:** [Why PCs enter]

[Visual signature paragraph — what PCs see on approach.]

## Origin and Current State

[2 short paragraphs. Origin = who built it / when / why. Current
state = what happened since, who's here now.]

## Map

[ASCII or text map. Number rooms 1–N. Mark connections, doors,
hazards, vertical changes.]

## Zones

- **Zone A: [Name]** — Rooms 1–[N]. [One-sentence character.]
- **Zone B: [Name]** — Rooms [N+1]–[M]. [...]
- [...]

## Faction & Inhabitants

| Faction / Creature | Where | Activity | Stat Block |
|---|---|---|---|
| [Cult of the Drowned Bell] | Rooms 4, 7, 9 | Guarding the relic; patrols every 10 min | Cultist (MM); Cult Fanatic for Brother Saul (MM) |
| [...] | [...] | [...] | [...] |

## Room Key

### 1. [Room Name]
*[Sensory hook]*

**Read-Aloud**
[2–4 sentences.]

**Features**
- [...]

**Occupants**
- [...]

**Mechanics**
- [...]

**Secrets** *(if any)*
- [...]

**Connections**
- [Direction]: Room [N] via [door type]

[Repeat for all rooms.]

## Traps & Hazards Summary

| Location | Type | Trigger | DCs | Damage / Effect |
|---|---|---|---|---|
| Room 3 | Pressure plate → poison darts | Step on plate | Perception 14, Thieves' Tools 15 | 2d4 piercing + DC 13 Con save vs 1d6 poison |
| [...] | [...] | [...] | [...] | [...] |

## Treasure Summary

| Location | Item / Value | Notes |
|---|---|---|
| Room 12 (lair) | The Drowned Bell of Saint Mire (signature item) | See magic-item-creator output |
| Room 8 | 240 gp in silver chalices | Embossed with bell motif |
| [...] | [...] | [...] |

## GM Flow Notes

**Recommended Approach:** [...]
**Faction Response Chain:** [...]
**Time-Pressure Events:** [...]
**Victory Conditions:** [...]
**Failure / Flee Consequences:** [...]

## Plot Hooks

1. **[Hook Title].** [1–3 sentences.]
2. **[Hook Title].** [1–3 sentences.]
3. **[Hook Title].** [1–3 sentences.]

## Sequel Hooks

[1–2 hooks pointing to what comes after this dungeon is resolved —
faction retaliation, awakened threat, recovered artifact's next
custodian.]
```

**Language:** Match the language of the brief. If the brief is in
French, write the entire dungeon in French. Stat block references
remain in their published form (Manuel des Monstres p. X).

**Tone:** Adventure-module professional. Evocative read-aloud, precise
mechanics, GM notes that anticipate likely table moments.

---

## Scale-Specific Adjustments

### 5-Room Dungeon (one-shot, ~3 hours)

- **Layout:** Linear (1 → 2 → 3 → 4 → 5), with optional secret
  shortcut from 1 → 3.
- **Room functions:** Entrance / Puzzle or Social / Setback (combat
  or trap) / Climax (lair) / Reward.
- **Faction:** One faction or none — keep it simple.
- **Treasure:** Two items: one signature in the lair, one minor
  earlier.
- **Plot hooks:** 1–2 sufficient.
- **GM notes:** Short. Half a page.

### Small Site (10–15 rooms, one session)

- **Layout:** Branching or loop. At least one optional branch.
- **Zones:** 2 zones recommended.
- **Faction:** One faction occupying 60–70% of rooms; ambient
  threats in the rest.
- **Treasure:** 4–6 distinct items / hoards. One signature.
- **Plot hooks:** 2–3.
- **Hidden rooms:** 1–2.
- **GM notes:** Full page.

### Full Site (16–25 rooms, 2–3 sessions)

- **Layout:** Jaquayed. Multiple loops, vertical layering, secret
  passages.
- **Zones:** 3–4 zones.
- **Faction:** 1–2 factions in conflict (faction A occupies upper,
  faction B occupies lower; or faction A is being displaced by
  faction B mid-occupation).
- **Treasure:** 8–12 distinct items / hoards. 2 signature pieces.
- **Plot hooks:** 3–5.
- **Hidden rooms:** 3–5 (10–15% of total).
- **Mini-bosses:** 1 per major zone, plus a final lair.
- **GM notes:** 1.5–2 pages, including faction response matrix.

---

## Interaction with Other Skills

- **Dungeon sits inside a larger scenario** → run `scenario-writer`
  for the narrative wrapper (acts, three-clue rule, NPC web), then
  this skill for the site itself. Pass the scenario's victory
  condition into Step 1.
- **Faction occupying the dungeon needs depth** → run
  `faction-creator` for the organization, reference in Step 4.
- **Custom monster for the lair** → run `monster-creator` for the
  unique creature, reference in the Occupants line of the lair
  room.
- **Signature treasure** → run `magic-item-creator` for the boss
  reward, reference in Treasure Summary.
- **One specific combat in the dungeon needs full balance** → run
  `encounter-builder` on that specific room.
- **Random wandering encounters during the crawl** → run
  `random-encounter-creator` to layer a d20 or d100 table.
- **Read-aloud polish for entrance and key rooms** → run
  `read-aloud-crafter` on those entries.
- **Originality check** (is my "ancient crypt" too cliché?) → run
  `ttrpg-cliche-buster` on the concept *before* designing.
- **Pre-publication review** → run `ttrpg-supplement-reviewer` after
  the dungeon is complete.
- **Visual maps for publication** → use `midjourney-prompt-generator`
  on the map sketch.

---

## Edge Cases

**Brief is "build me a dungeon"** with no specifics: ask for scale,
party tier, theme, and stakes. Without these, the dungeon becomes
generic.

**Brief asks for a mega-dungeon (50+ rooms / multi-level)**: defer.
This skill produces *one level* at a time. Run it once per level
and produce a separate cross-level overview.

**Brief asks for a "dungeon" that is actually a settlement**
(a thieves' guild hideout sprawling across a district, a fortified
village with internal threats): use `settlement-toolkit-creator`
instead. The skills are distinguished by *function*: dungeons are
*sites of confrontation with a discrete objective*; settlements are
*living habitations with persistent residents*.

**Brief asks for a "dungeon" that is actually one encounter**
(a single goblin ambush in a cave mouth): use `encounter-builder`.

**Brief asks for a hex crawl / wilderness map**: defer. This skill
is for enclosed or semi-enclosed sites with a navigable internal
structure.

**Adult / mature themes**: standard 5e produces SFW by default.
Adult-themed flavor (sensual cult rituals, sensual entanglements,
explicit content) can be layered via Fantasy Vixens-specific skills
after this skill produces the structural baseline.

**No combat dungeon** (an investigation dungeon, a heist site, a
diplomatic compound): valid. Adjust Step 4 ratios — push the social
and exploration pillars, keep combat to 1–2 contingency encounters.
Document explicitly in GM notes that combat is the alarm condition,
not the expected mode.

**One-room "dungeon"** (a sealed vault, a single ritual chamber):
not enough. If the brief is genuinely one room, use
`encounter-builder` for the encounter and `read-aloud-crafter` for
the description.

**Dungeon for a system other than 5e 2024**: most patterns transfer.
Replace stat block references and DC ranges. The structural skeleton
(layout, room functions, faction occupancy, theme) is system-agnostic.

---

## Publication Checklist

Before considering a dungeon complete:

- [ ] Name, one-line pitch, visual signature.
- [ ] Origin and current state, in 2 paragraphs.
- [ ] ASCII map with numbered rooms and connection types.
- [ ] Zones labeled (if scale > 5-room).
- [ ] Every room has read-aloud, features, occupants (if any),
      mechanics (if any), connections.
- [ ] At least one secret room or hidden detail.
- [ ] Faction occupancy table.
- [ ] Traps & hazards summary table.
- [ ] Treasure summary table with at least one signature item.
- [ ] GM flow notes including faction response chain.
- [ ] At least 2 plot hooks and 1 sequel hook.
- [ ] Encounter mix balanced across the three pillars.
- [ ] Trap density appropriate to theme.
- [ ] All stat block references cite source (MM 2024 page, custom
      monster reference).
- [ ] Theme through-line visible in at least 4 rooms.

---

## Reference Files

Load these as needed — not all at once.

- `references/dungeon-structures.md` — Layout patterns (linear,
  branching, loop, hub-and-spoke, Jaquayed) with diagrams and worked
  examples. The 5-Room Dungeon model in detail. Vertical layering
  conventions. Door / passage typology. Map sketching conventions.
- `references/room-types-and-functions-2024.md` — The 10 standard
  room functions detailed: purpose, design considerations, pitfalls,
  sample variants. Plus a catalogue of room *subtypes* (e.g., for
  combat rooms: ambush corridor, choke-point arena, vertical fight,
  hazard fight; for puzzle rooms: gate puzzle, password lock,
  manipulation puzzle).
- `references/encounter-mix-and-pillars.md` — The three-pillar
  framework for D&D 5e 2024. Mix ratios by dungeon scale. Pacing
  curves. Encounter chaining (alarms, reinforcements, factional
  responses). Pillar-by-pillar design tips. Anti-patterns (combat
  cascade, social vacuum, exploration treadmill).
- `references/trap-and-hazard-library.md` — Trap categories
  (mechanical, magical, environmental, social-pressure). DCs by
  party tier. Telegraphing rules. Disable/bypass/suffer triad.
  Hazard catalogue (persistent environmental conditions). Anti-
  patterns ("gotcha" traps, instakills, undetectable hazards).
- `references/dungeon-themes-and-dressing.md` — Archetypal themes
  (drowned vault, necrotic crypt, fey-twisted hollow, industrial
  ruin, bureaucratic afterlife, living wood, infested machine,
  ash-and-slag forge). For each: signature visuals, sensory layer,
  iconography, lore seeds, monster suggestions, treasure flavor
  cues. Plus a sensory-layering protocol and an iconography
  recurrence schedule.
