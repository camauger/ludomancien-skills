# feat-creator Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Ajouter le skill `feat-creator` (feats custom D&D 5e 2024, 4 catégories PHB) au plugin ttrpg-creation, et publier la version 1.3.0 du plugin.

**Architecture:** Pattern spell-creator — un `SKILL.md` (scope, frontières, workflow 6 étapes, format de sortie PHB 2024) + 4 fichiers `references/` chargés à la demande. Mises à jour des manifests (plugin.json, marketplace.json), des READMEs (plugin + racine), du CHANGELOG, et mention croisée dans `backgrounds/SKILL.md`.

**Tech Stack:** Markdown (skills Claude Code), JSON (manifests). Aucun code exécutable. Vérifications : parse JSON, cohérence de version, structure frontmatter, validation finale via l'agent plugin-dev:plugin-validator.

**Spec :** `docs/superpowers/specs/2026-06-10-feat-creator-design.md`

**Étalon stylistique :** `plugins/ttrpg-creation/skills/spell-creator/SKILL.md` et ses références. Ton : prose dense, prescriptive, tableaux mécaniques, exemples officiels nommés. Les SKILL.md du dépôt sont rédigés en anglais avec triggers bilingues FR/EN dans la description.

---

## Données de référence D&D 5e 2024 (à utiliser dans les tâches 1–5)

Ces listes sont les données dures du PHB 2024. Les fichiers de référence les décortiquent ; ne pas en inventer d'autres.

**Origin feats (10)** : Alert, Crafter, Healer, Lucky, Magic Initiate, Musician, Savage Attacker, Skilled, Tavern Brawler, Tough.

**General feats (niv. 4+, +1 ASI inclus, sélection)** : Ability Score Improvement, Actor, Athlete, Charger, Chef, Crossbow Expert, Crusher, Defensive Duelist, Dual Wielder, Durable, Elemental Adept, Fey-Touched, Grappler, Great Weapon Master, Heavily Armored, Heavy Armor Master, Inspiring Leader, Keen Mind, Mage Slayer, Martial Weapon Training, Medium Armor Master, Moderately Armored, Mounted Combatant, Observant, Piercer, Poisoner, Polearm Master, Resilient, Ritual Caster, Sentinel, Shadow-Touched, Sharpshooter, Shield Master, Skill Expert, Skulker, Slasher, Speedy, Spell Sniper, Telekinetic, Telepathic, War Caster, Weapon Master.

**Fighting Style feats (10)** : Archery, Blind Fighting, Defense, Dueling, Great Weapon Fighting, Interception, Protection, Thrown Weapon Fighting, Two-Weapon Fighting, Unarmed Fighting.

**Epic Boons (niv. 19+, +1 ASI jusqu'à 30, sélection)** : Boon of Combat Prowess, Boon of Dimensional Travel, Boon of Energy Resistance, Boon of Fate, Boon of Fortitude, Boon of Irresistible Offense, Boon of Recovery, Boon of Skill, Boon of Speed, Boon of Spell Recall, Boon of the Night Spirit, Boon of Truesight.

**Format PHB 2024 d'une entrée de feat :**

```markdown
#### Feat Name
*General Feat (Prerequisite: Level 4+, Strength 13+)*

You gain the following benefits.

**Ability Score Increase.** Increase your Strength score by 1, to a maximum of 20.

**Named Benefit.** Benefit text using 2024 vocabulary.

**Repeatable.** (only if applicable) You can take this feat more than once…
```

Variantes d'en-tête : `*Origin Feat*` (pas de prérequis, pas d'ASI), `*Fighting Style Feat (Prerequisite: Fighting Style Feature)*` (pas d'ASI), `*Epic Boon Feat (Prerequisite: Level 19+)*` (ASI jusqu'à 30).

**Vocabulaire 2024 obligatoire** : Advantage/Disadvantage (capitalisés), Heroic Inspiration, « once per turn », « when you take the Attack action », « Long Rest / Short Rest » capitalisés, « a number of times equal to your Proficiency Bonus ». Interdits (syntaxe 2014) : « ability check, attack roll, or saving throw » non capitalisés dans les noms de mécaniques nommées, « racial traits », « one of your skill proficiencies of choice » à l'ancienne.

---

