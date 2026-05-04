---
name: midjourney-prompt-auditor
description: Audit and score Midjourney prompts before spending credits. Runs seven structural checks — token competition, grammar conflicts, CLIP vocabulary alignment, negative prompt coherence, specificity gradient, parameter-content alignment, and reduction testing — then produces a pass/fail scorecard with surgical rewrites for failures. Use whenever the user says "check this prompt", "audit my prompt", "will this work", "review before I generate", "score this prompt", "what's wrong with this prompt", "why isn't this working", "fix my Midjourney prompt", "optimize this prompt", or submits a Midjourney prompt and asks for feedback. Also triggers when the user pastes a prompt that produced bad results and wants to understand why. Works for any Midjourney version (v5–v7) and any subject matter. Complements midjourney-prompt-generator (which creates prompts) and midjourney-sensual-art (which handles filter navigation) — this skill evaluates prompts those skills produce or that the user writes independently.
---

# Midjourney Prompt Auditor

Evaluate Midjourney prompts against seven structural criteria before generation. Produce a scorecard with pass/fail verdicts, specific failure explanations, and surgical rewrites for anything that fails.

## When to Use

- User submits a prompt and wants it reviewed before generating
- User got bad results and wants to understand why
- User asks to "optimize", "fix", "check", "audit", or "improve" a prompt
- User asks "will this work?" or "what's wrong with this?"
- As a QA pass after generating prompts with midjourney-prompt-generator or midjourney-sensual-art
- When batch-preparing prompts and wanting consistency checks

## The Seven Audit Criteria

Run every prompt through all seven checks, in order. Each check produces PASS or FAIL plus a specific explanation.

### 1. Token Competition

**What it catches:** Too many descriptors fighting for attention, causing Midjourney to pick winners semi-randomly.

**How to check:**
- Identify the three concepts Midjourney will weight most heavily (first ~10 words, plus any high-CLIP-signal terms anywhere in prompt)
- Ask: are those three the user's actual priorities?
- Count total descriptive concepts (not articles/prepositions). More than 12-15 distinct concepts = competition risk
- Check if any single concept is described with redundant synonyms ("messy, tousled, disheveled, unkempt hair" — pick one)

**PASS if:** The top 3 weighted concepts match user intent, total concept count is manageable, no redundant synonyms
**FAIL if:** Important concepts are buried past word 30, or the prompt has 15+ competing concepts, or the same idea is restated in different words

**Rewrite strategy:** Front-load the priority concepts. Merge or cut redundant descriptors. Move secondary details after primary subject+style.

### 2. Grammar Conflicts

**What it catches:** The prompt asking for two incompatible rendering paradigms simultaneously.

**Common conflict pairs:**
- Camera language ("85mm", "f/2.8", "bokeh", "lens flare") vs. painting language ("impasto", "brushstrokes", "oil on canvas")
- "Clean white backdrop" vs. "chiaroscuro" or "dramatic shadows"
- "Photorealistic" vs. "watercolor" or "sketch"
- "Minimalist" vs. detailed scene descriptions
- "Flat design" vs. volumetric lighting
- "Candid snapshot" vs. elaborate posed composition
- Modern clothing/setting terms vs. historical/fantasy period terms
- Multiple art movements that pull in opposite directions ("art nouveau AND brutalist")

**Productive tension (NOT a conflict):**
- "Photorealistic face dissolving into gestural abstraction" — achievable because it defines WHERE each paradigm applies
- "Digital painting with visible oil brushwork" — these coexist because one is medium, one is texture

**The test:** For each pair of descriptors, do they pull the model toward the same rendering pipeline or different ones? If different — does the prompt specify HOW they coexist spatially, or is Midjourney left to guess?

**PASS if:** All descriptors are compatible, or tensions are explicitly resolved with spatial/hierarchical instructions
**FAIL if:** Incompatible paradigms coexist without resolution

**Rewrite strategy:** Pick one paradigm. If the tension is intentional, add explicit spatial instructions ("face rendered with photographic precision, background dissolving into loose brushwork").

### 3. CLIP Vocabulary Alignment

**What it catches:** Terms the model doesn't know, poetic phrases with no visual correlate, human-readable mood words that CLIP maps to nothing or something random.

**High-CLIP-signal terms** (model knows these well):
- Established art movements: "impressionist", "art nouveau", "baroque"
- Named techniques: "chiaroscuro", "impasto", "sfumato", "tenebrism"
- Known artists with large training representation: "Sargent", "Caravaggio", "Mucha", "Frazetta"
- Photography terms: "rim light", "golden hour", "shallow depth of field"
- Material descriptors: "oil on canvas", "watercolor", "charcoal", "ink wash"
- Standard composition terms: "rule of thirds", "dutch angle", "bird's eye view"

