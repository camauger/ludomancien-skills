---
name: editorial-tic-auditor
description: >
  Audit AI-generated long-form fiction (anthologies, collections, multi-chapter novels) for
  recurring stylistic tics — structural patterns, near-identical phrases, syntactic constructions,
  and inter-story duplicates — then generate surgical alternatives per occurrence.
  Use whenever a writer suspects their AI agent is repeating itself, when editing multi-story
  collections before publication, when reviewing a draft for variation and freshness, or when
  asked to "check for tics", "find repetitions", "audit the style", "make the stories feel more
  distinct", or "prevent the AI from writing the same thing twice". Also use proactively when
  *generating* new content that must not repeat patterns already identified in a project.
  Two modes: AUDIT (analyze existing text → tic inventory + alternatives) and GUARD
  (generation time → actively avoid known tic patterns when writing new content).
---

# Editorial Tic Auditor

Prevents AI-generated fiction from developing the verbal, structural, and syntactic habits
that flatten an anthology into a single voice. Works in two modes:

- **AUDIT** — Scans existing text across multiple stories and produces a surgical tic report
- **GUARD** — Uses a tic registry (from a previous AUDIT or user-supplied) to constrain live generation

---

## Tic Taxonomy

Seven categories. Every tic belongs to at least one. For a full catalog of known AI defaults
per category, load `references/tic-library.md` during audit setup.

### S — Structural Tics
Recurring *scene shapes* or *narrative gestures*: how stories begin, resolve, or end.
Examples: protagonist always climaxes into private reflection; stories always close on a
direct address to the reader; a specific vignette type (masturbation, prayer, letter) appears
in every piece.

**Detection signal:** Step back from prose level. Ask: *if I mapped only the scene shape —
what happens, in what order — would multiple stories share the same skeleton?*

### P — Phrasal Tics
Near-identical phrases or sentence fragments repeated across stories, often with minor
cosmetic variation. The content changes; the phrasing doesn't.
Examples: `"Your hip. The angle. Let me—"` / `"Not yet"` as a standalone spoken line.

**Detection signal:** Collect every line of dialogue or action that feels *functional* (advances
the scene mechanically). Run them against each other. If two belong to different stories but
could swap without the reader noticing: phrasal tic.

### V — Syntactic / Verbal Tics
Recurring grammatical constructions that the AI defaults to under pressure: corrections,
contrasts, intensifiers. The specific words change; the sentence shape doesn't.
Examples: `"Not X — Y."` / `"Not X, exactly, but Y."` / `"Less X than Y."` / the em-dash
pivot as default for emotional revelation.

**Detection signal:** Strip content words and look at the skeleton. `"Not pleasure, exactly, but release."` and `"Not arousal. Recognition."` share a skeleton even if they mean different things.

### D — Doublon Tics (Inter-Story Duplicates)
Two stories share a *specific* motif, detail, or sensory image at the same level of
particularity. Distinguishable from thematic resonance by specificity: two characters
having ink-stained fingers is a doublon; two characters being defined by their craft is theme.

**Detection signal:** List every concrete sensory detail (taste, smell, texture, color,
sound). Look for identical entries across stories. The more specific the detail, the more
certain the doublon.

### M — Metaphoric Tics
Recurring metaphor *clusters* — the AI defaults to a small pool of base images to signal
emotion. Each individual metaphor may be original; the problem is that they all come from
the same drawer.
Examples: heat/fire/warmth as the default arousal cluster; gravity/pull/magnetic as the
default attraction cluster; drowning/flooding/wave as the default overwhelm cluster.

**Detection signal:** Extract every metaphor or image used for emotion. Group by vehicle
(what the thing is compared to). If the same vehicle dominates — *heat* in 6 of 8 arousal
descriptions — it's a metaphoric tic, even if no two sentences are identical.