### Task 1: `references/feat-categories-2024.md`

**Files:**
- Create: `plugins/ttrpg-creation/skills/feat-creator/references/feat-categories-2024.md`

- [ ] **Step 1 : Écrire le fichier** (~200–280 lignes) avec ce squelette :

```markdown
# Feat Categories — D&D 5e 2024

(intro : 4 catégories, où chacune entre en jeu dans la progression)

## Category Comparison Table
| Category | Access | ASI | Prerequisites | Power position |  ← tableau de la spec §2

## Origin Feats
- Structure exacte : *Origin Feat*, no prerequisite, no ASI
- Acquisition : via background au niveau 1 (+ Human qui en gagne un de plus)
- Les 10 officiels listés avec une ligne d'analyse chacun
  (ex. Lucky = ressource par Long Rest scalée sur PB ; Tough = +2 HP/level…)
- Dissection de 2 exemples : Magic Initiate (Repeatable, choix de liste),
  Skilled (Repeatable, pure proficiency)
- Ce qu'un Origin feat peut donner / ne peut jamais donner

## General Feats
- Structure exacte : *General Feat (Prerequisite: Level 4+ …)*, +1 ASI ciblé
- Le « half-feat universel » : en 2024 TOUS les General feats incluent +1 ASI
- Prérequis légaux : niveau (4+, 8+…), score de caractéristique (13+),
  feature (Spellcasting/Pact Magic), proficiency (armor training)
- Dissection de 3 exemples : Great Weapon Master (trade-off),
  Resilient (défensif pur), War Caster (enabler de build)

## Fighting Style Feats
- Structure : *Fighting Style Feat (Prerequisite: Fighting Style Feature)*
- Pas d'ASI ; étroit, combat only ; remplaçable à level-up (Fighter)
- Les 10 officiels listés ; dissection : Defense (+1 AC passif plancher),
  Dueling (+2 dégâts conditionnel = plafond)

## Epic Boon Feats
- Structure : *Epic Boon Feat (Prerequisite: Level 19+)*, ASI +1 jusqu'à 30
- Position : capstone, peut casser les règles de base (téléportation
  par tour, Truesight permanent…)
- Les 12 officiels listés avec une ligne d'analyse
- Dissection : Boon of Combat Prowess (auto-hit 1/tour),
  Boon of Fate (réaction narrative)

## Choosing the Right Category (arbre de décision court)
```

- [ ] **Step 2 : Vérifier la structure** — titre H1 unique, sections H2 dans l'ordre du squelette, tableau comparatif présent, les 4 catégories couvertes.

- [ ] **Step 3 : Commit**

```bash
git add plugins/ttrpg-creation/skills/feat-creator/references/feat-categories-2024.md
git commit -m "feat(ttrpg-creation): add feat-creator reference — feat categories 2024"
```

### Task 2: `references/power-budgets-and-benchmarks.md`

**Files:**
- Create: `plugins/ttrpg-creation/skills/feat-creator/references/power-budgets-and-benchmarks.md`

- [ ] **Step 1 : Écrire le fichier** (~200–280 lignes), squelette :

```markdown
# Power Budgets and Benchmarks — Feats 2024

## The Currency: +1 ASI ≈ half a feat
- Un General feat 2024 = +1 ASI + « l'autre moitié » (le benefit réel)
- Donc l'autre moitié doit valoir ~ un Origin feat
- Conséquence : benchmark un General feat custom = ASI + 1-2 benefits
  comparables à un Origin feat existant

## Benchmarks par catégorie
### Origin floor & ceiling
- Floor : Musician (utilité situationnelle) ; Ceiling : Lucky / Magic Initiate
- Un Origin custom doit tenir ENTRE ces deux bornes (tableau floor/ceiling)
### General floor & ceiling
- Floor : Keen Mind ; Ceiling : Great Weapon Master / Sharpshooter / War Caster
### Fighting Style floor & ceiling
- Floor : Protection (réaction conditionnelle) ; Ceiling : Defense (+1 AC toujours actif)
### Epic Boon floor & ceiling
- Floor : Boon of Skill ; Ceiling : Boon of Combat Prowess / Irresistible Offense

## Quantified guidelines (tableau)
| Effet | Valeur indicative |
- +1 AC permanent ≈ un General feat entier (cf. Defense + Dueling cumulés)
- Advantage permanent sur un type de roll fréquent = trop pour Origin
- Ressource 1/Long Rest ≈ ½ feat si effet niveau sort 1-2
- PB/Long Rest uses = le pattern 2024 par défaut pour les ressources
- +X HP par niveau : 2/level = Tough = un Origin entier
- Dégâts : +PB dégâts 1/tour conditionnel ≈ ½ General feat

## What each category must never grant
- Origin : ASI, bonus de combat passifs chiffrés (+X hit/AC/dégâts), Extra Attack
- General : 2 ASI, des features de classe entières, Concentration-free buffs
- Fighting Style : quoi que ce soit hors combat
- Epic Boon : (presque tout est permis) — mais pas d'action economy infinie

## Calibration protocol (5 étapes)
1. Nommer 2-3 feats officiels de même catégorie et créneau
2. Comparer benefit par benefit (tableau)
3. Si le custom gagne sur TOUS les axes → nerf
4. Si le custom perd sur tous → buff ou élargir le créneau
5. Verdict d'une ligne : « comparable à X, plus étroit que Y »
```

