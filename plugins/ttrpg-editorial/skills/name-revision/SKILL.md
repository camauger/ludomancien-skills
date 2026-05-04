---
name: name-revision
description: Revise AI-generated text to replace overused, generic fantasy names with creative alternatives. Use when reviewing any AI-generated content (stories, TTRPG material, character descriptions, worldbuilding) that contains character or place names. Triggers on requests to "revise names," "fix generic names," "replace AI names," or when the user indicates names feel repetitive or unoriginal.
---

# Name Revision Skill

Revise AI-generated text by replacing overused names with creative, distinctive alternatives.

## Core Problem

LLMs have predictable name preferences. The same names appear constantly across outputs: Seraphina, Lyra, Kira, Aldric, Theron, Shadowmere. These names signal "AI-generated" and break immersion.

## Revision Workflow

1. **Scan** the text for all proper nouns (character names, place names, faction names)
2. **Check** each name against the banned list in `references/banned-names.md`
3. **Flag** names that appear on the list or match banned patterns
4. **Generate** replacements using techniques from `references/naming-patterns.md`
5. **Replace** consistently throughout the document
6. **Verify** no banned names remain

## Replacement Rules

When generating replacement names:

- **Never** use any name from the banned list, even as a base
- **Never** use names ending in -ine, -ina, -ara, -yra, -iel, -ius for protagonists (overused suffixes)
- **Avoid** names that "sound fantasy" in the generic sense (elvish-adjacent, soft consonants, excessive vowels)
- **Prefer** names with harder consonants, unexpected combinations, real-world etymological roots
- **Match** the cultural/linguistic feel of the setting if established
- **Maintain** gender coding if present in original (or explicitly note if neutralizing)

## Quick Reference: Red Flag Patterns

Names likely AI-generated if they:
- End in -phina, -sera, -lith, -wyn, -ael, -iel
- Start with Syl-, Lyr-, Cel-, Ser-, Ael-, Thal-
- Contain -shadow-, -moon-, -star-, -blade-, -storm-
- Sound like "Tolkien lite" or "YA fantasy protagonist"
- Could be a D&D 5e NPC from any official module

## Output Format

When revising, present changes as:

```
ORIGINAL → REPLACEMENT (rationale)
Seraphina → Maret (Breton origin, grounded)
Shadowmere → Kaltvass (Germanic compound, "cold-water")
```

Then provide the revised text with all replacements applied.

## Reference Files

- `references/banned-names.md` — Comprehensive list of names to never use
- `references/naming-patterns.md` — Linguistic techniques for original names
