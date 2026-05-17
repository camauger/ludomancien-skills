# Changelog

Le format suit [Keep a Changelog](https://keepachangelog.com/fr/1.1.0/) et le projet adhère au [versioning sémantique](https://semver.org/lang/fr/) par plugin.

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
