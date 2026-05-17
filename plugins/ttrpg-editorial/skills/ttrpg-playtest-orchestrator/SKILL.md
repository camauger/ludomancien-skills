---
name: ttrpg-playtest-orchestrator
description: >
  Run a full multi-pass playtest of a TTRPG scenario before publication or before
  running it at the table. Orchestrates four passes: (1) mechanical audit
  system-adapted (5e 2024, OSR, narrative PbtA/FitD), (2) simulated playthrough
  with 4-5 player personas producing a real transcript with branching decision
  points, (3) per-persona feedback in voice, (4) cross-referenced synthesis with
  severity-graded findings and ranked top fixes. Use on "playtest mon scénario",
  "simule une partie", "joue ce module", "fais-moi un playtest", "audit avant
  publication", "comment ça va se passer à la table", "trouve les trous", "stress
  test ce module", "what breaks at the table", "test before DriveThruRPG release",
  or any request to evaluate a scenario through simulated play rather than pure
  editorial review. Also triggers when the user wants to see how an adventure
  holds up under different player archetypes, or wants a transcript-style
  preview of a session. NOT for editorial manuscript review (use
  ttrpg-supplement-reviewer), creation (use scenario-writer), or cliché audit
  (use ttrpg-cliche-buster). This skill simulates play; it does not write or
  rewrite content.
---

# TTRPG Playtest Orchestrator

Run a structured, multi-pass playtest of a scenario, module, or one-shot. The
goal is to surface what only emerges from play — pacing sag, illusory choices,
information bottlenecks, persona mismatches, mechanical mis-calibrations — not
to review the manuscript as prose. This is the **playtest layer**; editorial
review is `ttrpg-supplement-reviewer`.

The orchestrator runs four passes and produces a single synthesized report.
Each pass has a narrow job. They do not duplicate each other.

---

## Before You Begin

1. **Identify the system.** Default is D&D 5e 2024. If the scenario uses another
   system (OSR family, PbtA, FitD, generic narrative), load the relevant section
   of `references/system-adapters.md`. If unclear, infer from stat blocks and
   terminology; if still unclear, ask once.
2. **Identify the party.** Without a party comp, the mechanical pass is
   guesswork. Default: 4 PCs at the level the scenario targets, mixed roles. If
   the user has a real party, use it.
3. **Identify the focus.** Three modes — `full` (all four passes, the default),
   `quick` (mechanical + synthesis only, ~5 min), `narrative` (playthrough +
   persona feedback + synthesis, skip mechanical). The user can override.
4. **Load `references/personas.md`** for the five player archetypes used in
   passes 2 and 3.

---

## The Four Passes

### Pass 1 — Mechanical Audit

**Job:** find numerical and structural problems that a competent GM would only
notice after running it.

System-adapted. For 5e 2024: CR vs. party APL, encounter XP budget vs. daily
adventuring day budget, save DC ranges by tier, action economy of opposing
forces, expected damage vs. party HP pool, save-or-suck without legendary
resistance, skill DC calibration, hazard math. For OSR: HD math, resource
attrition curve, lethality calibration, fail-forward gaps, no-skill-check zones,
hexcrawl/dungeon turn budget. For PbtA: clock pacing, MC moves at every silence,
snowball danger, threat type variety, principles adherence. For FitD: clock
slope, faction tier vs. crew tier, position/effect calibration, downtime budget.

Each finding gets a **severity**: `critical` (will break the session),
`high` (will frustrate players or the GM), `medium` (will dull a scene),
`low` (taste/polish), `note` (observation, no action required).

