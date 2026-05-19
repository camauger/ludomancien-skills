# Changelog

Le format suit [Keep a Changelog](https://keepachangelog.com/fr/1.1.0/) et le projet adhère au [versioning sémantique](https://semver.org/lang/fr/) par plugin.

## [0.7.0] — 2026-05-19

### Ajouts

- Plugin `ttrpg-creation` (v0.5.0) : deux nouvelles skills qui ferment l'asymétrie identifiée dans l'audit du marketplace.
  - `dungeon-creator` — création de donjons complets pour D&D 5e 2024, à l'unité, à trois échelles (5-room ~3h / small 10–15 rooms / full 16–25 rooms). Workflow en six étapes (Concept → Layout pattern → Room key → Encounter mix & faction → Pièges/trésor/secrets → Theme & GM deliverables). Cinq patterns de layout (linéaire, branching, loop, hub-and-spoke, Jaquayed avec couches verticales). Dix fonctions de salles standardisées (entrée, combat, énigme, piège, trésor, transition, social, repos, lair, rituel) avec mix ratios par échelle. Inclut cinq fichiers `references/` : `dungeon-structures.md` (patterns, 5-Room Dungeon model, layering vertical, typologie des portes/passages, conventions de carte), `room-types-and-functions-2024.md` (10 fonctions × sous-types + pitfalls + vocabulaire FR), `encounter-mix-and-pillars.md` (three-pillar framework, pacing curves, chaînes d'encounters, faction response matrix, anti-patterns), `trap-and-hazard-library.md` (4 catégories de pièges, DCs par tier, telegraphing, triade disable/bypass/suffer, catalogue de hazards, anti-patterns), `dungeon-themes-and-dressing.md` (8 thèmes archétypaux : drowned vault, necrotic crypt, fey-twisted hollow, industrial ruin, bureaucratic afterlife, living wood, infested machine, ash-and-slag forge ; sensory layering, iconography recurrence, lore seed distribution).
  - `spell-creator` — création de sorts custom pour D&D 5e 2024, à l'unité, au format PHB 2024. Couvre tous les niveaux (Cantrip → 9e), les 8 écoles, toutes les classes PHB 2024 (Bard, Cleric, Druid, Paladin, Ranger, Sorcerer, Warlock, Wizard, Artificer reprint). Workflow en six étapes (Concept → Niveau/École/Classes → Casting frame → Effet → Scaling → Assignation classe/lore/hooks). Frontière explicite avec `magic-item-creator` (effets chargés d'objets), `monster-creator` (innate spellcasting), et futures skills (class features, epic / 10e+ niveau). Inclut cinq fichiers `references/` : `spell-levels-and-tiers-2024.md` (économie de slots par niveau de personnage, benchmarks damage/condition/utility par niveau, choix du bon niveau, anti-patterns par tier), `schools-and-tradition-2024.md` (8 écoles détaillées avec conventions thématiques, mécaniques, signatures, pitfalls, anti-patterns + arbre de décision pour choisir l'école + vocabulaire FR), `casting-time-and-components-2024.md` (Action/Bonus Action/Reaction/long, syntaxe des triggers de Reaction, components V/S/M et règles de costly material, ritual rules, Concentration discipline avec anti-patterns), `spell-effect-library.md` (formes d'AoE et tailles par niveau, save vs attack rules, patterns de damage / condition / buff / debuff / summon 2024 / utility / divination / battlefield-shape), `balance-and-anti-patterns.md` (benchmarks damage par niveau, scaling math, cadence de save, discipline Concentration, catalogue d'anti-patterns : universal-anti-everything, must-have-or-die, ceiling-buster, ritual loophole, action-economy abuse, save-or-die sans staging, etc.).

### Modifications

- `ttrpg-creation` : description et tags étendus pour refléter les dimensions donjon et sort (`dungeon`, `spell` ajoutés aux tags). Le plugin couvre maintenant 11 skills (9 → 11), restant le plugin le plus dense du marketplace.
- `marketplace.json` : version bumpée à 0.7.0, description étendue aux donjons et aux sorts custom.
- `README.md` : décompte mis à jour (23 → 25 skills), deux nouvelles lignes ajoutées au tableau `ttrpg-creation`.

### Fermeture de la symétrie de création

Cette release ferme deux asymétries identifiées dans l'audit du marketplace : `settlement-toolkit-creator` couvrait les habitations sans `dungeon-creator` pour les sites de confrontation, et `magic-item-creator` couvrait le matériel sans `spell-creator` pour les options de caster. Le plugin `ttrpg-creation` couvre maintenant symétriquement personnages (PNJ / backgrounds), organisations (factions), lieux (settlements / dungeons), créatures (monstres), équipement (magic items), magie (sorts), scènes (encounters / read-aloud) et chaînes (scénarios).

## [0.6.0] — 2026-05-18

### Ajouts

- Plugin `ttrpg-creation` (v0.4.0) : nouvelle skill `encounter-builder` — construction d'encounters table-ready pour D&D 5e 2024, à l'unité, couvrant les 5 types officiels (Combat, Social, Exploration, Chase, Downtime). Workflow en cinq étapes (Setup → Calibrage → Terrain → Objectifs → Livrables table). Calibrage adaptatif par type : XP budget pour combat, attitude ladder + DCs pour social, multi-path pour exploration, lead distance + complications pour chase, time/gold + side effects pour downtime. Frontière explicite avec `scenario-writer` (chaîne narrative) et `monster-creator` (tactiques runtime). Inclut six fichiers `references/` : `encounter-types-2024.md` (5 types détaillés avec pitfalls et arbre de décision), `xp-budget-and-difficulty-2024.md` (table maître Low/Moderate/High XP × niveau, multipliers multi-monstres, daily budget, party composition adjustments), `terrain-and-objectives-library.md` (patterns terrain : cover/élévation/hazards/POI ; 8 patterns d'objectifs alternatifs au TPK ; 5 layouts archétypaux), `social-and-exploration-protocols.md` (attitude ladder, persuasion DCs, information graph, multi-path exploration, environmental hazards), `chase-and-downtime-protocols.md` (anatomie de chase, complications par terrain, exhaustion ; catalogue downtime, world reaction, side effects), `read-aloud-protocols.md` (templates par type d'encounter + résolution branches, sensory ladders, pacing, pitfalls, hand-off vers `read-aloud-crafter`).

### Modifications

- `ttrpg-creation` : description et tags étendus pour refléter la dimension encounter (`encounter`, `combat` ajoutés aux tags). Le plugin couvre maintenant 9 skills (8 → 9), devenant le plugin le plus dense du marketplace.
- `marketplace.json` : version bumpée à 0.6.0, description étendue aux encounters.

### Complétion des trous Tier 1

Cette release ferme les **4 trous Tier 1** identifiés lors de l'audit initial du marketplace : `digital-product-evaluator` (mise en marché), `monster-creator` (créatures), `magic-item-creator` (objets magiques), `encounter-builder` (encounters). Le pipeline création → audit → playtest → publication est maintenant complet.

## [0.5.0] — 2026-05-18

### Ajouts

- Plugin `ttrpg-creation` (v0.3.0) : nouvelle skill `magic-item-creator` — création d'objets magiques custom pour D&D 5e 2024, à l'unité, au format DMG. Couvre les 8 catégories standards (Armor, Weapons, Potions, Rings, Rods, Scrolls, Staves, Wands, Wondrous Items) aux 5 raretés (Common, Uncommon, Rare, Very Rare, Legendary). Workflow en six étapes (Concept → Catégorie/Frame → Mécanique → Propriétés → Lore/Origine → Variantes/Plot hooks). Calibrage par rareté. Hors-scope explicite : artefacts uniques, items sentients complets, items maudits complets (à venir comme skills dédiées). Inclut cinq fichiers `references/` : `rarity-and-attunement-guide.md` (5 raretés × power level × prix × cadence par tier de campagne ; règles d'attunement et de slots), `item-categories-2024.md` (les 8 catégories détaillées : conventions, sous-types, naming patterns, balance considerations, pitfalls, vocabulaire FR), `property-library.md` (bibliothèque de patterns récurrents : bonus statiques, triggers conditionnels, charges, daily uses, spell-like abilities, résistances, sens, mouvement, action economy, communication), `balance-and-power-budgets.md` (système informel de power budgets par rareté, tiering par niveau, synergies/anti-synergies, identity test, 6 anti-patterns à éviter), `lore-and-hook-templates.md` (11 catégories de Maker, 7 Journey Patterns, 8 Current State options, 5 Cultural Significance Tiers, 5 catégories de Plot Hooks avec exemples).

### Modifications

- `ttrpg-creation` : description et tags étendus pour refléter la dimension objets magiques (`magic-item`, `treasure` ajoutés aux tags).
- `marketplace.json` : version bumpée à 0.5.0, description étendue aux objets magiques.

## [0.4.0] — 2026-05-18

### Ajouts

- Plugin `ttrpg-creation` (v0.2.0) : nouvelle skill `monster-creator` — création de monstres complets pour D&D 5e 2024, à l'unité, au format Monster Manual. Workflow en six étapes (Concept → Stat block → Lair actions/regional effects/variants → Lore/écologie → Tactiques GM → Plot hooks). Frontière explicite avec `npc-creator` (humanoïdes nommés narratifs restent sur npc-creator ; créatures avec écologie passent ici). Calibrage par tier (CR 0–4 / 5–10 / 11–17 / 18–20 / 21+) et par rôle de combat. Inclut cinq fichiers `references/` : `cr-design-protocol-2024.md` (table maître CR×stats, offensive/defensive CR, leviers d'ajustement, calibrations par CR), `creature-types-and-tags-2024.md` (14 types officiels, tags, langues, sens, vocabulaire FR), `combat-roles.md` (8 rôles tactiques : Skirmisher, Brute, Artillery, Lurker, Soldier, Controller, Leader, Spoiler, avec stat distributions et exemples), `trait-and-action-library.md` (bibliothèque de traits, multiattack patterns, recharge abilities, réactions, legendary/lair/mythic actions), `lore-templates.md` (11 templates écologiques : apex predator, ambush hunter, swarm, scavenger, parasite, sentient collective, undead echo, fiendish bargain, fey trickster, elemental embodiment, planar exile).

### Modifications

- `ttrpg-creation` : description et tags étendus pour refléter la dimension création de monstres (`monster`, `bestiary` ajoutés aux tags).
- `marketplace.json` : version bumpée à 0.4.0, description étendue aux monstres.

## [0.3.0] — 2026-05-18

### Ajouts

- Plugin `ttrpg-editorial` (v0.3.0) : nouvelle skill `digital-product-evaluator` — évaluation commerciale d'un produit JDR sur DriveThruRPG selon quatre axes (Listing copy, Pricing strategy, Visuels, Positionnement). Deux modes (pre-launch et post-launch) avec scorecard verdict (Strong / Adequate / Needs Work / Blocking Issue) et plan d'action priorisé par ROI. Comble la référence en hand-off déclarée par `ttrpg-supplement-reviewer` et `ttrpg-playtest-orchestrator`. Inclut cinq fichiers `references/` : `drivethrurpg-anatomy.md` (taxonomies, badges, POD, NSFW gating), `pricing-benchmarks.md` (benchmarks prix × pages × type, PWYW vs fixed, calendrier promos), `listing-copy-patterns.md` (formules de titres, structures de blurbs, tag-stacking, exemples avant/après), `visual-evaluation-protocol.md` (test thumbnail, typographie cover, preview pages, gallery), `positioning-templates.md` (USP, paysage concurrentiel, personas, audience-channel fit, alignement marque).

### Modifications

- `ttrpg-editorial` : description et tags étendus pour refléter la dimension mise en marché (`drivethrurpg`, `pricing` ajoutés aux tags).
- `marketplace.json` : version bumpée à 0.3.0, description étendue à la mise en marché.

## [0.2.0] — 2026-05-17

### Ajouts

- Plugin `ttrpg-editorial` (v0.2.0) : nouvelle skill `ttrpg-playtest-orchestrator` — playtest multi-passes (audit mécanique, simulation de partie avec cinq personas, retours en voix, synthèse cross-référencée) pour D&D 5e 2024/2014, OSR, PbtA, FitD et systèmes narratifs génériques. Inclut un orchestrateur Python (`scripts/playtest_orchestrator.py`) en dry-run par défaut.

### Modifications

- `ttrpg-editorial` : description et tags étendus pour refléter la dimension playtest (`playtest` ajouté aux tags).

## [0.1.0] — 2026-05-04

### Ajouts

- Création initiale du marketplace `ludomancien-skills`.
- Plugin `ttrpg-creation` (v0.1.0) : `npc-creator`, `faction-creator`, `scenario-writer`, `settlement-toolkit-creator`, `backgrounds`, `read-aloud-crafter`.
- Plugin `ttrpg-editorial` (v0.1.0) : `ttrpg-supplement-reviewer`, `ttrpg-cliche-buster`, `name-revision`, `editorial-tic-auditor`.
- Plugin `ttrpg-tables` (v0.1.0) : `urban-d100-encounters`, `random-encounter-creator`.
- Plugin `ttrpg-print` (v0.1.0) : `ttrpg-print-design`, `midjourney-prompt-generator`, `midjourney-prompt-auditor`, `tarot-card-portrait`.
- Plugin `jdr-fr` (v0.1.0) : `mots-rares-jdr`, `fanzine-advice`.
- Script de validation `scripts/validate.py`.
