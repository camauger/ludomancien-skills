---
name: midjourney-prompt-generator
description: Generate effective Midjourney prompts for AI image generation with focus on TTRPG illustrations, character art, scenes, and environments. Covers prompt structure, parameters, style references, composition techniques, and filter navigation strategies.
---

# Midjourney Prompt Generator Skill

## Purpose
Generate effective, well-structured Midjourney prompts that produce high-quality AI-generated images, with particular focus on TTRPG illustrations including character art, creatures, environments, items, and scenes. This skill covers prompt architecture, parameter usage, style techniques, composition strategies, and methods for achieving desired aesthetics while working within platform constraints.

## When to Use This Skill
- Creating character portraits for TTRPGs
- Generating creature and monster illustrations
- Designing fantasy environments and locations
- Creating item and equipment illustrations
- Producing scene compositions for adventures
- Developing cover art or key art
- Generating reference images for worldbuilding
- Creating visual assets for supplements or sourcebooks
- Exploring visual concepts and aesthetics

## Midjourney Fundamentals

### Basic Prompt Structure

**Standard Format**
```
/imagine prompt: [subject], [description], [style], [parameters]
```

**Component Breakdown**
1. **Subject**: What you're creating (character, creature, scene)
2. **Description**: Details about the subject (appearance, action, mood)
3. **Style**: Artistic approach, medium, artist references
4. **Parameters**: Technical settings (aspect ratio, quality, stylization)

### Prompt Architecture

**Front-Loading Important Elements**
- Most important details go first
- Midjourney weighs earlier words more heavily
- Subject and key descriptors before style
- Critical details in first 30-40 words

**Weight Distribution**
- First 10 words: ~60% influence
- Next 10-20 words: ~30% influence
- Remaining words: ~10% influence
- Parameters affect entire image equally

**Example Progression**
- ❌ Weak: "A fantasy image of a character with sword in medieval style"
- ✅ Strong: "Female knight in ornate silver armor, wielding flaming longsword, determined expression, windswept crimson hair, medieval fantasy, dramatic lighting"

## Important V7 Updates (April 2025)

**Breaking Changes from V6**
- **Character Reference (--cref) NO LONGER WORKS** - Use Omni Reference (--oref) instead
- **Quality parameter changed**: Values are now 1, 2, 4 (not 0.25, 0.5, 1, 2)
- **Multi-prompting limited**: May not work as expected; use V6 if needed
- **Style Reference versions**: New --sv 4 and --sv 6 system

**New V7 Features**
- **Omni Reference (--oref)**: More versatile character/subject consistency
  - Works across different art styles
  - --ow parameter (0-1000, default 1000)
  - Can maintain people, animals, objects
- **Improved prompt adherence**: Better natural language understanding
- **Better anatomy and composition**: More realistic proportions
- **Extended image weight range**: --iw 0-3 with decimal support

**Parameter Quick Reference**
- Character consistency V7: `--oref [URL] --ow 1000`
- Character consistency V6: `--cref [URL] --cw 100`
- Quality V7: `--q 1` (default), `--q 2`, `--q 4`
- Quality V6: `--q 0.25`, `--q 0.5`, `--q 1`, `--q 2`
- Style reference: `--sref [URL] --sw 100` (both versions)

**When to Use V6 Instead of V7**
- Need multi-prompting with weights (::)
- Prefer established V6 aesthetic
- Using old sref codes (add `--sv 4` in V7 or switch to V6)
- Want lower quality draft mode (`--q 0.25`, `--q 0.5`)
- Having issues with V7's interpretation

## Core Parameters

### Aspect Ratio (--ar)

**Common Ratios**
- `--ar 1:1` - Square (default, social media)
- `--ar 3:2` - Portrait orientation (character portraits)
- `--ar 2:3` - Tall portrait (full body characters)
- `--ar 16:9` - Landscape (scenes, environments)
- `--ar 9:16` - Tall landscape (towers, vertical dungeons)
- `--ar 4:5` - Instagram portrait
- `--ar 7:4` - Panoramic landscape

**TTRPG Use Cases**
- Character portraits: `--ar 2:3` or `--ar 3:4`
- Battle maps: `--ar 16:9` or `--ar 1:1`
- Cover art: `--ar 2:3` or `--ar 3:4`
- Landscape scenes: `--ar 16:9` or `--ar 21:9`
- Item illustrations: `--ar 1:1` or `--ar 4:5`

### Stylization (--s or --stylize)

**Scale: 0-1000**
- `--s 0`: Literal interpretation, minimal artistic license
- `--s 50`: Low stylization, more prompt adherence (Preset: Stylize Low)
- `--s 100`: Balanced (default, Preset: Stylize Med)
- `--s 250`: Increased artistic interpretation (Preset: Stylize High)
- `--s 500-750`: Heavily stylized, artistic freedom
- `--s 750`: Very high stylization (Preset: Stylize Very High)
- `--s 1000`: Maximum artistic interpretation

