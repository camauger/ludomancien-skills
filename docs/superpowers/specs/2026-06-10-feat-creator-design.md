# Spec — skill `feat-creator` (plugin ttrpg-creation)

**Date :** 2026-06-10
**Statut :** approuvé (design validé en dialogue le 2026-06-10)
**Version cible du plugin :** ttrpg-creation 1.3.0

---

## 1. Mission

Créer des feats custom pour D&D 5e 2024, au format du Player's Handbook 2024,
publication-ready. Le skill produit **un feat par appel**, ou un **petit set
thématique de 2–4 feats liés** (ex. chaîne d'un ordre de chevalerie :
1 Origin + 2 General + 1 Epic Boon).

Comme spell-creator, le skill est mécanique *et* narratif : discipline de
balance non négociable, mais chaque feat reçoit une identité, une origine
et 1–2 plot hooks.

## 2. Périmètre — les 4 catégories du PHB 2024

| Catégorie | Niveau d'accès | ASI | Prérequis | Position de puissance |
|---|---|---|---|---|
| **Origin** | 1 (via background) | non | aucun | plancher — utile mais jamais must-pick |
| **General** | 4+ | +1 (half-feat par défaut en 2024) | niveau + parfois caractéristique/feature | référence du homebrew |
| **Fighting Style** | via trait Fighting Style | non | trait Fighting Style | combat uniquement, étroit |
| **Epic Boon** | 19+ | +1 jusqu'à 30 | niveau 19+ | capstone, identity-defining |

## 3. Frontières (boundary)

- **`backgrounds`** : crée des backgrounds qui *référencent* un Origin feat.
  Quand un Origin feat custom est nécessaire, **feat-creator est l'autorité**.
  Une mention croisée est ajoutée dans `backgrounds/SKILL.md` (section Feat),
  sans réécrire ce skill.
- **Features de classe / sous-classe** (Eldritch Invocations, manœuvres,
  Metamagic, formes de moine) : hors scope — même frontière que spell-creator.
- **Feats 2014** (format sans ASI systématique) : hors scope, 2024 only.
- **Validation d'un feat existant** : ttrpg-supplement-reviewer.
- **Sorts** : spell-creator. **Objets magiques** : magic-item-creator.

## 4. Architecture des fichiers

```
plugins/ttrpg-creation/skills/feat-creator/
├─ SKILL.md
└─ references/
   ├─ feat-categories-2024.md
   ├─ power-budgets-and-benchmarks.md
   ├─ feat-effect-library.md
   └─ balance-and-anti-patterns.md
```

Pattern identique à spell-creator : SKILL.md porte le scope, les frontières,
le workflow et le format de sortie ; les références sont chargées à la
demande (progressive disclosure).

### 4.1 SKILL.md

1. **Frontmatter description** : triggers FR/EN (« crée un don »,
   « create a feat », « origin feat custom », « epic boon for my barbarian »,
   « half-feat homebrew », « feat chain », « don pour mon paladin »,
   « fighting style homebrew »…) + boundary explicite.
2. **Before You Begin** — 5 points à régler avant de concevoir :
   concept/identité, catégorie (donc niveau d'accès), prérequis,
   budget de puissance vs feats officiels comparables, hook d'identité.
3. **Workflow en 6 étapes** :
   1. Concept & nom (distinctif, pas générique)
   2. Catégorie & prérequis
   3. Conception mécanique — 2–3 bénéfices max, règle « un feat fait
      une chose bien »
   4. Calibrage — comparaison explicite à 2–3 feats officiels nommés
   5. Texte PHB 2024 — vocabulaire 2024 (Advantage/Disadvantage, Heroic
      Inspiration, pas de syntaxe 2014)
   6. Lore & plot hooks (1–2, origine ou utilisateur notable)
4. **Format de sortie** : entrée PHB 2024 (nom, catégorie, prérequis,
   repeatable ou non, bénéfices en liste à puces nommées) + paragraphe
   lore + hooks.
5. **Mode set thématique (2–4 feats)** : cohérence de nommage, progression
   de puissance entre catégories, pas de stacking abusif intra-set.

### 4.2 Références

| Fichier | Contenu |
|---|---|
| `feat-categories-2024.md` | Anatomie des 4 catégories : structure exacte, prérequis légaux, présence/absence d'ASI, exemples officiels décortiqués |
| `power-budgets-and-benchmarks.md` | Étalonnage : valeur d'un +1 ASI (~½ feat), benchmarks officiels par catégorie, half-feats vs full-feats, ce qu'un Origin feat ne doit jamais donner |
| `feat-effect-library.md` | Briques mécaniques réutilisables par pilier (combat / exploration / social), coûts en action economy, effets « once per rest » vs « per Proficiency Bonus » |
| `balance-and-anti-patterns.md` | Pièges : must-pick (trop fort), trap option (trop faible), stacking avec feats officiels, feat qui marche sur une feature de classe, bonus passifs empilables |

## 5. Mises à jour du marketplace

- [ ] `plugins/ttrpg-creation/.claude-plugin/plugin.json` : version
      **1.2.0 → 1.3.0** + description enrichie (mention feats)
- [ ] `.claude-plugin/marketplace.json` : version + description du plugin
      ttrpg-creation
- [ ] `plugins/ttrpg-creation/README.md` : ligne feat-creator dans le tableau
- [ ] `README.md` racine : ligne feat-creator dans le tableau
- [ ] `CHANGELOG.md` : entrée v1.3.0
- [ ] `plugins/ttrpg-creation/skills/backgrounds/SKILL.md` : mention croisée
      vers feat-creator pour les Origin feats custom (1–2 lignes, pas de
      réécriture)

## 6. Critères de succès

- [ ] Le skill suit le format des skills récents du plugin (spell-creator
      comme étalon) : frontmatter description riche, Before You Begin,
      workflow numéroté, format de sortie, références à la demande.
- [ ] Les 4 catégories 2024 sont couvertes avec leurs règles structurelles
      exactes (Origin sans ASI, General avec +1, Epic Boon +1 jusqu'à 30).
- [ ] Chaque feat produit est calibré contre des feats officiels *nommés*.
- [ ] Vocabulaire strictement 2024 (pas de syntaxe 2014).
- [ ] La boundary description évite les collisions de triggering avec
      backgrounds, spell-creator et magic-item-creator.
- [ ] Manifests et READMEs à jour, version 1.3.0 cohérente partout.

## 7. Hors scope (explicitement)

- Mode batch large (10–20 feats avec audit croisé façon bestiary-builder) —
  différé ; le mode set 2–4 couvre le besoin courant.
- Feats 2014 et conversion 2014 → 2024 (adventure-converter couvre la
  conversion générale).
- Design de nouvelles classes ou sous-classes.