**Low-CLIP-signal terms** (likely ignored or randomly mapped):
- Abstract emotional phrases: "the quiet ache of longing", "sovereign stillness"
- Invented compound descriptors: "audace silencieuse", "naughty innocence"
- Narrative/temporal concepts: "the aftermath more eloquent than the act"
- Non-visual sensory language: "the taste of copper", "a whispered secret"
- Obscure or niche references the model likely hasn't seen in captions
- French or non-English terms (unless they're art-specific like "trompe l'oeil")

**Gray zone — might work, test first:**
- Mood words with some visual correlate: "melancholic", "ethereal", "ominous"
- Cultural references: "Victorian", "Edo period", "Moorish"
- Emotional states with visual expression: "defiant", "vulnerable", "smug"
- Specific-but-niche artists: test with `--s 0` to see if recognized

**PASS if:** 80%+ of descriptive terms have strong CLIP signal. Low-signal terms are limited to 1-2 closing flourishes (harmless dead weight)
**FAIL if:** Core structural terms (subject, style, lighting) rely on low-signal vocabulary, or more than 30% of the prompt is CLIP-invisible

**Rewrite strategy:** Replace low-signal terms with high-signal equivalents. Keep poetic closers only if they don't compete with functional terms. Example: "sovereign stillness" → "composed regal expression, steady gaze" (two CLIP-visible terms instead of one invisible one).

### 4. Negative Prompt Coherence

**What it catches:** The `--no` flag contradicting the positive prompt, or missing critical exclusions.

**How to check:**
- List every term in `--no`
- For each, scan the positive prompt for the same term or a strong synonym/implication
- Check: does the positive prompt use camera language while `--no` blocks "photograph"? (The positive terms likely overpower)
- Check: are there obvious exclusions missing? (e.g., a painterly prompt with no `--no text watermark`)

**Common contradictions:**
- Prompt says "warm amber light" + `--no warm` 
- Prompt uses "85mm shallow depth" + `--no photograph`
- Prompt describes "detailed background" + `--no background`

**Common missing exclusions:**
- Painterly prompts should typically `--no text watermark`
- Character prompts often need `--no extra limbs duplicate`
- Dark/moody prompts may need `--no bright neon oversaturated`

**PASS if:** No contradictions between positive and negative, reasonable exclusions present
**FAIL if:** Any term appears in both positive and `--no`, or critical exclusions are missing for the style

**Rewrite strategy:** Remove contradictions (decide which direction wins). Add standard exclusions for the genre.

### 5. Specificity Gradient

**What it catches:** Uniform detail density that fights the model, or critical elements left unspecified while trivial ones are over-described.

**Principle:** Detail should cluster on what the user cares about controlling. Deliberately vague areas give Midjourney room to improvise (which it's good at).

**How to check:**
- Identify the three most detailed sections of the prompt
- Ask: are those the three things the user would be most upset to see wrong?
- Check for "orphan specifics" — one hyper-detailed element surrounded by vague ones (e.g., "a woman in a room with a specifically described 14th century Venetian glass chandelier with 47 candles" — the chandelier will dominate the image)
- Check for "missing anchors" — no description at all for a critical element (e.g., detailed face description but zero guidance on what she's wearing → random modern clothing on a fantasy character)

**PASS if:** Detail density correlates with importance. Critical elements are specified, secondary elements are loosely guided or omitted
**FAIL if:** Detail is uniformly distributed, or the wrong things are specified, or a critical element has zero guidance

**Rewrite strategy:** Add minimal guidance to unspecified critical elements. Reduce over-specified secondary elements to 1-2 words. Let the specificity gradient match priority.

### 6. Parameter–Content Alignment

**What it catches:** Technical parameters that fight the prompt's intent.

**Key checks:**

| Parameter | Check |
|-----------|-------|
| `--ar` | Does it match the composition? Portrait prompt + `--ar 16:9` forces unwanted horizontal fill. Full-body character needs `--ar 2:3`, not `--ar 1:1`. |
| `--s` | Stylize 0-50 fights painterly/artistic prompts. Stylize 500+ fights prompts needing precision/accuracy. Sweet spots: photorealistic 50-100, painterly 200-350, experimental 500+. |
| `--c` | Chaos >30 on prompts requiring consistency (character sheets, series). Chaos <10 on exploration prompts wastes the opportunity for variation. |
| `--v` | V7 for most work. V6 if using `--cref`, multi-prompting with weights, or needing legacy quality values. |
| `--q` | V7 uses 1/2/4. If prompt says `--q 0.5` on v7, it's invalid. |
| `--no` | See criterion 4 above. |
| `--raw` | Fights high-stylize. Redundant with `--s 0`. |

**PASS if:** All parameters support the prompt's intent and are valid for the selected version
**FAIL if:** Any parameter contradicts intent or is invalid for the version

**Rewrite strategy:** Adjust parameters to match intent. Flag version-incompatible values.

### 7. Reduction Test

**What it catches:** Dead weight — words that take up tokens without influencing the output.

**How to check:**
- Read each phrase in the prompt
- Ask: if I remove this phrase, does the imagined output change?
- If no → it's dead weight
- Categories of dead weight:
  - **Redundant restating**: "same blue eyes, consistent blue eyes, matching blue eyes" → say it once
  - **Human-readable-only closers**: "the painting itself an act of slow attention" → CLIP doesn't parse this
  - **Filler adjectives**: "very", "really", "truly", "extremely" → CLIP ignores these
  - **Narrative framing**: "imagine a scene where", "picture this:" → invisible to model
  - **Contradicted terms**: anything also listed in `--no`

**PASS if:** Removing 20% or less of the prompt would change nothing. Prompt is lean.
**FAIL if:** 30%+ of the prompt is dead weight. There's room for significant compression.

**Rewrite strategy:** Cut dead weight. Compress redundancies. A lean 50-word prompt where every token pulls its weight outperforms a verbose 120-word prompt.

## Output Format

For each audit, produce this scorecard:

```
## Prompt Audit Scorecard

**Prompt:** [the prompt being audited, truncated to first 50 words + "..."]
**Version detected:** [v5/v6/v7 or "not specified"]
**Word count:** [N words positive prompt] + [N words in --no]

| # | Criterion | Verdict | Issue |
|---|-----------|---------|-------|
| 1 | Token Competition | PASS/FAIL | [specific issue or "—"] |
| 2 | Grammar Conflicts | PASS/FAIL | [specific issue or "—"] |
| 3 | CLIP Vocabulary | PASS/FAIL | [specific issue or "—"] |
| 4 | Negative Coherence | PASS/FAIL | [specific issue or "—"] |
| 5 | Specificity Gradient | PASS/FAIL | [specific issue or "—"] |
| 6 | Parameter Alignment | PASS/FAIL | [specific issue or "—"] |
| 7 | Reduction Test | PASS/FAIL | [N% removable] |

**Score: [N]/7**

### Failures Explained
[For each FAIL: what specifically is wrong and why it matters for the output]

### Rewritten Prompt
[Full rewritten prompt with all failures addressed. Show the prompt ready to paste.]

### What Changed
[Bullet list of specific changes and rationale — not vague "improved flow" but "moved X before Y because weight distribution", "replaced Z with W because CLIP signal"]
```

## Style-Specific Audit Extensions

When the user is working in a known house style (e.g., Fantasy Vixens painterly impasto), apply additional checks:

**Fantasy Vixens House Style Checklist:**
- Does the prompt include impasto/palette knife texture language?
- Is chiaroscuro lighting specified with warm single source?
- Is the palette limited to 3 hues maximum?
- Are edges described with lost-and-found hierarchy (hard on focal points, soft elsewhere)?
- Does `--no` exclude "photograph digital smooth clean airbrushed flat background text watermark"?
- Is `--s` in the 250-300 range?
- Is `--ar 2:3` for portraits?
- Is the face/skin rendered with more precision than the background (specificity gradient matching the style's core paradox)?

If working in this style, add a **House Style Compliance** row to the scorecard (PASS/FAIL) with specific missing elements listed.

## Batch Audit Mode

When auditing multiple prompts (e.g., a series or character sheet set):

1. Run the 7-check audit on each prompt individually
2. Then run cross-prompt checks:
   - **Palette consistency**: Are the same character's colors consistent across prompts?
   - **Parameter consistency**: Are `--s`, `--c`, `--v` the same across the batch?
   - **Identity anchors**: Do character-defining features (eye color, hair, distinguishing marks) appear in the same position and wording across all prompts?
   - **Style coherence**: Are all prompts using the same rendering paradigm?
3. Flag any cross-prompt inconsistencies in a separate section of the report

## Edge Cases

- **Intentionally experimental prompts**: If `--c` is high (50+) and the prompt is clearly exploratory, relax criteria 1, 5, and 7. The user is exploring, not controlling.
- **Multi-prompt syntax** (`::` weights): Check that weights are valid for the version. V7 has limited multi-prompt support — flag if v7 is specified.
- **Style reference prompts** (`--sref`): When a style reference URL is present, the prompt's style language matters less (the reference dominates). Relax criterion 3 for style terms but keep it strict for subject terms.
- **Permutation prompts** (`{option1, option2}`): Audit each permutation independently if there are ≤4. If more, audit the base structure and spot-check 2-3 permutations.