**Settings Panel Presets**
- Stylize Low = 50
- Stylize Med = 100 (default)
- Stylize High = 250
- Stylize Very High = 750

**When to Use**
- Low (0-50): Technical diagrams, specific accuracy needed, RAW aesthetic
- Medium (50-150): Balanced character art, most TTRPG use
- High (150-400): Painterly art, atmospheric scenes
- Maximum (400-1000): Abstract art, experimental styles

### Chaos (--c or --chaos)

**Scale: 0-100**
- `--c 0`: Consistent, predictable results
- `--c 10-30`: Slight variation (good for iterations)
- `--c 40-60`: Moderate variation, more creativity
- `--c 70-100`: High variation, unexpected results

**TTRPG Applications**
- Character portraits: `--c 10-20` (consistency)
- Environment concepts: `--c 30-50` (exploration)
- Monster designs: `--c 40-60` (creativity)
- Abstract magic effects: `--c 70-100` (experimentation)

### Quality (--q)

**Values for V7: 1, 2, 4**
- `--q 1`: Standard quality (default)
- `--q 2`: High quality (2x GPU time, more detail)
- `--q 4`: Maximum quality (4x GPU time, highest detail)

**Legacy Values (V6 and earlier): 0.25, 0.5, 1, 2**
- `--q 0.25`: Fast, draft quality (4x faster) 
- `--q 0.5`: Reduced quality (2x faster)

**Notes**
- Quality parameter only affects initial generation, not variations or upscales
- For draft work, consider Draft Mode instead of lower quality
- `--q 3` in V7 automatically switches to `--q 4`
- `--q 4` is not compatible with Omni Reference

**Recommendation**: Use `--q 1` for most work, `--q 2` or `--q 4` for final renders

### Version (--v or --version)

**Current Versions**
- `--v 7`: Latest, most advanced (default as of April 2025)
- `--v 6.1`: Previous stable version
- `--v 6.0`: Earlier V6 version
- `--v 5.2`: Legacy, different aesthetic
- Omit parameter to use current default

### Other Useful Parameters

**Raw Mode (--raw)**
- Reduces Midjourney's default stylistic alterations
- Produces more literal interpretation of prompts
- No value needed: `--raw`
- Useful for: Photorealistic images, technical accuracy, less artistic flair

**Stop (--stop)**
- `--stop 10-100`: Percentage of generation to complete
- Lower values: Sketch-like, incomplete
- Use for iterative exploration: `--stop 50-70`

**Weird (--weird or --w)**
- `--weird 0-3000`: Quirky, unconventional results
- Default: 0 (off)
- Sweet spot: 250-1000 for interesting variations
- High values: Very unusual, experimental

**Tile (--tile)**
- Creates seamless repeating patterns
- No value needed: `--tile`
- Useful for: Textures, backgrounds, wallpapers

**No (--no)**
- Negative prompt, removes elements
- Example: `--no weapons, armor, helmet`
- **IMPORTANT**: Reads each word independently
- `--no modern clothing` = "no modern" + "no clothing"
- Be specific with each term

**Personalization (--p)**
- Applies your personalized aesthetic profile
- Created through rating images in Midjourney
- Can have multiple profiles
- Set default in settings or specify per-prompt

## Subject Types and Techniques

### Character Portraits

**Essential Elements**
1. **Species/Type**: Human, elf, dwarf, tiefling, etc.
2. **Gender/Age**: Male, female, non-binary, young, elderly, etc.
3. **Class/Role**: Warrior, wizard, rogue, cleric, etc.
4. **Physical Features**: Hair, eyes, skin tone, build
5. **Equipment**: Armor, weapons, accessories
6. **Expression/Mood**: Determined, jovial, mysterious, fierce
7. **Framing**: Headshot, bust, half-body, full-body

**Example Prompt**
```
/imagine prompt: Half-elf female ranger in her late twenties, shoulder-length auburn hair with braids, piercing green eyes, weathered leather armor with forest-green cloak, longbow across back, confident smirk, standing in dappled forest light, fantasy character portrait, detailed digital painting, --ar 2:3 --s 150
```

**Key Techniques**
- Specify viewing angle: "three-quarter view", "profile", "front view"
- Add personality: "battle-scarred veteran", "naive optimist", "cynical mercenary"
- Include signature elements: "ornate family signet ring", "ritual tattoos", "glowing runes"
- Define lighting: "dramatic side lighting", "soft natural light", "magical glow"

### Creature and Monster Design

**Core Components**
1. **Base Creature**: Dragon, demon, undead, elemental, beast
2. **Size/Scale**: Tiny, small, medium, large, huge, gargantuan
3. **Key Features**: Horns, wings, tentacles, multiple limbs, unusual anatomy
4. **Texture/Material**: Scales, fur, chitin, stone, ethereal
5. **Coloration**: Specific colors or patterns
6. **Mood/Threat**: Terrifying, majestic, alien, corrupted
7. **Environment Context**: Where it lives/hunts

