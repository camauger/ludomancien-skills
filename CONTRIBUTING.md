# Contribuer à Ludomancien Skills

Ce marketplace est un projet personnel maintenu par Christian Maugé. Les contributions externes sont les bienvenues mais doivent respecter la philosophie et les conventions décrites ici.

## Philosophie

Deux types de contenu cohabitent :

- **Skills** — atomiques, déclenchés par phrase, font *une* chose bien. Un `SKILL.md` + un dossier `references/` avec la matière de référence.
- **Agents** — orchestrateurs, pilotent plusieurs skills pour produire un livrable composite. Un seul fichier `.md` avec frontmatter et system prompt.

Quand quelqu'un découvre le marketplace, il doit voir tout de suite ce que chaque skill fait, dans quel système il opère, et où sont les bornes. Pas de skills fourre-tout, pas d'agent qui se contente d'enchaîner deux skills (autant les invoquer directement).

D&D 5e (2024) par défaut quand des règles sont impliquées. La plupart des skills restent system-agnostic et adaptables à PF2e, OSR, ou systèmes narratifs.

## Structure du repo

```
ludomancien-skills/
├── .claude-plugin/marketplace.json
├── plugins/
│   ├── <plugin>/
│   │   ├── .claude-plugin/plugin.json
│   │   ├── skills/
│   │   │   └── <skill-name>/
│   │   │       ├── SKILL.md
│   │   │       └── references/
│   │   │           └── *.md
│   │   └── agents/                  # optionnel
│   │       └── <agent-name>.md
├── scripts/validate.py
├── examples/                        # galerie curatée d'outputs
├── CHANGELOG.md
├── CONTRIBUTING.md
└── README.md
```

## Ajouter un skill