### A — Anatomical Tics
Body parts acting with autonomous agency: they *find*, *trace*, *catch*, *tighten*,
*part* — detached from the character's intention. The AI uses anatomical autonomy as a
shortcut to show involuntary emotion.
Examples: `"her hands found his face"` / `"something caught in her throat"` / 
`"her lips parted"` as default arousal signal / `"his eyes found hers across the room"`.

**Detection signal:** Scan every sentence where a body part is the grammatical subject. Ask:
is the body part doing something *the character chose to do*, or is the body part *acting
on its own*? Autonomous body parts are the tic. Count per story; flag if > 4.

### R — Rhythmic Tics
Sentence-level rhythm defaults: the AI reaches for the same beat patterns when it needs
to signal intensity, transition, or climax.
Examples: the one-word paragraph used as a hammer; the three-noun fragment sequence;
the slow-motion passage where every micro-movement is adverb-weighted.

**Detection signal:** Read aloud. If the same rhythm pattern appears at every emotional
peak, the rhythm is doing the work that the content should be doing. The pattern itself
becomes predictable — the reader anticipates the beat before the meaning arrives.

### F — Frequency Tics
Short phrases (2–5 words) or individual lexical items that appear at high absolute
frequency across the corpus. These are **invisible to qualitative reading** — no single
occurrence is wrong, but the cumulative count creates a rhythm the reader unconsciously
registers as repetition.

Two sub-types:
- **F-P (Phrase)** — 2–5 word sequences: `"for a heartbeat"` / `"her voice was"` /
  `"as if she"` / `"felt the"`
- **F-W (Word/Theme)** — single words carrying thematic or stylistic weight:
  `"witness"` / `"confession"` / `"jasmine"` / `"ancient"`

**Detection signal:** This category *cannot be reliably detected by qualitative reading*.
It requires a word-frequency count. When using a script or tool is possible, run one.
When working manually, extract every occurrence of the P-scan targets plus any word that
"feels" frequent, count them, and build a frequency table before judging any individual
instance. **Do not skip this scan.** F-tics are the category most likely to survive
all other scans and still flag in editorial review.

**Thresholds (prose fiction, 10-story anthology ~200 pages):**
- F-P phrase: flag at > 5× corpus, or > 2× within a single story
- F-W thematic word: flag at > 15× corpus, or > 8× within a single story
- F-W atmospheric word (sensory/setting): flag at > 10× corpus

**Critical distinction — concentration vs. distribution:**
A word appearing 15× evenly across 10 stories is different from 15× concentrated in
2 stories. Flag both patterns, but treat them differently:
- *Distributed* → global reduction needed
- *Concentrated* → the story that owns the word keeps priority; all others cut

### O — Opening Structure Tics
Recurring grammatical patterns in the **first sentence** of each story. These operate
at the table-of-contents level — a reader who glances at story openings detects the
pattern before they've read a word of narrative.

Common AI defaults for story openings:
- `"I had [past perfect for duration]"` — *"I had worn my cassock for twenty-three years"*
- `"She had [past perfect for state]"` — *"She had my wife's face"*
- `"I recognized X before I recognized Y"` — contrast opening
- `"She was [adjective]"` — physical description opening

**Threshold:** Flag if > 2 stories share the same opening grammatical structure.
**Target:** Fewer than 2 stories with the same first-sentence skeleton.
**Detection signal:** List only the first sentence of each story. Strip content words.
Compare the grammatical skeletons. If two are identical, that is an O-tic.

### G — Mechanical Tics *(RPG supplements only)*
Recurring *game design defaults*: the AI applies the same mechanical expressions, stat
conventions, encounter structures, and NPC templates throughout a supplement. Unlike
prose tics, mechanical tics have **functional consequences**: the GM stops reading carefully
because every section is structurally predictable; players stop being surprised because
every challenge follows the same calibration logic.
Examples: every moderate check is DC 15; every major NPC has exactly one secret;
every faction ends with exactly three hooks in the same format.

**Detection signal:** Strip the fiction. Look at the numbers and structure alone. If the
mechanical skeleton of Section 4 is indistinguishable from Section 9 — same DCs, same
action economy, same hook count, same template order — it's a mechanical tic.