- [ ] **Step 2 : Vérifier** — chaque benchmark cite des feats officiels nommés (aucun benchmark abstrait), le protocole de calibrage a 5 étapes.

- [ ] **Step 3 : Commit**

```bash
git add plugins/ttrpg-creation/skills/feat-creator/references/power-budgets-and-benchmarks.md
git commit -m "feat(ttrpg-creation): add feat-creator reference — power budgets and benchmarks"
```

### Task 3: `references/feat-effect-library.md`

**Files:**
- Create: `plugins/ttrpg-creation/skills/feat-creator/references/feat-effect-library.md`

- [ ] **Step 1 : Écrire le fichier** (~220–300 lignes), squelette :

```markdown
# Feat Effect Library — Reusable Mechanical Bricks

(intro : briques combinables ; un feat = 2-3 briques max, dont 1 signature)

## Resource patterns (les « moteurs » 2024)
- Per Long Rest (1×) / Per Short or Long Rest / PB per Long Rest /
  Once per turn / Recharge on Initiative (rare)
- Quand utiliser quoi (tableau pattern → fréquence d'usage attendue)

## Combat bricks
- Attack riders (dégâts bonus conditionnels, push/prone/grapple on hit)
- Defensive bricks (réactions défensives, resistances conditionnelles, temp HP)
- Action economy bricks (Bonus Action attacks, Dash/Disengage riders) — DANGER ZONE
- Weapon Mastery interactions (le sous-système 2024 : Sap, Vex, Topple…)

## Exploration bricks
- Mouvement (climb/swim speed, ignore difficult terrain, jump)
- Sens (Darkvision, Blindsight courte portée — Epic only pour Truesight)
- Survie (rations, navigation, climat) ; outils et crafting

## Social bricks
- Proficiency/Expertise ciblée, Advantage conditionnel sur Influence
- Lecture (Insight riders), langues, contacts narratifs

## Magic bricks
- Cantrips/spells connus (le pattern Magic Initiate / Fey-Touched :
  1 cantrip + 1 sort niveau 1, 1 cast gratuit par Long Rest, re-cast avec slots)
- Interaction Concentration (War Caster pattern) ; rituels (Ritual Caster pattern)

## Scaling knobs (comment une brique grandit d'une catégorie à l'autre)
- Origin → General : ajouter ASI + retirer une restriction
- General → Epic Boon : retirer la limite de ressource OU rendre permanent
(tableau d'exemples : même concept décliné aux 3 niveaux de puissance)
```

- [ ] **Step 2 : Vérifier** — chaque brique cite au moins un feat officiel qui l'utilise ; la « danger zone » action economy est marquée.

- [ ] **Step 3 : Commit**

```bash
git add plugins/ttrpg-creation/skills/feat-creator/references/feat-effect-library.md
git commit -m "feat(ttrpg-creation): add feat-creator reference — effect library"
```

### Task 4: `references/balance-and-anti-patterns.md`

**Files:**
- Create: `plugins/ttrpg-creation/skills/feat-creator/references/balance-and-anti-patterns.md`

- [ ] **Step 1 : Écrire le fichier** (~180–250 lignes), squelette :

