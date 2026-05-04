---
name: npc-creator
description: Create complete TTRPG NPCs with narrative depth and mechanical stats for D&D 5e. Generates appearance, personality, desires, secrets, backgrounds, stat blocks (tiered by importance), portrayal cues (voice, mannerisms, GM tips), and plot hooks. Handles quick background NPCs, significant social characters, major combat-capable characters, and everything between. Use when GM needs fleshed-out NPCs for campaigns, modules, or improvisation.
---

# NPC Creator

Transform NPC concepts into complete, playable characters with narrative depth and mechanical stats optimized for D&D 5e (2024 rules).

## What This Skill Does

Create NPCs at three complexity tiers:

**Tier 1 (Background):** Quick NPCs for scenes - name, appearance, key trait, minimal stats
**Tier 2 (Significant):** Social-focused NPCs - full narrative, simplified stats, portrayal guidance
**Tier 3 (Major):** Campaign-level NPCs - everything in Tier 2 + full combat stats, multiple hooks, vulnerability scenes

## Workflow

### 1. Receive NPC Brief

Accept any input format:
- Concept: "Corrupt magistrate who takes bribes but feels guilty"
- Bullet points: "Excommunicated priest / Still has divine powers / Building new theology"
- Detailed: Complete character concept with specific requirements
- Setting context: Velnaris, Zarathar, generic fantasy, etc.

### 2. Determine Complexity Tier

Ask user if not specified:

**Tier 1 - Background NPC:**
- Use when: Mentioned once, minimal interaction, no combat expected
- Examples: Shopkeeper, guard, servant, random citizen

**Tier 2 - Significant NPC:**
- Use when: 2-3 appearances, social role, possible combat, quest-related
- Examples: Quest giver, ally, informant, rival, minor villain

**Tier 3 - Major NPC:**
- Use when: Recurring character, plot-central, combat likely, campaign importance
- Examples: Major villain, key ally, faction leader, love interest, mentor

### 3. Build Narrative Sections

Generate based on tier (see `references/narrative-structure.md` for detailed guidance):

**All Tiers:**
- **Appearance**: 1-5 paragraphs depending on tier
- **Personality**: Core traits, contradictions, decision-making style
- **Desire**: What drives them, surface vs. deep wants
- **Secret**: What they hide and why

**Tier 2+:**
- **Background**: 2-5 paragraphs of relevant history
- **Hooks**: If Approached/Pressed/Refused/In Danger

**Tier 3 Only:**
- **Allure/Presence** (if relevant to role)
- **A Moment of Vulnerability** (humanizing scene)
- **Multiple Quests** (2-4 interconnected plot threads)
- **Relationships** (connections to other NPCs)
- **Running [Name]** (extensive GM guidance)

### 4. Create Stat Block

Generate D&D 5e mechanics (see `references/stat-block-templates.md` for frameworks):

**Tier 1:**
- Basic ability modifiers
- 1-2 relevant skills
- Simple trait
- CR 0-1/4

**Tier 2:**
- Full stat block (AC, HP, Speed, abilities)
- Saving throws and skills
- 2-3 traits supporting their role
- 1-2 actions (including social abilities)
- CR 1/2-5
- Proficiency bonus

**Tier 3:**
- Complete stat block with all defenses
- Condition immunities/resistances where appropriate
- 3-5 defining traits
- Multiple action options
- Bonus actions and reactions
- Legendary actions if CR 5+
- Equipment list
- CR varies widely

### 5. Add Portrayal Guidance

Create GM roleplay tools (see `references/portrayal-framework.md` for frameworks):

**Tier 1:** Voice/manner only

**Tier 2:**
- Voice/manner (how they sound and move)
- 2-3 physical tells
- Entrance line (memorable first words)
- Basic verbal tic or pattern
- Quick GM tip

**Tier 3:**
- Full voice/manner description
- Multiple physical tells with frequency
- Entrance line
- Comfort vs. threat behaviors
- Rich verbal patterns
- Extensive GM tips section
- Scene-specific guidance

### 6. Format and Deliver

