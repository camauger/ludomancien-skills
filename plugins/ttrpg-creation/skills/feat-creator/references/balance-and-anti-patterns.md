# Balance and Anti-Patterns — Feats 2024

A feat fails in exactly two directions, and a catalog of recurring
design mistakes maps the road to each. Run the final checklist before
delivering any feat.

## The Two Failure Modes

**Must-pick (too strong).** If a given build *must* take it, it is a
tax, not a choice.
*Test:* at level 4, does this feat beat +2 ASI for every character of
its target archetype, with no build that reasonably prefers the ASI?
If yes → must-pick.

**Trap option (too weak).** If no one ever takes it, it wastes page
space and player trust.
*Test:* can you describe ONE concrete build that prefers this feat to
Resilient (the universal "safe" pick)? If not → trap.

The target is the band between: *best in its niche, ignorable outside
it* (the Healer standard).

## Anti-Pattern Catalog

**1. Passive stacking**
*Bad:* "+1 to all damage rolls." Stacks with everything, always on,
invisible at the table but real on the sheet.
*Why it breaks:* flat always-on numbers multiply across a build; three
such feats and the math drifts permanently.
*Fix:* condition + once per turn + PB scaling (the GWM rider shape).

**2. Walking on a class feature**
*Bad:* a feat granting an Extra Attack, a Sneak Attack die, Channel
Divinity-like turns, or Weapon Mastery wholesale.
*Why it breaks:* it sells another class's level-5+ identity for one
feat slot; multiclass math collapses.
*Fix:* grant an *interaction with* the feature for those who have it,
never the feature itself (cf. Martial Weapon Training: proficiency,
not mastery).

**3. ASI double dip**
*Bad:* a General feat with "+2 to one score" or "+1 to two scores"
plus benefits.
*Why it breaks:* the Ability Score Improvement feat IS the +2 — a feat
granting +2 *and* benefits strictly dominates it.
*Fix:* exactly +1, from a short thematic list, max 20.

**4. The Swiss Army knife**
*Bad:* five unrelated benefits ("+1 Wis, Darkvision, Advantage vs
poison, a free spell, and a skill").
*Why it breaks:* no identity, impossible to calibrate, reads as a
wishlist. War Caster has three benefits — all serving one fantasy.
*Fix:* cut to 2–3 bricks pointing at the same archetype; move the
rest to a second feat (or a thematic set).

**5. Cosmetic prerequisite**
*Bad:* "Prerequisite: Charisma 13+" on a feat any build could abuse
identically with Charisma 8.
*Why it breaks:* prerequisites are balance levers; a fake one signals
unexamined design and gates nothing real.
*Fix:* either the prerequisite shapes who benefits (Grappler needs
Strength because the *checks* need Strength), or remove it.

**6. The numeric Origin feat**
*Bad:* an Origin feat granting +1 to hit, +1 AC, or +2 damage.
*Why it breaks:* it is free at level 1, before any opportunity cost
exists, and stacks under every later choice. No official Origin feat
grants a flat combat number (Tough's HP is the closest, and HP is the
least multiplicative stat).
*Fix:* convert to a reroll (Savage Attacker), a 1/rest resource, or
move the feat to General with an ASI.

**7. Infinite action economy**
*Bad:* "You can make one additional attack as a Bonus Action" — no
trigger, no cost.
*Why it breaks:* every martial takes it; DPR baselines shift ~30%
game-wide. Official Bonus Action attacks are triggered (GWM: crit or
kill) or paid (Two-Weapon Fighting: your off-hand and your Bonus
Action every turn).
*Fix:* attach a trigger that fires roughly once per combat, not once
per turn.

**8. The tax feat**
*Bad:* a feat that fixes a weakness *every* character has ("you no
longer suffer Disadvantage for [universal situation]").
*Why it breaks:* fixing a universal pain point makes the feat a tax on
everyone, crowding out flavorful picks. War Caster skirts this and
stays legal because Resilient (Constitution) and high Constitution are
genuine alternatives.
*Fix:* narrow the fix to an archetype, or make the benefit the *best*
way to handle the situation rather than the only way.

**9. Forgotten scaling**
*Bad:* "deal 3 extra damage" or "DC 13 save" written at level 4 math.
*Why it breaks:* fixed numbers are dead weight at Tier 3 and warping
at Tier 1 if buffed.
*Fix:* PB-based numbers, the user's save DC formula (8 + PB + mod),
or dice that ride on existing rolls.

**10. The timid boon**
*Bad:* an Epic Boon that reads like a General feat ("+1 Str and
Advantage on Athletics checks").
*Why it breaks:* level 19+ characters fight liches and tarrasques; a
boon that doesn't bend a rule is a dead level. The category's floor
is "proficiency in ALL skills" (Boon of Skill).
*Fix:* take the concept's General-feat version and turn the permanence
knob (see the scaling ladder in feat-effect-library.md).

## Stacking Audit (protocol)

1. List the 3–5 official feats sharing the custom feat's niche
   (same weapon class, same defensive slot, same spell-support slot).
2. For each, check the **pairwise combo** custom + official on an
   optimized build: do bonuses of the same type add? Does one reset
   or refund the other's resource?
3. Red flags: two always-on bonuses to the same roll; a resource loop
   (A refunds B, B triggers A); a custom trigger that fires off an
   official feat's free attack.
4. If a red flag fires, the fix is usually a "once per turn" line or
   typing the bonus so it doesn't stack with itself.

## Repeatable Rules

**Healthy Repeatable** — each instance forces a *different choice*:
Magic Initiate (a different spell list each time), Skilled (different
proficiencies). The feat's power is a menu; repeating widens the menu.

**Unhealthy Repeatable** — each instance stacks the *same number*:
"+1 AC, Repeatable" is +3 AC by level 12. Never mark a numeric benefit
Repeatable.

Default: omit Repeatable unless the menu structure makes it obviously
safe — and say which choice must differ, exactly as Magic Initiate does.

## Final Checklist (before delivering any feat)

- [ ] Header matches the category template exactly (see feat-categories-2024.md)
- [ ] General/Epic: ASI present, +1 only, correct cap (20 / 30); Origin/Fighting Style: no ASI
- [ ] 2–3 benefits max, exactly one signature, all serving one identity
- [ ] No flat always-on combat numbers outside Fighting Style
- [ ] Every resource uses a 2024 pattern (once/turn, 1/LR, PB/LR, recharge)
- [ ] Calibration table cites 2–3 named official feats + one-line verdict
- [ ] Stacking audit run against the niche's official feats
- [ ] Prerequisite (if any) gates something real
- [ ] Repeatable (if present) is menu-shaped, never numeric
- [ ] Text uses 2024 vocabulary only (capitalized Advantage/Disadvantage, Heroic Inspiration, PB phrasing)