```markdown
# Balance and Anti-Patterns — Feats 2024

## The two failure modes
- Must-pick : si un build « doit » le prendre, il est trop fort
  (test : remplace-t-il systématiquement l'ASI +2 au niveau 4 ?)
- Trap option : si personne ne le prend jamais, il gaspille de l'encre
  (test : existe-t-il UN build qui le préfère à Resilient ?)

## Anti-pattern catalog (8-10 entrées, chacune : nom, exemple raté,
   pourquoi ça casse, le fix)
1. Stacking passif (+1 dégâts qui s'empile avec tout, toujours)
2. Le feat qui marche sur une feature de classe
   (donner Extra Attack, Sneak Attack-like, Channel Divinity-like)
3. Double dip ASI (+2 ou deux +1 dans un General feat)
4. Le couteau suisse (4+ benefits sans identité)
5. Prérequis cosmétique (prérequis qui ne gate rien de réel)
6. L'Origin feat de combat chiffré (+X hit/dégâts/AC au niveau 1)
7. Action economy infinie (Bonus Action attack sans condition ni coût)
8. Le feat-impôt (corrige une faiblesse universelle → tout le monde le prend ;
   cf. pourquoi War Caster reste acceptable : il a des alternatives)
9. Scaling oublié (effet chiffré fixe qui devient nul à T3-T4 ou
   brisé à T1 — utiliser PB ou des dés)
10. Le boon timide (Epic Boon calibré comme un General feat)

## Stacking audit (protocole)
- Lister les 3-5 feats officiels qui partagent le créneau
- Vérifier les combos 2 à 2 (custom + officiel) sur un build optimisé
- Red flags : cumul de bonus de même type, boucles de ressources

## Repeatable rules
- Quand « Repeatable » est sain (choix différent à chaque prise :
  Magic Initiate, Skilled) vs malsain (empilement du même bonus)

## Final checklist (10 cases avant livraison d'un feat)
```

- [ ] **Step 2 : Vérifier** — 8–10 anti-patterns, chacun avec exemple + fix ; checklist finale présente.

- [ ] **Step 3 : Commit**

```bash
git add plugins/ttrpg-creation/skills/feat-creator/references/balance-and-anti-patterns.md
git commit -m "feat(ttrpg-creation): add feat-creator reference — balance and anti-patterns"
```

### Task 5: `SKILL.md`

**Files:**
- Create: `plugins/ttrpg-creation/skills/feat-creator/SKILL.md`

- [ ] **Step 1 : Écrire le frontmatter.** Description sur le modèle spell-creator (`>` multiline) :

```yaml
---
name: feat-creator
description: >
  Create complete custom feats for D&D 5e 2024, formatted to match the
  2024 Player's Handbook style. Covers all four feat categories: Origin
  feats (level 1, no prerequisite, no ASI), General feats (level 4+,
  +1 Ability Score Increase included — the 2024 half-feat structure),
  Fighting Style feats (Fighting Style feature prerequisite), and Epic
  Boons (level 19+, ASI up to 30). Each feat ships with PHB-format entry
  (name, category, prerequisite, repeatable flag, named benefits),
  calibration against named official feats, lore paragraph and 1–2 plot
  hooks. Produces ONE feat per call or a small thematic set of 2–4
  linked feats (e.g. a knightly order chain: 1 Origin + 2 General +
  1 Epic Boon). Use on "crée un don", "create a feat", "custom feat",
  "origin feat custom", "epic boon for my barbarian", "half-feat
  homebrew", "feat chain", "don pour mon paladin", "fighting style
  homebrew", "feat for my campaign", "homebrew feat 2024". Boundary:
  class and subclass features (Eldritch Invocations, Battle Master
  maneuvers, Metamagic, monk techniques) are NOT feats — out of scope.
  Backgrounds referencing an Origin feat are built by the backgrounds
  skill; when that background needs a CUSTOM Origin feat, this skill is
  the authority. Spells use spell-creator; magic items use
  magic-item-creator; validating an existing feat uses
  ttrpg-supplement-reviewer. Targets 2024 rules only.
---
```

- [ ] **Step 2 : Écrire le corps** (~250–350 lignes), sections dans cet ordre (modèle spell-creator) :

