# ttrpg-creation

Création de contenu JDR : PNJ, factions, scénarios, settlements, monstres, objets magiques, encounters, donjons, sorts et dons custom, plus un agent de design itératif pour concevoir un scénario avant de l'écrire. D&D 5e (2024) par défaut, la plupart des skills sont system-agnostic.

## Skills

| Skill | Rôle |
|---|---|
| `npc-creator` | PNJ complets (apparence, désirs, secrets, stat blocks tiered, plot hooks) |
| `faction-creator` | Organisations avec structure, ressources, NPCs clés, dynamiques inter-factions |
| `scenario-writer` | Scénarios publication-ready style Casus Belli (4-6h, three-clue rule, scènes standardisées) |
| `settlement-toolkit-creator` | Toolkits de villages/villes (10-20 pages, lieux, PNJ, accroches, lore) |
| `backgrounds` | Backgrounds D&D 5e 2024 au format PHB officiel |
| `read-aloud-crafter` | Transformation de texte de jeu en narration immersive pour la table |
| `monster-creator` | Monstres complets D&D 5e 2024 (stat block + lair actions + écologie + tactiques GM + plot hooks), format Monster Manual |
| `magic-item-creator` | Objets magiques custom D&D 5e 2024 — 8 catégories, 5 raretés, format DMG complet |
| `encounter-builder` | Encounters table-ready D&D 5e 2024 — 5 types (combat, social, exploration, chase, downtime), calibrage par party, terrain + objectifs alternatifs + livrables table |
| `dungeon-creator` | Donjons complets — 3 échelles (5-room / small 10-15 / full 16-25), 5 patterns de layout, ASCII map + room key + GM flow notes |
| `spell-creator` | Sorts custom D&D 5e 2024 — tous niveaux (Cantrip → 9e), 8 écoles, toutes classes PHB 2024, format PHB officiel |
| `feat-creator` | Dons custom D&D 5e 2024 — 4 catégories (Origin / General / Fighting Style / Epic Boon), format PHB officiel, calibrage contre feats nommés, mode set thématique 2–4 feats |

## Agents

| Agent | Rôle |
|---|---|
| `scenario-architect` | Dialogue itératif pour concevoir un scénario *avant* de l'écrire. Sept stages (seed, tone & genre, antagonist & stakes, pillar mix & set pieces, structure pattern, key NPCs & locations, encounter shortlist), 2-4 questions par stage, détection de tensions cross-stage. Produit un *Scenario Design Brief* Markdown prêt à passer à `scenario-writer`. À utiliser quand tu pars d'une idée vague ; à ne pas utiliser si tu as déjà un design complet (invoque `scenario-writer` directement) |
| `bestiary-builder` | Orchestrateur de bestiaire cohérent (5-30 créatures). Designe un framework écologique (origine partagée, prédateurs-proies, niches non-redondantes, traits récurrents), planifie le roster, orchestre `monster-creator` par entrée avec le framework en contexte, audite cross-créature par batch (niche duplication, framework drift, CR distribution, encounter mix), optionnellement valide via `stat-block-validator`, assemble un bestiaire publication-ready (intro + créatures + diagramme prédateurs-proies + encounter tables). À utiliser pour un *set* de créatures ; pour un seul monstre, invoque `monster-creator` directement |

## Quand utiliser quoi

- **Idée vague de scénario** → `scenario-architect` (dialogue, brief) → `scenario-writer` (prose)
- **Design de scénario déjà clair** → `scenario-writer` directement
- **Un seul monstre** → `monster-creator` directement
- **Set cohérent de 5-30 créatures** → `bestiary-builder` (orchestrateur)
- **Création d'éléments isolés** (PNJ, sort, donjon, objet magique) → skill atomique correspondant

## Installation

```
/plugin install ttrpg-creation@ludomancien-skills
```

Une fois installés, les skills se déclenchent automatiquement quand tu décris une tâche qui correspond, ou tu peux les invoquer explicitement avec `/nom-du-skill`.

## Voir aussi

- [`ttrpg-editorial`](../ttrpg-editorial/) — audit, playtest, conversion, mise en marché
- [`README.md`](../../README.md) — vue d'ensemble du marketplace
- [`CONTRIBUTING.md`](../../CONTRIBUTING.md) — conventions et workflow d'ajout
