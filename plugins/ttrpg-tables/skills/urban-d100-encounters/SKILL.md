---
name: urban-d100-encounters
description: >
  Generate d100 (or d20–d1000) random encounter tables for dark fantasy cities,
  one theme per table. Themes include combat, social, horror, mystery, erotic,
  ethical, environmental, weird, religious-occult, event, and economic. Outputs
  either compact Markdown d100 tables or expanded seven-field blocks. Also
  orchestrates multi-table product assembly for publication (DriveThruRPG, PDF).
  Use when the user asks for "d100 encounters", "random encounter table",
  "100 encounters for [theme]", "encounter book", "urban encounter generator",
  "city encounters dark fantasy", or references existing encounter files.
  Also triggers on: "batch encounters", "generate encounters", "encounter table
  for [district/theme]", "expand this encounter", "assemble encounter book".
  Do NOT use for wilderness/dungeon encounter tables, single encounter write-ups
  (use scenario-writer), or NPC-only generation (use npc-creator).
---

# Urban d100 Encounter Tables

Generate themed random encounter tables for dark fantasy cities — from single d20 subtables to full multi-theme publication books.

---

## 1. Decide scope

| Scope | What the user wants | Workflow |
|-------|---------------------|----------|
| **Single table** | One d100 for one theme | §2–7 |
| **Subtable** | A d20 or d50 slice | §2–7 (adjust count) |
| **Book assembly** | Multiple themed d100s packaged as a product | §2–8 |
| **Expansion** | Upgrade existing Tier 1 entries to Tier 2–3 | §9 |

Default to **single table, compact format** unless the user specifies otherwise.

---

## 2. Pick theme

Each theme has a **primary job** — the encounter's main beat must belong to that lane.

| Theme | Primary job | Core tension |
|-------|-------------|--------------|
| **Combat** | Violence now or imminent; clear sides; environment complicates | Survival, tactical choice |
| **Social** | Human interaction — commerce, status, favors, grudges | Relationships, reputation |
| **Horror** | Dread, corruption, wrongness; the city is sick | Fear, revulsion, helplessness |
| **Mystery** | Clues, secrets, loose threads; something doesn't add up | Curiosity, paranoia |
| **Erotic / Mature** | Desire, scandal, intimacy, power through seduction | Temptation, vulnerability, taboo |
| **Ethical** | Choice over dice; conflicting goods; no clean answer | Conscience, consequence |
| **Environmental** | Place, weather, architecture, sensory pressure — city as actor | Atmosphere, navigation, endurance |
| **Weird** | Structured wrongness; wonder tinged with unease | Disorientation, awe |
| **Religious / Occult** | Believers, doctrine, rituals, institutional faith, prices | Devotion, hypocrisy, cosmic debt |
| **Event** | Public spectacle, civic ritual, crowd dynamics | Participation, crowd danger, timing |
| **Economic** | Black markets, debt, scarcity, desperate transactions | Greed, desperation, opportunity |

### Theme crossing

Cross **one** secondary theme into ~10–15% of entries for city texture. Use this matrix:

| Primary ↓ / Secondary → | Combat | Social | Horror | Mystery | Erotic | Ethical | Env. | Weird | Relig. | Event | Econ. |
|---|---|---|---|---|---|---|---|---|---|---|---|
| **Combat** | — | ✓ | ✓✓ | ✓ | · | ✓ | ✓✓ | ✓ | ✓ | ✓ | ✓ |
| **Social** | ✓ | — | · | ✓✓ | ✓✓ | ✓ | · | · | ✓ | ✓ | ✓✓ |
| **Horror** | ✓ | · | — | ✓✓ | ✓ | ✓ | ✓✓ | ✓✓ | ✓✓ | · | · |
| **Mystery** | · | ✓✓ | ✓✓ | — | ✓ | ✓ | ✓ | ✓✓ | ✓ | ✓ | ✓ |
| **Erotic** | · | ✓✓ | ✓ | ✓✓ | — | ✓✓ | · | ✓ | ✓ | · | ✓ |
| **Ethical** | ✓✓ | ✓✓ | ✓ | ✓ | ✓ | — | · | · | ✓✓ | ✓ | ✓✓ |
| **Environmental** | ✓ | · | ✓✓ | ✓ | · | · | — | ✓✓ | ✓ | ✓ | · |
| **Weird** | ✓ | · | ✓✓ | ✓✓ | ✓ | · | ✓✓ | — | ✓✓ | ✓ | ✓ |
| **Religious** | ✓ | ✓ | ✓✓ | ✓ | ✓ | ✓✓ | ✓ | ✓✓ | — | ✓✓ | ✓ |
| **Event** | ✓ | ✓✓ | · | ✓ | · | ✓ | ✓ | ✓ | ✓✓ | — | ✓✓ |
| **Economic** | ✓ | ✓✓ | · | ✓ | ✓ | ✓✓ | · | ✓ | · | ✓ | — |

`✓✓` = strong pairing · `✓` = works if done well · `·` = avoid unless deliberately subverting

### Intensity dial

Each theme supports three intensity levels. Declare in YAML frontmatter.

| Level | Label | What it means |
|-------|-------|---------------|
| 1 | **Atmospheric** | Suggestive, implied, background texture |
| 2 | **Confrontational** | Direct, visceral, demands player reaction |
| 3 | **Graphic** | Explicit detail, potentially disturbing, requires content warning |

Theme-specific calibration:

- **Erotic** — L1: innuendo, charged glances, tension. L2: overt desire, partial nudity, scandal with consequences. L3: explicitly sexual, adult-only product, full content warning.
- **Horror** — L1: unease, wrongness, atmosphere. L2: body horror, visible corruption, dread. L3: graphic violence, torture imagery, extreme visceral detail.
- **Combat** — L1: tension and threat. L2: blood, injuries, real danger. L3: graphic mutilation, war-crime-level violence.
- **Ethical** — L1: mild inconvenience dilemma. L2: real sacrifice required, no good option. L3: involves children, slavery, or irreversible harm — handle with care.

---

## 3. Pick output format

| Format | Best for | Structure |
|--------|----------|-----------|
| **Compact** | Fast rolls, stacking tables, smaller products | Single Markdown table, 1–3 sentences per row |
| **Expanded** | Session centerpieces, rich NPCs, premium products | Seven-field blocks per entry, district sections |

Default to **compact** unless the user says "expanded", "Velnaris blocks", "seven-field", or "premium format".

---

## 4. Entry tiers

| Tier | Share | Length | Purpose |
|------|-------|--------|---------|
| **Tier 1 — Vignette** | 60% | 1–2 sentences | Atmospheric flavor, background color, no mechanics |
| **Tier 2 — Developed** | 30% | 3–5 sentences | NPC with motivation, minor hook, optional consequence |
| **Tier 3 — Mini-scene** | 10% | 2–3 paragraphs | Named NPC, clear stakes, multiple resolutions, stat hooks |

---

## 5. Compact format spec

### YAML frontmatter

```yaml
---
title: "[Theme] Encounters — d100"
type: encounter-table
game_system: D&D 5e (2024) | system-agnostic
setting: generic dark city | Velnaris | Zarathar
theme: [primary theme]
intensity: [1|2|3]
status: draft | review | final
language: en | fr
tags: [dark-fantasy, urban, encounters, theme-tag]
content_note: "Required for intensity 2–3 erotic/horror/ethical."
---
```

### Table columns

```markdown
| d100 | Tags | Encounter |
|------|------|-----------|
| 1 | market, guild | Full sentence encounter text. |
```

