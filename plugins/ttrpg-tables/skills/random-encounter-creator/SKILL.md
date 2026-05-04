---
name: random-encounter-creator
description: Generate large-scale random encounter tables (d100 to d1000) for dark fantasy cities. Creates tiered encounters (vignettes, developed, mini-scenes) across six categories (Social, Danger, Mystery, Horror, Environmental, Event) with metadata for filtering (district, time, danger level). Outputs structured Markdown tables. Includes Python script for batch generation via Anthropic API. Use when creating random encounter tables, city event generators, or atmospheric content for urban dark fantasy settings.
---

# Random Encounter Creator

Generate comprehensive random encounter tables for dark fantasy urban settings. Designed for batch generation of 100-1000 entries with consistent quality and variety.

## Output Structure

### Table Format

```markdown
# [Table Name] - d[Size] Urban Encounters

| d[Size] | Type | District | Time | Danger | Encounter |
|---------|------|----------|------|--------|-----------|
| 1 | Social | Market | Day | None | [Encounter text] |
| 2 | Horror | Slums | Night | Low | [Encounter text] |
```

### Entry Tiers

**Tier 1 - Vignettes (60% of entries)**
- 1-2 sentences
- Atmospheric observations, minor events, background color
- No mechanical impact, pure flavor

**Tier 2 - Developed (30% of entries)**
- 1 paragraph (3-5 sentences)
- Potential interaction, NPC with motivation, minor hook
- Optional consequence or follow-up

**Tier 3 - Mini-scenes (10% of entries)**
- 2-3 paragraphs
- Flash NPC, clear stakes, multiple resolution paths
- Mechanical hooks (combat possible, skill checks, rewards)

## Taxonomy

### Encounter Types

| Type | Description | Examples |
|------|-------------|----------|
| **Social** | Human interaction, commerce, conflict | Merchant dispute, noble procession, beggar's plea |
| **Danger** | Threats, violence, criminals | Ambush, pickpocket, gang confrontation |
| **Mystery** | Clues, strange events, secrets | Coded message, disappearance, whispered conspiracy |
| **Horror** | Dread, corruption, supernatural | Corpse discovery, plague signs, entity manifestation |
| **Environmental** | Setting, atmosphere, weather | Fog rolling in, building collapse, crowd surge |
| **Event** | Public occurrences, ceremonies | Execution, festival, riot, procession |

### District Types

- **Slums**: Poverty, crime, desperation, rats, disease
- **Market**: Commerce, crowds, diversity, opportunity, theft
- **Temple**: Religion, ritual, pilgrims, hypocrisy, sanctuary
- **Noble**: Wealth, intrigue, guards, protocol, secrets
- **Docks**: Trade, sailors, smuggling, foreign, danger
- **Artisan**: Crafts, guilds, pride, competition, fire risk
- **Necropolis**: Death, mourning, undead, grave robbers, silence

### Time of Day

- **Day**: Commerce, crowds, authority visible
- **Night**: Crime, supernatural, reduced visibility
- **Dawn**: Transition, workers, deliveries, hangovers
- **Dusk**: Closing shops, changing guard, shadows lengthening

### Danger Levels

- **None**: Pure flavor, no threat
- **Low**: Minor inconvenience, easy avoidance
- **Medium**: Real threat, combat possible, consequences
- **High**: Significant danger, likely combat, potential death

## Workflow

### 1. Define Table Parameters

Specify before generation:
- **Table size**: d100, d200, d500, d1000
- **Focus** (optional): Specific district, time, or type emphasis
- **Tone calibration**: Horror ratio, danger distribution
- **Setting anchors**: Generic terms to use ("the Guard", "the Temple", etc.)

### 2. Calculate Distribution

For a d100 table, target distribution:

**By Tier:**
- Tier 1: 60 entries
- Tier 2: 30 entries
- Tier 3: 10 entries

**By Type (default):**
- Social: 25%
- Danger: 15%
- Mystery: 15%
- Horror: 15%
- Environmental: 15%
- Event: 15%

**By Time:**
- Day: 40%
- Night: 35%
- Dawn: 10%
- Dusk: 15%

**By Danger:**
- None: 40%
- Low: 30%
- Medium: 20%
- High: 10%

Adjust distributions based on table focus.

### 3. Generate in Batches

Use `scripts/generate_encounters.py` for batch generation:

```bash
python scripts/generate_encounters.py \
  --size 100 \
  --output encounters.md \
  --focus "market district, day encounters" \
  --tone "high horror, medium danger"
```