```markdown
# Feat Creator
(2 paragraphes : mission, mécanique ET narratif)

## Scope and Boundary
(tableau In scope / Out of scope — reprendre la spec §3 ;
 mention explicite : backgrounds → origin feat custom → ici)

## Before You Begin
(5 points : 1. Concept, 2. Category — avec mini-tableau des 4 catégories
 et pointeur vers references/feat-categories-2024.md, 3. Prerequisites,
 4. Power budget — pointeur vers references/power-budgets-and-benchmarks.md,
 5. Identity hook. « If any of these is unclear, ask before designing. »)

## The Six-Step Creation Workflow
### Step 1 — Concept and Name (nom distinctif ; anti-générique)
### Step 2 — Category and Prerequisites (règles structurelles par catégorie)
### Step 3 — Mechanical Design (2-3 benefits max, 1 signature ;
   pointeur vers references/feat-effect-library.md)
### Step 4 — Calibration (protocole : 2-3 feats officiels NOMMÉS,
   tableau de comparaison ; pointeur vers references/power-budgets-and-benchmarks.md
   et references/balance-and-anti-patterns.md)
### Step 5 — PHB 2024 Text (le format exact d'entrée + vocabulaire 2024 ;
   liste des interdits 2014)
### Step 6 — Lore and Plot Hooks (origine, utilisateur notable, 1-2 hooks)

## Output Format
(gabarit complet d'une livraison : entrée PHB + « Design Notes » avec
 le verdict de calibrage + lore + hooks)

## Thematic Set Mode (2–4 feats)
(cohérence de nommage, progression Origin → General → Epic Boon,
 audit de stacking intra-set, un seul thème mécanique partagé)

## Common Requests (tableau requête type → décision de catégorie)
```

- [ ] **Step 3 : Vérifier la structure** — frontmatter YAML valide (name + description seulement, comme les autres skills du plugin), les 4 références pointées chacune au moins une fois, format PHB présent dans Step 5 et Output Format.

- [ ] **Step 4 : Commit**

```bash
git add plugins/ttrpg-creation/skills/feat-creator/SKILL.md
git commit -m "feat(ttrpg-creation): add feat-creator skill (SKILL.md)"
```

### Task 6: Mention croisée dans `backgrounds/SKILL.md`

**Files:**
- Modify: `plugins/ttrpg-creation/skills/backgrounds/SKILL.md` (section « ### 3. Feat », lignes ~47–50)

- [ ] **Step 1 : Ajouter la ligne de renvoi.** Dans la section `### 3. Feat`, après « Custom feats must follow 2024 origin feat design principles », ajouter :

```markdown
- For a fully designed custom Origin feat (mechanics, calibration, lore), delegate to the `feat-creator` skill — it is the authority on feat design; this skill then references the resulting feat by name
```

- [ ] **Step 2 : Vérifier** — la modification est de 1–2 lignes, rien d'autre ne change dans le fichier.

- [ ] **Step 3 : Commit**

```bash
git add plugins/ttrpg-creation/skills/backgrounds/SKILL.md
git commit -m "docs(ttrpg-creation): backgrounds delegates custom origin feats to feat-creator"
```

### Task 7: Manifests — `plugin.json` et `marketplace.json`

**Files:**
- Modify: `plugins/ttrpg-creation/.claude-plugin/plugin.json` (version + description)
- Modify: `.claude-plugin/marketplace.json` (entrée ttrpg-creation : version + description)

- [ ] **Step 1 : Mettre à jour `plugin.json`** — `"version": "1.3.0"` et insérer dans la description, après « …et sorts custom (Cantrip → 9e niveau, 8 écoles) », le segment : « , dons custom (feats 2024 : Origin / General / Fighting Style / Epic Boon) ». Ne pas toucher au reste.

- [ ] **Step 2 : Mettre à jour `marketplace.json`** — pour l'entrée du plugin ttrpg-creation : `"version": "1.3.0"`, même enrichissement de description (lire d'abord la ligne existante, appliquer le même segment), et ajouter un tag `"feats"` si l'entrée a un tableau `tags`.

- [ ] **Step 3 : Vérifier que les deux JSON parsent**

