---
name: adventure-converter
description: >
  Convert TTRPG adventures, scenarios, supplements, and stat blocks between
  fantasy systems. Four paths: (1) D&D 5e 2014 → 5e 2024, (2) D&D 5e →
  Pathfinder 2e, (3) D&D 5e → OSR (B/X, OSE, Shadowdark, generic old-school),
  (4) D&D 5e → narrative-light (PbtA/FitD adaptation notes). For each: audit
  source, build conversion matrix, convert stat blocks and DCs, adjust
  encounter design, document kept/cut/added, deliver a publishable
  target-system document with GM notes. Use on "convert to 5e 2024", "port
  my 5e 2014 module to 2024", "5e to PF2e conversion", "OSR version of my
  scenario", "Shadowdark port", "convertis en 5e 2024", "porte en PF2e",
  "version OSR", "adapte en old-school". Boundary: converts an EXISTING
  adventure (use scenario-writer to create new content). NOT for cross-genre
  conversion (fantasy → sci-fi), NOT for systems outside the four supported
  paths (Call of Cthulhu, Vampire, Mörk Borg — bespoke handling), NOT for
  reverse conversion (target → source is a different discipline once
  warranted).
---

# Adventure Converter

Convert existing TTRPG adventures, scenarios, supplements, and stat blocks
between fantasy systems. The output is what a publisher's conversion editor
would deliver when porting a successful 5e adventure to a new system, or
when updating a 5e 2014 module to 2024 rules.

Conversion is **mechanical, structural, and narrative**. Numbers must
match the target system's math; design assumptions must match the target
system's expectations; tone and pacing must respect the target audience.
A pure stat-block swap is *not* a conversion — it's a translation that
leaves the product feeling wrong at the table.

---

## Scope and Boundary

This skill covers **four conversion paths** with fantasy as the genre on
both sides.

| Path | Direction | Difficulty |
|---|---|---|
| 5e 2014 → 5e 2024 | One edition forward | Easy (most-similar) |
| 5e → Pathfinder 2e | Cross-system, same genre | Hard (different action economy + math) |
| 5e → OSR (B/X, OSE, Shadowdark) | Cross-philosophy | Hard (different assumptions) |
| 5e → Narrative-light (PbtA/FitD adaptation notes) | Cross-philosophy | Light (structural notes only) |

| In scope | Out of scope |
|---|---|
| Adventure modules, scenarios, one-shots | Full system creation |
| Settlement / dungeon / faction supplements | Cross-genre conversion (fantasy → sci-fi) |
| Stat block conversion | Reverse conversion (target → source) |
| Encounter rebalancing | Bespoke systems not on supported list |
| Spell / magic item port (mechanical equivalents) | Granular crunch (subclass equivalence in PF2e — too case-by-case) |
| Treasure / XP / wealth rebalancing | Player-character conversion (a specific PC build → another system) |

**Reverse conversions** (e.g., a PF2e module → 5e) are a different skill
discipline because each target system imposes its own design priors. If
the user wants a reverse conversion, decline politely and suggest
running this skill in reverse-direction manually with caveats.

---

## Before You Begin

Five things to settle before converting:

1. **Source system + edition.** Confirm exactly what is being converted
   FROM:
   - D&D 5e 2014 (PHB / DMG / MM 2014–2023 errata)
   - D&D 5e 2024 (PHB / DMG / MM 2024)
   - Other (refuse if outside supported paths)

2. **Target system + edition.** Confirm exactly what is being converted
   TO:
   - D&D 5e 2024
   - Pathfinder 2e (Remastered baseline)
   - OSR — specify subsystem:
     - **B/X / OSE** — most classic, descending AC, ability checks
       rare, class-as-race optional
     - **Shadowdark** — modern OSR with ascending AC, simplified
       saves, real-time torch tracking
     - **Generic old-school** — uses descending AC, saving-throw
       categories, classic XP-for-gold
   - Narrative-light (adaptation notes only) — specify game (Dungeon
     World, Blades in the Dark, Brindlewood Bay-style, generic
     PbtA)

3. **Scope of conversion.** Three modes:
   - **Full conversion** — every stat block, every DC, every encounter
     rebalanced; structural notes included; deliverable is a
     publishable target-system document.
   - **Mechanical conversion only** — stat blocks and DCs only;
     structure and narrative kept as-is.
   - **Adaptation notes** — GM guidance on running the source
     unchanged in the target system, without full conversion. Used
     when the source has too much system-specific text to convert
     economically.

