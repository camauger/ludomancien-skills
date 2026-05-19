# Dungeon Structures

Layout patterns, the 5-Room Dungeon model, vertical layering, door
typology, map conventions.

---

## The Five Layout Patterns

### 1. Linear

```
[1] — [2] — [3] — [4] — [5]
```

Single path, no choice. Each room must be entered to progress.

**When to use:** 5-room dungeons, tight one-shots, story-heavy
sequences where decision points come *within* rooms rather than
between them.

**Pitfalls:**
- Failure to progress halts the table — every gate must have a
  bypass.
- Linear dungeons feel like rails. Use only when pacing demands it.
- The fix: add at least one *internal* choice (which door to open
  first in a 2-exit room) or one secret shortcut.

### 2. Branching

```
        [3]
         |
[1] — [2] —[4] — [5]
         |
        [6]
```

Main path with side branches. Branches are optional and lead to
treasure, lore, or alternative paths.

**When to use:** 10–15 room sites. The main path completes the
objective; branches reward exploration.

**Pitfalls:**
- Branches that go nowhere feel like padding. Each branch should
  *give* something: treasure, lore, an alternative path, a faction
  contact, or a piece of the puzzle.
- Don't let branches be longer than the main path or the structure
  reads as confused.

### 3. Loop

```
[1] — [2] — [3]
 |           |
[6] — [5] — [4]
```

Closed circuit. Multiple paths return to a common point. PCs can
choose direction.

**When to use:** Investigation dungeons, escape scenarios, faction
patrol routes, sites the players will re-enter multiple times.

**Pitfalls:**
- Loops without internal landmarks confuse players. Use distinctive
  room features so players can describe their position.
- A pure loop with no inner rooms is just a corridor. Add at least
  one inner chamber accessible from multiple points.

### 4. Hub-and-Spoke

```
       [2]
        |
[3] — [HUB] — [4]
        |
       [5]
```

Central hub connects to multiple zones. PCs return to the hub
between zones.

**When to use:** Faction sites where the hub is contested or
controlled (the cult's atrium, the guildmaster's office). Sites
where PCs need a recurring landmark.

**Pitfalls:**
- The hub must be *interesting* — not just a connector. Put NPCs,
  a major encounter, or a puzzle there.
- If the hub is dangerous (occupied by enemies), traversal back to
  the hub becomes a recurring tension. If safe, it becomes a rest
  point.

### 5. Jaquayed

```
       [3] — [4] — [secret 5]
        |     |        |
[1] — [2] — [HUB] — [6]
              |      |
       [7] — [8] — [9 lower lvl]
              |
       [10 below]
```

Multi-loop with shortcuts, secret connections, vertical layering,
and alternate entries. Named after Jennell Jaquays, who pioneered
this approach.

**When to use:** Full sites (16–25 rooms), replayable dungeons,
mega-dungeon levels.

**Properties of a well-Jaquayed dungeon:**
- **Multiple entries / exits.** PCs can come in from different
  points (back door, drainage tunnel, collapsed wall, sewer
  access). The entry chosen affects what they encounter first.
- **Loops, not dead ends.** Most rooms have multiple connections.
  Backtracking is rarely required.
- **Shortcuts.** Secret passages collapse what would otherwise be
  long traversal sequences. Often discovered by examining a room
  more carefully than expected.
- **Vertical layering.** Stairs, shafts, ladders, ramps. The site
  exists in 3D, not 2D.
- **Asymmetric difficulty.** Some routes are easier (but more
  watched, more trapped, or longer). Some are harder (but bypass
  defenses or shorten the journey).
- **Independent factional movement.** Occupants can move through
  the dungeon without crossing the players' path. Patrol routes
  exist.

**Pitfalls:**
- Over-engineering. A dungeon with 18 secret passages becomes
  navigation soup. 2–4 shortcuts in a 20-room dungeon is typical.
- Confusing maps. Players need a *legible* map even if the dungeon
  is non-linear. Use clear iconography.

---

## The 5-Room Dungeon Model

The 5-Room Dungeon (popularized by Johnn Four) is a tight one-shot
structure that runs ~3 hours at the table. Each room has a fixed
function:

### Room 1 — Entrance / Guardian

- Sets tone, establishes the dungeon's theme.
- May contain a *Guardian* — a creature, a riddle, a lock that
  must be passed.
- The Guardian is **not** a major fight — it's a gatekeeper.

### Room 2 — Roleplay / Puzzle

- Non-combat challenge: a puzzle, a social encounter with a
  prisoner or ghost, a moral choice.
- Tests the party in a different pillar than Room 1.
- May reveal critical lore.