Run (PowerShell) :
```powershell
Get-Content "plugins/ttrpg-creation/.claude-plugin/plugin.json" -Raw | ConvertFrom-Json | Select-Object name, version
Get-Content ".claude-plugin/marketplace.json" -Raw | ConvertFrom-Json | Out-Null; "marketplace.json OK"
```
Expected : `ttrpg-creation 1.3.0` et `marketplace.json OK`.

- [ ] **Step 4 : Commit**

```bash
git add plugins/ttrpg-creation/.claude-plugin/plugin.json .claude-plugin/marketplace.json
git commit -m "chore(ttrpg-creation): bump to 1.3.0 — feat-creator"
```

### Task 8: READMEs et CHANGELOG

**Files:**
- Modify: `plugins/ttrpg-creation/README.md` (tableau des skills)
- Modify: `README.md` racine (tableau des skills, après la ligne `spell-creator` ~ligne 45)
- Modify: `CHANGELOG.md` (nouvelle entrée en tête)

- [ ] **Step 1 : Ajouter la ligne au tableau du README racine** (après `spell-creator`) :

```markdown
| `feat-creator` | Dons custom D&D 5e 2024 — 4 catégories (Origin / General / Fighting Style / Epic Boon), format PHB 2024 (catégorie / prérequis / ASI / benefits nommés + lore + plot hooks), calibrage contre feats officiels nommés, mode set thématique 2–4 feats liés |
```

- [ ] **Step 2 : Ajouter la ligne équivalente dans `plugins/ttrpg-creation/README.md`** — lire d'abord le format du tableau de ce README (il peut différer du README racine) et s'y conformer.

- [ ] **Step 3 : Ajouter l'entrée CHANGELOG** — lire le format des entrées existantes et le suivre ; contenu :

```markdown
## ttrpg-creation 1.3.0 — 2026-06-10
### Added
- **feat-creator** : nouveau skill — dons custom D&D 5e 2024, 4 catégories
  (Origin / General / Fighting Style / Epic Boon), format PHB 2024, calibrage
  contre feats officiels nommés, mode set thématique 2–4 feats.
- `backgrounds` délègue désormais la conception des Origin feats custom à feat-creator.
```

- [ ] **Step 4 : Commit**

```bash
git add README.md plugins/ttrpg-creation/README.md CHANGELOG.md
git commit -m "docs: feat-creator in READMEs and CHANGELOG (ttrpg-creation 1.3.0)"
```

### Task 9: Validation finale

**Files:** aucun nouveau ; vérification transversale.

- [ ] **Step 1 : Lancer l'agent plugin-dev:plugin-validator** sur `plugins/ttrpg-creation` (structure, plugin.json, frontmatter des skills).

- [ ] **Step 2 : Vérifier la cohérence de version 1.3.0** :

Run (Grep) : chercher `1\.3\.0` dans `plugins/ttrpg-creation/.claude-plugin/plugin.json`, `.claude-plugin/marketplace.json`, `CHANGELOG.md`.
Expected : 3 fichiers matchent ; aucune occurrence restante de `"version": "1.2.0"` pour ttrpg-creation.

- [ ] **Step 3 : Vérifier les pointeurs de références** — chaque fichier de `references/` est cité au moins une fois dans `SKILL.md` (Grep `references/` dans le SKILL.md → 4 fichiers distincts).

- [ ] **Step 4 : Corriger tout défaut relevé, puis commit final si corrections**

```bash
git add -A
git commit -m "fix(ttrpg-creation): address validation findings for feat-creator"
```

---

## Self-review (fait à la rédaction du plan)

- **Couverture spec** : §1 mission → Task 5 ; §2 catégories → Tasks 1, 5 ; §3 frontières → Tasks 5, 6 ; §4 architecture → Tasks 1–5 ; §5 marketplace → Tasks 7, 8 ; §6 critères → Task 9 ; §7 hors scope → respecté (pas de tâche batch). Aucun écart.
- **Placeholders** : les squelettes de fichiers sont volontairement des plans de section détaillés (contenu rédactionnel produit à l'exécution en suivant l'étalon spell-creator) — chaque section indique son contenu réel, ses exemples officiels et ses données chiffrées ; pas de « TBD ».
- **Cohérence** : noms de fichiers identiques entre spec, Task 1–4 et pointeurs de Task 5 ; version 1.3.0 partout.
