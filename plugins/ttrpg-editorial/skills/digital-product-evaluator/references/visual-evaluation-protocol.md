# Visual Evaluation Protocol

A step-by-step protocol for evaluating the visual surfaces of a
DriveThruRPG listing: cover at thumbnail size, cover at hero size,
preview pages, and supplementary image gallery.

This is the playbook for Axis 3 (Visuals) of `digital-product-evaluator`.

---

## 1. The Thumbnail Test (the only test that matters first)

DriveThruRPG's primary discovery surface is the **search grid
thumbnail**, roughly 200 × 260 pixels on desktop, smaller on mobile.
If the cover fails at this size, nothing else matters — no one is
clicking through to read the blurb.

### Protocol

1. Open the cover image at its full export resolution.
2. Resize / view it at exactly **200 pixels wide**.
3. Step back from the screen about an arm's length, OR squint, OR
   blur the image with a 1-pixel Gaussian blur in any image editor.
4. Answer these questions in order:

| Question | Pass criteria | Failure signal |
|---|---|---|
| Can you read the title? | All title words readable in <1s | Squinting or guessing |
| Can you identify the genre? | Medieval fantasy vs sci-fi vs horror vs urban vs adult, in <1s | Ambiguous |
| Is there a clear focal subject? | One thing is the focus | Cluttered, no anchor |
| Is the author or imprint legible? (optional) | Readable at thumbnail | Cosmetic only |

If any of the first three fails, the cover is leaking clicks. The fix
is almost always one of:

- Title too small → increase size, add panel/banner background, add
  drop shadow or stroke
- Too many fonts → consolidate to one or two
- Subject too busy → simplify or crop
- Low contrast → add panel under text, darken or lighten subject

### Example failures

- A beautiful illustration of a dragon flying over a city, with the
  title "The Fall of Drakharan" in elegant gold serif over the
  cloudscape. **At thumbnail size, the title vanishes into the
  clouds.** The cover looks like generic fantasy art with no text.
- A character portrait taking 95% of the cover, with the title and
  subtitle stacked in a tiny banner at the bottom. **The eye lands
  on the character, the text never registers.**
- Title in white over a sky background that fades to white at the
  top. **The first three letters of the title are invisible.**

### The five-second rule

A buyer scrolling the search grid spends ~0.5 seconds per thumbnail.
The cover has *one chance* to communicate genre and earn a stop. If
the buyer must work to identify what the product is, they scroll past.

---

## 2. Cover Typography Checklist

### Title font

- [ ] Single primary font (or at most two with clear hierarchy)
- [ ] Font weight heavy enough to remain visible at thumbnail size
- [ ] Title occupies 15–25% of cover height (fiction-style book)
- [ ] Title occupies 20–35% of cover height (zine / supplement)
- [ ] All-caps OR title-case used consistently
- [ ] Letter spacing tight enough to avoid title falling apart
  (especially in serif fonts)

### Title legibility

- [ ] White text over a dark area (or panel) OR
- [ ] Dark text over a light area (or panel)
- [ ] Drop shadow, stroke, or panel/banner background where needed
- [ ] Text not placed over the busiest part of the illustration
- [ ] Title cleanly separated from author name and subtitle (clear
  hierarchy)

### Subtitle / tagline (if present)

- [ ] Distinguishable from title by size (smaller) and weight (lighter)
- [ ] Same font family or a complementary one (not a third font)
- [ ] Readable at thumbnail OR explicitly accepted as hero-only

### Author / imprint

- [ ] Visible but secondary (not competing with title)
- [ ] Bottom of cover or top corner are conventional placements
- [ ] If imprint has a logo, it should be small and consistent across
  the catalog

### System / version callout (if applicable)

- [ ] "For D&D 5e 2024" or "OSR-Compatible" or equivalent
- [ ] Small, near bottom or corner
- [ ] Helps qualified buyers know it's for them at thumbnail

---

## 3. Cover Art Quality and Genre Fit

### Genre signaling at first glance

Without reading the title, the cover should signal genre. Here are
the visual conventions buyers expect:

| Genre | Visual cues |
|---|---|
| High Fantasy | Bright colors, heroic poses, dramatic vistas, magic effects |
| Dark Fantasy | Muted colors, lone figures, gothic architecture, shadowed scenes |
| Grimdark | Dirt, blood, broken weapons, oppressive lighting |
| Sword & Sorcery | Solo warrior figure, ancient ruins, weird beasts |
| Horror | High contrast, off-balance composition, unnatural color, isolated figures |
| Cosmic Horror | Vast scale, alien geometry, sickly greens and purples |
| Sci-Fi / Space Opera | Stars, ships, glowing tech, bright primary colors |
| Cyberpunk | Neon over rain-slick streets, holographic displays, mixed light sources |
| Post-Apocalyptic | Rust, scavenged tech, desert or ruin backgrounds, muted palette |
| Urban Fantasy | City silhouette + magical element, contemporary clothing |
| Pulp / Weird West | Sepia tones, period costume, weird elements (creature, occult symbol) |
| Adult / Erotica | Tasteful pose, suggestive composition, lighting that signals sensuality without being explicit (covers must be SFW-visible) |

### Genre mismatch — common failure

A horror module with a heroic fantasy cover (bright colors, hero
pose) miscommunicates the product. Buyers expecting heroic fantasy
will be disappointed; buyers wanting horror won't even click.

### AI art pitfalls

If the cover is AI-generated, audit specifically for:

- **Hand and finger anomalies** (six fingers, fused fingers, warped)
- **Broken or nonsense text** (any title-area text NOT added by the
  designer; AI generates squiggles that look like text)
- **Anatomy errors** (extra limbs, broken joints, melted features)
- **Object continuity** (a sword that becomes a different sword along
  its length, etc.)
- **Heraldry / symbol coherence** (AI invents symbols that look
  vaguely meaningful but parse as nonsense to anyone with a
  background in heraldry, runic systems, or scripts)
- **Background coherence** (architecture that doesn't follow
  physics, melted perspectives, repeating texture artifacts)

A cover with visible AI errors signals **low production polish**,
which is a strong negative trust signal for the listing.

### Original art quality

If the cover is commissioned or hand-drawn:

- Style consistency across the cover (no clashing techniques)
- Composition with clear focal subject and visual flow
- Color palette intentional (3–5 dominant colors, not muddled)
- Resolution sufficient for print (300 DPI at intended print size)
  if POD is planned

---

## 4. Preview Pages Curation

(See `drivethrurpg-anatomy.md` Section 5 for the platform mechanics.)

### What strong previews include

A curated 3–5 page preview should contain:

1. **A full-bleed atmosphere page** — a beautiful spread or layout
   that establishes tone. Ideally featuring the best art piece
   in the product.
2. **A keyed location or scene** — text that demonstrates the writing
   voice. The buyer reads ~200 words and decides whether the prose
   delivers.
3. **A stat block or mechanical element** — if the product is
   mechanically loaded, show one stat block. The buyer evaluates
   the format and clarity.
4. **A map or handout** — if applicable, show one isolated map page
   with its legend. Demonstrates production value.
5. **The opening of the strongest section** — the first page of the
   most compelling chapter, not the foreword.

### What strong previews avoid

- Cover page (already seen)
- Copyright / credits page
- Table of contents (forgivable if compact and visually appealing)
- Foreword / introduction (mostly unread by buyers)
- Spoilers (the boss reveal, the plot twist resolution)
- Anything that violates the platform's SFW threshold for adult
  products

### How to build a custom preview PDF

1. Open the product PDF.
2. Identify the 3–5 pages that, alone, would convince you to buy
   this product if you were the target buyer.
3. Extract those pages into a separate PDF (most PDF editors support
   "extract pages" or "print to PDF" with page range).
4. Optionally add a one-page "preview" header explaining what's
   shown (rarely needed; the pages should speak for themselves).
5. Upload as the custom preview in the DriveThruRPG publisher
   dashboard.

### Preview page count guidance

