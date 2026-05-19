# Room Types and Functions (D&D 5e 2024)

The 10 standard room functions, their design intent, subtypes,
pitfalls, and sample variants.

A dungeon room should be **functional first, themed second**. Decide
what the room *does* before you decide what it *looks like*. A
combat room with no combat, a puzzle room with no puzzle, or a
treasure room with no payoff is dead space.

---

## 1. Entrance / Threshold

**Purpose:** First impression. Sets tone, telegraphs theme,
introduces the dungeon's signature element.

**Design considerations:**
- The threshold should *say something* about the dungeon. A blood-
  stained door teaches the players what kind of place this is.
- May include a *guardian* — a creature, a riddle, a lock. The
  guardian is a gatekeeper, not a major encounter.
- Provide a clear point of no return — once past the threshold,
  the dungeon's rules apply.

**Subtypes:**
- **Open mouth** — visible from approach (cave mouth, ruined arch).
  No bypass needed.
- **Sealed door** — requires action to enter (key, ritual, riddle,
  forced).
- **Hidden entry** — must be discovered (collapsed passage, secret
  panel, illusory wall).
- **Trial threshold** — requires a test to enter (combat trial,
  social challenge, sacrifice).
- **Active threshold** — the entrance itself is dangerous (acid
  rain, magical decay, guarded approach).

**Pitfalls:**
- Generic stone arch with no character. The threshold should be
  the *most* themed room.
- Too-hard a guardian. The threshold sets tone — it shouldn't be
  the climactic fight.

---

## 2. Combat

**Purpose:** Hostile encounter resolved through violence (or
clever bypass).

**Design considerations:**
- Use terrain. Open rooms with no cover are boring. Vertical
  changes, cover, hazards, line-of-sight blockers all matter.
- Define why the occupants are *here* (guarding, sleeping,
  ritualizing, eating, patrolling, ambushing). The activity at
  the moment of intrusion shapes the opening rounds.
- Include alternative win conditions where appropriate (kill the
  leader, dispel the ward, capture the prisoner, survive 5
  rounds).

**Subtypes:**
- **Ambush corridor** — narrow space; defenders gain surprise from
  cover.
- **Choke-point arena** — bottleneck forces tactical positioning.
- **Vertical fight** — combat across multiple levels (balcony,
  pit, scaffolding).
- **Hazard fight** — environmental hazard in play (lava channel,
  collapsing floor, summoned undead).
- **Boss antechamber** — fight against the boss's elite guard
  before the lair.
- **Patrol intercept** — fight against a moving patrol; reinforcement
  timing matters.

**Pitfalls:**
- "Four orcs in an empty room." No terrain, no stakes, no story.
- Save-or-die saves (insta-kill conditions on Tier 1 parties).
- Reinforcements that never end (combat-as-grind).

**For full balancing of a specific encounter:** use
`encounter-builder` once the room concept is settled.

---

## 3. Puzzle / Lock

**Purpose:** Gates progress, rewards investigation, exercises
non-combat skills.

**Design considerations:**
- Puzzles should have **multiple solution paths.** A spell, a
  skill check, a clever use of an item, brute force — all should
  be viable at some cost.
- Telegraph the puzzle's *mechanics* clearly. Mystery is fine;
  unclear rules are not.
- Reward partial solutions: getting it half-right opens a partial
  path or reduces a penalty.

**Subtypes:**
- **Gate puzzle** — the puzzle is the door. Solve to pass.
- **Password lock** — a phrase, gesture, or item unlocks.
- **Manipulation puzzle** — physical objects must be arranged
  (statues turned, levers pulled, weights placed).
- **Symbolic puzzle** — iconography must be read or matched.
- **Ritual completion** — an incomplete ritual must be finished
  with the right components.
- **Logic puzzle** — riddles, deduction (use sparingly; not all
  tables enjoy these).

**Pitfalls:**
- Single-solution puzzles that block the table indefinitely.
- Puzzles solved entirely by player out-of-character cleverness
  with no character skill investment.
- Puzzles whose solution requires information not present in
  the dungeon.

---

## 4. Trap

**Purpose:** Punishes carelessness, telegraphs danger, rewards
caution and investigation.

**Design considerations:**
- **Always telegraph.** Stains, scorch marks, a previous victim's
  remains, a worn spot on the floor, an audible click.
- **Always have a disable / bypass / suffer path** — Thieves'
  Tools DC for disable, alternative route for bypass, save with
  proportionate damage for the unlucky.
