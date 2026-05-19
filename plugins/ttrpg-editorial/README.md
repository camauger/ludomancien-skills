# ttrpg-editorial

Audit éditorial, playtest, mise en marché et orchestration de pipeline pour suppléments JDR. Couvre la revue de publication, la chasse aux clichés, les tics récurrents, les noms génériques, la simulation de playtest, l'évaluation commerciale DriveThruRPG, la conversion entre systèmes et l'audit mécanique de stat blocks. Inclut le premier agent orchestrateur du marketplace.

## Skills

| Skill | Rôle |
|---|---|
| `ttrpg-supplement-reviewer` | Revue éditoriale 6 axes (writing, mechanics, table utility, structure, brand, verdict) |
| `ttrpg-cliche-buster` | Détection des clichés et alternatives créatives (FR/EN) |
| `name-revision` | Remplacement des noms fantasy génériques générés par IA |
| `editorial-tic-auditor` | Audit des tics récurrents dans la fiction long-form |
| `ttrpg-playtest-orchestrator` | Playtest multi-passes (audit mécanique, simulation 4-5 personas, retours en voix, synthèse) — 5e 2024, OSR, PbtA, FitD |
| `digital-product-evaluator` | Évaluation commerciale DriveThruRPG 4 axes (listing, pricing, visuels, positionnement) — modes pre-launch et post-launch |
| `adventure-converter` | Conversion d'aventures et suppléments entre systèmes : 5e 2014 → 5e 2024, 5e → PF2e, 5e → OSR (B/X, OSE, Shadowdark), 5e → narratif. Audit source + matrice de conversion + livrable converti + notes GM |
| `stat-block-validator` | Audit mécanique de stat blocks D&D 5e 2024 (format MM 2024, arithmétique, math CR offensive/défensive, action economy, vocabulaire 2024). Pure validation, non-éditorial |

## Agents

| Agent | Rôle |
|---|---|
| `ttrpg-publication-director` | Orchestrateur full-pipeline draft → launch en 7 stages (Cliché → Mécanique → Style → Playtest → Éditorial → Conversion → Marché). Triage les skills à invoquer selon le type de produit et l'intent commercial, synthétise les findings cross-stage, produit un rapport unifié avec verdict de launch et plan d'action priorisé |

## Installation

```
/plugin install ttrpg-editorial@ludomancien-skills
```

Une fois installés, les skills se déclenchent automatiquement, ou tu peux les invoquer avec `/nom-du-skill`. L'agent `ttrpg-publication-director` s'invoque sur des requêtes du type « review this for publication », « is this ready to launch », « pipeline draft to launch », ou explicitement.

## Quand utiliser quoi

- **Skill atomique** (`ttrpg-cliche-buster`, `stat-block-validator`, etc.) — pour une vérification ciblée sur un aspect précis
- **Agent orchestrateur** (`ttrpg-publication-director`) — quand tu veux un audit *complet* avant publication, avec synthèse cross-stage et verdict de launch

L'agent invoque les skills atomiques pour toi quand pertinent — pas besoin de les lancer en amont si tu vas faire un pipeline complet.

## Voir aussi

- [`ttrpg-creation`](../ttrpg-creation/) — création du contenu à auditer
- [`README.md`](../../README.md) — vue d'ensemble du marketplace
- [`CONTRIBUTING.md`](../../CONTRIBUTING.md) — conventions et workflow d'ajout