| Product page count | Recommended preview length |
|---|---|
| <20 pages | 2–3 pages (don't give away half the product) |
| 20–60 pages | 3–4 pages |
| 60–120 pages | 4–6 pages |
| 120+ pages | 5–8 pages |

The preview is a sample, not a tasting menu. Show enough to convert,
not enough to satisfy.

---

## 5. Supplementary Image Gallery

DriveThruRPG allows 1–8 supplementary images in the gallery on the
product page. These appear below the cover and convert hesitant buyers.

### Recommended set (3–4 images for most products)

1. **An interior layout spread** — shows typography, page density,
   color usage. Demonstrates production polish.
2. **A map** — isolated, with legend visible. For settings,
   adventures, dungeons.
3. **A signature illustration** — the best piece of art in the
   product, cropped to a thumbnail-friendly composition.
4. **A stat block or mechanical excerpt** — for mechanically dense
   products. Shows the format the GM will use at the table.

### Optional additions

- A character portrait gallery (for NPC-dense products)
- A handout (for adventures with strong handout design)
- A "what's inside" infographic (works for some product types but
  can feel like marketing collateral; use sparingly)
- A "before and after" comparison (rare, but works for revised
  editions)

### What doesn't work

- Multiple cover-style images that don't appear in the product
  (the buyer feels misled)
- Low-resolution exports that pixelate at gallery size
- Text-heavy images with text too small to read
- Duplicates of the cover at different angles or crops
- Pure marketing graphics (banners, "available now" badges)

### Image specs (early 2026)

- DriveThruRPG re-compresses uploaded images. Upload at higher
  resolution than needed; the platform downsamples.
- Recommended: 1200–1600 pixels on the long edge, JPG or PNG.
- Aspect ratio: portrait (matching the product layout) for full-page
  shots; landscape for spreads or maps; square for crops.
- File size: <5 MB per image is safe.

---

## 6. Adult Content Visual Considerations

Adult-tagged products have additional visual constraints.

### The SFW threshold for public surfaces

- The cover must be **SFW-visible** in the product page header and
  thumbnail. This means no explicit nudity, no genitalia visible,
  no overtly sexual acts depicted.
- A tasteful pose, suggestive composition, lingerie or implicit
  nudity (back view, strategic crops) is the standard.
- The custom preview PDF must also respect this threshold for the
  pages shown publicly.

### Strategy

- Design two versions of key art: one **SFW marketing version** for
  cover, preview, and gallery, and one **explicit version** for
  the actual product interior.
- Reserve explicit content for inside the product where the buyer
  has consented (purchased and opened).
- If the product has both a SFW and explicit edition (some adult
  creators publish parallel versions), ensure the listing makes
  this clear.

### Audience signaling

The audience for adult TTRPG content expects:

- High production polish (cheap-looking adult content reads as scam)
- Clear consent and content signaling (what is and isn't depicted)
- Genre layer (dark fantasy erotica vs sci-fi adult vs romance —
  the cover should signal both adult AND genre)

---

## 7. Brand Visual Consistency

For creators with multiple products, visual consistency across the
catalog signals professionalism and builds brand recognition.

### What to align

- **Typography**: same title font family across the catalog (with
  variations for tone, but recognizable)
- **Imprint logo / wordmark**: visible on every cover, same placement
- **Color palette**: a brand palette that variants but stays
  recognizable
- **Composition conventions**: e.g., Ludomancien fanzines all use
  a central figure with title above; Fantasy Vixens portraits use
  a recurring tarot-card framework

### What can vary

- Illustration style per product (each product can have its own art
  style)
- Color emphasis (one product can be predominantly red, another
  predominantly blue)
- Atmosphere and mood (a horror product looks horror; a comedy
  product can look comedy)

### Audit question

Open the publisher's full catalog on DriveThruRPG. Do the products
visually feel like they come from the same imprint, OR do they
look like 12 different creators with no through-line? If the
through-line is weak, brand recognition is leaking.

---

## 8. Quick Visual Audit Checklist

Before declaring a listing visually launch-ready:

- [ ] Cover passes the thumbnail test (title legible at 200px wide)
- [ ] Genre is identifiable at thumbnail without reading the title
- [ ] One clear focal subject in the cover
- [ ] Typography: single primary font, sufficient size, sufficient
      contrast
- [ ] Author / imprint visible but not competing
- [ ] System callout if relevant
- [ ] No AI art errors (six fingers, broken text, anatomy)
- [ ] Custom preview PDF uploaded (not default)
- [ ] Preview shows 3–5 pages of strong content, not front matter
- [ ] 2+ supplementary images in the gallery
- [ ] Supplementary images are readable at gallery size
- [ ] Adult content (if applicable) complies with SFW threshold for
      public surfaces
- [ ] Visual style fits within the brand's catalog identity