1. **Choisis le plugin** où il va vivre. S'il n'y a pas de fit clair parmi les cinq plugins existants, propose la création d'un nouveau plugin (rare).
2. **Crée le dossier** : `plugins/<plugin>/skills/<skill-name>/SKILL.md`. Le nom de dossier doit matcher exactement le `name:` du frontmatter — c'est validé par `scripts/validate.py`.
3. **Rédige `SKILL.md`** avec le frontmatter ci-dessous, puis la partie *Instructions* du skill (workflow, étapes, format de sortie, boundaries).
4. **Ajoute les references/** si le skill a besoin de matière de référence — tables, formats officiels, exemples calibrés, libraries de patterns. Un fichier `.md` par sujet. Tu peux y mettre autant de matière que tu veux, ces fichiers ne sont chargés que sur demande du skill.
5. **Bump la version du plugin** dans `plugins/<plugin>/.claude-plugin/plugin.json` (MINOR pour ajout de skill, voir Versioning).
6. **Mets à jour le README top-level** (table des skills du plugin concerné) et le `marketplace.json` (description et tags si pertinent).
7. **Ajoute une entrée dans CHANGELOG.md**.
8. **Valide** : `python scripts/validate.py`.

### Frontmatter de SKILL.md

```yaml
---
name: <skill-name>                    # doit matcher le nom de dossier
description: >
  <Description longue et précise. Inclut : ce que le skill fait, dans quel
  système, les bornes, et une liste de trigger phrases (FR + EN) qui
  permettent à Claude de reconnaître quand le déclencher. Maximum 1536
  caractères — au-delà, Claude Code tronque silencieusement.>
---
```

Le frontmatter est le seul mécanisme de découverte du skill. La description est lue par Claude pour décider quand l'invoquer — sois précis sur les trigger phrases et explicit sur les boundaries (« Boundary: this skill produces ONE X per call. Y is out of scope. »).

## Ajouter un agent

Les agents vivent dans `plugins/<plugin>/agents/<agent-name>.md` (un seul fichier, pas de dossier `references/`).

1. **Crée le fichier** `plugins/<plugin>/agents/<agent-name>.md`. Le nom de fichier (sans `.md`) doit matcher le `name:` du frontmatter.
2. **Frontmatter** :

```yaml
---
name: <agent-name>
description: >
  <Description longue précisant : ce que l'agent orchestre, dans quels cas
  l'utiliser, les inputs attendus, le livrable produit, et les trigger
  phrases. Max 1536 caractères.>
tools: Read, Write, Edit, Glob, Grep, Bash, Skill, TaskCreate, TaskUpdate, TaskList, TaskGet
model: opus
---
```

3. **Body** : le system prompt complet de l'agent (rôle, méthodologie stage-par-stage, format de sortie, garde-fous token-budget, halt-on-catastrophic).
4. **Bump la version du plugin** (MINOR).
5. **README + CHANGELOG + marketplace.json** comme pour un skill.
6. **Valide** : `python scripts/validate.py` (il valide aussi les agents).

Un agent ne se justifie que s'il produit une *synthèse* qu'un appel direct de skills ne produirait pas. Si l'agent ne fait qu'enchaîner deux skills sans valeur ajoutée, redirige vers un usage direct des skills.

## Style et langue

- **Français en priorité** dans les SKILL.md et la documentation top-level. L'anglais reste acceptable pour les SKILL.md de skills qui ciblent un public anglophone (la plupart des skills 5e), mais le contenu francophone (`jdr-fr/`) reste en français.
- **Orthographe française complète** : tous les accents, cédilles, et diacritiques. Jamais de substitution ASCII (`naïve` pas `naive`, `clé` pas `cle`).
- **Pas d'emojis** dans le code, les SKILL.md, les agents ou la doc, sauf si explicitement demandé.
- **Trigger phrases** : multilingues quand pertinent (FR + EN), couvrant les variations naturelles (« crée un X », « create an X », « fabrique-moi », « génère »).

## Validation locale

Avant chaque commit :

```bash
python scripts/validate.py
```

Le script vérifie :

- `marketplace.json` parse et a les champs requis
- chaque `plugin.json` parse et a `name`, `version`, `description`
- chaque `SKILL.md` a un frontmatter YAML valide avec `name` et `description`, et le `name` matche le nom de dossier
- chaque agent (`<plugin>/agents/<nom>.md`) a un frontmatter YAML valide, et le `name` matche le nom de fichier
- chaque description ≤ 1536 caractères (avertissement sinon — Claude Code tronque au-delà)
- chaque skill ou agent listé existe physiquement

Aucune dépendance externe : le script utilise un mini-parser YAML maison, pas de `pyyaml`.

## Versioning

Versioning par plugin (chaque `plugin.json` a son propre `version`) plus une version globale du marketplace (`marketplace.json`).

- **MAJOR** : changement non-rétrocompatible (renommage de skill, suppression, changement de signature majeur)
- **MINOR** : ajout d'un skill ou d'un agent, enrichissement substantiel d'un skill existant
- **PATCH** : corrections, ajustements mineurs, clarifications de doc

Bump le plugin concerné *et* le marketplace global quand tu releases. Une entrée correspondante dans `CHANGELOG.md`.

## Commit messages

Style observé dans le repo :

```
feat(<plugin>): ajout du skill <skill-name> (vX.Y.Z)
feat(<plugin>): nouveau agent <agent-name>
fix(<plugin>): corrige <quoi> dans <skill-name>
chore: <maintenance>
docs: <changement de doc>
```

Le scope `(<plugin>)` est utile mais pas obligatoire pour les changements transversaux (`chore: bump marketplace to v1.0.0`).

## Galerie d'exemples

Le dossier `examples/` est une **galerie curatée** d'outputs réels jugés exemplaires. Voir `examples/README.md` pour le mécanisme d'ajout. Les contributions à la galerie sont les bienvenues — colle l'output brut, remplis le frontmatter, commit.

## Hors-scope

Ce marketplace ne contient **pas** :

- Du contenu adulte ou explicite (voir `camauger/fantasy-vixens-skills`)
- Des outils de développement web ou d'audit frontend (voir `camauger/dev-skills`)
- Des skills purement personnels ou single-purpose qui ne profitent qu'à un projet client confidentiel

Si un skill tombe dans une zone grise, ouvre une issue avant de coder.

## Licence

MIT — voir `LICENSE`. En contribuant, tu acceptes que ta contribution soit licenciée sous MIT.