**Example Prompt**
```
/imagine prompt: Massive elder dragon with obsidian black scales, four eyes glowing like molten gold, tattered membrane wings, jagged crystalline growths along spine, coiled atop mountain of treasure in dark cavern, volumetric light rays from above, menacing presence, fantasy monster art, highly detailed, --ar 16:9 --s 200 --c 40
```

**Monster Design Tips**
- Combine unexpected elements: "shark-headed humanoid with beetle carapace"
- Specify proportions: "disproportionately long arms", "barrel-chested"
- Add environmental integration: "moss-covered", "partially incorporeal"
- Include scale reference: "towering over ruined buildings", "small enough to fit in a hand"

### Environment and Location

**Essential Elements**
1. **Location Type**: Forest, dungeon, city, cave, mountain, ruins
2. **Time of Day**: Dawn, midday, dusk, night, eternal twilight
3. **Weather/Atmosphere**: Foggy, stormy, clear, magical aura
4. **Scale/Scope**: Close-up, medium view, vista, aerial
5. **Key Features**: Architectural details, natural formations, points of interest
6. **Mood/Tone**: Ominous, peaceful, abandoned, thriving, mysterious

**Example Prompt**
```
/imagine prompt: Ancient elven library ruins overgrown with luminescent vines and flowers, crumbling marble columns with carved runes, shafts of moonlight through broken dome ceiling, floating books and magical particles in air, ethereal blue-green glow, sense of lost knowledge and melancholy beauty, fantasy environment concept art, detailed matte painting style, --ar 16:9 --s 300
```

**Environment Techniques**
- Define depth layers: "foreground cliffs, middle ground forest, background mountains"
- Add atmospheric effects: "morning mist", "heat shimmer", "magical distortion"
- Include narrative elements: "abandoned camp", "signs of recent battle", "mysterious footprints"
- Specify perspective: "ground level view", "bird's eye view", "isometric angle"

### Items and Equipment

**Core Components**
1. **Item Type**: Weapon, armor, accessory, artifact, tool
2. **Material**: Steel, wood, crystal, dragon bone, ethereal energy
3. **Condition**: Pristine, battle-worn, ancient, corrupted
4. **Special Features**: Enchantments, runes, gems, engravings
5. **Presentation**: Displayed on stand, in use, floating, embedded
6. **Lighting**: How light interacts with materials

**Example Prompt**
```
/imagine prompt: Legendary greatsword with blade forged from starlight metal, intricate Celtic knotwork etched along fuller, pommel set with pulsing sapphire gem, leather-wrapped grip with silver wire, faint blue-white glow emanating from runes, displayed on ornate weapon stand, studio lighting with dramatic shadows, fantasy item illustration, photorealistic materials, --ar 4:5 --s 100
```

**Item Design Tips**
- Specify viewing angle: "three-quarter view", "isometric", "front and side view"
- Add history: "battle-notched blade", "heirloom with family crest", "recently unearthed artifact"
- Include scale context: "next to human hand for scale", "worn by knight in background"
- Detail materials: "Damascus steel pattern", "iridescent dragonscale leather", "translucent crystal"

## Style and Medium Techniques

### Art Style References

**Painterly Styles**
- "Oil painting style, classical composition"
- "Watercolor illustration, soft washes"
- "Acrylic painting, bold brushstrokes"
- "Gouache painting, matte finish"
- "Fresco technique, aged patina"

**Digital Art Styles**
- "Digital painting, detailed rendering"
- "Concept art style, professional illustration"
- "Matte painting technique, photorealistic"
- "Character design sheet, turnaround views"
- "Artstation trending, high detail"

**Traditional Media**
- "Graphite sketch, cross-hatching"
- "Ink illustration, fine line work"
- "Charcoal drawing, dramatic values"
- "Colored pencil, layered textures"
- "Pen and ink, medieval manuscript style"

**Genre-Specific Styles**
- "Dark fantasy art, Frank Frazetta influence"
- "High fantasy, classic D&D art style"
- "Grimdark fantasy, gothic horror elements"
- "Whimsical fantasy, storybook illustration"
- "Epic fantasy, cinematic composition"

### Artist Reference Techniques

**Format Options**
1. Direct reference: "in the style of [Artist Name]"
2. Combined styles: "style blend of [Artist A] and [Artist B]"
3. Movement reference: "Pre-Raphaelite style", "Art Nouveau influence"
4. Studio reference: "Blizzard Entertainment style", "Magic: The Gathering art"