**Tags** (2–4 per row):
- **District/venue:** `market`, `docks`, `temple`, `slums`, `noble`, `artisan`, `necropolis`, `gate`, `sewer`, `rooftop`, `tavern`, `brothel`, `generic`
- **Channel:** theme-specific qualifier (e.g. `ambush`, `ritual`, `scandal`, `dilemma`, `fog`, `auction`, `corpse`, `omen`)
- **Time** (if relevant): `day`, `night`, `dawn`, `dusk`
- **Danger** (if relevant): `none`, `low`, `medium`, `high`

### Prose rules

- Write **full sentences**, not chains of bolded keywords.
- Use **bold** for one name or one stake per entry, maximum.
- Setting-agnostic by default. Use generic anchors (§7.2). Name Velnaris or Zarathar only when the user specifies.
- Encounters describe **something happening now or about to happen**, not backstory or yesterday's news.
- Rows 1–100 inclusive: no duplicates, no skipped numbers.

### Compact examples by theme

**Combat, Tier 1:**
`| 14 | docks, ambush, night | Two figures drag a third into a warehouse — the victim's heels leave wet streaks on the cobblestones, and a muffled scream cuts short. |`

**Ethical, Tier 2:**
`| 42 | slums, dilemma, day | A landlord's enforcers are bricking shut the doors of a tenement for unpaid rent — with families still inside. The Guard watches from across the street but hasn't moved. A child's face appears at a second-floor window. Intervening means assaulting the landlord's legal agents; doing nothing means watching eviction turn into entombment. The landlord holds contracts signed by the city magistrate. |`

**Weird, Tier 1:**
`| 71 | market, omen | Every fishmonger's stall displays the same species today — a deep-water eel no one in the market can name — and none of them remembers placing an order. |`

**Erotic (L2), Tier 2:**
`| 56 | noble, scandal, dusk | A noblewoman's sedan chair sits abandoned in an alley, curtains torn, perfume still thick in the air. Her signet ring lies on the cushion beside a love letter addressed to someone who is decidedly not her husband. A servant arrives moments later, panicked, offering gold for silence and the letter's return. |`

---

## 6. Expanded format spec (seven fields)

Per entry: number, title, tagline, optional tier/level band.

| Symbol | Field | Purpose |
|--------|-------|---------|
| ► | **Situation** | What the PCs walk into — immediate, active, present tense |
| ◈ | **Sensory** | What they see/hear/smell/feel before they understand |
| ● | **NPC** | Name — role; want; stake (flash method) |
| → | **Hooks** | How PCs get pulled in; 2–3 intervention vectors |
| ◆ | **City fact** | One true detail about law, custom, geography, or faction |
| ◇ | **Gossip** | What NPCs say about this — rumor, opinion, misinformation |
| ∞ | **Recurrence** | What happens if PCs ignore it; faction memory; revenge or gratitude |

### Seven-field examples by theme

**Combat:**
► A Syndicate enforcer pins a debtor against a fountain rim, blade at throat. Two lookouts block the side streets. The debtor sees the PCs and screams for help.
◈ Copper-scented water splashing onto stone. The enforcer's leather coat creaks. A dog barks somewhere above.
● **Maren Koss** — Syndicate collector; wants the debt paid, not blood; will lose standing if she lets the debtor go publicly.
→ Fight the enforcers (3 thugs, AC 12, HP 11). Negotiate — Maren accepts alternative payment. The debtor offers a secret worth more than his debt.
◆ In this district, the Guard does not enter Syndicate disputes. It's considered a private contract matter.
◇ "Koss is reasonable unless you shame her. The last person who did that turned up in the canal."
∞ If PCs help the debtor: Maren remembers faces. If PCs stay out: the debtor vanishes; his shop is boarded up by morning.

