# Ludomancien Skills

Boîte à outils Claude Code pour la création de contenu de jeu de rôle sur table.

Cinq plugins, vingt-sept skills et un premier agent orchestrateur — couvrant la création (PNJ, factions, scénarios, settlements, monstres, objets magiques, encounters, donjons, sorts custom), l'audit éditorial (revue, playtest, mise en marché, conversion entre systèmes, validation de stat blocks), l'orchestration de pipeline (`ttrpg-publication-director` pilote draft → launch), les tables aléatoires, la préparation print, et le contenu francophone.

D&D 5e (2024) par défaut quand des règles sont impliquées, mais la majorité des skills est *system-agnostic* et adaptable à PF2e, OSR ou des systèmes narratifs.

## Installation

Dans Claude Code :

```
/plugin marketplace add camauger/ludomancien-skills
```

Puis installe les plugins qui t'intéressent :

```
/plugin install ttrpg-creation@ludomancien-skills
/plugin install ttrpg-editorial@ludomancien-skills
/plugin install ttrpg-tables@ludomancien-skills
/plugin install ttrpg-print@ludomancien-skills
/plugin install jdr-fr@ludomancien-skills
```

Une fois installés, les skills se déclenchent automatiquement quand tu décris une tâche qui correspond, ou tu peux les invoquer explicitement avec `/nom-du-skill`.

## Plugins

### `ttrpg-creation` — Création de contenu