**Notable Fantasy Artists** (examples for reference)
- "Frank Frazetta style" - Pulp fantasy, muscular figures
- "Brom style" - Dark fantasy, gothic elements
- "Michael Whelan style" - Epic fantasy, cosmic scope
- "Larry Elmore style" - Classic D&D, heroic fantasy
- "Wayne Reynolds style" - Dynamic action, Pathfinder aesthetic
- "Todd Lockwood style" - Dragon art, detailed rendering
- "Yoshitaka Amano style" - Ethereal, flowing, Japanese influence

**Caution**: Artist references can be unpredictable; use as inspiration, not exact replication

### Lighting Techniques

**Lighting Types**
- "Dramatic side lighting with strong shadows"
- "Soft diffused natural light, golden hour"
- "Rim lighting, backlit silhouette"
- "Volumetric light rays, god rays through mist"
- "Magical bioluminescent glow"
- "Candlelight, warm intimate lighting"
- "Storm light, ominous gray-blue cast"
- "Moonlight, cool silver illumination"

**Lighting Mood**
- "Chiaroscuro, dramatic contrast"
- "High key lighting, bright and hopeful"
- "Low key lighting, mysterious and moody"
- "Split lighting, half face in shadow"
- "Rembrandt lighting, classic portrait"

### Color Palette Specification

**Color Approaches**
- "Muted earth tones palette"
- "Vibrant saturated colors"
- "Monochromatic blue scheme"
- "Warm palette, reds and golds"
- "Cool palette, blues and purples"
- "Complementary orange and teal"
- "Analogous green to yellow"
- "Desaturated with color accent"

**Atmosphere Through Color**
- "Sepia tones, aged photograph feel"
- "Cold blue-gray color scheme, winter"
- "Deep burgundy and black, gothic"
- "Emerald greens and gold, luxury"
- "Dusty pastels, dream-like"

## Advanced Prompting Techniques

### Multi-Prompting with Weights

**Syntax**: Use `::` to separate concepts and numbers to weight them
```
/imagine prompt: warrior knight::2 medieval castle::1 sunset::1
```
- Higher numbers = more influence
- Useful for balancing multiple subjects
- Default weight is 1 if not specified

**⚠️ V7 Compatibility Note**
Multi-prompting may have limited or no support in V7. If it doesn't work as expected, try:
- Using V6 with `--v 6`
- Adjusting --iw (image weight) instead for image references
- Front-loading important elements in prompt text

**Example Application (V6)**
```
/imagine prompt: female elf ranger::3 enchanted forest::2 magical creatures::1 ethereal lighting::2 --ar 2:3 --v 6
```

### Negative Prompting

**Using --no Parameter**
```
/imagine prompt: dwarf blacksmith, fantasy portrait --no beard, helmet, armor
```

**⚠️ CRITICAL: How --no Works**
The --no parameter reads each word INDEPENDENTLY. This means:
- `--no modern clothing` is read as "no modern" AND "no clothing"
- This removes ALL clothing, not just modern clothing
- `--no long hair` = "no long" + "no hair" = removes all hair

**Correct Usage Examples**
- ❌ Wrong: `--no long hair` (removes all hair)
- ✅ Right: `--no hair` or describe desired hair in prompt
- ❌ Wrong: `--no modern clothing` (removes all clothing)
- ✅ Right: `--no modern` + specify "medieval tunic" in prompt
- ❌ Wrong: `--no big sword` (removes all swords)
- ✅ Right: `--no sword` or specify "dagger" in prompt

**When to Use Negative Prompts**
- Removing common associations: `--no beard` for clean-shaven dwarf
- Eliminating unwanted elements: `--no wings` for grounded creatures
- Avoiding style elements: `--no photorealistic, 3d, cgi`
- Preventing specific features: `--no helmet, crown, jewelry`

**Effective Negative Prompts**
- Be specific with SINGLE words: `--no helmet` not `--no metal helmet`
- Stack separate removals: `--no weapons, armor, jewelry, scars`
- Remove style elements: `--no photo, render, cgi`
- Each comma-separated term is independent

### Permutation Prompts

**Syntax**: Use `{}` with comma-separated options
```
/imagine prompt: {red, blue, green} dragon in cave --ar 16:9
```
- Creates three separate images
- Useful for exploring variations
- Maximum 4-5 variations recommended

**TTRPG Application**
```
/imagine prompt: {human, elf, dwarf, halfling} fighter in plate armor, fantasy portrait --ar 2:3
```

### Image Prompting (Style Reference)

**Using Uploaded Images**
1. Upload reference image to Midjourney
2. Copy image URL
3. Add URL at start of prompt: `[URL] your prompt text`

**Style Reference Parameter (--sref)**
```
/imagine prompt: warrior character --sref [URL]
```
- Borrows style from reference image
- Weight with `--sw 0-1000` (default 100)
- Higher = stronger style influence
- Compatible with V6 and V7