- **Proportionate consequence.** Tier 1 traps deal 2–4d6, not 8d6.
  Tier 4 traps deal substantial damage but rarely instakill.

See `references/trap-and-hazard-library.md` for full catalogue
and DC ranges.

**Pitfalls:**
- "Gotcha" traps — no warning, no save, instant death.
- Trap density above 1 per 4 rooms in non-trap-themed dungeons.
- Identical traps repeated (the same dart-trap door three times).

---

## 5. Treasure / Reward

**Purpose:** Payoff. Material reward for risk taken.

**Design considerations:**
- Treasure should be **guarded, hidden, or earned.** "A pile of
  gold sits in the middle of the room" is dead.
- At least one piece of treasure per dungeon should be **signature**
  — themed, unique, tied to the dungeon's story (use
  `magic-item-creator` for the signature piece).
- Include **non-monetary value:** information, lore fragments,
  faction reputation, narrative items (a letter, a portrait, a
  diary).

**Subtypes:**
- **Vault** — concentrated treasure behind a locked / trapped door.
- **Hoard** — boss-room treasure, mixed with bones / spoil.
- **Hidden cache** — discovered by investigation (loose stone,
  false bottom, behind a portrait).
- **Treasure-as-trap** — taking the item triggers consequences
  (curse, alarm, summoning).
- **Treasure-on-corpse** — looted from defeated enemies.

**Pitfalls:**
- Treasure that's pure gold-coin. Mix item types.
- Signature item that doesn't fit the dungeon's theme.
- Treasure rooms without context — *why* is this hoard here?

---

## 6. Transition

**Purpose:** Connective tissue. Atmospheric pacing between major
encounters. May contain hints, foreshadowing, or lore.

**Design considerations:**
- Transition rooms are **not filler.** They serve the rhythm of
  the dungeon. After a hard fight, a transition room lets the
  party breathe.
- Include atmosphere: a sensory detail, a recurring iconographic
  element, a sound the party can hear from elsewhere.
- May contain a single lore fragment — a carving, a torn page,
  a withered offering.

**Subtypes:**
- **Corridor** — pure connection, with one or two atmospheric
  details.
- **Antechamber** — pause room before a major encounter; may
  include benches, statues, or wards.
- **Mood room** — heavy on atmosphere, light on mechanics (the
  candlelit chapel, the moss-grown stairs).
- **Lore room** — contains discoverable information (library
  fragment, mural, ghost echo).

**Pitfalls:**
- Too many transition rooms in a row. After 3 in a row, the
  party feels they're padding.
- Transition rooms with no character. "An empty corridor" is
  worse than no room at all.

---

## 7. Social / NPC

**Purpose:** Talking encounter. Faction representative, ghost,
captive, rival adventurer, prisoner.

**Design considerations:**
- The NPC should **want something the party can affect.** Pure
  exposition NPCs are dull.
- Include **stakes** — what the NPC will do if not satisfied
  (warn the boss, attack, refuse to share info, summon
  reinforcements).
- Make the NPC **non-obvious.** A scared cultist might be a
  defector; a captive might be an infiltrator; a friendly ghost
  might be a deceiver.

**Subtypes:**
- **Captive** — wants rescue, may have information, may be
  lying.
- **Rival** — competing party or faction representative; may
  parley, fight, or strike a deal.
- **Defector** — wants to betray the dungeon's faction; offers
  intel for protection.
- **Guardian-spirit** — ghost, animated statue, bound elemental
  with rules of engagement.
- **Boss's lieutenant** — speaks for the boss, may make demands
  or threats.
- **Wandering loner** — hermit, scavenger, prisoner-turned-
  inhabitant; may be a wildcard.

**Pitfalls:**
- NPC info-dumps with no stakes (PCs ask, NPC tells, scene ends).
- NPCs with no consequence for poor handling.
- NPCs whose only role is to dispense the next plot beat.

For deep NPC design, use `npc-creator`.

---

## 8. Rest / Safe

**Purpose:** Short-rest or long-rest viable. Replenishes resources.

**Design considerations:**
- Rest rooms make resource management *meaningful.* Without them,
  every encounter is a nova-fight.
- **Long-rest sites** should be earned — often hidden, often
  requiring the party to clear adjacent threats.
- **Short-rest sites** can be more common — a defensible nook,
  a sealed chamber, the body of a slain boss.
- May still have *narrative* tension — what the party hears
  during the rest, what they witness, what they decide.

**Subtypes:**
- **Defensible chamber** — single entry, can be barricaded.
- **Hidden shrine** — safe, restorative, possibly with a minor
  benefit (advantage on next save, temporary HP).