| Skill | Rôle |
|---|---|
| `npc-creator` | PNJ complets (apparence, désirs, secrets, stat blocks tiered, plot hooks) |
| `faction-creator` | Organisations avec structure, ressources, NPCs clés, dynamiques inter-factions |
| `scenario-writer` | Scénarios publication-ready style Casus Belli (4-6h, three-clue rule, scènes standardisées) |
| `settlement-toolkit-creator` | Toolkits de villages/villes (10-20 pages, lieux, PNJ, accroches, lore) |
| `backgrounds` | Backgrounds D&D 5e 2024 au format PHB officiel |
| `read-aloud-crafter` | Transformation de texte de jeu en narration immersive pour la table |
| `monster-creator` | Monstres complets D&D 5e 2024 (stat block + lair actions + écologie + tactiques GM + plot hooks) — à l'unité, format Monster Manual |
| `magic-item-creator` | Objets magiques custom D&D 5e 2024 — 8 catégories standards (Armor/Weapons/Potions/Rings/Rods/Scrolls/Staves/Wands/Wondrous), 5 raretés (Common→Legendary), format DMG complet (stat + lore + variants + plot hooks) |
| `encounter-builder` | Encounters table-ready D&D 5e 2024 — 5 types (combat, social, exploration, chase, downtime), calibrage par party (XP budget, DCs, lead distance), terrain + objectifs alternatifs + livrables table (read-aloud + GM cheat sheet) |
| `dungeon-creator` | Donjons complets D&D 5e 2024 — 3 échelles (5-room / small 10-15 / full 16-25), 5 patterns de layout (linéaire / branching / loop / hub-and-spoke / Jaquayed), 10 fonctions de salles, occupation factionnelle dynamique, pièges + hazards + theme through-line, ASCII map + room key + GM flow notes |
| `spell-creator` | Sorts custom D&D 5e 2024 — tous niveaux (Cantrip → 9e), 8 écoles, toutes classes PHB 2024, format PHB officiel (niveau / école / temps d'incantation / portée / composantes / durée / classes + description + scaling + lore + plot hooks). Discipline Concentration, save vs attack roll, scaling cantrip et upcast |

### `ttrpg-editorial` — Audit éditorial, playtest et mise en marché

| Skill | Rôle |
|---|---|
| `ttrpg-supplement-reviewer` | Revue éditoriale 6 axes (writing, mechanics, table utility, structure, brand, verdict) |
| `ttrpg-cliche-buster` | Détection des clichés et alternatives créatives (FR/EN) |
| `name-revision` | Remplacement des noms fantasy génériques générés par IA |
| `editorial-tic-auditor` | Audit des tics récurrents dans la fiction long-form |
| `ttrpg-playtest-orchestrator` | Playtest multi-passes (audit mécanique, simulation 4-5 personas, retours en voix, synthèse) — 5e 2024, OSR, PbtA, FitD |
| `digital-product-evaluator` | Évaluation commerciale DriveThruRPG 4 axes (listing, pricing, visuels, positionnement) — modes pre-launch et post-launch |
| `adventure-converter` | Conversion d'aventures et suppléments JDR entre systèmes : 5e 2014 → 5e 2024, 5e → PF2e, 5e → OSR (B/X, OSE, Shadowdark), 5e → narratif (PbtA/FitD notes). Audit source + matrice de conversion + livrable converti + notes GM |
| `stat-block-validator` | Audit mécanique de stat blocks D&D 5e 2024 (format MM 2024, arithmétique, math CR offensive/défensive, action economy, vocabulaire 2024). Rapport de défauts avec sévérité et correctifs proposés. Pure validation, non-éditorial |

**Agents :**

| Agent | Rôle |
|---|---|
| `ttrpg-publication-director` | Orchestrateur full-pipeline draft → launch en 7 stages (Cliché → Mécanique → Style → Playtest → Éditorial → Conversion → Marché). Triage les skills à invoquer selon le type de produit et l'intent commercial, synthétise les findings cross-stage, produit un rapport unifié avec verdict de launch (Launch-Ready / Launch-Ready with Caveats / Conditional / Major Revision Required) et plan d'action priorisé |

### `ttrpg-tables` — Tables aléatoires

| Skill | Rôle |
|---|---|
| `urban-d100-encounters` | Tables d100 par thème (combat, social, horreur, mystère, occulte, etc.) |
| `random-encounter-creator` | Tables d100-d1000 tiered avec script Python d'orchestration |

### `ttrpg-print` — Production print

| Skill | Rôle |
|---|---|
| `ttrpg-print-design` | Layout, typographie, specs print pour DriveThruRPG |
| `midjourney-prompt-generator` | Génération de prompts Midjourney pour illustrations JDR |
| `midjourney-prompt-auditor` | Audit qualité de prompts avant dépense de crédits (7 vérifications structurelles) |
| `tarot-card-portrait` | Prompts pour portraits de personnages style carte de tarot |

### `jdr-fr` — Contenu francophone

| Skill | Rôle |
|---|---|
| `mots-rares-jdr` | Articles de mots rares français pour jeuxderole.org/mots-rares |
| `fanzine-advice` | Articles de conseil GM style fanzine (1000-2000 mots) |

## Structure du repo

```
ludomancien-skills/
├── .claude-plugin/
│   └── marketplace.json          # catalogue principal
├── plugins/
│   ├── ttrpg-creation/
│   │   ├── .claude-plugin/plugin.json
│   │   ├── README.md
│   │   └── skills/
│   │       ├── npc-creator/
│   │       │   ├── SKILL.md
│   │       │   └── references/
│   │       └── ...
│   ├── ttrpg-editorial/
│   │   ├── .claude-plugin/plugin.json
│   │   ├── README.md
│   │   ├── skills/               # skills atomiques
│   │   └── agents/               # agents orchestrateurs
│   │       └── ttrpg-publication-director.md
│   ├── ttrpg-tables/
│   ├── ttrpg-print/
│   └── jdr-fr/
├── scripts/
│   └── validate.py               # valide manifestes, SKILL.md, agents/
├── examples/                     # galerie curatée d'outputs
│   ├── README.md
│   └── TEMPLATE.md
├── CHANGELOG.md
├── CONTRIBUTING.md
└── README.md
```

Chaque plugin a son propre `README.md` qui détaille ses skills et leur workflow type. `CONTRIBUTING.md` couvre les conventions de SKILL.md, d'agents, de versioning et de validation.

## Validation locale

Avant de publier ou de pousser un changement :

```bash
python scripts/validate.py
```

Le script vérifie que :

- `marketplace.json` parse et a les champs requis
- chaque `plugin.json` parse et a les champs requis
- chaque `SKILL.md` a un frontmatter YAML valide avec `name` et `description`
- chaque fichier d'agent (`<plugin>/agents/<nom>.md`) a un frontmatter YAML valide avec `name` et `description`, et le `name` correspond au nom de fichier
- chaque skill listé dans un plugin existe physiquement sur le disque

## Versioning

Le marketplace suit un versioning par plugin (chacun a son propre `version` dans `plugin.json`). Quand un plugin change de manière non-rétrocompatible, bump le `MAJOR`. Quand un skill est ajouté ou enrichi, bump le `MINOR`. Pour des corrections, bump le `PATCH`.

## Exemples

Le dossier `examples/` contient une galerie curatée d'outputs réels produits par les skills et agents, sélectionnés parce qu'ils représentent bien ce que ces outils peuvent produire. Voir `examples/README.md` pour le mécanisme de curation et `examples/TEMPLATE.md` pour ajouter un nouvel exemple.

## Hors-scope

Ce marketplace ne contient **pas** :

- Les skills de contenu adulte ou explicite (voir `camauger/fantasy-vixens-skills`)
- Les outils de développement web ou d'audit frontend (voir `camauger/dev-skills`)

## Licence

MIT — voir `LICENSE`.