**Style Reference Versions (--sv)**
- **V7**: `--sv 4` (old V7 model) or `--sv 6` (default, current)
- **V6**: `--sv 1` through `--sv 4` (default)
- Different versions interpret style differently
- Experiment to find best results
- Note: Some old sref codes may not work the same in V7; use `--sv 4` for old codes

**Character Reference (--cref)** ⚠️ V6 ONLY
```
/imagine prompt: character in different pose --cref [URL]
```
- Maintains character consistency across generations  
- Weight with `--cw 0-100` (default 100)
- **NOT COMPATIBLE WITH V7** - Use Omni Reference instead

**Omni Reference (--oref)** ✨ V7 FEATURE
```
/imagine prompt: character in different scene --oref [URL]
```
- V7's evolution of Character Reference
- Maintains character/subject consistency across styles
- Weight with `--ow 0-1000` (default 1000)
- More versatile than --cref, works across art styles
- Can apply to people, animals, objects
- Not compatible with `--q 4`

**Image Weight (--iw)**
- Controls influence of image prompts on composition
- V7 and V6 range: `--iw 0-3` (default 1)
- V5 range: `--iw 0-2`
- Supports decimals: `--iw 0.01`, `--iw 0.5`, `--iw 1.5`
- Higher values = closer to original image
- Use as fine-tuning slider for reference strength

### Remix Mode

**Activation**: `/settings` then select "Remix Mode"
**Use**: Modify prompts when upscaling or varying
- Change elements while keeping composition
- Adjust style, lighting, or details
- Useful for iterative refinement

## TTRPG-Specific Strategies

### Character Consistency

**Version 7: Omni Reference**
```
/imagine prompt: Female tiefling warlock, pale purple skin, curved black horns with gold bands, heterochromia eyes (left amber, right violet), straight white hair to mid-back, small pointed nose, sharp cheekbones, confident expression, dark robes with constellation patterns, silver jewelry, fantasy character portrait, digital painting --ar 2:3 --s 150 --oref [URL] --ow 1000
```

**Version 6: Character Reference**
```
/imagine prompt: [same prompt] --ar 2:3 --s 150 --cref [URL] --cw 100
```

**Omni Reference Strategy (V7)**
- Generate initial portrait with detailed description
- Save image and use `--oref [URL]` for subsequent images
- Adjust `--ow 0-1000` for consistency strength
  - High (800-1000): Very close match to reference
  - Medium (400-700): Recognizable but with variation
  - Low (100-300): Loose interpretation
- Works across different art styles
- Can maintain consistency for objects, animals, people

**Character Reference Strategy (V6)**
- Use `--cref [URL]` for character consistency
- Adjust `--cw 0-100`:
  - `--cw 100`: Match face, hair, and clothing closely
  - `--cw 50`: Moderate consistency
  - `--cw 0`: Very flexible, loose match

**Technique 3: Seed Consistency**
- Note seed number from results: `--seed 12345`
- Use same seed + similar prompt = similar results
- Varies with prompt changes but maintains core aesthetic

### Token Economy Strategy

**Prioritize Word Choices**
- Use precise terms over vague descriptions
- "Ornate elven plate armor with filigree" > "fancy armor"
- "Weathered oak staff with crystal topper" > "magic staff"
- "Narrow haunted eyes, sunken cheeks" > "scary face"

**Eliminate Filler Words**
- Remove: "a", "the", "is", "has", "with" (when possible)
- Before: "A warrior with a sword who has red hair"
- After: "Warrior, drawn sword, crimson hair"

### Working with Content Filters

**Mature Fantasy Content**
When creating content that might trigger filters (tasteful sensuality, dark themes):

**Approach 1: Euphemistic Language**
- "Elegant evening wear" instead of direct descriptions
- "Classical artistic nudity, Renaissance painting style"
- "Tasteful, museum-quality artistic figure study"
- "Romantic fantasy, Pre-Raphaelite influence"

**Approach 2: Art Historical References**
- "Botticelli composition"
- "Titian style portraiture"
- "Classical sculpture aesthetic"
- "Academic art tradition"

**Approach 3: Clothing and Pose Emphasis**
- Specify elegant garments in detail
- "Flowing silk gown", "ornate ceremonial robes"
- Focus on facial expression and atmosphere
- "Confident pose, regal bearing"

**Approach 4: Context and Class**
- "Courtesan in lavish boudoir, baroque opulence"
- "Noble lady in private chambers"
- "Dancer in performance, graceful movement"
- Frame as character portrait, not sexualization

**Dark Fantasy Content**
- "Gothic horror aesthetic" over "gore"
- "Ominous atmosphere, shadowy" over explicit violence
- "Battle-scarred, weathered" over graphic wounds
- "Eldritch, cosmic horror" for disturbing elements

### Scene Composition for TTRPG

**Rule of Thirds Application**
```
/imagine prompt: Lone adventurer (positioned left third) facing massive ancient gate (right two-thirds), dramatic scale difference, misty atmosphere, fantasy scene, cinematic composition --ar 16:9
```

