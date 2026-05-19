---
name: digital-product-evaluator
description: >
  Evaluate the commercial readiness of a TTRPG product listing on DriveThruRPG
  (with secondary coverage of itch.io and Ko-fi). Four-axis audit: Listing copy
  (title, blurb, tags, keywords, category fit), Pricing strategy (PWYW vs fixed,
  copper/silver/gold/platinum thresholds, bundles, sale cadence), Visuals (cover
  legibility at thumbnail size, preview pages, screenshot strategy), and
  Positioning (USP, competitive landscape, target audience). Two modes:
  pre-launch (before publishing) and post-launch (already on sale, sales
  underperforming). Produces a scorecard with Strong / Adequate / Needs Work /
  Blocking Issue per axis plus a prioritized action list. Use on "audit my
  DriveThruRPG listing", "is my product page good", "should I price this
  pay-what-you-want", "review my cover thumbnail", "why isn't this selling",
  "evaluate before launch", "is my title clickable", "what keywords should I
  use", "audite ma page DriveThruRPG", "ma fiche produit est-elle bonne",
  "stratégie de prix pour ce supplément", "mon titre fonctionne-t-il",
  "pourquoi ça ne se vend pas", "diagnostiquer après lancement", "optimise mes
  tags", "ma couverture est-elle lisible en miniature". Also triggers on
  "ready to publish", "honest take on my listing", "competitive analysis",
  "post-mortem on sales". NOT for content quality (use ttrpg-supplement-reviewer),
  print layout (use ttrpg-print-design), or cover art generation (use
  midjourney-prompt-generator + tarot-card-portrait). This skill evaluates the
  product as a thing to sell, not as a thing to read.
---

# Digital Product Evaluator

Evaluate the commercial readiness of a TTRPG product on DriveThruRPG (primary)
with secondary coverage of itch.io and Ko-fi. This skill is what a publisher's
marketing director would deliver before greenlighting a launch — or before
declaring a post-launch product dead.

The report is honest, specific, and ranked by ROI. The goal is not to be
encouraging — it is to identify what will move the needle on sales.

---

## Before You Begin

1. **Determine the mode.** Two modes change the emphasis dramatically:
   - **Pre-launch:** product not yet published. Focus on whether the listing
     is ready and what to fix before going live.
   - **Post-launch:** product already on DriveThruRPG, sales underperforming
     or stagnant. Focus on diagnosing why and which lever to pull.
   If unclear, ask. Default to pre-launch.

2. **Gather inputs.** Minimum viable submission:
   - Product title and subtitle (if any)
   - Long description / blurb as it will appear (or appears) on the listing
   - Tags and keywords selected
   - Cover image (or description if no image yet)
   - Price (or pricing plan: fixed, PWYW, bundle, etc.)
   - Page count, system, format (PDF / softcover / hardcover)
   For post-launch: also gather sales data if available (units sold, time on
   market, traffic source, recent ranking).

3. **Identify the niche.** Where on DriveThruRPG does this product compete?
   (D&D 5e adventures, OSR zines, Fantasy Vixens-style adult, system-agnostic
   GM tools, settings, bestiaries, etc.) Niche shapes every axis.

4. **Identify the brand.** Solo creator? Established imprint (Ludomancien,
   Fantasy Vixens, custom)? Brand affects pricing latitude, audience trust,
   and how aggressively the blurb can lean on persona.

If the user has not provided enough information, ask before evaluating.
Do not invent data.

---

## The Four Axes

Every evaluation covers all four axes. Each axis produces:

- A **diagnostic** (what's working, what isn't, with specific quotes or details)
- A **verdict**: **Strong / Adequate / Needs Work / Blocking Issue**
- **Actionable recommendations** ranked by expected impact

### Axis 1 — Listing Copy

The textual page-product surface: title, subtitle, blurb, tags, keywords,
category placement. This is what converts a thumbnail click into a wishlist
or a buy.

**Evaluate:**