4. **Target audience.** Who reads the converted document?
   - Long-time players of the target system: lean into target-system
     conventions and vocabulary; minimize source-system traces.
   - Players new to the target system, coming from the source: keep
     some source-system anchoring; add target-system tutorials in
     sidebars.
   - GMs doing personal conversion: terse, mechanical-focused output.

5. **Publication intent.** Is this:
   - A commercial release on DriveThruRPG (full prose, art, layout)?
   - A personal GM port (no publishing intent)?
   - A community-share (free PDF, blog post)?
   This affects how much polish goes into prose vs. raw mechanical
   tables.

If any of these is unclear, ask before converting. Source/target
mismatch is the most common failure mode of bad conversion.

---

## The Conversion Workflow

Every conversion passes through six phases.

### Phase 1 — Source Audit

Inspect the source document to inventory what needs conversion.

Build an inventory:

| Element | Count | Notes |
|---|---|---|
| Stat blocks (unique monsters / NPCs) | N | List by page / name |
| Stat blocks (existing-in-MM) | N | List name; source-system page reference |
| DCs (Investigation, Perception, Persuasion, etc.) | N | List each unique check |
| Spells referenced by name | N | List with mechanical relevance |
| Magic items | N | Distinguish standard (in DMG) vs custom |
| Encounter calibration markers (CR, XP budget, party-level recommendations) | N | List |
| Trap statistics | N | List |
| Treasure totals (gp, gems, magic items) | N | Total value |
| System-specific rules invoked (advantage, inspiration, exhaustion levels, etc.) | N | List with context |
| References to other source-system books | N | List for replacement |

Document **what's mechanical** vs **what's narrative**:
- Narrative content (descriptions, NPC personalities, plot, lore,
  read-aloud) converts with zero mechanical changes; the system-
  specific labels get swapped (DC X check → target-system equivalent).
- Mechanical content (stat blocks, encounter math, treasure tables)
  needs full conversion with target-system math.

### Phase 2 — Conversion Matrix

Build the conversion matrix — the explicit mapping from source-system
mechanics to target-system equivalents. Load the appropriate references
file:

- 5e 2014 → 5e 2024: `references/5e-2014-to-2024-deltas.md`
- 5e → PF2e: `references/5e-to-pf2e-mapping.md`
- 5e → OSR: `references/5e-to-osr-translation.md`
- Mechanical tables (XP, treasure, AC, DCs across all paths):
  `references/mechanical-conversion-tables.md`

The matrix specifies, for each source element:
- What it becomes in the target system (or is dropped).
- Why (cite the target system's design philosophy).
- Whether it requires GM-side handling vs being baked into the
  conversion.

**Example matrix entries:**

| Source (5e 2014) | Target (5e 2024) | Notes |
|---|---|---|
| Advantage on Dex (Stealth) | Same | No change |
| Hide action vs Stealth check | New: explicit Hide action with DC 15 default | Use 2024 Hide rules — clearer trigger |
| Disengage as Action | Same | No change |
| `bonus action` (lowercase legacy) | `Bonus Action` (capitalized 2024) | Format-level change |
| Cleric Channel Divinity 2/short rest | Cleric Channel Divinity 3/short rest (lvl 2+) | Mechanical buff in 2024 |

| Source (5e) | Target (PF2e) | Notes |
|---|---|---|
| AC 15 medium armor | AC 17 medium armor (PF2e level adjustment for level 1) | PF2e AC scale baseline +2 |
| DC 15 Perception check | DC 16 (Trained), DC 18 (Expert) — PF2e is level-scaled | Use PF2e DC table |
| 4d6 fireball | 6d6 (PF2e baseline is higher dice count at level) | PF2e damage scaling |
| Concentration | Sustained spell / Concentrate trait | PF2e has different action cost |
| Spell slot | Spell slot (but PF2e has heightening per level, not at-higher-level) | Heighten conversion |

### Phase 3 — Mechanical Conversion

Convert each stat block, DC, spell reference, magic item, and encounter
math element.

**Stat block conversion (general protocol):**

1. **Identify the monster's role and CR** in the source system.
2. **Find or create the target-system equivalent:**
   - 5e 2014 → 2024: most monsters have 2024 versions; use them
     directly if available. If unique custom, convert in place.
   - 5e → PF2e: use Bestiary equivalents where they exist; else
     build PF2e stat block at equivalent CR-to-level mapping.
   - 5e → OSR: use OSR reference monster at equivalent HD; collapse
     to simpler stat block.
3. **Preserve identity:** the converted monster should feel like the
   same creature, not a generic equivalent.
4. **Apply target-system math:** AC, HP, saves, attacks, damage,
   special abilities use target-system formulas.
5. **Convert special abilities:** named abilities may keep their
   names; rewrite mechanics to target-system rules. If an ability
   doesn't translate (e.g., a 5e "Once per long rest" → PF2e where
   long rest is different), pick the closest target-system pattern.