**Establishing Shots**
```
/imagine prompt: Sprawling medieval city built on tiered cliff faces, waterfall cascade through center, castle at summit, fishing boats in harbor below, warm sunset light, aerial perspective, fantasy city establishing shot, matte painting style --ar 21:9 --s 400
```

**Action Scenes**
```
/imagine prompt: Female warrior mid-leap with greatsword raised, hair and cape flowing, sparks from blade, ruins background, dynamic action pose, motion blur on edges, dramatic low angle, fantasy battle illustration --ar 2:3 --s 200
```

### Batch Concept Exploration

**Using Chaos + Permutations**
```
/imagine prompt: {fire, ice, lightning, shadow} elemental mage, fantasy character design --ar 2:3 --c 50
```

**Testing Style Variations**
```
/imagine prompt: dragon in lair, {painterly oil painting, digital concept art, watercolor illustration, pen and ink drawing} --ar 16:9
```

**Environment Moods**
```
/imagine prompt: haunted forest, {dawn mist, midnight storm, autumn twilight, winter frost} atmosphere --ar 16:9 --s 300
```

## Common Issues and Solutions

### Problem: Generic Results

**Solutions**
- Add specific unique details
- Include personality descriptors
- Specify unusual combinations
- Reference specific time periods or cultures

**Before**: "Elf wizard"
**After**: "Ancient elf archmage with star-map tattoos covering bald head, blind white eyes that see magic, flowing midnight blue robes with constellation embroidery, gnarled ironwood staff topped with captured starlight, emanating quiet power and ancient wisdom"

### Problem: Unwanted Modern Elements

**Solutions**
- Use `--no modern, contemporary, present-day`
- Specify time period: "medieval", "ancient", "early Renaissance"
- Add "historically accurate" or "period-appropriate"
- Use "traditional fantasy" to anchor genre

### Problem: Wrong Proportions or Anatomy

**Solutions**
- Specify anatomy explicitly: "accurate human proportions"
- Reference art style known for good anatomy: "classical figure drawing"
- Use lower stylization: `--s 50-100`
- Specify viewing angle to control distortion
- Add "anatomically correct" or "professional anatomy"

### Problem: Muddy or Unclear Details

**Solutions**
- Reduce chaos: `--c 10-20`
- Lower stylization for accuracy: `--s 75-150`
- Use "sharp focus", "highly detailed", "crisp"
- Specify "clean linework" or "clear definition"
- Try `--q 2` for more detail processing

### Problem: Over-Stylized

**Solutions**
- Lower stylization: `--s 50-100`
- Add "realistic" or "naturalistic" to prompt
- Remove artistic style references
- Use "subtle" or "understated" modifiers
- Focus on technical accuracy terms

### Problem: Not Matching Reference Style

**Solutions**
- Front-load style descriptor in prompt
- Use multiple style terms consistently
- Try `--sref` with similar artwork
- Be more specific about medium: "oil painting on canvas" vs. "painting"
- Increase `--sw` value for stronger style reference

## Prompt Templates

### Character Portrait Template

```
/imagine prompt: [Species] [gender] [class/profession], [age descriptor], [hair description], [eye description], [distinctive facial features], [clothing/armor details], [equipment/accessories], [expression/personality], [pose or action], [background/environment hint], fantasy character portrait, [art style], [lighting description], --ar 2:3 --s [100-200]
```

### Creature/Monster Template

```
/imagine prompt: [Size descriptor] [creature type] with [distinctive features], [texture/material], [color palette], [additional limbs/unusual anatomy], [mood/threat level], [environment context], [pose or action], fantasy creature design, [art style], [lighting], --ar [varies] --s [150-250] --c [30-60]
```

### Environment Template

```
/imagine prompt: [Location type] with [key architectural/natural features], [time of day], [weather/atmospheric effects], [scale descriptor], [color palette], [mood/tone], [narrative elements], fantasy environment, [art style], [lighting approach], --ar 16:9 --s [200-400]
```

### Item/Equipment Template

```
/imagine prompt: [Item type] crafted from [materials], [decorative elements], [condition/age], [magical effects/glow], [special features], [presentation/display method], [viewing angle], fantasy item illustration, [art style], [lighting setup], --ar [4:5 or 1:1] --s [100-150]
```

### Scene/Story Template

```
/imagine prompt: [Main subject action], [secondary elements], [environment setting], [atmospheric conditions], [emotional tone], [composition notes], [color palette], fantasy scene, [art style], [lighting], --ar [varies] --s [200-300]
```

## Efficiency Tips

### Iterative Refinement Process

1. **Concept Pass** (quick exploration)
   - Basic prompt, `--q 0.5`, `--c 40-60`
   - Test multiple variations with permutations
   - Identify promising directions