**Two sub-types:**
- **G-S (Structural)** — repeated *organizational templates*: NPC entries always in the
  same order, encounter blocks always with the same sections, location entries always
  ending the same way
- **G-N (Numerical)** — repeated *calibration defaults*: DC clustering, CR clustering,
  damage expression patterns, resource counts always at the same values

---

## AUDIT Mode — Step-by-Step

### Step 1 — Intake

Receive the corpus: a list of stories/chapters. If they are not in context, request them.
Note for each: **title**, **character/POV**, **setting**, **core thematic arc** (1 sentence).

If the user has already done partial tic identification (as with the *What the House Keeps*
document), import their findings directly and move to Step 3.

### Step 2 — Systematic Scan

For each tic category, work through the full corpus:

**S-scan:** Map scene shapes. Note: opening gesture / escalation method / climax type /
closing gesture. Flag any skeleton appearing ≥ 2 times.
Cross-check against S-DEFAULT entries in `references/tic-library.md`.

**P-scan:** Extract all:
- Lines of dialogue that are short and functional (commands, refusals, invitations)
- Physical action descriptions that carry mechanical weight (repositioning, control gestures)
- Phrases describing involuntary emotional states
Compare across stories. Flag near-matches.
Cross-check against P-DEFAULT entries in `references/tic-library.md`.

**V-scan:** Extract all sentences using:
- `Not X — Y` / `Not X, but Y` / `Not X, exactly`
- Correction structures (`or not only`, `or rather`, `or perhaps`)
- Em-dash pivots used for revelation
- Tricolon lists (adj, adj, and adj; noun, noun, and noun)
- Redundant intensifiers (`truly`, `deeply`, `profoundly`, `utterly`)
- Hedged emotion (`something that might have been X` / `what felt like X`)
- Passive agency (`she found herself doing X` / `she heard herself say`)
Count per story. Flag any structure appearing > 2× in a single story or > 3× across corpus.
Cross-check against V-DEFAULT entries in `references/tic-library.md`.

**D-scan:** Build a sensory inventory per story. Cross-reference. Flag identical specifics.

**M-scan:** Extract every metaphor used to signal emotion. Group by vehicle (the image
used, not the tenor). Flag any vehicle cluster dominating > 3 occurrences across the corpus.
Cross-check against M-DEFAULT clusters in `references/tic-library.md`.

**A-scan:** Find every sentence where a body part is the grammatical subject. Tally per
story. Flag stories with > 4 autonomous body part constructions.
Cross-check against A-DEFAULT entries in `references/tic-library.md`.

**R-scan:** Identify peak-intensity passages in each story. Map their rhythm. Note:
one-word paragraphs / fragment sequences / slow-motion micro-movement passages /
"And then." paragraph breaks. Flag recurring peak-beat patterns across stories.

**F-scan — MANDATORY, run before all other scans:**

This scan must produce a frequency table before the qualitative work begins.
If a script is available, use it. If working manually, do this explicitly:

*Step 1 — Phrase frequency:* Extract every 2–5 word sequence that appears more than
once. Build a ranked list. Flag anything appearing > 5× across the corpus or > 2× in
one story. Priority targets (check these first — they are confirmed AI defaults):
`"for a heartbeat"` / `"her voice was"` / `"as if she"` / `"felt the"` /
`"as if he"` / `"seemed to"` / `"something in her"` / `"for a moment"`

*Step 2 — Thematic word frequency:* Count every word carrying thematic or aesthetic
weight. Flag anything > 15× corpus. Priority targets:
`witness` / `confession` / `surrender` / `tender` / `ancient` / `sacred` /
`shatter` / `fracture` / `undone` / `ache` — plus any word in the project title
or a character name that could migrate into prose

*Step 3 — Atmospheric word frequency:* Count sensory/setting defaults. Flag > 10×:
`jasmine` / `candlelight` / `velvet` / `stone` / `smoke` / `shadow` / `silk` /
`silver` / `gold` — note concentration by story

