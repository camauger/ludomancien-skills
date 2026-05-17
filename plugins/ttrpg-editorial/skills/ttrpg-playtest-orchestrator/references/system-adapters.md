# System Adapters

The mechanical audit (pass 1) is system-specific. Different systems break in
different ways. This reference gives the calibration data and pass-1
checklists per system family.

If the system is hybrid or not listed, fall back to **Generic narrative** mode
and flag mechanical concerns qualitatively rather than numerically.

---

## D&D 5e 2024 (default)

### Reference math

**Encounter difficulty (2024 DMG, encounter budget per PC by level):**

| Level | Low | Moderate | High |
|---|---|---|---|
| 1 | 50 | 75 | 100 |
| 2 | 100 | 150 | 200 |
| 3 | 150 | 225 | 400 |
| 4 | 250 | 375 | 500 |
| 5 | 500 | 750 | 1100 |
| 6 | 600 | 1000 | 1400 |
| 7 | 750 | 1300 | 1700 |
| 8 | 1000 | 1700 | 2100 |
| 9 | 1300 | 2000 | 2600 |
| 10 | 1600 | 2300 | 3100 |
| 11-14 | scaled, see DMG |
| 15-20 | scaled, see DMG |

Multiply by number of PCs for the party budget. Sum the monster XP and compare.

**Save DC ranges (effective, by tier):**

| Tier | Levels | Typical save DC | Hard save DC |
|---|---|---|---|
| 1 | 1-4 | 11-13 | 14-15 |
| 2 | 5-10 | 13-15 | 16-17 |
| 3 | 11-16 | 15-17 | 18-19 |
| 4 | 17-20 | 17-19 | 20-22 |

A DC outside its tier band is a finding. DC 18 for a tier-1 scenario is
near-impossible without optimization; DC 12 at tier 3 is trivial.

**Damage expectations.** A tier-1 PC has roughly 25-40 HP. Single-hit damage
above 20 is a likely two-shot. A boss that deals 35+ in one round to one PC
at tier 1 needs a flag.

**Action economy.** With four PCs, the party gets ~6-8 actions per round
counting bonus actions. A solo boss without legendary actions, legendary
resistance, or minions usually gets one action per round and loses fast.
Flag any boss fight where the opposing side has fewer than 3 turns per
round counting all sources.

### Pass-1 checklist

- [ ] Every combat encounter has computed XP; flag any that fall outside the
      Low–High band for the party.
- [ ] Every save DC falls within the tier band; flag outliers.
- [ ] Boss fights have ≥3 turns/round on the opposing side OR legendary
      actions/resistance.
- [ ] No single-hit damage exceeds 2× PC HP at the target level.
- [ ] No save-or-suck (Hold Person, Banishment, etc.) without counterplay
      against single boss.
- [ ] Skill DCs fall within 10 (easy) / 15 (medium) / 20 (hard) / 25 (very
      hard) bands and the scenario states which.
- [ ] Hazard damage is calibrated to the tier (1d6 trap at level 12 is
      pointless).
- [ ] Short rest opportunities match encounter density (Warlocks, Monks need
      short rests).
- [ ] The party's expected daily resource budget is not blown by encounter 1.

---

## D&D 5e 2014

Same structure as 2024, but use the 2014 encounter-budget table (Easy/Medium/
Hard/Deadly with encounter multipliers for number of monsters). Save DC
ranges are similar. Action economy concerns are sharper — pre-2024 solo
bosses without legendary actions are weaker, flag aggressively.

---

## OSR (B/X, OSE, Knave, Cairn, Mausritter, Into the Odd, Mörk Borg)

### Philosophy

OSR systems are attrition-focused. Lethality is high, character HP is low,
resources matter. The mechanical audit asks different questions than 5e.

### Pass-1 checklist

- [ ] Lethality calibration: is the deadliest encounter survivable by a fresh
      party, or only by an attrited party with no resources? Both are valid
      design, but they should be intentional.
- [ ] Resource attrition curve: torches, rations, HP, spell slots. By the
      "midpoint" scene, how much has the party spent?
- [ ] Fail-forward: every check that gates progress has a fail-state that
      keeps the fiction moving (cost, complication, alternate route).
- [ ] No-skill-check zones: classical OSR avoids skill check density. Are
      there scenes that reduce to "roll a check" when player creativity should
      be the path?
- [ ] Dungeon/hexcrawl turn budget: do declared distances and rest rules
      match the scenario's intended duration?
- [ ] Reaction rolls, morale rolls, encounter checks: are they prescribed
      where the system expects them?
