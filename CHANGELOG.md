# Changelog

Le format suit [Keep a Changelog](https://keepachangelog.com/fr/1.1.0/) et le projet adhère au [versioning sémantique](https://semver.org/lang/fr/) par plugin.

## [1.2.0] — 2026-05-19

### Ajouts

- Plugin `ttrpg-creation` (v1.2.0) : **troisième agent du marketplace** et premier orchestrateur de génération de set.
  - `bestiary-builder` — agent qui produit un bestiaire cohérent de 5-30 créatures (pas un monstre à la fois ; un *set* avec ecology partagée, prédateurs-proies, niches non-redondantes, traits récurrents). Pattern : orchestrateur de génération (contrairement à `scenario-architect` qui est un design partner dialogué, et `ttrpg-publication-director` qui est un orchestrateur d'audit). Huit stages séquentiels : (1) Triage & brief (theme / count / CR range / system / intent, plus anchor creatures et exclusions optionnels), (2) Coherence Framework (shared origin / predator-prey structure / niche assignments / recurring trait keywords / tone keywords / anti-theme — ce qui n'appartient pas), (3) Roster Planning (table pré-génération validée par l'utilisateur avant token-expensive generation), (4) Generation Loop (invocation `monster-creator` par entrée avec framework + roster slot + voisins déjà générés en contexte, génération en batchs de 3-5 avec audit entre batchs), (5) Cross-Creature Audit (niche duplication, framework drift, CR distribution, trait conflict, anti-theme violation, encounter mix feasibility, voice consistency), (6) Mechanical Validation optionnelle (`stat-block-validator` par créature, halt-on-catastrophic si >2 errors critiques), (7) Polish & Resolution (renommage, voice fix, trait keyword recovery, niche fix, mechanical fix), (8) Final Assembly (intro + diagramme prédateurs-proies ASCII/Mermaid + creature entries + encounter tables tiered + appendix). Discipline tokens : estimation prealable, batchs avec checkpoints, warning utilisateur avant grand set. Halt conditions documentées : CR range trop large (1/8 → 25 dans un même bestiaire), theme self-contradictory, count irréaliste (>30 = split en volumes), erreurs critiques en cascade (>2 = framework problem). Anti-patterns documentés : the 20-creature dump, the CR clustering, the niche collision, the framework dilution, the encounter unfeasibility, the kitchen sink, the framework smuggle (générer sans passer le framework à `monster-creator`), the single-pass audit, the publication-director mimic. Model : `opus` (orchestration multi-skill + raisonnement cross-créature). Tools : Read, Write, Edit, Glob, Grep, Bash, Skill, TaskCreate, TaskUpdate, TaskList, TaskGet. Fichier : `plugins/ttrpg-creation/agents/bestiary-builder.md`.

### Modifications

- `ttrpg-creation` : description et tags étendus (`orchestration` ajouté). Le plugin couvre maintenant 11 skills + 2 agents.
- `marketplace.json` : version bumpée à 1.2.0, description étendue au troisième agent. Le marketplace compte maintenant 27 skills + 3 agents.
- `README.md` : décompte mis à jour (27 skills + 3 agents), `bestiary-builder` ajouté au tableau *Agents* du plugin `ttrpg-creation`, structure du repo enrichie pour montrer les deux fichiers d'agent.
- `plugins/ttrpg-creation/README.md` : nouvelle entrée *Agents* + section *Quand utiliser quoi* enrichie pour distinguer `monster-creator` (un monstre) de `bestiary-builder` (set cohérent).

### Pourquoi un orchestrateur (pas juste un loop de monster-creator)

Générer 20 monstres avec 20 appels indépendants de `monster-creator` produit 20 stat blocks valides mais qui ne forment pas un *bestiaire* — pas d'écologie partagée, niches qui se dupliquent, traits récurrents absents, encounter table impossible à construire. `bestiary-builder` orchestre la même skill mais *en passant un framework partagé et les voisins déjà générés* à chaque appel, puis audite cross-créature pour rattraper les drifts. La valeur n'est pas dans la génération individuelle ; elle est dans le framework + l'audit + l'assembly. C'est aussi pour ça que l'agent fait du chunking explicite (batchs de 3-5 avec audit entre) — la cohérence se perd quand on génère 20 stat blocks d'affilée sans check.

### Trois agents, trois patterns distincts

Le marketplace contient maintenant trois agents avec trois patterns distincts :
- `ttrpg-publication-director` (ttrpg-editorial) — **orchestrateur d'audit**. Prend un manuscrit existant, le passe à travers les skills d'audit, synthétise un verdict.
- `scenario-architect` (ttrpg-creation) — **design partner dialogué**. Pas d'orchestration ; pure conversation sur 7 stages pour produire un brief.
- `bestiary-builder` (ttrpg-creation) — **orchestrateur de génération**. Génère un set cohérent en appelant `monster-creator` avec framework partagé, audit cross-batch.

Cette diversité de patterns est intentionnelle : les agents ne sont pas tous le même type de chose. Futurs agents pressentis : `campaign-prep-agent` (préparation hebdomadaire de session avec mémoire cross-sessions — pattern *mémoire persistante*, encore non explorée).

## [1.1.0] — 2026-05-19

### Ajouts

- Plugin `ttrpg-creation` (v1.1.0) : **deuxième agent du marketplace** et premier agent dans `ttrpg-creation`.
  - `scenario-architect` — agent de design itératif pour concevoir un scénario *avant* de l'écrire. Pas un orchestrateur de skills (contrairement à `ttrpg-publication-director`) : un design partner en dialogue. Sept stages séquentiels : (1) Seed (système / party / longueur / prémisse en une phrase), (2) Tone & Genre (registre fantasy, registre tonal, références optionnelles), (3) Antagonist & Stakes (qui pousse, conséquence d'échec, tick rate du clock), (4) Pillar Mix & Set Pieces (% combat/social/exploration, 1-3 scènes obligatoires), (5) Structure Pattern (node-based / mystery / dungeon / time-pressure / heist / siege / chase / hybrid avec strengths et risks documentés), (6) Key NPCs & Locations (3-5 de chaque, notes de stat block en une ligne — pas de stat blocks complets), (7) Encounter Shortlist & Synthesis (2-4 encounters load-bearing avec chemins alternatifs). Discipline de dialogue : 2-4 questions max par stage, recap d'état entre stages, détection de tensions cross-stage (genre vs antagonist, length vs scope, party level vs encounter difficulty, pillar mix vs structure pattern, set piece vs pattern). Halt conditions documentées (mismatch fondamental, prémisse structurellement impossible, design déjà complet, scope explosion). Anti-patterns documentés (wall of questions, silent drift, writing the scenario, premature lock-in, brainstorm explosion, completeness fetish, scenario-writer mimic). Output : un *Scenario Design Brief* Markdown structuré (technical card, premise, antagonist & faction pressure, stakes & clock, structure pattern, key NPCs, key locations, encounter shortlist, design tradeoffs locked in, open questions for scenario-writer) prêt à passer directement à `scenario-writer`. Model : `opus` (synthèse de design itératif). Tools : Read, Write, Edit, Glob, Grep, Skill, TaskCreate, TaskUpdate, TaskList, TaskGet (pas de Bash — l'agent ne lance rien). Boundary stricte : l'agent *designe*, `scenario-writer` *écrit*. Fichier : `plugins/ttrpg-creation/agents/scenario-architect.md`.

