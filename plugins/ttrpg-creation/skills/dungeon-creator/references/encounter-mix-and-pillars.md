# Encounter Mix and Pillars

The three-pillar framework, pacing curves, encounter chaining,
factional response, anti-patterns.

---

## The Three Pillars (D&D 5e 2024)

D&D 5e 2024 builds its play loop on three pillars:

1. **Combat** — violence, tactics, action economy.
2. **Exploration** — traversal, investigation, environmental
   interaction.
3. **Social Interaction** — talking, persuading, deceiving,
   intimidating, parleying.

A balanced dungeon engages **all three** pillars. A dungeon that is
90% combat exhausts the table; one that is 90% social feels
inert; one that is 90% exploration loses tension.

---

## Mix Ratios by Scale

**5-Room Dungeon:**
- 40% combat (the climax + one earlier fight)
- 20% social (often Room 2)
- 40% exploration (Rooms 1, 3, sometimes 5)

**Small Site (10–15 rooms):**
- 30–40% combat
- 20–30% exploration
- 15–20% social
- 15–20% trap / puzzle / hazard
- 10% rest / treasure

**Full Site (16–25 rooms):**
- 25–35% combat
- 20–25% exploration
- 15–20% social
- 15% trap / puzzle / hazard
- 10–15% transition / rest / treasure
- 5–10% hidden / optional

These ratios are *defaults*. A dungeon's premise can shift them:

| Premise | Combat | Social | Exploration |
|---|---|---|---|
| War-fortress, military assault | High | Low | Medium |
| Cult temple, infiltration | Medium | High | Medium |
| Lost tomb, archaeology | Low | Low | High |
| Thieves' den, faction politics | Medium | High | Medium |
| Wizard's tower, puzzle-heavy | Low | Medium | High (puzzle-dense) |
| Bandit lair, simple raid | High | Low | Low |

---

## Pacing Curves

A dungeon should breathe. Alternate intensity rather than stack
hard encounters.

### Recommended Pacing Pattern (small site, ~12 rooms)

```
Intensity
  ↑
HARD       3       7         12
           |       |         |
MED   1    |   5   |   9    11
      |    |   |   |   |   |
LOW   0—1—2—3—4—5—6—7—8—9—10—11—12 Room number
        2     4     6 (rest)  10
```

- **Room 1 (entrance):** Low — establishes tone.
- **Room 2 (puzzle / social):** Low to medium.
- **Room 3 (first fight):** Hard or medium.
- **Room 4 (transition):** Low.
- **Room 5 (combat or hazard):** Medium.
- **Room 6 (rest opportunity):** Low — recovery point.
- **Room 7 (set-piece):** Hard.
- **Room 8 (transition or social):** Low to medium.
- **Room 9 (combat):** Medium.
- **Room 10 (treasure / hidden):** Low.
- **Room 11 (lieutenant fight):** Medium-hard.
- **Room 12 (lair / climax):** Hard / set-piece.

### Anti-pattern: Combat Cascade

Three hard fights in a row. Party burns spell slots, HP, and
patience. By the third fight, mistakes happen — TPK risk rises
not from challenge but from attrition.

**Fix:** Insert a transition, a social, or a rest room after every
1–2 hard fights.

### Anti-pattern: Social Vacuum

12 rooms, zero social encounters. Combat-heavy parties enjoy this,
but most tables miss talking. Adds variety even for combat parties.

**Fix:** Include at least one social NPC per 5 rooms, even if just
a captive, a ghost, or a defector cultist.

### Anti-pattern: Exploration Treadmill

Six transition rooms in a row with no payoff. Becomes navigation
busywork.

**Fix:** Compress transitions, or give each one a *distinct*
atmospheric detail or hint.

---

## Encounter Chaining

Encounters become memorable when consequences ripple. Design with
chain reactions in mind.

### Alarm Chains

If the party makes noise / triggers an alarm / leaves witnesses,
nearby occupants respond. Map this explicitly:

```
Room 4 (Patrol Room): If combat goes beyond Round 3, or any
                      occupant raises an alarm:
   → Room 7 (Barracks): 4 cultists arrive in Round 5.
   → Room 9 (Captain's Office): Captain arrives in Round 8 with
     2 elite guards.
   → Room 12 (Lair): Boss begins lair-tier preparations
     (regional effect activates).
```

### Resource Depletion Chains

Loud or magical fights deplete dungeon resources. Map this:

```
If party expends 3+ spell slots clearing Room 5:
   → Boss in Room 12 anticipates and casts pre-buffs.
```

### Information Chains

What the party learns in early rooms affects later rooms.

```
If party reads the journal in Room 3:
   → They know the password for the door in Room 8 (DC 5 vs 18
     History check).
```

### Faction Movement Chains

Occupants in a Jaquayed dungeon move independently. Patrols leave
and return on a schedule. Mark this:

```
Patrols: 2 cultists patrol Rooms 4 → 5 → 9 → 5 → 4 on a 20-minute
loop. If killed silently in Room 5, their absence is noticed at
Round 30 by the Room 9 occupants.
```

These chains are documented in the **GM Flow Notes** section of
the dungeon doc, not buried in individual rooms.

---

## Factional Response Matrix

For dungeons with factional occupants, prepare a response matrix.

**Trigger events:**
- Alarm raised (verbal shout, bell, magical alarm)
- Occupant killed silently
- Door breached audibly
- Spell with audible / visible casting in a non-secluded room
- Light source detected in a normally-dark area
- Faction NPC captured / questioned

**Response levels:**

| Level | Trigger | Faction action |
|---|---|---|
| 0 | None — party is undetected | Patrols continue normally |
| 1 | Suspicion — odd absence, faint noise | Patrol routes tighten; alert guards posted |
| 2 | Confirmed intrusion — alarm, witness | Reinforcements move to last known position; choke points reinforced |
| 3 | Active combat known to leadership | Boss begins preparation; key NPCs evacuate or fortify |
| 4 | Party reaches inner sanctum | Final defense; boss engages with lair-tier capabilities |

Map each level to specific room reactions in the GM Flow Notes.

---

## Three-Pillar Design Tips

### Combat Pillar
- Every combat room has *terrain* (not just an empty rectangle).
- Use the dungeon's theme in combat encounters (drowned cultists
  drag PCs into water; necrotic guardians corrupt healing).
- Pre-roll initiative for static defenders so the GM can hit the
  ground running.

### Exploration Pillar
- Make the dungeon *itself* readable. PCs should be able to gather
  information by looking, not just by rolling.
- Reward checks with partial information — a passive Perception
  check yields the obvious, an Investigation roll yields the
  hidden.
- Distribute lore across multiple rooms so investigation actually
  pays off.

### Social Pillar
- Every social NPC wants *something the PCs can affect.*
- Provide multiple approaches — Persuasion, Deception,
  Intimidation should all be viable, with different stakes /
  costs.
- Social NPCs should have **secrets** the PCs can uncover, not
  just exposition.

---

## Pillar Distribution Audit

Before publishing a dungeon, audit each room:

| Room | Primary Pillar | Secondary Pillar |
|---|---|---|
| 1 | Exploration | — |
| 2 | Social | Exploration (lore) |
| 3 | Combat | Exploration (terrain) |
| 4 | Trap | Exploration |
| 5 | Combat | Social (parley option) |
| 6 | Rest | — |
| 7 | Ritual / Set-piece | Combat |
| 8 | Transition | Exploration (lore) |
| 9 | Combat | — |
| 10 | Treasure | Exploration |
| 11 | Combat | — |
| 12 | Lair | Combat + Social (parley option) |

**Audit check:** Do all three pillars appear at least twice as
*primary*? If not, the dungeon is unbalanced — consider redesigning
a room's primary pillar.