*Step 4 — Framing verb frequency:* These are structurally weak and accumulate
invisibly. Count per story, flag if > 5 per story:
`"felt the"` / `"her voice was"` / `"as if she/he"` / `"seemed to"` /
`"looked like"` / `"appeared to"`

Cross-check results against F-DEFAULT entries in `references/tic-library.md`.

**O-scan:** Extract the first sentence of each story/chapter. Strip content words.
Compare grammatical skeletons. Flag any skeleton appearing ≥ 2 times.
Cross-check against O-DEFAULT patterns in `references/tic-library.md`.

**G-scan** *(RPG supplements only):*

*G-S structural scan:* Extract the template skeleton of each entry type (NPC, location,
faction, encounter, magic item). Compare across entries of the same type. Flag when
≥ 70% of entries share the same section order and section count.

*G-N numerical scan:* Build a DC distribution table, a CR distribution table, and a
damage expression inventory. Flag:
- DC clustering: any single DC value appearing in > 40% of checks
- CR clustering: more than 3 consecutive entries at the same CR
- Damage monoculture: the same dice expression (e.g. 2d6+mod) used for > 3 distinct
  sources in the same section
- Resource uniformity: all legendary actions = 3 / all lair action slots = 3 /
  all skill proficiency counts identical across NPCs of different roles
Cross-check against G-DEFAULT entries in `references/tic-library.md`.

### Step 3 — Tic Register

Produce a **Tic Register** in this format for each tic found:

```
## TIC [CATEGORY][NUMBER] — [Short Name]

**Type:** S / P / V / D
**Occurrences:** [n] across [list of stories]
**Effect (when it works):** [1 sentence — what is the tic achieving?]
**Problem:** [1 sentence — why repetition neutralizes it]

| Story | Current Instance | Verdict |
|-------|-----------------|---------|
| Title | Quoted passage  | KEEP / REPLACE / REMOVE |

**Replacement Principles:**
[2–4 concrete strategies that achieve the same effect through different means]

**Distribution Rule:**
[Which story gets to keep the original; what the others must find instead]
```

### Step 4 — Decision Table

After all tics are registered, produce a summary table:

| Tic | Action | Stories Touched |
|-----|--------|-----------------|
| [ID] — [Name] | KEEP × n / REPLACE × n / REMOVE × n | [list] |

### Step 5 — Governing Principle

Close the report with 1–3 sentences articulating the **editorial logic** specific to this
corpus — what the tics reveal about the AI's defaults, and what the revision is protecting.

Example: *"Each device must feel discovered in this story — not imported from a template.
Test: if a phrase functions identically in three different stories, it belongs to none."*

---

## REVISION Mode — Surgical Execution

AUDIT produces a diagnosis. REVISION executes the repairs.

**Critical rule:** The auditor alone cannot write the replacements correctly. Replacing
a passage in literary erotica requires the voice of the story, the emotional register of
the moment, and the character's psychology — not a generic editorial suggestion.
**Always load the appropriate writer skill before executing replacements.**

### Companion Skills to Load for Execution

Choose based on the project's readership and register:

**Literary erotica for female/romantasy readership** (*What the House Keeps* and similar):
→ Load `erotica-fantasy-feminine` — handles interiority, female desire as primary,
  the romantasy register, and explicit content that serves emotional truth.
  This skill contains the Tic Revision Mode with voice anchors for each courtesan.

**General literary erotica (English, mixed readership):**
→ Load `erotica-fantasy-en` + `intimate-noir-prose` for voice calibration

**French erotica:**
→ Load `erotica-fantasy-fr`

**Non-erotica prose fiction:**
→ Load the appropriate genre writer skill for the project

The auditor *identifies and briefs*. The writer skill *executes*.

### Surgical Brief Format

For each passage to replace, the auditor produces a brief in this format:

```
## BRIEF [TIC-ID] — [Story Title] — [Approximate Location]

**Tic category:** [F-P / F-W / V / P / S / etc.]
**What the tic is:** [exact phrase or pattern — e.g., "for a heartbeat"]

**Exact passage to replace:**
"[verbatim text — complete sentence(s) including the tic]"

**Word budget:** ± [n] words — [expand / contract / same length]

**What this passage does narratively:**
[1 sentence: its function — e.g., "marks a micro-pause of hesitation before she speaks"]

**Emotional register at this moment:**
[1 sentence: character state — e.g., "Severine has just yielded control for the first
time; she is raw, surprised by herself, not yet integrated"]

**Character voice signature:**
[3-5 words: e.g., "military precision, controlled, newly permeable"]

**Surrounding context:**
BEFORE: "[sentence immediately before the passage]"
AFTER: "[sentence immediately after the passage]"

**The tic to avoid:** [exact phrase or construction — do not reproduce]

**Direction (not prescriptive):**
[concrete suggestion from the auditor — e.g., "replace the time marker with a physical
anchor specific to this moment — something in the dungeon, her own body, his breath"]
```

### Brief Production Rules

- **One brief per replacement.** Do not batch multiple tics into one brief.
- **Never suggest the replacement in the brief.** The direction gives a vector, not an answer.
  The writer skill must generate the actual prose.
- **Word budget is firm.** If the original is 8 words, the replacement must be 6–10.
  The surrounding prose rhythm cannot absorb a 40-word insertion.
- **Emotional register takes priority over avoiding the tic.** A replacement that loses
  the emotional beat is worse than keeping the tic.
- **Character voice is non-negotiable.** Cirelle sounds nothing like Severine. The brief
  must encode the difference. The writer skill must honor it.

### Execution Protocol

1. Auditor produces all Surgical Briefs for a story
2. Writer skill is loaded with the story's character profile and voice context
3. Writer skill processes one brief at a time
4. Writer skill produces the replacement and explains what function it preserves
5. Auditor skill verifies: does the replacement introduce a new tic? Does it stay within budget?
6. If a new tic is introduced → cycle back to writer skill with a revised brief
7. When all replacements are clean → compile into a revision document

---

## GUARD Mode — Generation Constraints

Use when writing *new* content for a project that already has a tic registry.

### Loading the Registry

The registry can come from:
1. A previous AUDIT output (in context or in a file)
2. A user-supplied list of forbidden patterns
3. A live audit of already-written stories in the project

### Constraint Application

Before generating any scene, internalize the active constraints as a **negative space**:

```
FORBIDDEN STRUCTURES (this session):
- S: [list of forbidden scene shapes]
- P: [list of forbidden phrases, verbatim or near-verbatim]
- V: [list of forbidden syntactic skeletons]
- D: [sensory details already used; do not repeat]
- M: [metaphor vehicles already dominant; find new vehicles]
- A: [body-part autonomy budget: max 4 per story; track count]
- R: [rhythm patterns already used at climax; vary the beat]
- F-P: [phrases at or near corpus threshold; avoid entirely this session]
- F-W: [thematic words at saturation; substitute or remove]
- O: [opening skeleton already used ≥ 2 times; this story must open differently]
- G-S: [RPG only — entry templates that are locked; this entry must use a different structure]
- G-N: [RPG only — DC/CR/damage values already saturated; use different numbers]

ASSIGNED VARIANTS (if this story has been assigned a specific variant):
- [e.g., "Use Option A: slowdown without withdrawal" for delayed orgasm]
- [e.g., "Closing gesture must be object-based, not declarative"]
- [RPG e.g., "This NPC entry has no 'secret' field — replace with a public contradiction"]
- [RPG e.g., "No DC 15 checks in this location — calibrate at 12 or 18"]
```

### Self-Check Protocol

After drafting any scene, story, or supplement section:

1. **Phrase check** — scan dialogue and action lines against P-register
2. **Skeleton check** — identify all `Not X` constructions; count per story (max 2)
3. **Structure check** — compare scene shape to S-register forbidden shapes
4. **Sensory check** — verify no D-doublon with already-written stories
5. **Closing check** — ensure ending gesture is assigned variant, not default
6. **Metaphor check** — group all emotion-metaphors by vehicle; no single vehicle > 2 uses
7. **Anatomy check** — count autonomous body-part constructions; enforce max 4
8. **Rhythm check** — read aloud the peak-intensity passage; is the beat pattern new?
9. **Frequency check** — count F-P phrases in this draft; none should exceed corpus threshold
10. **Thematic saturation check** — count F-W words; flag any approaching per-story limit
11. **Opening check** — does this story's first sentence share a skeleton with any other? If yes, rewrite.
12. **Template check** *(RPG)* — compare this entry's skeleton to the three most recent
    entries of the same type; flag if > 2 sections are in identical order
13. **Numbers check** *(RPG)* — list all DCs, CRs, damage expressions in this section;
    verify no value exceeds 40% saturation relative to the project register

If a violation is found: **do not preserve it as a stylistic choice**. Revise immediately
using the replacement principles from the register.

---

## Replacement Principles (Universal)

These apply across all tic types when the register doesn't specify:

**For structural tics:**
- Replace declaration with gesture
- Replace verbal invitation with physical action
- Replace resolution with suspension (leave the thread live)
- Replace the private vignette with a public or social consequence

**For phrasal tics:**
- Replace the functional phrase with a *specific* object or sensory detail
- The object should be narratively native to this story, not transferable
- Test: would this exact replacement work in any other story? If yes: too generic.

**For syntactic tics:**
- If `Not X — Y` is the default: try *assertion* (`It was Y.`) or *question* (`Was it X?`)
- If the em-dash pivot is the default: try a paragraph break, or remove the revelation entirely
- If correction is the default (`or not only`): try omitting the correction — let the first
  statement carry ambiguity
- If the tricolon is the default: try a single well-chosen noun. *Specificity beats accumulation.*
- If the redundant intensifier is the default (`truly felt`): remove the intensifier entirely.
  The bare verb is almost always stronger.

**For doublon tics:**
- Identify which story has *narrative priority* for the detail (where it does the most work)
- That story keeps it; all others must find a *functionally equivalent* but *specifically different* detail
- The test: same emotional register, different sensory content

**For metaphoric tics:**
- Do not simply replace the vehicle. Ask first: *does this moment need a metaphor at all?*
- If the literal description is already vivid, cut the metaphor entirely
- If a metaphor is necessary: leave the dominant cluster (heat, water, gravity) and choose
  from a different sensory domain — sound, texture, weight, taste, geometry

**For anatomical tics:**
- Return agency to the character: `"she touched his face"` replaces `"her hands found his face"`
- Or describe the action *from the outside*, removing the body part entirely:
  `"She was gentler than he expected"` — no body part named
- Reserve autonomous body parts for moments where the character genuinely has no control
  (involuntary reaction, shock, dissociation). Use sparingly — then the autonomy *means* something.

**For rhythmic tics:**
- If the one-word paragraph is overused: merge it into the preceding sentence, or delete it
  and let the preceding sentence carry the beat
- If the fragment sequence is overused: write one full sentence with a subordinate clause
  instead — *complexity*, not fragmentation
- If the slow-motion passage is overused: cut it to two or three actions maximum; trust the reader

---

## Quality Criteria

A tic report is good when:
- Every KEEP verdict has a stated reason (not just "it works here")
- Every REPLACE verdict has a concrete alternative, not a vague direction
- The replacement alternatives are *native* to the specific story, not generic advice
- The governing principle could be handed to a different editor and they'd make the same decisions
- The register is short enough to hold in working memory during generation (ideally < 30 entries)

A generation pass is good when:
- No phrase from the P-register appears verbatim or within cosmetic variation
- No syntactic skeleton exceeds its maximum count
- The closing gesture of the new story is structurally distinct from the three most recent closings
- At least one sensory detail in the new story has no precedent in the corpus

