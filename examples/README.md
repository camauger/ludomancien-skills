# Examples — Galerie curatée

Ce dossier rassemble des **outputs réels** produits par les skills et agents du marketplace, sélectionnés parce qu'ils représentent bien ce que ces outils peuvent produire dans un usage de table ou de publication.

Ce ne sont pas des fixtures de test ni des démos synthétiques : ce sont des contenus jugés *exemplaires* par le mainteneur après usage. La galerie sert à deux choses :

1. **Donner une idée concrète** à quelqu'un qui découvre le marketplace : « voilà ce que ça sort, pour de vrai. »
2. **Servir de référence calibrée** pour ajuster un skill si son output dérive avec le temps — un exemple ancien qu'on aime encore est un point de repère utile.

## Comment ajouter un exemple

Quand un output te plaît assez pour être préservé :

1. Copie `TEMPLATE.md` vers un nouveau fichier dans ce dossier.
2. Nomme-le `<skill-ou-agent>-<slug-court>.md` — par exemple `monster-creator-stalker-de-bois-fer.md` ou `npc-creator-veuve-cendres.md`. Garde le slug descriptif mais court (3-5 mots, kebab-case).
3. Remplis le frontmatter (au minimum `skill`, `plugin`, `date`, `why`).
4. Colle l'output tel quel sous le frontmatter — pas de retouche ni de polissage. L'intérêt est de montrer ce qui sort vraiment.
5. Commit avec un message du style `docs(examples): add <slug>`.

C'est tout. Pas de validation automatique, pas de schéma rigide à respecter : le seul critère, c'est ton jugement éditorial.

## Qu'est-ce qui mérite d'être préservé

Pas tout. Préfère :

- Un output que tu utiliserais **tel quel** en table ou en publication, avec zéro édition
- Un cas où le skill a particulièrement bien capté un brief difficile ou nuancé
- Un format ou un ton que tu aimerais voir reproduit
- Un output qui démontre une capacité non-évidente du skill (un cas limite bien géré, une synthèse cross-stage réussie pour un agent)

Évite :

- Les outputs « corrects mais sans plus » — la galerie n'est pas un dépotoir d'historique
- Les outputs lourdement édités à la main après coup (ils ne représentent plus le skill)
- Les contenus liés à des projets clients confidentiels — anonymise ou n'inclus pas

## Structure

Pas de sous-dossiers pour l'instant. Si la galerie grossit (>30 fichiers), on regroupera par plugin :

```
examples/
├── README.md
├── TEMPLATE.md
├── monster-creator-stalker-de-bois-fer.md
├── npc-creator-veuve-cendres.md
├── ttrpg-publication-director-rapport-bell-of-mire.md
└── ...
```

## Lien avec les skills

Si un exemple révèle qu'un skill a particulièrement bien performé sur un cas, c'est aussi un signal utile pour l'évolution du skill lui-même. Un exemple peut servir de point d'ancrage dans un futur ajout au `references/` d'un skill (« voir style de cet exemple »).