### Modifications

- `ttrpg-creation` : description et tags étendus pour refléter l'ajout du premier agent du plugin (`agent`, `design` ajoutés aux tags). Le plugin couvre maintenant 11 skills + 1 agent. Le README du plugin gagne une section *Agents* et une section *Quand utiliser quoi* pour clarifier le workflow `scenario-architect` → `scenario-writer`.
- `marketplace.json` : version bumpée à 1.1.0, description étendue au deuxième agent. Le marketplace compte maintenant 27 skills + 2 agents.
- `README.md` : décompte mis à jour (27 skills + 2 agents), nouvelle section *Agents* dans le tableau `ttrpg-creation`, structure du repo enrichie pour montrer `agents/` aussi dans `ttrpg-creation`.

### Pourquoi un agent de design (pas juste un skill enrichi)

`scenario-writer` produit une aventure complète en one-shot quand on lui donne un brief clair. Beaucoup de cas réels partent d'une idée vague (« heist dans une cité d'horlogerie », « one-shot Halloween avec un démon de paralysie du sommeil ») où le design n'est pas encore lock. `scenario-architect` couvre cet upstream : il extrait les paramètres critiques par dialogue, surface les tradeoffs aux moments de décision, détecte les incohérences cross-stage (le piège classique « cozy fantasy + meurtre d'enfant » qui passe inaperçu en one-shot), et produit un brief qui rend `scenario-writer` plus efficace en aval. C'est un design partner, pas un orchestrateur — il n'invoque pas d'autres skills, sa valeur est dans la qualité du dialogue et de la synthèse.