2. **Detail Pass** (refinement)
   - Expand successful prompts with details
   - Standard `--q 1`, adjust `--s` and `--c`
   - Test lighting and style variations

3. **Final Pass** (production quality)
   - Refined prompt with all specifics
   - Use `--q 2` for maximum detail
   - Lock in seed if maintaining consistency
   - Upscale and minor variations

### Prompt Building Workflow

1. Start with subject noun
2. Add 3-5 key descriptors
3. Include style/medium
4. Add lighting/atmosphere
5. Specify composition if needed
6. Add parameters
7. Test and iterate

### Saving and Organization

**Document Your Prompts**
- Keep prompt library for successful patterns
- Note seed numbers for character consistency
- Save reference images with prompts
- Tag by category: characters, creatures, environments, items

**Naming Convention**
```
[Project]_[Type]_[Subject]_[Version]
Example: Zarathar_Character_NPC_Merchant_v3
```

## Quality Checklist

Before finalizing an image for use:
- [ ] Subject is clearly recognizable
- [ ] Proportions and anatomy are acceptable
- [ ] Style matches intended aesthetic
- [ ] Lighting enhances subject
- [ ] Colors are appropriate for tone
- [ ] Composition is balanced
- [ ] Details are crisp and clear (unless intentional)
- [ ] No unwanted modern elements
- [ ] Matches TTRPG genre expectations
- [ ] Usable at intended print/digital size

## Platform-Specific Notes

### Midjourney Version Differences

**V7 (Current - April 2025)**
- Better prompt adherence and natural composition
- Improved anatomy and proportions
- Omni Reference (--oref) replaces Character Reference
- Quality values: 1, 2, 4 (not 0.25/0.5)
- Style Reference versions (--sv 4, --sv 6)
- Multi-prompting may have limited support
- Image weight range: 0-3 with decimal support
- Recommended for most use

**V6.1 and V6.0**
- Character Reference (--cref) available
- Better text rendering (still limited)
- Quality values: 0.25, 0.5, 1, 2
- Style Reference versions (--sv 1-4)
- More predictable multi-prompting
- Use if V7 results too different from your workflow

**V5.2 (Legacy)**
- Different aesthetic (more painterly default)
- Can produce interesting alternatives
- Try if V6/V7 results too "clean"
- Use `--v 5.2` to test
- Quality values: 0.25, 0.5, 1, 2

**RAW Mode**
- Available across versions with `--raw`
- Reduces default Midjourney aesthetics
- More literal, less stylized results
- Useful for photorealistic or technical images

### Discord vs. Web Interface

**Discord Bot**
- Faster for batch work
- Permutation prompts work seamlessly
- Easier to track seeds and variations
- Better for community feedback
- Settings panel with presets
- Prefer suffix/option commands for shortcuts

**Web Interface** (midjourney.com)
- Cleaner interface for browsing
- Easier image management and upload
- Drag-and-drop for reference images
- Better for refinement work
- Gallery organization
- Separate columns for Image/Style/Omni Reference
- Lock feature to keep references across prompts

### Draft Mode
- Faster, lower-cost generation option
- Alternative to `--q 0.5` in legacy versions
- Useful for rapid exploration
- Enable in settings or web interface

## Example Prompts Collection

### Character Examples

**Grizzled Veteran**
```
/imagine prompt: Human male fighter in his fifties, gray-streaked black beard, battle scars across weathered face, one clouded eye, dented plate armor with decades of repairs, notched longsword at hip, thousand-yard stare, exhausted but determined expression, standing in aftermath of battle, smoke and embers drifting, fantasy character portrait, oil painting style, dramatic side lighting, --ar 2:3 --s 180
```

**Elegant Spellcaster**
```
/imagine prompt: Female elf sorcerer with flowing silver hair adorned with small crystal ornaments, luminous purple eyes with arcane glow, delicate features, graceful pose with one hand raised conjuring swirling magical energy, elegant dark purple robes with star patterns, moonlight filtering through ancient library windows, serene confidence, fantasy character portrait, detailed digital painting, soft magical lighting, --ar 2:3 --s 200
```

### Creature Examples

**Forest Guardian**
```
/imagine prompt: Massive tree ent with moss-covered bark skin, gnarled branch limbs, glowing amber sap veins, autumn leaves growing from body, wise ancient eyes like tree knots, protective stance, dappled forest sunlight, small woodland creatures nestled in branches, gentle giant presence, fantasy creature design, painterly style, warm natural lighting, --ar 2:3 --s 250 --c 40
```

**Demonic Horror**
```
/imagine prompt: Towering demon with charcoal black skin, multiple twisted horns, glowing sulfurous yellow eyes, massive clawed hands, tattered membrane wings, standing in hellish cavern with rivers of lava, heat shimmer effect, intimidating presence, dark fantasy creature, highly detailed, dramatic underlit, --ar 2:3 --s 220 --no modern
```