---

## Notes on AI-Specific Tic Formation

AI agents develop tics because:

1. **Functional phrases are rewarded** — if `"Not yet"` achieved tension once, the model
   reuses the shape that produced tension
2. **Closings are hard** — the model defaults to declarative structure under generation pressure
3. **Sensory defaults cluster** — ink, smoke, candlelight, stone appear because they are
   high-frequency in training data for the genre
4. **Vignette shapes are templates** — the model has learned "intimate scene" as a schema,
   not as a varied set of possibilities
5. **Autonomous anatomy is a shortcut** — rather than writing the character's interiority,
   the model offloads emotional work onto body parts: hands *find*, throats *catch*, hearts *clench*
6. **Metaphor vehicles are pre-loaded by genre** — the model has strong priors about what
   dark fantasy "sounds like": heat, shadow, stone, smoke. These vehicles arrive before
   the scene does — they're pulled from genre memory, not generated from the story
7. **Rhythm under pressure reverts to default** — at peak-intensity moments, the model
   reaches for its most reliable beat pattern (usually: fragment. fragment. One word. Then
   a long sentence that resolves everything). The beat becomes a cue that the climax is
   coming — which ruins the climax
8. **Hedges accumulate under uncertainty** — `something`, `somehow`, `almost`, `what might
   have been` — the model produces these when it is uncertain how much to commit. They are
   emotional equivocation, not literary ambiguity
9. **Game design defaults are load-bearing** *(RPG)* — the model has internalized D&D's
   template language so thoroughly that it reproduces the DMG's NPC format, the module's
   encounter block structure, and the adventure path's hook formula without being asked.
   These are not stylistic choices; they are unexamined defaults from training data
10. **DC 15 is the model's "medium"** *(RPG)* — asked to produce a check, the model
    anchors to 15 the way it anchors to `"Not X — Y"` for contrast. It is the path of
    least resistance, not a calibration decision
11. **Frequency tics are invisible to the model itself** — the model does not track
    cumulative word counts across a long generation session. It uses `"for a heartbeat"`
    on page 3 and again on page 47 without any awareness that it has done so. This is why
    F-category tics survive every qualitative scan: the model cannot detect its own
    frequency patterns without an external count. **Always run the F-scan with a count,
    not a reading.**
12. **Opening structures are template-selected, not composed** — when beginning a new
    story, the model reaches for its highest-probability "story opening" pattern from
    training data. For first-person literary fiction with a male protagonist, that pattern
    is `"I had [duration/state]"`. It feels like a choice; it is a prior.

The auditor's job is to map the schema the AI has fallen into, then break it — not by
forbidding entire categories, but by requiring *specificity* that forces the model off the
default track.

---

## Reference Files

Load `references/tic-library.md` during AUDIT Step 2 for a full catalog of known AI
default tics, organized by category (S/P/V/D/M/A/R/F/O/G), with detection examples and
standard replacement strategies. This accelerates the scan phase significantly.

The library includes:
- Fiction tics (S through R) — universal across prose projects
- Frequency tics (F) — phrase and word counts with thresholds
- Opening structure tics (O) — first-sentence patterns
- RPG mechanical tics (G-S and G-N) — D&D 5e 2024 specific
- Genre-specific defaults for dark fantasy, literary erotica, and D&D supplements
- Zarathar-specific tic risks (Memory Saturation, Island Uniformity, Danger Flattening)

**Script for F-scan** (use when filesystem is available):
```python
from collections import Counter
import re

with open('corpus.txt') as f:
    text = f.read().lower()

# Phrase frequency (2-4 words)
words = re.findall(r'\b\w+\b', text)
for n in (2, 3, 4):
    ngrams = [' '.join(words[i:i+n]) for i in range(len(words)-n+1)]
    top = Counter(ngrams).most_common(40)
    print(f"\n--- {n}-grams ---")
    for phrase, count in top:
        if count >= 4:
            print(f"  {count:3d}  {phrase}")
```