### Room 3 — Setback / Twist

- A reversal: combat after expected social, ambush after
  expected exploration, a betrayal, a trap, a chase.
- The party loses something here — resources, an ally, a key,
  certainty.

### Room 4 — Climax / Lair / Boss

- The major confrontation. Boss fight, ritual interruption,
  faction showdown.
- Theme-defining encounter. Uses the dungeon's signature element.

### Room 5 — Reward / Revelation

- Payoff: treasure, rescued ally, sealed threat, recovered relic.
- Plus *revelation* — a piece of lore that recontextualizes the
  whole dungeon and seeds future adventures.

**Variations:**
- Swap Rooms 1 and 2 if a strong RP opener is desired.
- Compress Rooms 4 and 5 into a single encounter if time is tight.
- Add an optional Room 6 (hidden) for deep exploration.

---

## Vertical Layering

Three-dimensional dungeons are more memorable than flat ones.
Vertical changes also create natural choke points and traversal
challenges.

### Common vertical transitions

| Element | Mechanics | Notes |
|---|---|---|
| Stairs | Free traversal | Difficult terrain if rubble; spell line-of-sight blocker |
| Spiral stairs | Free traversal | Cover bonus for defenders, hard to retreat from |
| Ramp | Free traversal | Slow if slick; ranged advantage from top |
| Ladder | Half speed; one hand | Cannot fight effectively while climbing |
| Rope | Athletics check possible; one hand | Drops are a real risk |
| Shaft | Athletics DC or feather fall | Dramatic drop point |
| Pit / hole | Often hazardous | Coverable, ambushable from below |
| Trapdoor | Locked or hidden | Classic Jaquaying tool |

### Layered level conventions

- **Level 0 — Surface.** Approach, exterior, threshold. Often weather
  is in play.
- **Level 1 — Upper.** Public rooms, defenses, lighter occupants.
- **Level 2 — Inner.** More secure areas, faction leadership,
  treasure rooms.
- **Level 3 — Lower.** Sanctum, lair, sealed area. Hardest, most
  rewarding.
- **Level -1 — Sub-level / sealed.** Often older than the rest of the
  dungeon — pre-occupant ruins, older order, deeper threat.

---

## Door and Passage Typology

Use a consistent typology so the map is readable.

| Symbol | Type | Notes |
|---|---|---|
| `—` or `═` | Open passage | Free travel |
| `\|` `\` `/` | Diagonal / vertical passage | |
| `[D]` | Door (unlocked) | Free open |
| `[L]` | Door (locked) | Thieves' Tools or Athletics |
| `[B]` | Door (barred) | Athletics or social override |
| `[S]` | Secret door | Perception or Investigation to find |
| `[1→]` | One-way door | Travel allowed in arrow direction only |
| `[P]` | Portcullis | Mechanical; may be raised |
| `[A]` | Archway / open threshold | Decorative, narratively significant |
| `[R]` | Rubble / collapsed passage | Athletics to clear; may take rounds |
| `[F]` | Flooded passage | Swim required; may require breath check |
| `[V]` | Vertical (stairs, ladder, shaft) | Annotated in room key |

---

## Map Sketching Conventions

A text/ASCII map should be:

1. **Numbered.** Rooms 1–N, matching the key.
2. **Connected.** Use the door/passage typology above.
3. **Compass-oriented.** Indicate north (N) at the top by
   convention.
4. **Vertically annotated.** If multi-level, mark each level
   separately or use `↑` / `↓` for vertical transitions.
5. **Legible.** Don't try to be artistic in ASCII — be clear.

**Example:**

```
LEVEL 1 — UPPER VAULT
N

[1 Entry Hall]
   |
   D
   |
[2 Antechamber] —D— [3 Library]
   |                    |
   L                    S
   |                    |
[4 Patrol Room] ═════ [5 Hidden Study]
   |                    |
   V (down)             V (down)
   |                    |
   to Level -1          to Level -1
```

For publication, this sketch is replaced by a proper map asset —
but the sketch must be unambiguous on its own.

---

## Choosing the Right Pattern

| Scale | Default pattern |
|---|---|
| 5-room dungeon | Linear (with one optional shortcut) |
| Small site, story-heavy | Branching |
| Small site, investigation | Loop |
| Small site, faction-heavy | Hub-and-spoke |
| Full site, replayable | Jaquayed |
| Full site, mega-dungeon level | Jaquayed with vertical layering |

When in doubt: start with a simpler pattern and add complexity only
where the dungeon's premise demands it. Players don't need to feel
the cleverness of the layout — they just need to navigate without
confusion.
