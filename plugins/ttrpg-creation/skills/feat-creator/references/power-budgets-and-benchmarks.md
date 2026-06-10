# Power Budgets and Benchmarks — Feats 2024

Calibration is comparison. A custom feat is never "balanced" in the
abstract — it is balanced *against named official feats* occupying the
same niche. This file gives the currency, the floor and ceiling per
category, quantified guidelines, and the calibration protocol.

## The Currency: +1 ASI ≈ Half a Feat

Every 2024 General feat = **+1 Ability Score Increase + the actual
benefit package**. Since the whole General feat competes against +2 ASI
(the Ability Score Improvement feat is itself a General feat — the
baseline made explicit), the benefit package is worth roughly **one +1
ASI**, which is also roughly **one Origin feat**.

Working consequences:

- **Custom General feat** = +1 ASI + a package you could almost ship
  as an Origin feat. If the package alone would be a *strong* Origin
  feat (Lucky-grade), the General feat is over budget.
- **Custom Origin feat** = one package, no ASI, bounded by Skilled
  (floor of usefulness) and Lucky / Magic Initiate (ceiling).
- **Custom Epic Boon** = +1 ASI (max 30) + one effect that would be
  *broken* on a General feat. If the signature effect would be merely
  "strong" at level 8, it is an under-budgeted boon.

## Benchmarks per Category

### Origin — floor and ceiling

| Bound | Feat | Why it sits there |
|---|---|---|
| Floor | **Musician** | Heroic Inspiration to PB allies after a rest — real but situational, no combat math |
| Mid | **Skilled**, **Tough** | The yardsticks: 3 proficiencies, or +2 HP/level |
| Ceiling | **Lucky**, **Magic Initiate** | PB-scaled Long Rest resources with combat impact |

A custom Origin feat should be *clearly better than Musician in its
niche* and *never better than Lucky overall*.

### General — floor and ceiling

| Bound | Feat | Why it sits there |
|---|---|---|
| Floor | **Keen Mind** | +1 mental score + skill utility + Study as Bonus Action — clean, modest |
| Mid | **Resilient**, **Mage Slayer** | ASI + one solid, identity-defining benefit |
| Ceiling | **Great Weapon Master**, **Sharpshooter**, **War Caster** | ASI + 2–3 benefits forming a build cornerstone |

A custom General feat at the ceiling must pay for it the way GWM does:
conditional triggers, once-per-turn limits, PB scaling instead of flat
numbers.

### Fighting Style — floor and ceiling

| Bound | Feat | Why it sits there |
|---|---|---|
| Floor | **Protection** | Reaction cost + 5 ft range + shield requirement |
| Ceiling | **Defense** (+1 AC), **Archery** (+2 ranged to-hit) | Unconditional, always on |

The whole category lives inside one benefit block. A custom style
should be exactly one mechanic whose value sits between these bounds.

### Epic Boon — floor and ceiling

| Bound | Feat | Why it sits there |
|---|---|---|
| Floor | **Boon of Skill** | All-skill proficiency + one Expertise — wide but not spectacular |
| Ceiling | **Boon of Combat Prowess**, **Boon of Irresistible Offense** | Standing rewrites of the attack roll / resistance rules |

## Quantified Guidelines

Indicative values, cross-checked against official feats:

| Effect | Indicative cost |
|---|---|
| +1 AC, always on | ≈ a whole Fighting Style feat (Defense); too much for any Origin feat |
| +2 to hit (one weapon class) | ≈ a whole Fighting Style feat (Archery) |
| Advantage on a frequent roll type, permanent | Too much below Epic; official feats grant Advantage *narrow* (War Caster: Concentration saves only) |
| Resource, 1/Long Rest, level 1–2 spell-grade effect | ≈ ½ feat (Magic Initiate's free cast) |
| Resource, PB/Long Rest | The 2024 default for scaling resources (Lucky, Musician) — Origin ceiling when combat-relevant |
| +2 HP per level | ≈ a whole Origin feat (Tough) |
| +PB damage, once per turn, conditional | ≈ ½ General feat (Great Weapon Master's rider) |
| 3 proficiencies | ≈ a whole Origin feat (Skilled) |
| Saving throw proficiency | ≈ ½ General feat (Resilient's non-ASI half) |
| Bonus Action attack, triggered | ≈ ½ General feat (GWM's Hew — note the trigger: crit or kill) |
| Ignore a universal defense (resistance), permanent | Epic Boon territory (Irresistible Offense) |

**Two soft rules the table implies:**

1. **Flat numbers don't scale; PB does.** A +2 that is fine at level 4
   is invisible at level 17. Official 2024 design replaced almost every
   flat scaling number with PB. Do the same.
2. **"Always on" costs double.** The same effect, gated behind a
   condition or a Reaction, costs half. Compare Defense (+1 AC, always)
   vs Interception (Reaction, one attack).

## What Each Category Must Never Grant

- **Origin:** an ASI; any always-on numeric combat bonus; Extra Attack
  or multiattack riders; broad permanent Advantage; saving throw
  proficiency (that is Resilient's General-feat niche).
- **General:** +2 ASI or two +1s (that is the Ability Score Improvement
  feat's whole budget); a full class feature (Sneak Attack, Channel
  Divinity, Rage); Concentration-free duplication of a concentration
  spell; unconditioned Bonus Action attacks.
- **Fighting Style:** anything outside combat; anything resource-based
  (per-rest); packages of multiple mechanics.
- **Epic Boon:** infinite action-economy loops (extra full turns,
  unlimited Reactions); effects that invalidate a whole pillar for the
  table (auto-success on all social checks). Nearly everything else is
  legal here.

## Calibration Protocol (5 steps)

Run this for every custom feat, and show the result in the deliverable's
Design Notes:

1. **Name 2–3 official feats** of the same category occupying the
   nearest niche. "There is no comparable feat" almost always means
   the category is wrong — re-route via the decision tree in
   `feat-categories-2024.md`.
2. **Compare benefit by benefit** in a table: custom's benefit vs the
   closest official analog, marked stronger / equal / weaker.
3. **If the custom feat is stronger on every axis → nerf.** Add a
   condition, a once-per-turn limit, or downgrade a flat number to PB.
4. **If weaker on every axis → buff or narrow the niche.** A feat may
   be weak overall if it is the *best* option inside a well-defined
   niche (cf. Healer).
5. **Write the one-line verdict:** "Comparable to X, narrower than Y,
   stronger than Z only when [condition]." If you cannot write this
   sentence, the calibration is not done.