**DC conversion:**
- 5e 2014 → 2024: same DC scale, mostly unchanged. Update phrasing
  to 2024 conventions.
- 5e → PF2e: use PF2e level-based DC table (see
  `mechanical-conversion-tables.md`).
- 5e → OSR: collapse to OSR's coarser scale (often ability check
  on d6 or roll-under attribute, or specific saving throw category).

**Spell conversion:**
- 5e 2014 → 2024: most spells unchanged; some renamed or rebalanced.
  Cite 2024 PHB version.
- 5e → PF2e: find PF2e equivalent (most fantasy staples exist),
  heighten to closest level. Some spells don't exist directly (use
  closest functional equivalent).
- 5e → OSR: OSR spells are coarser; "Fireball" exists in most OSR
  systems but with different damage scaling. Use OSR spellbook.

**Magic item conversion:**
- 5e 2014 → 2024: rare changes; some items rebalanced.
- 5e → PF2e: PF2e has a different rune system; convert items as
  appropriate equivalents (a +1 sword becomes a striking rune
  weapon).
- 5e → OSR: simplify items; OSR magic items rarely have charges,
  attunement, or complex mechanics.

**Encounter rebalancing:**
- 5e 2014 → 2024: CR table mostly unchanged; encounter difficulty
  thresholds (Easy/Medium/Hard/Deadly → Low/Moderate/High in 2024)
  adjusted.
- 5e → PF2e: use PF2e encounter budget (XP threshold per party
  level, severity tiers Trivial/Low/Moderate/Severe/Extreme).
- 5e → OSR: encounters are HD-based, with fewer creatures often
  more deadly. Calibrate to OSR's deadlier baseline.

### Phase 4 — Structural Conversion

Mechanical conversion alone leaves the product feeling wrong. Structural
conversion adjusts design assumptions.

**5e 2014 → 5e 2024 structural deltas:**
- Background reframing (2024 backgrounds grant ability score increases
  + a feat; this changes encounter difficulty by ~+1 XP level
  effective).
- Weapon Mastery system requires combat encounters to be tested
  against new options.