**Ethical:**
► A temple orphanage burns. The children are out safe — but a bound prisoner in the cellar is screaming, and the priests aren't moving to help.
◈ Smoke, the crack of timber, the smell of incense burning wrong. The prisoner's voice is raw, barely human.
● **Sister Vael** — orphanage matron; believes the prisoner is possessed; refuses to risk the children by opening the cellar.
→ Enter the cellar (DC 12 Athletics, fire damage). Convince Sister Vael (DC 15 Persuasion). Break through from the alley side (DC 14 Investigation to find the entrance).
◆ The Temple has legal custody of anyone declared "afflicted" — the prisoner may not legally be a prisoner at all.
◇ "They brought someone in last week, chained and hooded. The children weren't told why."
∞ If the prisoner dies: nothing changes publicly, but a noble family begins asking questions two days later. If rescued: the prisoner knows something about the Temple's exorcism practices that the clergy would kill to keep hidden.

**Weird:**
► Every merchant on Candlers' Row is selling the same object today: a brass key with no teeth. None of them remember stocking it.
◈ The keys are warm to the touch. They hum faintly when held near each other. The air smells of ozone and tallow.
● **No single NPC** — the merchants are confused, slightly dazed, cooperative but useless.
→ Buy a key and investigate (Arcana DC 13 reveals residual conjuration). Follow the supply chain (Investigation DC 14: the keys arrived in unmarked crates from the harbor, no manifest). Bring two keys together (they point like compass needles toward the Necropolis).
◆ Candlers' Row normally sells wax, wicks, and lamp oil. No metalwork stall has ever operated here.
◇ "I dreamed of a door last night. Didn't think anything of it until I opened my shop."
∞ If ignored: by nightfall, every key is gone — and every lock on Candlers' Row opens to nothing behind the doors.