## [1.0.0] — 2026-05-19

Première release stable. Le marketplace couvre 27 skills et 1 agent orchestrateur répartis sur 5 plugins, avec une documentation complète (top-level README, per-plugin READMEs, CONTRIBUTING.md, galerie d'exemples curatée).

### Ajouts

- **`examples/`** — galerie curatée d'outputs réels jugés exemplaires. Pas de fixtures synthétiques ni de démos pré-écrites : le mainteneur dépose un output quand il le juge bon, frontmatter minimal (skill, plugin, date, why), output collé brut. Voir `examples/README.md` pour le mécanisme de curation et `examples/TEMPLATE.md` pour ajouter un nouvel exemple. La galerie sert à la fois de vitrine concrète pour un nouveau visiteur et de référence calibrée pour détecter une dérive future d'un skill.
- **`CONTRIBUTING.md`** — conventions complètes : philosophie skills vs agents, structure du repo, workflow d'ajout d'un skill (frontmatter, references/, validation), workflow d'ajout d'un agent (frontmatter avec tools/model, single-file), style et langue (français primaire, accents stricts, pas d'emojis), validation locale, versioning sémantique par plugin, style de commit, scope du marketplace.
- **5 READMEs par plugin** : `plugins/ttrpg-creation/README.md`, `plugins/ttrpg-editorial/README.md`, `plugins/ttrpg-tables/README.md`, `plugins/ttrpg-print/README.md`, `plugins/jdr-fr/README.md`. Chacun liste ses skills (et son agent pour `ttrpg-editorial`), explique le workflow type quand pertinent, et pointe vers le top-level README et CONTRIBUTING.md.

### Modifications

- **`README.md`** : structure du repo enrichie pour montrer `examples/`, `CONTRIBUTING.md`, et les READMEs par plugin. Nouvelle section *Exemples* pointant vers `examples/README.md`. Note explicite sur les READMEs et CONTRIBUTING.md.
- **Bumps de version vers v1.0.0** :
  - `marketplace.json` : 0.9.0 → 1.0.0
  - `plugins/ttrpg-creation/plugin.json` : 0.5.0 → 1.0.0
  - `plugins/ttrpg-editorial/plugin.json` : 0.5.0 → 1.0.0
  - `plugins/ttrpg-tables/plugin.json` : 0.1.0 → 1.0.0
  - `plugins/ttrpg-print/plugin.json` : 0.1.0 → 1.0.0
  - `plugins/jdr-fr/plugin.json` : 0.1.0 → 1.0.0

### Note sur la curation d'exemples (pivot pendant la release)

La version initialement prévue incluait un walkthrough synthétique de `ttrpg-publication-director` sur un manuscrit pré-écrit délibérément défectueux. Après réflexion, le format synthétique a été abandonné au profit d'une galerie curatée : un walkthrough synthétique vieillit mal (les skills évoluent, l'exemple dérive) alors qu'une galerie d'outputs réels jugés exemplaires reste utile dans le temps et reflète plus fidèlement ce que le marketplace produit. Le fixture initial (`examples/sample-5-room-dungeon.md`) a été supprimé.

### Contrat de stabilité v1.0.0

À partir de cette release :

- **MAJOR** sera bumpé pour : renommage de skill, suppression, changement de signature majeur du SKILL.md ou d'un agent.
- **MINOR** : ajout d'un skill ou agent, enrichissement substantiel (nouveau workflow, références ajoutées).
- **PATCH** : corrections, clarifications de doc, ajustements de trigger phrases.

Les `references/` internes des skills restent en libre évolution (ils ne font pas partie du contrat public).

## [0.9.0] — 2026-05-19

### Ajouts

- Plugin `ttrpg-editorial` (v0.5.0) : **premier agent orchestrateur** du marketplace.
  - `ttrpg-publication-director` — agent (pas skill) qui pilote un produit JDR à travers le pipeline de publication complet draft → launch en sept stages : (1) Originality Audit (`ttrpg-cliche-buster`), (2) Mechanical Validation (`stat-block-validator` + flags pour sorts/items), (3) Style Audit (`editorial-tic-auditor` + `name-revision`), (4) Table Playtest (`ttrpg-playtest-orchestrator`), (5) Holistic Editorial Review (`ttrpg-supplement-reviewer`), (6) System Conversion optionnelle (`adventure-converter`), (7) Market Readiness (`digital-product-evaluator`). Triage upfront pour décider quels stages courir selon le type de produit (scénario / bestiaire / settlement / etc.), le système cible, et l'intent commercial. Synthèse cross-stage avec identification des concerns récurrents (cliché + tic + naming overlap, mechanical + playtest overlap, etc.). Output : rapport unifié avec verdict de launch (Launch-Ready / Launch-Ready with Caveats / Conditional / Major Revision Required), launch blockers, polish prioritisé, et estimation du chemin de launch. Discipline opérationnelle : halt-on-catastrophic, parallélisation des stages indépendants (2+3), skip rules par type de produit, anti-patterns documentés (verdict inflation, findings dump, mission creep). Model : `opus` (synthèse complexe). Tools : Read, Write, Edit, Glob, Grep, Bash, Skill, TaskCreate, TaskUpdate, TaskList, TaskGet. Fichier : `plugins/ttrpg-editorial/agents/ttrpg-publication-director.md`.

### Modifications

- `ttrpg-editorial` : description et tags étendus pour refléter l'arrivée du premier agent (`agent`, `orchestration` ajoutés aux tags). Le plugin couvre maintenant 8 skills + 1 agent.
- `marketplace.json` : version bumpée à 0.9.0, description étendue au premier agent orchestrateur.
- `README.md` : décompte mis à jour (27 skills + 1 agent), nouvelle section « Agents » dans le tableau `ttrpg-editorial`, structure du repo enrichie pour montrer `agents/`, section Validation locale enrichie.
- `scripts/validate.py` : étendu pour valider aussi les fichiers `<plugin>/agents/*.md` (frontmatter YAML, name match avec nom de fichier, longueur de description, limite 1536 chars). Le script reste sans dépendances PyYAML (parseur minimaliste maison).

### Première extension de la taxonomie : skills + agents

Cette release introduit la distinction skills / agents dans le marketplace. Les **skills** sont atomiques, déclenchées par phrase-clé, exécutent une tâche précise. Les **agents** sont orchestrateurs, gèrent leur propre contexte sur plusieurs étapes, invoquent des skills à la volée. Le marketplace peut maintenant héberger les deux. Futurs agents prévus : `bestiary-builder` (multi-monstres avec cohérence cross-créature), `scenario-architect` (dialogue itératif pour designer un scénario), `campaign-prep-agent` (préparation hebdomadaire de session avec mémoire cross-sessions).

## [0.8.0] — 2026-05-19

### Ajouts

- Plugin `ttrpg-editorial` (v0.4.0) : deux nouvelles skills Tier-1 qui complètent le pipeline éditorial avec la conversion entre systèmes et l'audit mécanique pur.
  - `adventure-converter` — conversion d'aventures, scénarios et suppléments entre systèmes JDR fantasy. Quatre chemins supportés : (1) D&D 5e 2014 → 5e 2024 (mise à jour d'édition), (2) D&D 5e → Pathfinder 2e (Remastered), (3) D&D 5e → OSR (B/X, OSE, Shadowdark, old-school générique), (4) D&D 5e → narratif (notes d'adaptation PbtA/FitD). Workflow en six phases (Audit source → Matrice de conversion → Conversion mécanique → Conversion structurelle → Polish narratif → Assemblage livrable). Modes : full conversion / mechanical only / adaptation notes. Inclut cinq fichiers `references/` : `5e-2014-to-2024-deltas.md` (changements complets entre éditions : weapon mastery, nouvelles règles Hide/Search, exhaustion simplifié, refonte des classes, sorts renommés/refondus, format de stat block, vocabulaire « race » → « species »), `5e-to-pf2e-mapping.md` (architecture comparée : trois actions par tour, MAP cascade -0/-5/-10, DCs niveau-scaled, traits PF2e, succès/échec critique 10-point swing, conditions graduées, ancestry+heritage, encounter budgets Trivial→Extreme, heightening vs upcast), `5e-to-osr-translation.md` (sous-systèmes OSR détaillés : B/X / OSE / Shadowdark / Dolmenwood, HP scaling, AC ascendante vs descendante, catégories de sauvegarde classiques vs ability saves modernes, encounter philosophy avec réaction rolls et morale, treasure-as-XP, procédure de donjon avec tours et torches), `mechanical-conversion-tables.md` (tables transversales : XP par CR/niveau, treasure value, AC mapping, save DC mapping, damage scaling, monster HP scaling, spell level alignment, encounter difficulty mapping), `tone-and-structure-conversion.md` (philosophies de design par système, attentes par communauté, sidebars de conversion, règles de préservation du read-aloud, what-to-cut / what-to-add, anti-patterns de ton, template de conversion notes).
  - `stat-block-validator` — audit mécanique pur de stat blocks D&D 5e 2024. Cinq checks séquentiels : (1) conformité format MM 2024 (ordre des champs, vocabulaire, Habitat/Treasure 2024), (2) validation arithmétique (modificateur depuis score, save depuis mod+PB, attack depuis mod+PB, AC depuis armure+Dex, HP depuis HD+Con), (3) audit math CR offensive (DPR × 3 rounds) + défensive (HP × multiplier + AC), (4) audit action economy (multiattack par tier, recharge ranges, budget legendary actions, lair/regional/mythic), (5) audit vocabulaire 2024 (conditions capitalisées, action types capitalisés, recharge syntax, damage type capitalisé). Sortie : rapport de défauts structuré avec sévérité (Critical/High/Medium/Low) et stat block corrigé. Boundary explicite avec `monster-creator` (création) et `ttrpg-supplement-reviewer` (éditorial qualitatif). Inclut cinq fichiers `references/` : `stat-block-format-2024.md` (layout canonique MM 2024 avec ordre des champs, syntaxe par section, vocabulaire FR Manuel des Monstres), `cr-math-2024.md` (tables CR offensive et défensive, PB par CR, ajustements AC/attack/save, exemples chiffrés), `action-economy-audit.md` (budgets par tier, patterns standards multiattack/recharge/réaction/bonus action/legendary/lair/regional/mythic, anti-patterns), `trait-vocabulary-2024.md` (conditions officielles 2024, syntaxe save/damage/attack/targeting, vocabulaire FR complet pour conditions + damage types), `common-stat-block-errors.md` (catalogue de 24 erreurs récurrentes : arithmétique A1-A7, CR math C1-C4, action economy E1-E6, vocabulaire V1-V8, format F1-F5, avec priorité d'audit).

### Modifications

- `ttrpg-editorial` : description et tags étendus pour refléter les dimensions conversion et validation mécanique (`conversion`, `stat-block`, `validation` ajoutés aux tags). Le plugin couvre maintenant 8 skills (6 → 8).
- `marketplace.json` : version bumpée à 0.8.0, description étendue à la conversion entre systèmes et à l'audit mécanique de stat blocks.
- `README.md` : décompte mis à jour (25 → 27 skills), deux nouvelles lignes ajoutées au tableau `ttrpg-editorial`.

### Complétion du Tier-1 éditorial

Cette release ferme deux gaps Tier-1 identifiés dans l'audit du marketplace : la conversion entre systèmes (très forte valeur commerciale — la communauté JDR navigue constamment entre 5e 2014, 5e 2024, PF2e, et OSR) et la validation mécanique pure (complément indispensable à `monster-creator` pour le QA pre-publication). Le pipeline éditorial est maintenant : `ttrpg-cliche-buster` (originalité) → `monster-creator` / `magic-item-creator` / `spell-creator` (création) → `stat-block-validator` (QA mécanique) → `editorial-tic-auditor` + `name-revision` (style) → `ttrpg-playtest-orchestrator` (table) → `ttrpg-supplement-reviewer` (éditorial holistique) → `adventure-converter` (multi-système) → `digital-product-evaluator` (mise en marché).

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