- **Title.** Does it tell a browser what the product is in ≤8 words?
  - Includes the *category cue* (Adventure, Setting, Bestiary, Zine, etc.)?
  - Includes a *hook* (the unique angle, place, antagonist, or premise)?
  - Avoids fantasy noun-soup (e.g. "Shadows of the Forgotten Crown of the
    Ancient Realm") that conveys no specific promise?
  - System callout where relevant ("for D&D 5e", "OSR-compatible", etc.)?

- **Subtitle / tagline** (if used). Is it earning its line, or restating the
  title in different words? A good subtitle adds the *emotional or genre
  hook* the title couldn't fit.

- **Blurb structure.** The first paragraph must accomplish three things in
  under 100 words: (1) what is it, (2) who is it for, (3) why is it
  different from the 47 other products in the same category. The blurb that
  buries the answer to (1) past line 3 loses 80% of skimmers.

- **Blurb voice.** Does the voice match the niche?
  - OSR audience expects terse, evocative, no-fluff prose.
  - Adventure path buyers expect setup → stakes → promise of resolution.
  - Adult / Fantasy Vixens audience expects sensual register and explicit
    content signals.
  - GM advice / system-agnostic buyers expect "here's what you'll be able
    to do at your table after reading this."

- **What's inside.** Most blurbs forget to list the actual *contents*.
  Bulleted "What's Inside" sections lift conversion notably. Page count,
  number of NPCs/locations/encounters/maps included, handouts, VTT support,
  print-friendly version included or not.

- **Tags.** DriveThruRPG tag selection is a major discovery lever.
  - System tag(s) correct and complete (D&D 5e, D&D 2024, OSR, PF2e, etc.)?
  - Genre tag(s) selected (Dark Fantasy, Horror, Mystery, Urban, etc.)?
  - Content-warning tags applied when relevant (Adult, Violence, etc.)?
  - Format tags (Adventure, Setting, Toolkit, Bestiary, Zine)?
  - Common mistake: missing the *secondary system* tag (a 5e product
    sometimes also tags OSR-compatible when conversion is trivial).

- **Keywords.** DriveThruRPG keywords feed internal search.
  - Are common buyer queries covered? ("one-shot", "low-level adventure",
    "horror module", "session zero", "GM tools")
  - Does the listing surface for variant spellings? ("5e" vs "5E" vs "fifth
    edition" vs "2024 edition")
  - For FR products: are FR + EN keywords both present?

- **Category placement.** Is the product in the right primary category?
  Wrong category = invisible to the audience that would buy it.

**Verdict criteria:**

- **Strong:** Title is specific and hook-driven; blurb hits the 3 jobs in
  the first paragraph; tags and keywords are exhaustive; category is correct.
- **Adequate:** Title is functional but could be sharper; blurb works but
  buries the hook; 80%+ of relevant tags present.
- **Needs Work:** Generic title; blurb leads with worldbuilding instead of
  product; major tag gaps; visible category mismatch.
- **Blocking Issue:** Title is meaningless without context; blurb fails to
  explain what the product is; tags missing the primary system; category
  is wrong.

### Axis 2 — Pricing Strategy

How much to charge, in what model, with what cadence.

**Evaluate:**

- **Price point vs page count.** DriveThruRPG buyers internalize rough
  benchmarks. Anchor against these (2026 norms, USD):
  - **<10 pages:** $0.99–$2.99 (zine territory)
  - **10–30 pages:** $2.99–$5.99 (single-session content)
  - **30–80 pages:** $5.99–$11.99 (mini-supplements, full adventures)
  - **80–160 pages:** $11.99–$19.99 (full supplements)
  - **160+ pages:** $19.99–$34.99+ (campaign books, settings)
  Adjust for brand strength, color interior, art density, established
  audience. A solo creator's first product cannot price like Wizards.

- **PWYW vs fixed.**
  - PWYW with $0 minimum: maximum visibility, builds list/audience, low
    revenue per download. Right for: first release, building reputation,
    free quickstarts that lead to paid follow-ups, brand-building zines.
  - PWYW with suggested price: middle ground. Average pay often lands
    20–35% of suggested. Useful for "name your price but here's where I'd
    set it" framing.
  - Fixed price: maximum revenue per sale, lower download volume. Right
    for: established audience, dense product, sequel to a successful
    earlier release, niche premium content.
  - **Common mistake:** going fixed-price on a debut with no audience.
    The product becomes invisible because it has no downloads to drive
    DriveThruRPG's algorithmic surfacing.

- **Copper / Silver / Electrum / Gold / Platinum thresholds.** DriveThruRPG's
  best-seller badges are powerful conversion signals. Pricing too low
  may make Copper trivial; pricing too high may make even Silver hard to
  hit. Evaluate the implied unit-sales required to badge.

- **Bundles.** Does the product belong in a bundle?
  - "Bundle of Holding" / "Collector's Bundle" mechanics give a
    discounted multi-product offer that lifts average order value.
  - If the creator has 2+ related products, a bundle should exist.
  - If not, flag it as a future opportunity (and note: solo product
    has no bundle option until the second product ships).

- **Sale cadence (post-launch).** GMs Day (March), May the 4th, Christmas
  in July, Black Friday, Free RPG Day. A product with no sale plan leaves
  20–40% of yearly revenue on the table.

- **Print-on-demand opportunity.** Is the PDF print-ready (or close)?
  DriveThruRPG POD often doubles total revenue of a successful PDF
  release. If the product is interior-friendly (black & white or limited
  color, standard sizes), flag POD as a missed revenue lever if absent.

- **Currency and FR market.** Default DriveThruRPG currency is USD; FR
  buyers are a smaller but loyal audience. Note if the product has FR
  audience appeal but is English-only, or vice versa.

**Verdict criteria:**

- **Strong:** Price aligns with page count and brand strength; PWYW vs
  fixed choice fits the launch stage; POD considered; sale cadence
  planned or in place.
- **Adequate:** Price is reasonable but suboptimal (e.g. $7 where $5.99
  or $8.99 would convert better); pricing model defensible.
- **Needs Work:** Price clearly off the benchmark for the niche; POD
  ignored when product is print-ready; no sale strategy.
- **Blocking Issue:** Debut fixed-price at premium with no audience and
  no sample/quickstart; pricing model contradicts product type (e.g.
  charging $24.99 for a 12-page zine).

### Axis 3 — Visuals

What the buyer sees before reading a word.

**Evaluate:**

- **Cover legibility at thumbnail.** DriveThruRPG's primary discovery
  surface is the small thumbnail. Open the cover at the size it appears
  in search results (roughly 200×260 px). Can a browser:
  - Read the title?
  - Identify the genre at a glance (medieval fantasy vs sci-fi vs
    horror vs urban)?
  - See the focal subject without squinting?
  If any of these fail, the cover is leaking clicks. The mistake is
  almost always: title too small, too many fonts, focal subject too
  busy, low contrast between subject and background.

- **Title typography on cover.**
  - Single-font discipline (or at most two, with clear hierarchy)
  - Sufficient size (the title should occupy 15–25% of cover height
    for a fiction-style book; up to 30% for a zine)
  - Sufficient contrast (white-on-light or black-on-dark = failure)
  - Drop shadow / stroke / panel behind text if needed for legibility
    over busy art

- **Cover art quality and fit.** Does the art match the genre and
  promised content?
  - Generic AI fantasy cover on a horror module = mismatched promise
  - Cropped-too-tight figure with no environmental context = fails the
    "what is this product about" job
  - Cover should signal *what gameplay feels like*, not just "fantasy"

- **Preview pages.** DriveThruRPG lets you set preview pages. Default
  is first N pages, but you can curate.
  - Is the preview showing the best 3–5 pages, not the cover + ToC + 
    forward (which converts no one)?
  - Are stat blocks, maps, or a representative scene visible in the
    preview?
  - For adult content: are preview pages SFW-appropriate (sample of
    the product without triggering the platform's NSFW gating)?

- **Image gallery / screenshots.** Beyond the cover, DriveThruRPG allows
  additional preview images.
  - Are 2–4 supplementary screenshots provided showing layout, a map,
    a stat block, an NPC portrait?
  - Are these images optimized for thumbnail viewing (large text,
    high contrast)?

- **Brand consistency.** Does the cover style match the brand's existing
  catalog? An imprint with a clear visual identity (e.g. Ludomancien
  fanzine zines, Fantasy Vixens portrait cards) should not break style
  per product without intent.

**Verdict criteria:**

- **Strong:** Title legible at thumbnail; cover signals genre and
  premise; preview pages curated; 2+ supplementary screenshots.
- **Adequate:** Cover works but is generic; title legible; preview is
  default (first N pages) but acceptable.
- **Needs Work:** Title hard to read at thumbnail; cover art doesn't
  signal genre clearly; preview shows mostly front matter.
- **Blocking Issue:** Title illegible at thumbnail; cover is a placeholder
  or visibly AI-generated with errors (six-fingered hand, broken text,
  warped objects); no preview pages set.

### Axis 4 — Positioning

Where this product sits in the DriveThruRPG landscape and whether the
listing makes that position visible.

**Evaluate:**

- **USP (Unique Selling Proposition).** Can the user complete this
  sentence in one breath: "This is the only TTRPG product that ___."
  If not, the USP is muddy and the listing reflects it.

- **Competitive landscape.** Identify 3–5 products in direct competition.
  - What does this product do better than them?
  - What does it do worse?
  - Is the differentiator visible in the listing, or only obvious
    after reading the product?
  - Common mistake: the creator believes their hook is the worldbuilding,
    but the actual hook (and the thing buyers want) is the table
    procedure / format / utility.

- **Target audience.** Who specifically is the buyer?
  - System (D&D 5e 2024 buyer ≠ OSR buyer)
  - Experience level (new GM ≠ veteran GM)
  - Play style (combat-focused ≠ narrative-focused ≠ horror table)
  - Demographics where relevant (adult content, francophone market,
    casual vs hobbyist)
  - Is the listing speaking to this audience, or to a generic "RPG
    player"?

- **Audience-channel match.** DriveThruRPG audience skews D&D 5e and
  OSR-curious. itch.io audience skews indie / system-agnostic /
  narrative. Ko-fi audience is the creator's existing community.
  - Is the platform choice right for the product?
  - Should the product be on multiple platforms?

- **Positioning in series / catalog.** If the creator has other
  products, does the listing surface them?
  - "Other titles in this series" section in the blurb?
  - Cross-promotion in the description?
  - Bundle opportunity (see Axis 2)?

- **Brand alignment.** Does the product reinforce the brand's promise,
  or does it dilute it? An imprint known for one thing publishing a
  one-off in a different register without explanation confuses buyers.

**Verdict criteria:**

- **Strong:** Clear USP visible in title and blurb; competitive
  differentiation explicit; audience addressed by name and assumption;
  catalog cross-promotion in place.
- **Adequate:** USP exists but is buried; audience is implied not
  named; catalog promotion is absent but not damaging.
- **Needs Work:** USP unclear even after reading the listing; product
  competes against itself (own catalog) without bundling; audience is
  generic.
- **Blocking Issue:** Product has no identifiable USP; the listing
  could apply to any of 30 similar products; wrong platform for
  the audience.

---

## Output Format

The evaluation should read as a marketing director's commercial readiness
report. Use this structure:

```
# Évaluation Commerciale — [Product Title]

## Observation Liminaire
[1–3 sentences: product type, niche, brand context, launch mode.
Flag any fundamental positioning problem before the detailed audit.]

## Mode
[Pre-launch / Post-launch — and the specific question being answered.]

## Axe 1 — Listing Copy
[Diagnostic with specific quotes, verdict, top 2–3 recommendations]

## Axe 2 — Pricing Strategy
[Diagnostic with benchmark comparison, verdict, top 2–3 recommendations]

## Axe 3 — Visuals
[Diagnostic with thumbnail-size assessment, verdict, top 2–3 recommendations]

## Axe 4 — Positioning
[Diagnostic with competitive landscape, verdict, top 2–3 recommendations]

## Scorecard
| Axe | Verdict | Priorité de correction |
|---|---|---|
| Listing Copy | … | … |
| Pricing | … | … |
| Visuels | … | … |
| Positionnement | … | … |

## Verdict de Lancement / Diagnostic Post-Lancement
[Pre-launch: Ready / Almost / Not Yet, with the gating issues named.
Post-launch: most probable cause of underperformance and the one lever
most likely to move sales.]

## Plan d'Action Priorisé
1. [Highest-ROI fix, with specific edit]
2. [Next-highest-ROI fix]
3. [...]
[Ordered by expected impact on sales, not by axis order.]
```

**Language:** Match the language of the submitted listing. If the product
is FR, write the report in FR. If the user requests a different language,
comply.

**Tone:** Marketing director, not coach. Direct about what will sell and
what won't. The creator already invested in writing the product — respect
that by being useful, not by being soft.

---

## Mode-Specific Adjustments

### Pre-Launch Mode

- The four axes apply with equal weight.
- Add a **"Days to Launch-Ready"** estimate in the verdict: how many
  hours of work to clear the Blocking Issues and Needs Work items.
- Recommend a **soft-launch test**: post a sample / quickstart for free
  to gauge audience response before the full launch.

### Post-Launch Mode

- Adjust weights based on the **failure pattern**:
  - **Low impressions / low clicks** → Axis 3 (Visuals) is the
    primary suspect. The thumbnail isn't converting browsing into
    clicks.
  - **High clicks / low buys** → Axis 1 (Listing Copy) is the primary
    suspect. People are arriving and bouncing — the blurb isn't
    closing the sale.
  - **Sales stalled after initial bump** → Axis 4 (Positioning) is
    primary. The product reached its first-tier audience and isn't
    converting beyond it; the USP isn't broad enough or it's not
    being communicated to a second audience.
  - **Decent sales, low revenue** → Axis 2 (Pricing) is primary.
    Mispriced for the value delivered.
- Add a **"Three Levers"** recommendation: the three changes most
  likely to move the needle in the next 30 days, ranked by effort/impact.

---

## Interaction with Other Skills

This skill is the **commercial reviewer**. It identifies sales-blocking
issues but delegates content fixes:

- **Manuscript quality / content audit** → hand off to `ttrpg-supplement-reviewer`
- **Prose tics in the blurb** → hand off to `editorial-tic-auditor`
- **Generic fantasy names in title/blurb** → hand off to `name-revision`
- **Cliché trope in title/positioning** → hand off to `ttrpg-cliche-buster`
- **Cover or interior visual design** → hand off to `ttrpg-print-design`
- **Cover art generation (Midjourney prompts)** → hand off to
  `midjourney-prompt-generator` (or `tarot-card-portrait` for character cards)
- **Cover prompt audit** → hand off to `midjourney-prompt-auditor`
- **FR-specific listing nuances** → consider `mots-rares-jdr` /
  `fanzine-advice` for FR-language register

When a problem falls in another skill's domain, name the handoff
explicitly. Do not attempt to replicate another skill's protocol.

---

## Edge Cases

**No cover yet (pre-launch):** Skip the visual-evaluation portion of
Axis 3 (cover legibility) but still assess preview-page strategy and
screenshot planning. Flag the missing cover as a Blocking Issue with
the highest-priority action.

**Free product:** Pricing axis adjusts — evaluate whether free is the
right choice (lead magnet, brand building, charity, free quickstart for
a paid follow-up). A free product can still be evaluated on whether it
*should* be free.

**Adult content:** Apply the platform's NSFW visibility rules. On
DriveThruRPG, adult content is gated and discovery is harder. Tag and
warning compliance is non-negotiable. Preview pages must respect the
SFW threshold for the platform's previewer.

**Multi-language product:** Evaluate the listing in each language if
both are present on the same product page. Note language-specific
register issues.

**Bundle as the product:** If the user is evaluating a bundle listing
(not a single product), Axis 2 (Pricing) becomes dominant — the bundle's
discount math and inclusion logic are the primary sales drivers.

**Crowdfunded product migrating to DriveThruRPG:** The listing must
re-explain the product to a cold audience that didn't back the campaign.
Listings copied verbatim from Kickstarter pages typically fail because
they assume backer context.

---

## Reference Files

Load these as needed — not all at once.

- `references/drivethrurpg-anatomy.md` — Platform-specific mechanics:
  category taxonomy, tag taxonomy, badge thresholds (Copper / Silver /
  Electrum / Gold / Platinum), recommended preview pages, NSFW gating
  rules, POD specs and minimum thresholds.
- `references/pricing-benchmarks.md` — Detailed price-by-pagecount
  benchmarks by product type (adventure, setting, bestiary, zine,
  player options), PWYW conversion data, sale-cadence calendar
  (GMs Day, May the 4th, Christmas in July, Black Friday).
- `references/listing-copy-patterns.md` — Title formulas that work
  (Hook + Category, Place + Genre, Question titles), blurb structure
  templates by product type, tag-stacking strategies, keyword
  research patterns.
- `references/visual-evaluation-protocol.md` — Step-by-step thumbnail
  legibility test, cover-art genre signaling checklist, preview-page
  curation protocol, screenshot strategy by product type.
- `references/positioning-templates.md` — USP framework, competitive
  landscape mapping protocol, audience-channel-fit matrix
  (DriveThruRPG / itch.io / Ko-fi), brand alignment audit.