**Erotic (L2):**
► A courtesan from the Red Vow stands barefoot on the bridge at dusk, holding an unsigned contract. She has been weeping. She asks the nearest PC to witness her signature — binding her to a patron she clearly fears.
◈ Bare feet on wet stone, kohl-streaked cheeks, the rustle of a silk robe that cost more than most people earn in a year. The contract smells of expensive ink and something sharper — alchemical binding agent.
● **Lysenne** — courtesan; wants a way out she cannot see; will sign if no one gives her a reason not to.
→ Refuse to witness (she signs anyway, alone). Witness and say nothing (complicity). Offer an alternative — money, protection, a name (she'll need proof). Read the contract (DC 14 Investigation reveals a non-compete clause that functionally makes her property).
◆ In this city, witnessed contracts are magically binding. A false witness is punishable by branding.
◇ "The Red Vow sells beauty and obedience. Lysenne was too much of one and not enough of the other."
∞ If PCs help: Lysenne becomes a valuable, fiercely loyal contact with access to the city's most private conversations. If they don't: she vanishes from public life within a week.

---

## 7. Generation workflow

### 7.1 Distribution targets (d100)

Adjust proportionally for other table sizes.

**By tier:**
- Tier 1: 60 · Tier 2: 30 · Tier 3: 10

**By district** (default spread):
- Distribute across 5–7 districts minimum
- No single district exceeds 25% unless the table is district-focused

**By time:**
- Day: 40% · Night: 35% · Dawn: 10% · Dusk: 15%

**By danger** (combat theme shifts upward):
- None: 40% · Low: 30% · Medium: 20% · High: 10%

### 7.2 Setting anchors (generic)

Use these references so GMs can rename for their world:

| Anchor | Represents |
|--------|------------|
| the Guard | City watch, militia, law enforcement |
| the Temple | Dominant religious institution |
| the Guild | Relevant trade or craft guild |
| the Court | Noble authority, aristocratic power |
| the Syndicate | Organized crime network |
| the Order | Religious or military order |
| the Academy | Arcane institution |
| the Council | City government, ruling body |

**Velnaris anchors** (when `setting: Velnaris`): House of Red Vows, the Ashen Court, the Pallid Council, plus district names from published canon.

**Zarathar anchors** (when `setting: Zarathar`): Council of 9 Masks, Artificiers Guild, Eight Forms of Memory, Draconides. **Important:** do not systematically weave memory/souvenir themes into every encounter — vary the cultural texture broadly.

### 7.3 Generation order

1. Generate **Tier 3** entries first (most complex, anchor the table's identity)
2. Generate **Tier 2** entries
3. Fill remaining with **Tier 1** vignettes
4. Shuffle and number 1–100
5. Run variety check (§7.4)

### 7.4 Variety checklist

Verify after generation — manually for ≤50 entries, via script for 100+:

**Distribution checks:**
- [ ] No repeated concept within 20 entries of each other
- [ ] All tag districts appear at least 3× per 50-entry block
- [ ] Danger levels match targets (±5%)
- [ ] Tier ratios maintained (±5%)
- [ ] NPC archetypes rotated (no two beggars within 20, no two guards within 15)
- [ ] Animals/creatures not repeated adjacently
- [ ] Weather distributed (fog, rain, heat, wind not clustered)
- [ ] Emotional register varied (not every horror entry about corpses, not every social about arguments)

**Anti-tic checks (see §7.6 for full rules):**
- [ ] No support field phrase appears >3× across the table (P1, P3)
- [ ] No ► text quoted or paraphrased in ◇ ◆ → ∞ ● fields (P2)
- [ ] No closer sentence appended identically to an entire field category (P3)
- [ ] Variants are mixed across deciles, not assigned in blocks (P4)
- [ ] ◈ sensory details match the ► scene's physical location (P7)
- [ ] → hooks respond to THIS scene's specifics, not a generic template (P1)
- [ ] Tier 3 Resolutions blocks are each mechanically distinct (different DCs, NPCs, rewards) (P1)

### 7.5 Rotation pools

Rotate through these to force variety during generation:

**NPC archetypes:** merchant, guard, priest, beggar, noble, artisan, sailor, courtesan, child, scholar, foreigner, veteran, thief, entertainer, servant, pilgrim, undertaker, midwife, smuggler, herbalist, alchemist, gravedigger, debt collector, street performer, wet nurse, tax assessor

**Sensory anchors:** smell (spice, rot, incense, blood, rain, brine, tallow), sound (bells, screams, music, hammering, silence, chanting, dripping), texture (wet stone, warm metal, cold silk, rough hemp, greasy leather), light (torchflicker, moonlight, none, colored lanterns, phosphorescence, hearthglow)

**Weather/atmosphere:** fog, drizzle, heat shimmer, ash fall, unnatural stillness, wrong-direction wind, sudden cold, oily rain, low thunderless lightning, dry electric air

**Resolution vectors:** flee, negotiate, fight, legal appeal, bribe, invoke custom, pray, hide, investigate, sacrifice something, call the Guard, blackmail, seduce, wait it out

### 7.6 Anti-tic rules (learned from editorial cycles)

These rules prevent the seven defect patterns (P1–P7) observed across six revision cycles of a 100-entry erotic encounters book. They apply to **any** d100 generation — combat, horror, mystery, etc.

#### P1 — Pool exhaustion: never recycle a support field

Each ◇, ◆, →, ●, ◈, and ∞ must be **written for its specific entry**. Do not create a pool of N variants and assign them round-robin. If a phrase appeared in entry #12, it cannot appear in entry #47 — not paraphrased, not restructured, not with a word swapped. The test: if a reader sees two entries side by side, would they notice a shared phrase? If yes, rewrite.

**Hard limits per 100-entry table:**
- No ◇ gossip sentence may share >5 words with any other ◇
- No ◆ city fact may appear more than once
- No → hook set may be reused — each entry's options must respond to THAT scene
- No ● NPC "want" phrasing may repeat within 20 entries
- No ◈ sensory line may appear more than 3× (location-matched only)

#### P2 — Context injection: never quote the ► in support fields

The ► situation text is **read-only context** for the other fields. No field (◇ ◆ → ● ◈ ∞ or Resolutions) may:
- Quote any fragment of the ► text
- Paraphrase the ► in «guillemets», parentheses, or dashes
- Include the ► as a variable or placeholder (e.g. "the moment around «[► text]»")

Each support field must be a **standalone sentence** that a GM could read without having seen the ►.

#### P3 — Closer addiction: no generic atmospheric tails

Do NOT append a "closer" phrase to any field. Specifically:
- No shared sentence appended to every ◈ ("Copper tightens…", "The X listens for…", etc.)
- No shared sentence appended to every ◆ ("The Syndicate keeps…", "Sergeants learn…", etc.)
- No shared sentence appended to every → ("…and the harbor remembers your boots", etc.)
- No shared sentence appended to every ∞ ("Choir notes the hour differently", etc.)

If a field feels incomplete without a closer, the field itself needs rewriting — not a decorative tail.

**Test:** Grep the finished table for any sentence that appears more than 3 times. If found, delete it.

#### P4 — Decile rotation: don't distribute variants by block

Do not assign variant A to entries 1–10, variant B to 11–20, etc. A reader who opens to any decile should not see the same pattern repeated within that page. Mix variants **across** deciles, not within them.

#### P5 — Syntactic monotony: vary sentence structure

If every ◈ ends with "[Abstract noun] [physical verb] [location]", the variation is cosmetic, not real. Vary:
- Sentence length (some short, some long)
- Sentence structure (fragments, questions, imperatives, not just SVO)
- The presence/absence of the element (some ◈ are 2 fragments, some are 5)

#### P6 — Whack-a-mole: don't replace a recycled phrase with another recycled phrase

When revising a repeated element, the fix is **deletion or per-entry rewriting**, never 1:1 substitution with a new phrase that will itself be recycled.

#### P7 — Location/sensory mismatch: match ◈ to the ► geography

If the ► takes place at the docks, the ◈ must smell of brine, not incense. If the ► takes place in a temple, the ◈ should not mention sawdust and forge-heat. Before finalizing, verify every ◈ against the scene's physical location.

### 7.7 Post-generation tic scan

After generating a full d100, run these automated checks (manually or via script):

```bash
# 1. Find any sentence appearing 4+ times (P1, P3)
grep -oP '(?<=◈ |◇ |◆ |∞ |→ ).+' entries.md | sort | uniq -c | sort -rn | head -20

# 2. Find ► text fragments leaked into other fields (P2)
# Extract each ►, check if any 6+ word substring appears in ◇/◆/∞/→
python check_injection.py entries.md

# 3. Find syntactically identical closers (P5)
# Regex for [Noun] [verb] [preposition] patterns at end of lines
grep -P '[A-Z][a-z]+ [a-z]+s? (for|in|at|under|behind|like|until|before|when|without) ' entries.md | sort | uniq -c | sort -rn

# 4. Check ◈ vs location match (P7)
python check_sensory_match.py entries.md
```

If any check flags >3 violations, fix before publication.

---

## 8. Book assembly (multi-table product)

When the goal is a **published encounter book** (PDF, DriveThruRPG, print):

### Product structure

```
[Book Title]
├── Cover + back cover blurb
├── Credits / legal / OGL-ORC
├── Table of Contents
├── Introduction (1–2 pages)
│   ├── What this book is
│   ├── How to use these tables
│   ├── Stacking tables (roll on 2+ simultaneously)
│   └── Safety tools reference (Lines & Veils, X-Card)
├── Theme Chapter 1: [Theme] — d100 table + intro paragraph
├── Theme Chapter 2: [Theme]
├── ...
├── Appendix A: District Quick-Reference
├── Appendix B: NPC Name Generator (by culture)
├── Appendix C: Encounter Chains (linked entries across tables)
└── Back matter / brand page
```

### Encounter chains

Flag entries across different theme tables that connect into mini-arcs:

```markdown
<!-- CHAIN: burning-debt -->
Combat #23 → Economic #47 → Ethical #81
```

A GM rolling on separate tables may hit chain links organically or follow them deliberately. List chains in Appendix C with suggested reading order and a one-line arc summary.

### Layout notes (Affinity Publisher / InDesign)

- Compact tables: one theme per chapter, 2–4 pages each
- Expanded entries: `\newpage` between district sections
- Content warnings in chapter headers for intensity 2–3 themes
- Tag index at back for cross-referencing by district
- Consider a "Quick Roll" reference card (one page, all tables summarized by d10 ranges)

---

## 9. Expansion mode

Take an existing entry and upgrade its tier:

| Upgrade | What to add |
|---------|-------------|
| **Tier 1 → 2** | NPC motivation, a complication, a possible consequence (3–5 sentences total) |
| **Tier 1 → 3** | All seven fields (►◈●→◆◇∞), named NPC with flash stats, 2–3 resolution branches, faction consequences |
| **Tier 2 → 3** | Missing seven fields, deeper NPC, mechanical hooks, recurrence |

**Rule:** preserve the original entry's core concept — expand it, don't replace it.

---

## 10. Batch generation (script)

For tables of 100+ entries, use `generate_encounters.py`:

```bash
python generate_encounters.py \
  --theme horror \
  --size 100 \
  --format compact \
  --intensity 2 \
  --setting generic \
  --output encounters/horror-encounters-d100.md
```

The script:
1. Calculates distribution targets from §7.1
2. Generates in batches of 20 via Anthropic API
3. Tracks variety pools across batches to prevent repetition
4. Validates metadata consistency (tags, tiers, distributions)
5. **Runs anti-tic scan (§7.7)** — flags any phrase appearing >3× across entries
6. **Validates ◈ location match (P7)** — checks sensory details against ► geography
7. Outputs formatted Markdown with YAML frontmatter

**Critical for batch scripts:** The system prompt for each API call MUST include:
- The full anti-tic rules from §7.6 (especially P2: no ► citation, P3: no closers)
- A blacklist of all phrases already generated in previous batches
- The last 20 ◇, ◆, ◈, and ∞ outputs to prevent near-duplicates

For manual generation (d20–d50), follow §7.3 directly without the script.

---

## 11. Content safety

- **Intensity 1:** no specific warnings needed.
- **Intensity 2–3 (horror / erotic / ethical):** `content_note` required in YAML frontmatter listing specific themes (e.g. "body horror, coercion, explicit sexuality, child endangerment").
- **Hard limits — never write:** harm to children presented approvingly, sexual violence played for titillation, real-world hate speech in fantasy disguise.
- **Erotic intensity 3** is for adult-only products — mark in product metadata and chapter headers.
- For player-facing safety: reference Lines & Veils and X-Card in the book introduction (§8).

---

## 12. Skill integrations

| Companion skill | When to invoke |
|-----------------|----------------|
| `npc-creator` | Tier 3 entries needing full NPC stat block and backstory |
| `scenario-writer` | Tier 3 entries with strong hook potential → expand into full scenarios |
| `faction-creator` | Entries referencing faction dynamics — ensure consistency |
| `erotica-fantasy-en` / `erotica-fantasy-feminine` | Tier 3 erotic entries needing developed prose (intensity 2–3) |
| `read-aloud-crafter` | Converting Tier 2–3 entries into table-ready narration |
| `editorial-tic-auditor` | **Mandatory** post-generation pass on tables of 50+ entries. Run in AUDIT mode to produce a tic inventory; flag any pattern matching P1–P7 from §7.6. If tics found, run field-level rewrites with the tic blacklist in the system prompt. |
| `ttrpg-cliche-buster` | Pre-generation or review pass to identify and replace generic tropes |

---

## 13. File placement

- Compact tables: `encounters/[theme]-encounters-d100.md` (kebab-case)
- Expanded blocks: `encounters/[theme]-encounters/[theme]-encounters.md`
- Book assembly: `encounters/[book-name]/` with one file per chapter
- Script: `encounters/generate_encounters.py`

---

*Skill version 3.0 — 2026. Fused from urban-d100-encounters + random-encounter-creator. Anti-tic rules (§7.6–7.7) derived from six editorial revision cycles on a 100-entry erotic encounters book.*
