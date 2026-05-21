---
name: curate-example
description: Ajouter un output curé à la galerie examples/ du marketplace ludomancien-skills. Skill projet user-only — invoqué via /curate-example quand un output de skill ou agent mérite d'être préservé. Guide à travers le frontmatter (skill source, plugin, date, slug, why, tags), demande l'output, et propose le fichier examples/<skill>-<slug>.md à valider avant écriture. Respecte le TEMPLATE.md du projet.
disable-model-invocation: true
---

# Curate Example

Ajouter un output exemplaire à la galerie `examples/` du marketplace `ludomancien-skills`.

## Quand utiliser

Déclenché par l'utilisateur via `/curate-example` quand un output produit par un skill ou un agent du marketplace mérite d'être préservé. La galerie sert deux objectifs : vitrine de ce que le marketplace peut produire, et calibrage pour la routine remote hebdomadaire qui lit `examples/` pour proposer des patches aux SKILL.md.

Critères de curation (rappel de `examples/README.md`) :

- Output utilisable **tel quel** en table ou en publication, zéro retouche.
- Cas non-trivial bien géré, ou pattern qu'on veut voir reproduit.
- Cas limite ou synthèse cross-stage particulièrement réussie.

À NE PAS curer : outputs corrects-mais-sans-plus, outputs lourdement édités, contenus liés à des projets clients confidentiels.

## Workflow

Dialogue avec l'utilisateur en 7 étapes. À aucun moment le skill n'écrit dans `examples/` sans validation finale explicite du contenu **et** du chemin.

### 1. Identifier la source

Demander :

- Quel skill ou agent a produit cet output ?
- Lookup dans `plugins/*/skills/*/SKILL.md` et `plugins/*/agents/*.md` pour valider que le skill ou l'agent existe. Si trouvé, déterminer automatiquement le `plugin` (ttrpg-creation, ttrpg-editorial, ttrpg-tables, ttrpg-print, jdr-fr).
- Si l'output vient d'un chaînage (ex: `monster-creator` → `stat-block-validator`), attribuer au skill primaire (celui qui a produit le contenu de fond) et mentionner le chaînage dans le `why`.

### 2. Récupérer le contexte de génération

- Le prompt source, si l'utilisateur l'a en main ; sinon demander un résumé en 1-3 phrases du brief.
- La date du jour, format `YYYY-MM-DD` (auto via shell, pas hardcoded).

### 3. Définir le slug et le pourquoi

- **Slug** : kebab-case, 3-5 mots, descriptif (ex: `stalker-de-bois-fer`, `veuve-cendres`, `mire-faim`). Pas d'accents (`é` → `e`), pas d'espaces, pas de caractères spéciaux. Vérifier qu'aucun fichier `examples/<skill>-<slug>.md` existant ne porte le même nom.
- **Filename final** proposé : `examples/<skill-ou-agent>-<slug>.md`. Si collision, demander un autre slug ou confirmer le remplacement.
- **Why** : 1-3 phrases sur ce qui est exemplaire. Précision attendue. Pas "c'est bon" — préférer "ancrage strict du concept X dans une mécanique Y, cohérence sonore traversant Z, ou révèle un pattern d'erreur récurrent attrapé par le pipeline". Si l'output a une dimension méta (a révélé un anti-pattern, a calibré une convention), le mentionner explicitement.

### 4. Tags

Liste de 3-6 tags en kebab-case. Avant de proposer des tags, lire rapidement quelques frontmatter de fichiers déjà présents dans `examples/` pour rester aligné sur le vocabulaire existant. Exemples observés : `aberration`, `fp-11`, `possession`, `voie-de-victoire-radiante`, `5e-2024`, `dark-fantasy`, `noir`, `meute`. Préférer réutiliser plutôt qu'inventer si un tag existant convient.

### 5. Edited ?

Par défaut `edited: false`. Si l'utilisateur a édité l'output ne serait-ce que minimalement après génération, demander :

- Passer à `edited: true`.
- Demander une ligne `edits:` qui décrit l'édition (ex: `"corrigé typo dans nom de NPC"`, `"renommé une location pour confidentialité"`).

### 6. Récupérer l'output

Demander à l'utilisateur de coller l'output complet. L'output est inséré sous le frontmatter **tel quel** — pas de retouche, pas de reformatage, pas de réorganisation. C'est une règle dure.

### 7. Assembler et valider avant écriture

Assembler le fichier en utilisant le format du `examples/TEMPLATE.md` :

```markdown
---
skill: <name>
plugin: <plugin>
date: YYYY-MM-DD
prompt: |
  <prompt source ou résumé>
why: |
  <pourquoi exemplaire>
tags: [tag1, tag2, ...]
edited: false
---

<output collé tel quel>
```

Si `edited: true`, ajouter `edits: |` avec la description avant la ligne de fermeture du frontmatter.

Présenter à l'utilisateur dans la conversation :

1. Le chemin final proposé : `examples/<skill>-<slug>.md`.
2. Le frontmatter assemblé (à valider).
3. Confirmation que l'output collé n'a pas été modifié par le skill.

Demander explicitement : *"OK pour écrire ce fichier ?"*. Sur réponse affirmative (`oui`, `go`, `vas-y`, équivalent), faire le Write. Sinon, ajuster selon le retour utilisateur et re-présenter.

## Contraintes strictes

1. **Aucune écriture sans validation finale** : l'étape 7 est toujours une confirmation utilisateur explicite. Pas de Write proactif même si toutes les autres étapes ont été validées une à une.
2. **Le slug ne doit jamais écraser silencieusement** : si `examples/<skill>-<slug>.md` existe déjà, demander un autre slug ou confirmer le remplacement explicitement.
3. **Le frontmatter doit respecter `examples/TEMPLATE.md`** : si le TEMPLATE.md évolue (champs ajoutés ou retirés), s'adapter au lieu de hardcoder les champs.
4. **Pas de retouche de l'output** : l'output collé est inséré tel quel. Le skill ne corrige pas la typographie, ne reformate pas le markdown, ne réorganise pas les sections. Pas d'exception.
5. **Pas de tags fantaisistes** : lire les frontmatter existants pour rester aligné. Inventer un tag est acceptable si rien d'existant ne convient, mais signaler le nouveau tag à l'utilisateur pour validation.

## Intégration avec la boucle d'amélioration

Ce skill alimente directement la routine remote hebdomadaire d'analyse des `examples/` (cron `0 14 * * 0`, dimanche 14h UTC), qui lit la galerie et propose des patches aux SKILL.md du marketplace. La routine a un seuil ≥3 exemples avant de produire une analyse complète ; en-dessous, elle produit un rapport "skipped".

Rythme attendu de curation : faible, 1 exemple par semaine ou moins selon ce qui sort comme exemplaire. Le skill doit donc rester rapide et sans friction — chaque utilisation représente une décision éditoriale rare et précieuse.