- [ ] Treasure-as-XP economy (if applicable): does the loot match the level
      of advancement the scenario implies?
- [ ] Random tables (encounters, weather, complications): does the scenario
      use them where the system expects them?

### Specific notes

- **Knave / Cairn / Into the Odd** — slot-based inventory. Flag any scene
  that gives the party more than 1-2 significant items without a slot-budget
  consideration.
- **Mörk Borg** — apocalyptic tone is a system feature; flag scenes that
  break tone without intent.
- **Mausritter** — small-scale, tactile. Flag scenes that scale to D&D-sized
  threats.

---

## PbtA (Apocalypse World, Monsterhearts, Masks, Monster of the Week, etc.)

### Philosophy

PbtA is move-driven and conversation-driven. Mechanical audit is about
**MC technique** rather than numerical balance. The MC has principles and
moves; the playtest checks that the scenario gives the MC opportunities to
use them well.

### Pass-1 checklist

- [ ] Threat clarity: every threat in the scenario has a stated type (Affliction,
      Brute, Warlord, etc. per the system) and impulse.
- [ ] MC move opportunities: silences in the scenario where the MC must make
      a soft or hard move — are they signposted? Is there enough threat ammunition?
- [ ] Snowball danger: does failure in scene N raise the stakes in scene N+1
      automatically, or does the scenario need explicit escalation rules?
- [ ] Countdown clocks (where the system supports them): are slopes legible
      and do they tick on appropriate triggers?
- [ ] Principles adherence: does the scenario implicitly violate principles
      (e.g., "name everyone, make them human" violated by faceless mooks)?
- [ ] Playbook engagement: every playbook gets at least one scene where
      their moves are likely to come up. (Monsterhearts: every Skin gets a
      scene engaging their darkest self.)
- [ ] Custom moves: if the scenario introduces them, are triggers and
      outcomes clear?

---

## FitD (Forged in the Dark — Blades, Scum & Villainy, Band of Blades, etc.)

### Philosophy

FitD is clock-and-flashback driven. Crew tier matters, position/effect
matters, downtime matters. Mechanical audit asks structural questions about
clocks and faction tiers.

### Pass-1 checklist

- [ ] Faction tier vs. crew tier: are oppositions calibrated, or set up to
      be impossible/trivial?
- [ ] Score structure: is the score "the right size" — a fortune roll, a
      single score, or a multi-stage operation? Does the scenario know which?
- [ ] Clock slope: how many tick-events per scene? Are slopes legible and
      paced?
- [ ] Position/effect calibration: are starting positions stated explicitly
      or left to GM improvisation?
- [ ] Downtime budget: if the scenario consumes downtime activities (heal,
      reduce heat, etc.) does it state the budget?
- [ ] Heat consequences: does the scenario foreshadow heat outcomes or just
      drop them on the crew?
- [ ] Engagement roll considerations: position modifiers for the engagement
      stated?
- [ ] Faction relationship swings: do they update at end-of-score per system
      expectations?

---

## Generic Narrative (Fate, Cortex, Fiasco, GMless, story games)

When the system is narrative-first or unfamiliar, skip pass 1's numerical
component and run only the **structural** audit:

- [ ] Premise clarity: can the GM and players state the premise in one
      sentence?
- [ ] Scene flow: does every scene end with something different from where
      it began?
- [ ] Stakes legibility: at every decision point, do the players know what's
      at risk?
- [ ] Resolution support: does the scenario give the system's resolution
      mechanics (aspects, traits, dice pools, whatever) enough to bite on?
- [ ] Endgame: does the scenario have a clear shape for closure (climax,
      epilogue, scene rotation), or does it expect the table to find one?

Flag concerns qualitatively. Don't fake numerical findings for a system
that doesn't use numbers in the way 5e does.

---

## Inference Cues

If the user hasn't specified a system, infer from:

- **Stat blocks with AC, HP, CR** → 5e family. Check for "saving throw" /
  "advantage" → 5e. Look for "Bonus Action" wording → 2024.
- **Stat blocks with HD, THAC0 or descending AC** → B/X / OSE / classic D&D.
- **Stat blocks with d20 + d6 damage + no skill list** → Knave / Cairn /
  Into the Odd family.
- **Stat blocks named as "Threats" with a type and impulse** → PbtA.
- **Mention of "clocks," "position/effect," "load," "stress,"** → FitD.
- **Aspects, fate points** → Fate.
- **No stat blocks, just narrative** → Generic narrative, possibly story game.

If two cues conflict (e.g., 5e + custom narrative rules), ask once. Don't
guess silently.