The script:
1. Calculates distribution targets
2. Generates encounters in batches of 20
3. Tracks variety to avoid repetition
4. Validates metadata consistency
5. Outputs formatted Markdown table

### 4. Manual Generation (Small Tables)

For d20-d50 tables, generate directly:

1. List distribution targets
2. Generate Tier 3 entries first (most complex)
3. Generate Tier 2 entries
4. Fill remaining with Tier 1 vignettes
5. Shuffle and number

### 5. Quality Control

After generation, verify:
- [ ] No repeated concepts within 20 entries
- [ ] All types represented per 50-entry block
- [ ] Danger levels appropriately distributed
- [ ] District/time combinations make sense
- [ ] Tier ratios maintained
- [ ] Setting anchors consistent (no proper nouns)

## Setting Anchors (Light Grounding)

Use generic references that GMs can rename:

| Anchor | Represents |
|--------|------------|
| the Guard | City watch, militia |
| the Temple | Dominant religion |
| the Guild | Relevant trade guild |
| the Court | Noble authority |
| the Syndicate | Organized crime |
| the Order | Religious/military order |
| the Academy | Magical institution |
| the Council | City government |

Never use proper nouns. Write "a guard captain" not "Captain Vorn".

## Variety Management

### Avoid Repetition

Track across generation batches:
- NPC archetypes used (no two beggars within 20 entries)
- Specific animals/creatures (no two rat encounters adjacent)
- Weather conditions (distribute fog, rain, heat)
- Emotional beats (not all Horror entries about corpses)

### Rotation Lists

See `references/variety-pools.md` for:
- NPC archetypes by social class
- Animals and vermin
- Trade goods and objects
- Sounds and smells
- Weather and atmospheric conditions
- Body language and mannerisms

## Examples

### Tier 1 Examples

```
| 7 | Environmental | Market | Day | None | The smell of burnt sugar drifts from a confectioner's stall where caramelized nuts cool on marble slabs. |

| 23 | Social | Docks | Dawn | None | Two sailors argue in a foreign tongue, gesturing at a crate that's clearly been opened and poorly resealed. |

| 41 | Horror | Slums | Night | Low | A child's laughter echoes from an alley that leads to a dead end. There's no child visible. |
```

### Tier 2 Examples

```
| 12 | Mystery | Noble | Dusk | Low | A servant in House livery approaches, pressing a sealed letter into the nearest PC's hand before vanishing into a side street. The seal bears no sigil—just a thumbprint in red wax. If opened, the letter contains a single phrase: "The third bell. The fountain. Come alone." |

| 67 | Danger | Market | Day | Medium | A pickpocket lifts a merchant's purse, but the merchant's bodyguard spots it. The thief—barely twelve—bolts directly toward the party, pursuers closing. Helping the child makes enemies of the merchant house; ignoring it means watching a child beaten in the street. |
```

### Tier 3 Example

```
| 88 | Horror | Temple | Night | High |
A procession of hooded figures emerges from the Temple's side entrance, carrying a shrouded body on a bier. The shroud moves. Not breathing—writhing. The figures chant in a language that hurts to hear.

**The Mourners** (6 cultists in Temple robes): AC 12, HP 9, dagger +3 (1d4+1). Won't fight unless attacked or followed into the catacombs. If confronted, claim they're "preparing the blessed for final rest."

**What's Really Happening**: The Temple disposes of failed resurrection attempts—bodies animated but mindless—by drowning them in the sacred well beneath the Necropolis. The "blessed" is a merchant who paid for resurrection but received something worse.

**If Followed**: The catacombs lead to the drowning well. 2d4 additional cultists present. The merchant's family would pay 500gp for proof of what happened to their patriarch.

**If Ignored**: The party hears rumors of "walkers in the deep" over the next week. The well is getting full.
```

## Integration

### With npc-creator

For Tier 3 entries requiring full NPCs, note: "See npc-creator for [role] at Tier [1-3]"

### With scenario-writer

Tier 3 entries can seed scenarios. Flag entries with strong hook potential for expansion.

### With faction-creator

Reference faction dynamics in Social and Danger entries: "Syndicate enforcers collecting protection" or "Guild inspectors checking permits"

## Resources

- `scripts/generate_encounters.py`: Batch generation script using Anthropic API
- `references/variety-pools.md`: Lists of NPCs, objects, sounds, smells for variety
- `references/encounter-templates.md`: Detailed templates and examples for each tier/type combination

Load references when:
- Generating large tables (100+ entries)
- Needing variety inspiration
- Ensuring type/tier coverage