Present in clean, organized format:
- Narrative sections with clear headers
- Stat block in standard D&D format
- Portrayal cues as actionable guidance
- Hooks as plot-ready scenarios

Use markdown formatting for readability. Include callout boxes for key information where appropriate.

## Key Principles

**Match Detail to Importance:** Don't create 5000-word profiles for NPCs who appear once. Scale to narrative weight.

**Playability Over Perfection:** Stat blocks should be easy to run at the table. Prioritize clarity over mechanical complexity.

**Actionable Guidance:** Portrayal cues should give GMs specific things to do/say, not abstract descriptions.

**Plot Hooks:** Every significant NPC should have clear ways to involve PCs. If they don't drive plot, they might not need stats.

**Internal Consistency:** Narrative should match mechanics. A scholarly NPC needs high Intelligence. A social manipulator needs high Charisma.

## Usage Examples

**Input (Concept):**
```
Corrupt magistrate in Velnaris. Takes bribes to fund daughter's medicine. 
She died anyway. Can't stop taking bribes now. Feels guilty. 
Tier 2 - significant NPC for investigation arc.
```

**Output:**
```
# Magistrate Cassius Vorn

## Appearance
A man in his fifties wearing the burgundy robes of city magistracy...
[3-4 paragraphs]

## Personality
Vorn is pragmatic to the point of cynicism...
[2-3 paragraphs including core conflict]

## Desire
To find redemption without sacrificing the survival his bribes have purchased...
[1-2 paragraphs]

## Secret
He ruled against an innocent woman, watched her hang...
[1-2 paragraphs]

## Background
Vorn rose through bureaucracy through competence and compromise...
[2-3 paragraphs]

[Stat Block - Tier 2 format with social abilities]

## Portrayal Cues
Voice/Manner: Measured, careful speech...
[Detailed portrayal section]

## Hooks
If Approached: [scenario]
If Pressed: [scenario]
[etc.]
```

## Common Requests

**"Make them more complex"**: Add contradictions to personality, layer secrets, create competing desires

**"Make them simpler"**: Reduce to core concept, minimize stat block, focus on one defining trait

**"Add combat abilities"**: Upgrade stat block tier, include appropriate weapon attacks and special abilities

**"More roleplay guidance"**: Expand portrayal section with additional tells, examples, scene-specific guidance

**"Connect to [setting]"**: Incorporate setting-specific elements (Velnaris corruption, Zarathar memory forms, etc.)

**"Add plot hooks"**: Generate 2-4 additional scenarios for PC interaction

## Special Considerations

### Mature Content (Velnaris-style)
- Handle sensuality with sophistication, not gratuitousness
- Focus on psychology and power dynamics
- Emphasize consent, agency, and complexity
- Use allure section to describe magnetism without explicit content

### Setting Integration
- Velnaris: Corruption, desire, secrets, noir fantasy
- Zarathar: Memory forms, volcanic cultures, colonialism
- Generic fantasy: Broadly applicable, avoid setting-specific mechanics

### Spellcasting NPCs
- Choose spells that match concept and support their role
- Include utility spells for non-combat scenes
- Thematic spell selection over mechanical optimization

### Social Combat
- Include social abilities (Insight, Persuasion, Deception)
- Create traits that support social interaction
- Consider non-violent resolution mechanics

## Resources

### References

- `references/stat-block-templates.md`: D&D 5e mechanical frameworks at three complexity tiers, CR guidelines, special ability design patterns
- `references/portrayal-framework.md`: How to create voice, mannerisms, physical tells, entrance lines, and GM guidance that makes NPCs memorable at the table
- `references/narrative-structure.md`: Building compelling appearance, personality, desire, secret, background, and hook sections with examples and templates

Load these references when:
- Creating complex stat blocks (Tier 3)
- Need inspiration for special abilities
- Building extensive portrayal guidance
- Structuring multiple quest threads
- Calibrating CR or power level

## Iteration and Refinement

After initial creation, NPCs can be:
- **Upgraded** (Tier 1 → 2 → 3) as they become more important
- **Simplified** if too complex for actual usage
- **Adjusted** for mechanical balance
- **Expanded** with additional hooks or relationships
- **Adapted** to different settings or systems