### Environment Examples

**Mystical Library**
```
/imagine prompt: Vast circular library with towering bookshelves reaching into darkness, floating books and magical tomes, spiral staircases, ethereal blue-white lights hovering, aged wooden tables with ancient scrolls, stained glass dome ceiling filtering moonlight, dust motes dancing in light beams, sense of infinite knowledge, fantasy interior environment, detailed matte painting, volumetric lighting, --ar 16:9 --s 350
```

**Volcanic Wasteland**
```
/imagine prompt: Desolate volcanic landscape with rivers of glowing lava cutting through black rock, obsidian spires jutting from ground, ash-filled sky with red glow, heat distortion waves, jagged terrain, oppressive and hostile atmosphere, distant volcano erupting, fantasy environment, concept art style, dramatic high contrast lighting, --ar 16:9 --s 300
```

### Item Examples

**Legendary Weapon**
```
/imagine prompt: Ancient elven longbow crafted from pale moonwood with silver inlay, curved with organic flowing design, ethereal blue-white glow along limbs, delicate vine engravings, string that shimmers like starlight, displayed at angle on velvet-draped pedestal, museum lighting, fantasy artifact illustration, photorealistic materials, shallow depth of field, --ar 4:5 --s 120
```

**Cursed Artifact**
```
/imagine prompt: Ominous black iron crown with jagged points, dark red gems set in metal that seem to pulse with inner light, ancient runes etched along band, aura of malevolence, wisps of shadow emanating, displayed on stone altar, cold blue-green lighting, fantasy cursed item, detailed illustration, dramatic shadows, --ar 1:1 --s 150
```

## Accessibility and Inclusivity

### Representing Diversity

**Physical Representation**
- Vary body types: "athletic", "stocky", "slender", "heavyset", "muscular"
- Diverse features: "broad nose", "high cheekbones", "rounded face", "angular features"
- Skin tones: Use specific descriptors rather than just "dark" or "light"
  - "Deep brown skin", "olive complexion", "bronze skin tone", "pale porcelain"
- Ages: Include elderly, middle-aged, young adult, adolescent
- Disabilities: "One-armed warrior with prosthetic", "blind oracle with staff"

**Cultural Sensitivity**
- Avoid stereotypes and caricatures
- Research cultural elements before incorporating
- Use specific cultural references thoughtfully
- Respect cultural dress and symbols
- Consider consulting sensitivity readers for public use

**Gender Representation**
- Vary gender presentation and expression
- Avoid over-sexualization of characters
- Include non-binary and gender-diverse characters
- Represent women in powerful roles naturally
- Male characters with emotional depth

## Legal and Ethical Considerations

### Copyright and Usage

**Midjourney Terms**
- Paid subscribers own generated images
- Free tier has more limited commercial use
- Review current TOS before commercial use
- Consider artist ethics in style mimicry

**Attribution**
- Not legally required for generated images
- Consider transparency: "AI-generated via Midjourney"
- Don't claim as hand-illustrated without disclosure
- Credit Midjourney when relevant

**Artist References**
- Using artist names is allowed but ethically complex
- Consider impact on living artists
- Use movement/style rather than specific artist when possible
- Support actual artists for professional work

### Content Policy

**Prohibited Content**
- No NSFW explicit content
- No realistic violence or gore
- No hate symbols or extremist imagery
- No harassment or harmful content
- Review Midjourney content policy

**Filter Respect**
- Work within platform guidelines
- Don't attempt to bypass safety filters maliciously
- Mature fantasy content possible within bounds
- Frame tastefully and contextually

## Output Guidelines

When generating Midjourney prompts using this skill, Claude should:

1. **Understand the request**: Clarify subject, style, purpose, and constraints
2. **Structure effectively**: Front-load important elements, use clear descriptors
3. **Choose appropriate parameters**: Match aspect ratio, stylization, and chaos to purpose
4. **Provide variations**: Offer 2-3 prompt options when ambiguity exists
5. **Explain choices**: Briefly note why certain terms or parameters were selected
6. **Include refinement tips**: Suggest iteration strategies
7. **Format clearly**: Present prompt ready to copy/paste
8. **Consider context**: Match TTRPG genre expectations and use case

**Output Format Example**
```
Here's a Midjourney prompt for [description]:

/imagine prompt: [full prompt with parameters]

Key choices:
- [Rationale for major descriptors]
- [Parameter explanation]
- [Style approach reasoning]

Refinement suggestions:
- [Iteration option 1]
- [Iteration option 2]
```

## Version Notes

This skill focuses on effective Midjourney prompt generation with special attention to TTRPG illustration needs. It covers technical parameters, style techniques, subject-specific strategies, and methods for working within platform constraints while achieving desired aesthetics. The skill balances creative expression with practical generation techniques and ethical considerations.
