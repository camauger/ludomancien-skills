# Spec — enrichissement de feat-effect-library.md (feat-creator)

**Date :** 2026-06-10
**Statut :** approuvé (design détaillé validé en dialogue le 2026-06-10)
**Version cible du plugin :** ttrpg-creation 1.4.0 (MINOR — enrichissement substantiel, contrat de stabilité v1.0.0)

---

## 1. Mission

Ajouter trois familles de briques mécaniques à
`plugins/ttrpg-creation/skills/feat-creator/references/feat-effect-library.md`,
révélées manquantes par le premier corpus d'usage réel (les 10 dons Zarathar,
curés dans `examples/feat-creator-dons-zarathar.md`) :

1. **Information Bricks** (divination & information)
2. **Bond & Companion Bricks** (lien & compagnon)
3. **Debt & Observance Bricks** (économie narrative & dette)

**Écarté explicitement** (choix utilisateur) : les Drawback riders /
malédictions — signature du format maison Zarathar, hors skill générique
pour l'instant.

## 2. Ancrage (décision validée)

**Officiel + exemple curé** : chaque brique s'étalonne sur des feats, sorts
ou features officiels 2024 (Augury, Detect Magic, Find Familiar, Telepathic,
Sharpshooter, Luck Points, Beast Master…) quand aucun feat officiel n'existe
dans la famille ; chaque section se clôt par un renvoi
*Illustrations: see `examples/feat-creator-dons-zarathar.md` (…)* —
le mécanisme prévu par `examples/README.md` (« un exemple peut servir de
point d'ancrage dans references/ »).

## 3. Emplacement et structure

Les trois sections s'insèrent **entre « Magic Bricks » et « Scaling Knobs »**,
dans cet ordre : Information → Bond & Companion → Debt & Observance.
Chaque section = préambule (1–3 phrases posant la règle de famille) +
tableau récapitulatif (brique / gabarit mécanique / étalon officiel / coût
indicatif) + détails par brique + ligne de scaling de famille + renvoi
galerie. Fichier : ~120 → ~240 lignes.

## 4. Contenu normatif des trois sections

### 4.1 Information Bricks

Préambule : l'information ne se mesure pas en DPR mais en **questions
fermées par repos** (1 question fermée/LR ≈ ½ feat) et en scènes d'enquête
économisées.

| Brique | Gabarit | Étalon | Coût |
|---|---|---|---|
| Closed oracle | 1/LR, 10 min d'exercice, question sur une action dans l'heure → *weal / woe / ambiguous* | Sort *Augury* (niv. 2, rituel) | ≈ ½ feat |
| Detection at range | UNE catégorie d'anomalie, rayon fixe 30–60 ft | *Detect Magic* rituel ; Divine Sense | ⅓–½ feat selon rareté |
| Intent reading | ≥ 1 min d'interaction, jet opposé → UN fait défini d'avance | Insight vs Deception ; *Detect Thoughts* (surface) | ⅓ feat ; ½ si fait fort |
| Diagnostic | 1 min d'examen → données mécaniques honnêtes (HP Dice, poisons, dégâts < 24 h) | Maîtrise Medicine | ⅓ feat, support |

Règles dures par brique :
- **Closed oracle** : 3 leviers (menu de réponses — jamais de texte libre ;
  conditions d'exercice — lieu / médium / fenêtre temporelle, chaque
  condition retirée = un cran de puissance ; sortie ambiguë **obligatoire**
  — soupape anti-court-circuit d'enquête). Anti-piège : sans fenêtre
  temporelle, l'oracle devient détecteur de mensonge universel.
- **Detection at range** : catégorie nommée et étroite (jamais « le
  danger ») ; passif légal seulement si la catégorie est rare (≤ 1/session
  typique) ; portée 30 ft Origin / 60 ft General / horizon Epic.
- **Intent reading** : le fait appris est écrit dans le feat, pas choisi à
  l'usage ; deux faits = deux fois le prix ; toujours un jet opposé, jamais
  de DD fixe ni d'automatisme sous l'Epic (Truesight = précédent du
  « toujours vrai »).
- **Diagnostic** : information mécanique honnête, sous-cotée et précieuse ;
  plafond : ne révèle jamais une statistique cachée par design sans accord MJ.

Scaling de famille : Origin = 1 question fermée/LR sous conditions ;
General = ASI + question élargie OU conditions allégées ; Epic = quasi
permanent.

Renvoi : *Lecture des vols, Sens des strates, Lire sous le masque, faveur
de Sokoros.*

### 4.2 Bond & Companion Bricks

Préambule : le compagnon de feat est **un capteur et un angle, jamais un
attaquant** — un second corps offensif est une feature de classe
(Beast Master). La famille vend des yeux ailleurs, et le prix qui va avec.

| Brique | Gabarit | Étalon | Coût |
|---|---|---|---|
| Shared senses | Action ou BA : percevoir par le compagnon ; aveugle/sourd à son corps pendant ce temps | *Find Familiar* | ½ feat à volonté ; ⅓ si 1/repos |
| Telepathic tether | Lien à portée ; impressions (Origin) vs phrases (General) | Familier 100 ft ; feat *Telepathic* (unilatéral) | ⅓ feat ; le contenu coûte plus que la portée |
| Positional rider | Compagnon à 5 ft de la cible : ignorer abri partiel et/ou portée longue | Moitié « abri » de *Sharpshooter* ; anti-modèle Pack Tactics | ½ feat — le compagnon s'expose |
| The bond's price | Stats de familier figées ; rupture du lien = coût écrit | Beast Master (précédent de la perte) | La moitié défensive du budget — non optionnel |

Règles dures par brique :
- **Shared senses** : 3 knobs — fréquence (1/LR → PB/LR → à volonté),
  action requise (action → BA), cécité propre (la retirer = buff notable).
  Plafond General : à volonté + BA.
- **Telepathic tether** : portée par bonds officiels (100 ft → 1 mile →
  8 km) ; le vrai palier de prix est le contenu (impressions = Origin,
  phrases = General, fusion sensorielle = Epic) ; unilatéral vs bilatéral
  est un choix de design.
- **Positional rider** : vendre un **angle de vue**, jamais l'avantage brut
  (Pack Tactics sur un PJ casse la courbe d'attaque) ; le coût est intégré
  (zone de mort) — ne jamais le supprimer par une autre brique du même feat
  (le compagnon intuable = anti-pattern).
- **The bond's price** : clauses écrites dans le feat — mort du compagnon
  (épuisement, perte des bénéfices jusqu'à re-rituel) ET séparation
  prolongée. Un feat de lien sans clause de rupture est incomplet.

Scaling de famille : Origin = sens partagés 1/repos + impressions ;
General = ASI + à volonté + portée + un rider positionnel ; Epic = fusion
permanente, le lien survit à la mort (et c'est un problème).

Renvoi : *Ciel partagé, Serres jumelles, malédiction du Fauconnier comme
clause de rupture exemplaire.*

### 4.3 Debt & Observance Bricks

Préambule : ces régulateurs **remplacent** les patterns de ressource
standard — jamais d'empilement (« 1/LR ET observance » = double taxation
injouable).

| Brique | Gabarit | Étalon | Coût |
|---|---|---|---|
| Observance gate | La ressource ne recharge qu'après un acte accompli avant la fin du prochain repos long | Équivalent 1/LR si l'acte tient dans une journée ordinaire | Neutre si jouable ; nerf déguisé si l'acte est rare |
| Capped inventory | N charges narratives, N = PB (ou plafond fixe si le feat ne doit pas grandir) | Luck Points | Le plafond est la balance |
| Non-gold currency | Bénéfice monnayable hors or (rêves, faveurs, secrets) | Aucun — territoire neuf | Fourchette de valeur obligatoire en Design Notes |
| Debt hook | Le feat naît endetté via le prérequis narratif | Le pacte de warlock comme fiction | Zéro math ; valeur d'accroche |

Règles dures par brique :
- **Observance gate** : l'acte est scénique (pas comptable), vérifiable à
  la table, et le texte précise l'échec (la ressource ne recharge pas,
  point — pas de punition empilée). Si l'observance échoue souvent par
  logistique de campagne, c'est un nerf déguisé : l'assumer ou élargir.
- **Capped inventory** : le contenu de l'inventaire n'a **pas** de valeur
  mécanique (sinon c'est un sac de charges de sort — autre famille) ; un
  jet de rétention scale avec le stock, jamais un DD fixe.
- **Non-gold currency** : les Design Notes fixent l'ordre de grandeur du
  marché — un marché non balisé rend le don gratuit ou cassé.
- **Debt hook** : la dette appartient au MJ, ne s'auto-règle jamais, et
  n'achète **pas** de puissance mécanique — elle achète de la présence.

Scaling de famille : par **gravité**, pas par puissance — Origin : rituel
personnel ; General : engage des tiers ; Epic : le créancier est une
entité et le non-paiement a une mécanique.

Renvoi : *les six observances de Voix de l'Autel, l'inventaire qui gratte
du Voleur de Rêves, la dette des Pirates.*

## 5. Intégrations

- [ ] `plugins/ttrpg-creation/.claude-plugin/plugin.json` : version 1.4.0
- [ ] `.claude-plugin/marketplace.json` : metadata.version 1.4.0
- [ ] `CHANGELOG.md` : entrée 1.4.0 (Ajouts + section « Pourquoi » sur la
      boucle galerie → références)
- [ ] Push + `claude plugin marketplace update` + `claude plugin update`
      (rendre la 1.4.0 disponible, comme pour la 1.3.0)
- Descriptions plugin/marketplace : **inchangées** (pas de nouveau skill ni
  de nouvelle catégorie de contenu)
- READMEs : **inchangés** (le décompte de skills ne bouge pas)
- SKILL.md : **inchangé** (il pointe déjà la bibliothèque)

## 6. Critères de succès

- [ ] Les 3 sections suivent la structure : préambule-règle, tableau
      4 colonnes, détails par brique, scaling de famille, renvoi galerie
- [ ] Chaque brique cite un étalon officiel 2024 (ou déclare « territoire
      neuf » avec l'obligation compensatoire, cas Non-gold currency)
- [ ] Les règles dures sont préservées telles quelles (sortie ambiguë
      obligatoire ; capteur jamais attaquant ; régulateurs non empilables ;
      jet de rétention scalant, jamais de DD fixe)
- [ ] Insertion entre « Magic Bricks » et « Scaling Knobs » ; le fichier
      reste lisible (~240 lignes)
- [ ] Version 1.4.0 cohérente (plugin.json, marketplace.json, CHANGELOG) ;
      `scripts/validate.py` passe ; plugin installé mis à jour

## 7. Hors scope

- Drawback riders / malédictions (choix utilisateur — signature Zarathar)
- Toute modification de SKILL.md, des autres références, des READMEs
- Nouveaux benchmarks dans power-budgets-and-benchmarks.md (les coûts
  indicatifs vivent dans les tableaux de briques)