- Free castings of certain spells (Hex, Hunter's Mark) once per long
  rest expand expected damage per encounter.
- Inspiration source changes — table inspiration tokens vs Heroic
  Inspiration mechanics.

**5e → PF2e structural deltas:**
- Three-action economy reshapes every combat. A 5e encounter expects
  one attack + Bonus Action; a PF2e encounter expects 3 attacks (with
  Multiple Attack Penalty cascading: -0/-5/-10) or 2 attacks + 1
  movement / 1 spell / 1 utility action.
- Skill DCs are level-based; flat "DC 15 Perception" doesn't translate.
- Traits replace stacking rules — every spell/feat/condition has
  trait tags that determine how it interacts.
- Conditions are graded (Frightened 1, Frightened 2, etc.) not binary.
- Critical success/failure: rolling 10 above DC = critical success;
  10 below = critical failure. This dramatically changes save-vs-die
  effects.

**5e → OSR structural deltas:**
- "Rulings, not rules" — most non-combat resolution is GM fiat with
  ability check or saving throw, not skill systems.
- Lethality is dramatically higher. A 5e Easy encounter is an OSR
  TPK risk. Calibrate encounters to OSR norms (1-2 monsters of
  party-level HD).
- HP totals are much lower (4d6+4 ogre, not 7d10+14).
- Treasure is gameplay, not reward — XP-for-gold incentivizes risk-
  vs-reward decisions about taking treasure that's hard to extract.
- Long rest concept doesn't exist; resource depletion across sessions
  is real.
- Save categories (Death, Wands, Paralysis, Breath, Spells) not
  ability saves.

**5e → Narrative-light:**
- Stats become **moves** with triggers.
- DCs become **threshold trigger language** ("On a 7-9, complicate
  the success").
- Combat becomes **dramatic conflict** with stakes negotiation,
  not turn-based math.
- This is rarely a full conversion; usually adaptation notes.

### Phase 5 — Narrative Polish

Convert the prose to match target-system conventions and audience
expectations.

**Vocabulary swaps:**
- 5e 2014 → 2024: minor terminology updates (e.g., "race" → "species",
  "Lawful Good" → species + alignment optional, etc.).
- 5e → PF2e: target-system vocabulary (Strike instead of attack
  roll context, Skill Increase instead of skill rank, Ancestry +
  Heritage instead of race + subrace, etc.).
- 5e → OSR: simpler vocabulary; cut "skill check" references
  except where mapped to ability check / saving throw.

**Read-aloud preservation:**
Read-aloud text *should not* change beyond removing system-specific
mechanical interjections. Atmospheric prose is system-agnostic.

**Sidebar additions:**
For audiences coming from the source system, add sidebars explaining
target-system mechanics that differ significantly (e.g., a sidebar
explaining PF2e's three-action economy to 5e converts).

**Cut content:**
Some source content doesn't translate and should be cut:
- 5e → PF2e: "long rest" mechanics that don't map cleanly.
- 5e → OSR: complex feat-stacking sequences.
- 5e 2014 → 2024: anything explicitly deprecated.

Document **what was cut and why** in the converter's notes.

### Phase 6 — Deliverable Assembly

Produce the converted document plus a **conversion notes** appendix.

The converted document is laid out exactly like the source, with
mechanics replaced. The conversion notes appendix is GM-facing and
documents:

- **What was kept** (narrative content, structure, encounter beats).
- **What was changed** (specific stat block conversions, DC
  recalibrations, with examples).
- **What was cut** (and why).
- **What was added** (sidebars, target-system tutorials, new
  mechanical content).
- **Open issues / GM judgment calls** (places where the conversion
  was approximate and the GM should adjust at their table).
- **Errata pointers** if source has known errors that affect the
  conversion.

---

## Output Format

Convert the source document section by section. Use this overall
structure for the deliverable:

```markdown
# [Original Title] — [Target System] Conversion

*Converted from [Source System] to [Target System].*

## Conversion Notes (GM-facing)

### What This Document Is
[1 paragraph: source identity + target system + scope of conversion.]

### Conversion Scope
- Full mechanical conversion: [yes / no]
- Structural adjustments: [yes / no, with which deltas applied]
- Narrative polish: [yes / no, with vocabulary updates]

### Key Conversion Decisions
- [List of significant judgment calls with rationale.]

### What Was Cut
- [List with reasons.]

### What Was Added
- [List with reasons — sidebars, tutorials, etc.]

### Open Issues
- [Areas where the conversion is approximate; GM should adjust.]

---

[Converted document content — section by section, matching source
structure, with mechanics replaced and prose updated.]

---

## Appendix A — Conversion Matrix

[The full source → target mapping table, for reference.]

## Appendix B — Stat Block Crosswalk

| Source Stat Block | Target Stat Block | Page Reference |
|---|---|---|
| [name] | [name in target system] | [page in target system or "custom in this doc"] |

## Appendix C — Errata / Open Questions

[Anything the converter flagged for follow-up.]
```

**Language:** Match the language of the brief and the source document.
If the source is in English and the brief is in French, ask whether the
output should be in source-language or target-language (typically
target-system communities have a dominant language).

**Tone:** Match the converted document to the target system's
publication conventions. PF2e community tends toward precision and
crunch; OSR community tends toward brevity and rulings-language; 5e
2024 tends toward polished evocative prose.

---

## Path-Specific Adjustments

### 5e 2014 → 5e 2024

- **Workload:** Light to medium. Most content survives unchanged.
- **Focus areas:** Background reframing, weapon mastery integration,
  new initiative rules, updated spell list, condition wording.
- **Common conversion pitfalls:** Forgetting to update 2014's
  "races" terminology to 2024's "species"; missing rebalanced
  spells (Banishing Smite, Conjure spells reworked); leaving Bonus
  Action wording lowercase in 2024 stat blocks.

### 5e → PF2e

- **Workload:** Heavy. Action economy reshapes every combat encounter.
- **Focus areas:** Three-action conversion, trait tagging, level-
  based DCs, encounter budget recalibration, condition grading.
- **Common conversion pitfalls:** One-to-one stat block conversion
  ignoring PF2e's MAP cascade; flat DCs not level-scaled; missing
  critical-success/failure 10-point swings; treating PF2e Strike as
  5e attack.

### 5e → OSR

- **Workload:** Medium, but conceptually heavy. Design philosophy
  shifts.
- **Focus areas:** HP reduction, simplified stat blocks, ability-
  check-as-rulings, treasure-as-XP, mortal-stakes encounter
  calibration, dungeon procedure (light tracking, encounter rolls).
- **Common conversion pitfalls:** Keeping 5e HP levels (kills the
  OSR feel); over-translating skill checks to ability checks (most
  resolution is GM fiat); ignoring XP-for-gold motivation reframing.

### 5e → Narrative-light

- **Workload:** Often "adaptation notes" only — the source isn't
  fully reskinned, just contextualized.
- **Focus areas:** Convert encounters to "stakes & threats", convert
  stat blocks to "playbook moves with conditions/clocks", convert
  treasure to "narrative reward". Document the source's
  procedural-vs-narrative tension.
- **Common conversion pitfalls:** Trying to do a full conversion
  (rarely worth it); failing to flag what the GM should improvise
  vs play by the book.

---

## Interaction with Other Skills

- **Audit the source before converting** → run
  `ttrpg-supplement-reviewer` on the source if it has unknown
  quality; bad sources convert badly.
- **Mechanical-only audit on converted stat blocks** → run
  `stat-block-validator` after conversion (for 5e 2024 target only,
  initially) to catch math errors.
- **Custom monster in source that converts to custom in target** →
  run `monster-creator` on the target-system version, then
  reference here.
- **Custom spell in source converts** → run `spell-creator` on the
  target-system version, then reference here.
- **Conversion is a step in publishing on DriveThruRPG** → run
  `digital-product-evaluator` on the converted listing.
- **Read-aloud conversion** → run `read-aloud-crafter` if the source's
  read-aloud needs polish on the target side.
- **Cliché audit of converted content** → run `ttrpg-cliche-buster`
  on the result; conversion sometimes exposes clichés that the
  source masked with system-specific flavor.
- **Originality / branding** → if the conversion is a paid commercial
  release, verify license compatibility (see Edge Cases).

---

## Edge Cases

**Source uses copyrighted IP** (Forgotten Realms, Eberron, specific
named NPCs / locations from official sources): the converter should
preserve narrative IP only if the user has license / fair use /
homebrew rights. For commercial publishing, advise the user to use
generic equivalents or obtain license.

**Source is itself a conversion** (e.g., the user's 5e module is
already a conversion of a 1e adventure): convert the current source,
not the upstream original. Note the chain in conversion notes.

**Source contains broken mechanics** (CR mismatches, math errors,
unclear rules): fix in the conversion. Document fixes in conversion
notes as "errata applied during conversion."

**Source has system-specific mechanics with no target equivalent**
(e.g., 5e Battle Master maneuvers → OSR; 5e Sorcery Points → PF2e):
provide the closest functional equivalent + a sidebar explaining
the design intent so the GM understands what was preserved.

**Source has very large scope** (hardcover-length adventure): break
into chapters, convert chapter by chapter, deliver iteratively.
Don't try to convert a 200-page adventure in one pass.

**Target system has multiple sub-systems** (OSR — B/X, OSE,
Shadowdark, Dolmenwood, Old-School Essentials all differ): commit
to one sub-system per conversion. Don't try to make the output
work for all OSR variants — pick one and note compatibility in
notes.

**Target system is in playtest / new edition** (PF2e Remastered
post-OGL changes, 5e 2024 still rolling out): cite which edition's
ruleset is the target, and note that future errata may affect the
conversion.

**Reverse conversion request** (PF2e → 5e, OSR → 5e, 5e 2024 → 5e
2014): defer. Each reverse direction has its own design priors.
Either decline politely or warn the user that the output will be
approximate and require their own validation.

**Multi-target conversion** (release the same product in 5e 2024 +
PF2e + OSR simultaneously): run this skill once per target.
Coordinate the narrative content (which doesn't change) so the
three documents share the same prose.

**System without a clean conversion path** (Call of Cthulhu,
Vampire: the Masquerade, Mörk Borg, Mothership): refuse / defer.
These systems aren't fantasy-mechanics-compatible with the supported
paths. Cross-genre / cross-feel conversion is a dedicated
discipline.

**Adult / mature content in source**: preserve as-is in the
conversion. Adult themes are content, not mechanics, and don't need
target-system rebalancing beyond what's required by the system's
own conventions.

---

## Publication Checklist

Before considering a conversion complete:

- [ ] Source system + edition confirmed in conversion notes.
- [ ] Target system + edition confirmed in conversion notes.
- [ ] Conversion scope declared (full / mechanical / notes).
- [ ] Inventory of source elements (stat blocks, DCs, spells,
      items, encounters) complete.
- [ ] Conversion matrix produced and referenced.
- [ ] Every stat block converted to target-system math.
- [ ] DCs recalibrated per target-system table.
- [ ] Encounters rebalanced per target-system budget.
- [ ] Structural deltas addressed (action economy, save semantics,
      etc.).
- [ ] Vocabulary updated to target-system conventions.
- [ ] What was cut / added documented in conversion notes.
- [ ] Open issues flagged for GM judgment.
- [ ] Stat block crosswalk appendix complete.
- [ ] License / IP issues flagged.
- [ ] For commercial release: target-system community conventions
      respected (forum vocabulary, art conventions, layout
      norms).

---

## Reference Files

Load as needed — not all at once.

- `references/5e-2014-to-2024-deltas.md` — Complete mechanical
  delta between 5e 2014 and 5e 2024: new rules (initiative,
  weapon mastery, exhaustion levels, new Hide/Search actions, new
  unarmed strike rules), revised classes and subclasses (Cleric
  Channel Divinity, Wizard subclass features, Sorcerer Sorcery
  Points), revised spells (renamed, rebalanced, dropped), revised
  monster CR (some monsters changed CR), revised conditions,
  revised exhaustion. Format-level deltas (stat block layout,
  vocabulary like "race" → "species", "Bonus Action" capitalized).
- `references/5e-to-pf2e-mapping.md` — System architecture
  comparison: three-action economy, MAP, level-based DCs, trait
  system, condition grading, critical success/failure 10-point
  rule, ancestry+heritage vs race+subrace, class structure, action
  cost conversion table, encounter budget (Trivial/Low/Moderate/
  Severe/Extreme), spell heightening conversion, sustained vs
  Concentration.
- `references/5e-to-osr-translation.md` — OSR sub-systems compared
  (B/X, OSE, Shadowdark, generic old-school): descending vs
  ascending AC, saving throw categories (Death/Wands/Paralysis/
  Breath/Spells in classic; simplified in modern OSR), HP scaling,
  monster HD vs CR, treasure-as-XP, encounter procedure (random
  encounter rolls, reaction rolls, morale), simplified stat
  blocks, dungeon time tracking (turns, torches), spell list
  conversion (most fantasy staples exist), class/race conversion.
- `references/mechanical-conversion-tables.md` — Cross-system tables:
  XP equivalents per CR/level, treasure value conversion (gp scale
  differences), AC/save DC mapping, ability score baseline
  comparison, damage dice scaling by level/tier, monster HP scaling
  (5e vs PF2e vs OSR norms), spell level alignment, encounter
  difficulty mapping (Easy/Medium/Hard/Deadly → Trivial/Low/
  Moderate/Severe/Extreme in PF2e; → not-applicable in OSR where
  it's HD-based).
- `references/tone-and-structure-conversion.md` — Beyond the
  numbers: design assumptions that shift between systems. 5e's
  ability-check-as-skill vs OSR's ability-check-as-fiat. 5e's
  long-rest reset vs OSR's resource attrition. 5e's heroic tone
  vs OSR's gritty stakes. PF2e's precision-heavy structure vs 5e's
  freeform interpretation. Audience expectations per community
  (5e community = broad, casual; PF2e community = crunch-focused;
  OSR community = procedure-and-rulings; narrative community =
  fiction-first). How to write conversion sidebars. When to keep
  read-aloud verbatim vs adjust. What to cut vs add.
