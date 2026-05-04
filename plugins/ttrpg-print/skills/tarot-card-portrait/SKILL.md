---
name: tarot-card-portrait
description: >
  Génère des prompts Midjourney complets pour illustrer un personnage TTRPG (ou original) sous forme
  de carte de tarot verticale et ornementale. Utiliser quand l'utilisateur veut créer une carte de tarot
  pour un personnage, illustrer un PNJ ou personnage joueur sous forme de tarot, assigner un arcane majeur
  à un personnage ou concevoir une illustration de tarot érotique/dark fantasy pour la marque Fantasy Vixens.
  Déclenche aussi sur : "fais-moi une carte de tarot pour [personnage]", "quel arcane représente [PNJ]",
  "génère le prompt Midjourney pour la carte de [personnage]", "illustre [personnage] en style tarot".
---

# Tarot Card Portrait — Skill

Génère un prompt Midjourney optimisé pour illustrer un personnage sous forme de **carte de tarot ornementale**
(format vertical, bordure illustrée, composition centrée, symbolisme de l'arcane intégré).

Compatible avec : Fantasy Vixens (Courtisanes de Velnaris), Zarathar, personnages génériques D&D 5e, PNJs de campagne.

---

## PROCESSUS EN 4 ÉTAPES

### Étape 1 — Extraire le profil du personnage

Collecter ces éléments depuis la fiche du personnage ou la description fournie :

| Donnée | Source |
|---|---|
| **Rôle / archétype** | classe, métier, statut social |
| **Traits physiques distinctifs** | couleur cheveux, morphologie, race/espèce, marqueurs visuels |
| **Émotion dominante** | ce que le personnage dégage, pas ce qu'il ressent en secret |
| **Objet emblématique** | arme, accessoire, symbole associé au personnage |
| **Environnement naturel** | là où on le trouve habituellement |
| **Ton narratif** | héroïque / tragique / séduisant / menaçant / mystérieux |

Si ces données ne sont pas toutes fournies, inférer à partir de ce qui est disponible. Ne pas demander des informations si l'essentiel est présent.

---

### Étape 2 — Assigner ou confirmer l'arcane majeur

#### Attribution automatique par archétype

Si l'arcane n'est pas précisé, utiliser cette correspondance :

| Archétype du personnage | Arcane suggéré |
|---|---|
| Débutant, voyageur impulsif, innocent | 0 — Le Mat |
| Manipulateur, illusionniste, marchand habile | 1 — Le Bateleur |
| Oracle, bibliothécaire, gardienne de secrets | 2 — La Papesse |
| Matriarche, déesse de la fertilité, mère puissante | 3 — L'Impératrice |
| Souverain, chef militaire, autorité absolue | 4 — L'Empereur |
| Prêtre, initiatrice, maîtresse de rites | 5 — Le Pape |
| Personnage au cœur d'un dilemme amoureux ou moral | 6 — L'Amoureux |
| Guerrier en route vers la victoire, conquérant | 7 — Le Chariot |
| Dompteur intérieur, soignant, calme sous pression | 8 — La Force |
| Sage reclus, chercheur de vérité, ascète | 9 — L'Ermite |
| Joueur, opportuniste, figure du destin | 10 — La Roue de Fortune |
| Juge, arbitre, figure de la loi | 11 — La Justice |
| Martyr, prisonnier volontaire, inversé du monde | 12 — Le Pendu |
| Personnage en transformation radicale, fin d'un cycle | 13 — La Mort |
| Alchimiste, diplomate, figure d'équilibre | 14 — La Tempérance |
| Figure du vice, de l'addiction, de l'ombre désirée | 15 — Le Diable |
| Brisé par la révélation, rebelle, après la catastrophe | 16 — La Maison Dieu |
| Guérisseur, porteur d'espoir, figure de renouveau | 17 — L'Étoile |
| Illusionniste, rêveur, personnage double ou ambigu | 18 — La Lune |
| Figure de joie pure, enfant-soleil, victoire simple | 19 — Le Soleil |
| Ressuscité, appelé, personnage en réveil | 20 — Le Jugement |
| Figure d'accomplissement, de totalité, de clôture | 21 — Le Monde |

---

### Étape 3 — Assembler le prompt (grammaire 7 modules)

Construire le prompt dans cet ordre exact :

```
[MODULE 1 : FORMAT] [MODULE 2 : STYLE] [MODULE 3 : SUJET] [MODULE 4 : POSE] [MODULE 5 : DISSIMULATION/ÉROTISME] [MODULE 6 : LUMIÈRE] [MODULE 7 : DÉCOR + BORDURE] [PARAMÈTRES TECHNIQUES]
```

#### MODULE 1 — Format (toujours identique)
```
tarot card illustration vertical composition,
```

#### MODULE 2 — Style artistique
Choisir **une référence principale + une technique** dans cette banque :

| Registre | Références recommandées |
|---|---|
| Art Nouveau organique | Alphonse Mucha, Jan Toorop, Eugène Grasset |
| Symbolisme onirique | Franz von Stuck, Fernand Khnopff, Odilon Redon |
| Fantastique classique | John William Waterhouse, Edward Burne-Jones |
| BD européenne adulte | Milo Manara, Moebius, Serpieri |
| Art Déco / architectural | Erté, Tamara de Lempicka |
| Klimt / ornemental | Gustav Klimt (motifs dorés + corps) |
| Dark fantasy contemporain | Boris Vallejo (puissance), Julie Bell (grâce) |

**Formule** : `[style mouvement] illustration in the manner of [artiste], [caractéristique technique distinctive],`

**Exemples** :
- `Art Nouveau illustration in the manner of Alphonse Mucha, fluid botanical linework,`
- `Symbolist fantasy illustration evoking Franz von Stuck, atmospheric deep-shadow rendering,`
- `painterly European fantasy illustration in the manner of Waterhouse, golden-hour luminous brushwork,`
- `dark fantasy graphic novel illustration in the style of Milo Manara, clean expressive ink lines,`

#### MODULE 3 — Sujet (personnage)
Décrire avec précision : **race/espèce** + **rôle lisible visuellement** + **traits physiques clés** + **vêtement/état vestimentaire** + **expression/qualité émotionnelle**.

**Formule** : `[race/espèce] [rôle] [description physique], [état vestimentaire artistique], [expression ou qualité émotionnelle distinctive],`

**Principes** :
- Éviter "allure" et "aura" — trop vagues
- Nommer une émotion spécifique : *"gaze of someone who has never needed to ask twice"*, *"vulnerable courage of being truly seen"*
- L'état vestimentaire : silk robe slipping from shoulder / ceremonial robes layered over ritual jewelry / armor of ceremony not combat / silk caught mid-motion

**Exemples** :
- `elegant tiefling courtesan with amber slit-pupil eyes and deep gold skin, crimson silk robe loosely draped revealing collarbones, knowing smile of someone who already knows your next move,`
- `scarred half-orc warrior woman, leather armor removed to the waist showing muscled shoulders, expression of vulnerable exhaustion contradicting her fierce reputation,`
- `silver-haired elven arcanist, ceremonial robes over seven-strand copper necklace, ceremonial bearing masking quiet grief,`

#### MODULE 4 — Pose
Choisir une pose en accord avec l'énergie de l'arcane :

| Énergie arcane | Poses adaptées |
|---|---|
| Autorité / Maîtrise (Emp., Pape, Justice) | seated with perfect composed symmetry / standing weight-shifted commanding stance |
| Mystère / Intériorité (Papesse, Ermite, Lune) | reclining close-up head tilted / half-profile gaze directed inward |
| Mouvement / Victoire (Chariot, Monde, Jugement) | mid-stride caught in motion / rising from surface arms beginning to lift |
| Abandon / Vulnérabilité (Pendu, Étoile, Mort) | draped backward over surface / side-lying pose tracing body arc / kneeling beside water |
| Invitation / Désir (Diable, Bateleur, Force) | leaning forward subtle arch in the back / outstretched hand invitation gesture |
| Joie / Plénitude (Soleil, Impératrice, Monde) | slow stretch with raised arms / reclining stretch with extended legs head tilted back |

**Formule** : `[description de la pose capturée],`

#### MODULE 5 — Dissimulation / Érotisme (ajuster selon le registre)

**Trois registres :**

**A. Sage (pour usage général, réseaux sociaux, DriveThruRPG covers)**
Suggestion uniquement via composition et tissu, sans ambiguïté érotique.
```
fabric artfully draped concealing while suggesting form, strategic composition focusing on face and hands,
```

**B. Sensuel (pour Fantasy Vixens — intermédiaire)**
Suggestion érotique claire mais artistiquement légitimée.
```
silk robe caught mid-fall revealing curve of shoulder and collarbones while chiaroscuro shadow conceals the rest, parted lips and heavy-lidded gaze of deliberate invitation,
```

**C. Explicitement suggestif (Fantasy Vixens — maximum)**
Nudité partielle artistiquement encadrée, corps révélé via lumière/ombre/tissu en mouvement.
```
silk unraveling from form in sculptural folds suggesting rather than concealing, warm light defining curve of bare shoulder and hip while strategic shadow preserves artistic tension, parted lips and yielding expression,
```

#### MODULE 6 — Lumière
La lumière est l'outil principal de mood et de légitimité artistique.

| Atmosphère | Configuration lumière |
|---|---|
| Intime / passionné | warm amber candlelight from below, chiaroscuro with strategic shadows |
| Mystérieux / nocturne | cool moonlight through gauze creating silver silhouette |
| Divin / révélation | single shaft of golden light descending from above |
| Onirique / double | dual light sources each casting different color temperature, meeting line down center |
| Dramatique / théâtral | dramatic upward candlelight casting theatrical shadows |
| Solaire / joyeux | cinematic warm backlighting creating luminous halo through translucent fabric |

**Formule** : `[configuration lumière principale], [effet secondaire ou couleur],`

#### MODULE 7 — Décor + Bordure
Combiner **environnement spécifique à l'arcane** + **motifs ornementaux de la bordure**.

**Environnements Velnaris par arcane :**

| Arcane | Environnement Velnaris |
|---|---|
| Le Mat | marble threshold of a Velnaris pleasure house, scattered rose petals |
| Le Bateleur | opulent consulting chamber with gilded walls and velvet-draped table |
| La Papesse | Velnaris secret library, floor-to-ceiling scrolls dissolving in shadow |
| L'Impératrice | window alcove of the Velnaris Maison Mère, climbing rose garden visible beyond |
| L'Empereur | marble audience hall with carved stone columns |
| Le Pape | Velnaris temple interior, incense coiling upward |
| L'Amoureux | crossroads chamber with twin carved doorways |
| Le Chariot | night streets of Velnaris, architecture streaming past in soft focus |
| La Force | Velnaris pleasure-garden interior, climbing flowering vines |
| L'Ermite | private cell with narrow window showing distant city lights |
| La Roue | Velnaris gambling house, shadowed fortune-seekers blurred in background |
| La Justice | High Court antechamber, carved justice reliefs in shadow |
| Le Pendu | boudoir with floor candelabras |
| La Mort | ritual chamber, death's-head moth symbolism in carved walls |
| La Tempérance | alchemical study, glass vessels and precious metals |
| Le Diable | shadow-temple interior, dark incense coils |
| La Maison Dieu | tower chamber, burst window and falling masonry frozen |
| L'Étoile | rooftop garden pool open to star-crowded night sky |
| La Lune | mirror-hall, multiple fractured reflections multiplying in darkness |
| Le Soleil | sun-court interior garden, flowering abundance |
| Le Jugement | ritual bath chamber, marble walls and carved seraphim |
| Le Monde | grand ceremonial hall, all factions gathered in shadowed background |

**Pour setting non-Velnaris** : remplacer par l'environnement naturel du personnage.

**Motifs de bordure par arcane :**

| Arcane | Motifs bordure |
|---|---|
| 0, 3, 8, 17, 19 | botanical / floral art nouveau flourishes |
| 1, 4, 11 | geometric / architectural gothic flourishes |
| 2, 5, 9 | ornate austere art nouveau lines |
| 6, 14, 21 | water and flame motifs alternating |
| 7, 10, 16 | swirling kinetic ornamental background |
| 12, 13, 15 | gothic skull-and-peony or shadow-vine flourishes |
| 18, 20 | wave and starlight patterns |

**Formule** : `[environnement du personnage ou Velnaris], ornate tarot card border with [motifs bordure],`

---

### Étape 4 — Ajouter les paramètres techniques

```
--ar 2:3 --stylize [VALEUR] --v 7
```

**Choisir le `--stylize` selon l'effet voulu :**

| Valeur | Effet | Utiliser pour |
|---|---|---|
| `--s 120` | Fidèle, photographique | Portraits réalistes, armures détaillées |
| `--s 150` | Équilibré | Cas général, personnages fantasy |
| `--s 175` | Artistique standard | Tarot Velnaris, dark fantasy sensuel |
| `--s 190` | Très interprétatif | Cartes oniriques (Lune, Pendu, Mort) |
| `--s 200` | Maximum artistique | Filtre-safe pour contenu adulte suggestif |

**Règle générale** : plus la carte est onirique ou sensuelle, plus `--stylize` monte.

---

## OBJETS SYMBOLIQUES PAR ARCANE

Intégrer ces objets dans la description du personnage ou du décor :

| Arcane | Objet symbolique à intégrer |
|---|---|
| 0 | small bundle tied to a walking staff, a white flower at their feet |
| 1 | jeweled wand or implement held above a draped table |
| 2 | ancient tome resting on her lap, diaphanous veil across her face |
| 3 | crown of living flowers, scepter, wheat sheaf motif |
| 4 | gold balance-scale brooch or emblem, stone throne |
| 5 | raised teaching hand, two-candelabra ritual setup |
| 6 | two hands reaching from outside frame (firelight / shadow) |
| 7 | sphinx or horse motif suggested in background, laurel crown |
| 8 | shadow-beast barely suggested at frame edge |
| 9 | oil lantern as only warm light source in the frame |
| 10 | large turning wheel integrated into background architecture |
| 11 | held scales or scale-brooch at the throat, sword leaning in shadow |
| 12 | T-bar suspension or curved chaise acting as inversion device |
| 13 | death's-head moth, chrysalis, unraveling silk cocoon |
| 14 | two crystal vessels, impossible luminous stream between them |
| 15 | chain jewelry deliberately chosen as adornment |
| 16 | scattered jewelry orbiting as debris, lightning motif |
| 17 | reflecting pool, scattered stars visible above, two vessels |
| 18 | ornate mirror, fractured reflections, crawfish in water |
| 19 | sunburst crown or sunlight halo, sunflowers at frame edge |
| 20 | water surface, floating water lilies, divine light descending |
| 21 | laurel wreath oval integrated into composition, four corner emblems |

---

## FORMAT DE SORTIE

Produire dans cet ordre :

1. **Arcane assigné** + justification en 1 ligne
2. **Prompt complet** (copier-coller ready)
3. **Note de dissimulation** : registre choisi (Sage / Sensuel / Suggestif) + raison
4. **Variations suggérées** : 1–2 ajustements alternatifs rapides (ex. changer artiste de référence, modifier `--stylize`)

---

## EXEMPLES COMPLETS

### Exemple A — Courtisane de Velnaris (Registre Sensuel)

**Input** : *"Seraya, courtisane tiefling aux yeux dorés, spécialiste en manipulation émotionnelle, toujours en soie rouge"*

**Arcane** : 15 — Le Diable (figure du désir, du lien délibéré)

**Prompt** :
```
tarot card illustration vertical composition, dark fantasy graphic novel illustration in the style of Milo Manara, clean expressive ink lines with shadow-dominant composition, elegant tiefling courtesan with golden slit-pupil eyes and garnet-red small horns, elaborate chain jewelry worn as garment over deep-plunge crimson silk — the chains ornamental and deliberately chosen, leaning forward with slow teasing gesture that invites and ensnares, heavy-lidded gaze of absolute invitation combined with the knowledge that she holds the key, smoky dramatic chiaroscuro with deep shadow consuming most of her form while warm light falls only on face, throat, and extended hand, Velnaris shadow-temple interior with dark incense coils and subtle watching presences in the darkness, ornate tarot card border with gothic shadow-vine flourishes --ar 2:3 --stylize 185 --v 7
```

**Note** : Registre Sensuel — invitation érotique lisible mais corps non révélé, chains-as-garment = suggestion sans nudité.

**Variations** :
- Remplacer Manara → Klimt pour version plus ornementale/flat
- `--stylize 200` si le filtre Midjourney résiste

---

### Exemple B — PNJ guerrier (Registre Sage)

**Input** : *"Aldric, vieux chevalier désabusé, porte une armure fissurée, regard d'homme qui a trop vu"*

**Arcane** : 12 — Le Pendu (le sacrifice consenti, la perspective inversée)

**Prompt** :
```
tarot card illustration vertical composition, Symbolist fantasy illustration evoking Fernand Khnopff, atmospheric deep-shadow rendering with inversion motifs, weathered human knight in cracked plate armor partially removed to the shoulders, draped backward over a stone ledge in an inverted arc, expression of exhausted transcendence — beyond fear, beyond regret, eyes open and directed upward, fabric artfully draped concealing while suggesting form beneath, single warm torch-light from below illuminating the cracked armor and lined face, stone dungeon antechamber with a narrow slit window showing moonlight above, ornate tarot card border with austere gothic vine lines --ar 2:3 --stylize 165 --v 7
```

**Note** : Registre Sage — composition centrée sur visage et armure, aucune ambiguïté érotique.

**Variations** :
- Ajouter `--chaos 15` pour variations de composition plus dynamiques
- Style Waterhouse au lieu de Khnopff pour version moins sombre

---

## CHECKLIST QUALITÉ

Avant de livrer le prompt, vérifier :

- [ ] Référence artiste précise (pas juste "art nouveau")
- [ ] Objet symbolique de l'arcane présent (dans sujet ou décor)
- [ ] Environnement spécifique (pas "fantasy background")
- [ ] Stratégie de dissimulation explicitée (lumière, tissu, composition)
- [ ] Émotion nommée avec précision (pas "allure" ou "aura")
- [ ] Paramètres `--ar 2:3 --stylize [X] --v 7` présents
- [ ] Mot "erotic" absent du prompt (remplacé par légitimité artistique)
- [ ] Cohérence entre registre (Sage/Sensuel/Suggestif) et usage déclaré

---

## NOTES TECHNIQUES MIDJOURNEY v7

- `--v 7` : version actuelle — meilleure cohérence anatomique et textile
- `--stylize` : contrôle l'interprétation artistique (50–1000, recommandé 150–200 pour ce style)
- `--chaos [0-100]` : ajouter si on veut des variations de composition (15–25 pour tarot)
- `--ar 2:3` : format portrait standard carte de tarot
- Éviter `--no` (negative prompts) sauf si résultat systématiquement mauvais
- Le mot "erotic" dans les prompts Midjourney v7 peut déclencher des filtres → toujours remplacer par légitimité artistique (références classiques, qualité muséale)