Each finding gets a **location** (scene, NPC, room, encounter name) and a
**concrete fix proposal** (not "rebalance this fight" but "drop the bandit
captain's HP from 65 to 48 and remove the third minion").

Output: list of `Finding` objects. Typically 8-25 findings for a one-shot,
20-60 for a full module.

### Pass 2 — Simulated Playthrough

**Job:** produce a real transcript of the scenario being played, with the five
personas making distinct, in-character decisions.

Format: scene by scene. Each scene begins with a one-line GM frame, then the
personas react. At every **decision point** (combat opening, NPC reveal,
mystery clue interpretation, moral dilemma), the simulator considers what
2-3 alternative party choices would plausibly happen and notes which paths
have problems (dead ends, info gaps, soft-locks, redundant outcomes). The
transcript follows the **most likely path**, but notes the alternates in
inline `[BRANCH: ...]` annotations.

Length budget: aim for 1500-3500 words for a one-shot, scaled for longer
modules. Do not produce a verbatim novelization — this is shorthand
transcript with enough texture to feel like a real table.

Detection targets — flag inline with `[FLAG: ...]`:

- A scene where one persona has nothing to do for >2 turns of in-fiction time.
- A clue or piece of info that only one NPC carries (single point of failure).
- A "choice" where all branches converge to the same next scene without
  meaningful change in fiction or fictional position.
- A combat where the party's most likely opening tactic trivializes it.
- A dialogue scene where the NPC has no agenda of their own, just info-dump.
- A pacing gap where the next required action isn't clear to the party.
- A skill check whose failure leaves no path forward.

### Pass 3 — Per-Persona Feedback

**Job:** each persona gives their honest one-paragraph takeaway in voice. Not
"what they did" — that's pass 2 — but **what they thought of the session**.
This is the player-facing layer.

Each persona checks against their own archetype priorities:

- **Maël (Tactician)** — were stakes clear? Did decisions matter mechanically?
- **Salomé (Method Actor)** — was there room for interiority? Did NPCs have
  agendas?
- **Jonas (Power Gamer)** — did encounters reward optimization? Was anything
  trivialized?
- **Inès (Storyteller)** — did the arc land? Did themes resonate?
- **Tarek (Specialist)** — did the scenario reward expertise diversity?

Voice matters: each persona should sound distinct. See `references/personas.md`.
Length: ~120-200 words per persona.

### Pass 4 — Synthesis

**Job:** cross-reference findings from passes 1-3, produce a publication or
table-readiness verdict.

Required sections:

1. **Verdict** — one of: `Ready to run`, `Ready with minor fixes`, `Needs
   targeted revision`, `Needs structural revision`, `Not ready`. One sentence
   justification.
2. **Persona-coverage map** — does every archetype get at least one moment?
   If Storyteller has nothing or Power Gamer has no challenge, flag it here.
3. **Top 5 fixes (ranked)** — actionable, specific, ordered by impact-to-
   effort ratio.
4. **Cross-pass patterns** — if the same problem appeared in mechanical audit,
   transcript, and persona feedback, that's a structural issue. Call it out.
5. **What the scenario does well** — at least three concrete strengths. A
   playtest report that only lists problems is editorially dishonest.

---

## Player Personas

Five archetypes adapted from Robin Laws' player typology, sharpened for this
skill. See `references/personas.md` for full voices and decision heuristics.

| Persona | Archetype | Primary concern |
|---|---|---|
| Maël | The Tactician | Clarity, consistency, meaningful choice |
| Salomé | The Method Actor | Interiority, NPC depth, dialogue space |
| Jonas | The Power Gamer | Mechanical payoff, calibrated difficulty |
| Inès | The Storyteller | Arc, theme, memorable beats |
| Tarek | The Specialist | Spotlight diversity, pillar variety |

The default party for the simulated playthrough is these five at the scenario's
target level. The user can substitute their real party if they want personas
weighted toward the actual table.

---

## System Adapters

Default is D&D 5e 2024. See `references/system-adapters.md` for the full
calibration data and pass-1 checklists per system.

Supported systems:

- **5e 2024** (default) and **5e 2014** — full mechanical pass
- **OSR** (B/X, OSE, Knave, Cairn, Mausritter) — attrition-focused mechanical pass
- **PbtA** (Apocalypse World, Monsterhearts, Masks, etc.) — clock and move-focused pass
- **FitD** (Blades, Scum & Villainy, Band of Blades) — clock slope and downtime pass
- **Generic narrative** — skip mechanical pass entirely, run only 2-4

When the system is hybrid or unfamiliar, run pass 1 in `generic narrative` mode
and flag mechanical concerns qualitatively rather than numerically.

---

## Using the Script

The orchestration logic is in `scripts/playtest_orchestrator.py`. It calls the
Anthropic API once per pass, then synthesizes. Dry-run by default — no API
calls unless `--run` is passed. This matches the project's safety pattern.

```bash
# Dry run: parse input, show what would happen, no API spend
python scripts/playtest_orchestrator.py scenario.md

# Real run, default 5e 2024 party of 4
python scripts/playtest_orchestrator.py scenario.md --run

# Specific system and party
python scripts/playtest_orchestrator.py scenario.md \
    --system osr \
    --party "4 PCs level 3, fighter+thief+cleric+MU" \
    --run

# Quick mode (mechanical + synthesis only)
python scripts/playtest_orchestrator.py scenario.md --mode quick --run

# Output to a specific directory
python scripts/playtest_orchestrator.py scenario.md \
    --output ./playtest-reports/ \
    --run
```

Output is a single Markdown file: `{scenario-name}-playtest-{timestamp}.md`,
plus a `{scenario-name}-playtest-{timestamp}.json` with structured findings
for downstream tooling.

### Inline mode (no script)

The skill works without the script. When invoked in a chat or in Claude Code
without running the Python pipeline, follow the same four-pass methodology by
hand. The output structure (see `references/output-template.md`) is identical.

The script's value is reproducibility and clean separation of passes — useful
when you're playtesting multiple modules in a series and want comparable
reports. For a one-off, inline is fine.

---

## Anti-Patterns

Things this skill must **not** do:

1. **Conflate review with playtest.** "The prose is purple" is a review note,
   not a playtest finding. Playtest findings are about what happens *at the
   table*. If you find yourself writing about word choice, you're in the wrong
   skill.
2. **Generate generic feedback.** "Pacing could be tighter" without a scene
   reference is not a finding. Every finding has a `location`.
3. **Praise-flood.** A report that finds no problems isn't a playtest. If a
   scenario truly is flawless, that's worth saying — but it's vanishingly
   rare, and "I can't find anything" usually means the audit wasn't deep
   enough. Push harder on the persona pass.
4. **Treat the transcript as the deliverable.** The transcript is *raw
   material* for findings. The deliverable is the synthesis. Some users will
   want the transcript visible; others won't. Either is fine, but never let it
   substitute for the synthesis.
5. **Pretend to know the actual party.** If the user hasn't specified one, say
   so in the report — "Simulated with default party, results may vary with
   different comp."
6. **Skip the persona-coverage map.** This is the most useful single artifact
   in the entire report. Modules that look fine on the page often lose one or
   two archetypes entirely.

---

## When to Use Other Skills Instead

- Prose tics or repetitive phrasing across stories → `editorial-tic-auditor`
- Tropes, clichés, predictability → `ttrpg-cliche-buster`
- "Is this publishable on DriveThruRPG?" → `ttrpg-supplement-reviewer`
- Listing strategy, pricing, sales page → `digital-product-evaluator`
- Creating the scenario in the first place → `scenario-writer`
- Read-aloud polish for a specific scene → `read-aloud-crafter`

A common sequence for a pre-publication pipeline:
`scenario-writer` → `ttrpg-cliche-buster` → `ttrpg-playtest-orchestrator` →
`ttrpg-supplement-reviewer` → `digital-product-evaluator`. This skill is the
third step: you've written it, you've checked it isn't generic, now you find
out how it actually plays.