- **Sealed sub-room** — found by investigation, isolated.
- **Cleared room** — formerly hostile, now safe (after combat).

**Pitfalls:**
- No rest sites in long dungeons — encounters become a war of
  attrition.
- Too many rest sites — pacing collapses; no resource pressure.
- Rest sites with no narrative purpose.

---

## 9. Lair / Boss

**Purpose:** The climactic encounter. Theme-defining. Where the
dungeon's premise pays off.

**Design considerations:**
- The lair should be **the most themed room.** Every visual,
  sensory, and iconographic element of the dungeon culminates
  here.
- The boss should **act in concert with the room** — lair
  actions, terrain manipulation, summoned minions, environmental
  hazards keyed to the boss's identity.
- Include **alternative win conditions** beyond killing the boss:
  destroy the relic, complete the counter-ritual, free the
  bound entity, survive until reinforcements arrive.

**Lair-specific 5e 2024 features:**
- **Lair actions** — environmental effects on initiative count 20
  (lose initiative ties).
- **Regional effects** — narrative environmental changes (visible
  *outside* the dungeon, signaling the boss's presence).
- **Legendary actions** — for tougher solo bosses.

**Subtypes:**
- **Throne / sanctum** — boss is enthroned; the encounter is
  ceremonial, with possible parley.
- **Ritual chamber** — boss is mid-ritual; interrupting is the
  objective.
- **Hunting lair** — boss is a predator; the room is its territory.
- **Workshop / forge** — boss is creator-type; tools and projects
  in the room can be weaponized or stolen.
- **Sealed vault** — boss is sealed away; the party may release
  *or* re-seal.

**Pitfalls:**
- Boss in an empty room with no environmental support.
- No alternative win condition — boss must be killed.
- Boss with no thematic connection to the rest of the dungeon.

For full monster design, use `monster-creator`.

---

## 10. Ritual / Set-Piece

**Purpose:** Interactive multi-turn scene with objective beyond
combat. Often time-pressured.

**Design considerations:**
- A ritual scene has **a clock.** A ritual completes in X rounds
  unless interrupted. A prison fills with water in Y rounds.
  The portal closes after Z rounds.
- Include **multiple win conditions:** stop the ritual, save the
  prisoner, escape with the relic, prevent the summoning.
- Include **complications:** monsters arrive on round 3; the
  altar must be physically reached; a sacrifice approaches.

**Subtypes:**
- **Ritual interruption** — stop the cult before they finish.
- **Escape scene** — get out before the dungeon collapses /
  floods / seals.
- **Defense scene** — hold a position until reinforcements
  arrive.
- **Object retrieval under pressure** — grab the relic before
  the room is destroyed.
- **Time-pressured negotiation** — convince the NPC before they
  act / die.

**Pitfalls:**
- No actual time pressure — clock has no teeth.
- Single solution path — only one way to "win."
- Scene resolves in one initiative round (no multi-turn drama).

---

## Mix Ratios by Dungeon Scale

| Function | 5-room | Small (10–15) | Full (16–25) |
|---|---|---|---|
| Entrance | 1 | 1 | 1 |
| Combat | 1 | 3–5 | 5–7 |
| Puzzle / Lock | 0–1 | 1–2 | 2–3 |
| Trap | 0–1 | 1–2 | 2–4 |
| Treasure | 1 | 2–3 | 3–4 |
| Transition | 0 | 1–2 | 2–4 |
| Social / NPC | 0–1 | 1–2 | 2–4 |
| Rest / Safe | 0 | 1 | 1–2 |
| Lair / Boss | 1 | 1 | 1–2 (with mini-boss) |
| Ritual / Set-piece | 0 | 0–1 | 1–2 |

Treat as guidelines, not quotas. The premise of the dungeon may
shift the ratio — a haunted tomb leans trap-heavy; a thieves'
guild leans social and stealth; a war-fortress leans combat.

---

## French Vocabulary

For French-language dungeons, the standard function labels:

| English | French |
|---|---|
| Entrance / Threshold | Entrée / Seuil |
| Combat | Combat / Affrontement |
| Puzzle / Lock | Énigme / Verrou |
| Trap | Piège |
| Treasure / Reward | Trésor / Récompense |
| Transition | Transition / Couloir |
| Social / NPC | Rencontre sociale / PNJ |
| Rest / Safe | Repos / Sanctuaire |
| Lair / Boss | Repaire / Boss |
| Ritual / Set-piece | Rituel / Scène-clé |
