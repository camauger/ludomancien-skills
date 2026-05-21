---
skill: monster-creator
plugin: ttrpg-creation
date: 2026-05-21
prompt: |
  Créer un monstre complet D&D 5e 2024 : une entité d'ombre et de pouvoir
  illusoire qui prend possession des objets magiques d'aventuriers pour les
  retourner contre eux. Calibré pour 6 PJ niveau 13 vs 6 instances (Hard).
  Exclusion explicite des actions légendaires/lair/mythiques malgré le tier
  (combat de meute, pas boss solitaire). Voie de victoire mécanique non-DPS
  exigée (libération radiante). Format MM 2024 complet : statblock +
  écologie + tactiques GM + hooks.
why: |
  Exemplaire à deux titres complémentaires. (1) Sur la dimension éditoriale :
  ancrage strict du concept "ombre + illusion" dans une origine cohérente
  (éclats d'un démiplan-miroir effondré) qui informe la mécanique signature
  (Possession d'objet magique). Le statblock structure Possession en
  sous-cas par type d'objet (arme / armure / focus) avec quatre voies de
  libération distinctes — discipline rare dans le homebrew. La cohérence
  sonore (succion humide, fragments de miroir, lumière froide) traverse
  écologie et tactiques GM. (2) Sur la dimension méta-process : cet output
  a aussi révélé un défaut d'arithmétique invisible à l'œil (PV 189 avec
  bonus +108 incohérent avec CON 17 (+3) — implique CON +6), attrapé par
  stat-block-validator dans le pipeline. C'est donc un exemple qui calibre
  à la fois ce que monster-creator produit de bon ET un anti-pattern récurrent
  à surveiller (cf. ajustement à CON 22 dans la version table-ready).
tags: [aberration, fp-11, possession, meute, ombre, voie-de-victoire-radiante, 5e-2024]
edited: false
---

# Le Mire-faim

*Une faim d'ombre qui dévore le moi des objets magiques et retourne leur pouvoir contre celui qui les porte.*

D'abord, on remarque les reflets : dans une lame polie, dans une mare, dans la garde d'un casque, quelque chose oscille qui ne devrait pas y être. Puis la silhouette se déplie depuis cette surface — taille d'un homme courbé, faite de noir liquide et de fragments de miroir suspendus, sans visage sinon une ouverture étroite où passe une lumière froide. Le Mire-faim ne touche pas le sol ; il flotte à hauteur d'épaule, lent et patient, et son regard se pose sans erreur sur ce qui, dans la pièce, irradie de magie.

## Bloc de stats

```
Mire-faim
Aberration Moyenne, Neutre Mauvais

CA      17
PV      189 (18d8 + 108)
Vitesse 0 m, vol 12 m (vol stationnaire, traverse les objets — voir Insubstantialité miroir)

         FOR     DEX     CON     INT     SAG     CHA
        8 (-1) 18 (+4) 17 (+3) 19 (+4) 16 (+3) 22 (+6)

Jets de sauvegarde   CHA +10, INT +8, SAG +7
Compétences          Arcanes +8, Discrétion +8, Perception +7
Résistances          nécrotique, psychique ;
                     contondant, perforant, tranchant des attaques non magiques
Vulnérabilités       radiant
Immunités aux états  agrippé, à terre, charmé, contraint, empoisonné, paralysé, pétrifié
Sens                 vision dans le noir 36 m, vision véritable 9 m, Perception passive 17
Langues              commun, profond, parler des profondeurs ; télépathie 18 m
FP                   11 (PX 7 200) ; BM +4
```

**Traits**

***Insubstantialité miroir.*** Le Mire-faim traverse créatures et objets comme un terrain difficile. Il subit 1d10 dégâts de force par 1,50 m parcourus dans un objet ou une créature. Tant qu'il occupe un objet magique via *Possession*, cet effet ne s'applique pas.

***Sensorium magique.*** Le Mire-faim perçoit en permanence l'emplacement, l'école et la rareté approximative de chaque objet magique dans un rayon de 36 m. Cet effet équivaut à *détection de la magie* permanent et ignore la couverture inférieure à 1 m de plomb.

***Résonance fragile.*** Quand le Mire-faim subit des dégâts radiants, il ne peut pas activer *Possession* ni utiliser sa réaction jusqu'au début de son prochain tour. Si l'attaque inflige 30 dégâts radiants ou plus, et qu'il est en train d'occuper un objet possédé, la *Possession* prend fin immédiatement.

**Actions**

***Attaque multiple.*** Le Mire-faim fait deux attaques de *Caresse d'érosion*, OU il utilise *Possession* puis fait une attaque de *Caresse d'érosion* si Possession ne réussit pas.

***Caresse d'érosion.*** *Attaque de sort au corps-à-corps :* +10 au toucher, allonge 1,50 m, une cible. *Touché :* 24 (4d8 + 6) dégâts nécrotiques. Si la cible porte au moins un objet magique, elle subit 9 (2d8) dégâts psychiques supplémentaires et a Désavantage à son prochain jet de Charisme avant la fin de son prochain tour.

***Possession (Recharge 5-6).*** Le Mire-faim désigne un objet magique transporté ou équipé par une créature qu'il peut percevoir dans un rayon de 9 m. Le porteur fait un jet de sauvegarde de Charisme DC 18. En cas d'échec, l'objet est *possédé* pendant 1 minute, et le Mire-faim disparaît dans l'objet : il devient un effet, n'est plus une créature ciblable, et ne peut être affecté que via l'objet. Tant que la Possession dure :

- **Si l'objet est une arme :** au début de chaque tour du porteur, l'arme tente de l'attaquer. Le porteur fait un jet de sauvegarde de Force ou de Dextérité (au choix) DC 18 ; en cas d'échec, il subit 27 (4d10 + 6) dégâts du type de l'arme (psychique si l'arme n'inflige normalement aucun dégât). Le porteur ne peut pas attaquer le Mire-faim avec cet objet.
- **Si l'objet est une armure ou un bouclier :** la CA du porteur diminue de 4. La première attaque qui le touche chaque round est un coup critique automatique.
- **Si l'objet est un focus magique, sceptre, baguette, anneau, amulette ou objet merveilleux :** le porteur ne peut pas lancer de sorts de niveau 1 ou supérieur. S'il en tente un, il subit 9 (2d8) dégâts psychiques et le sort échoue (l'emplacement de sort est perdu).

**Libération de la Possession.** La Possession prend fin si l'une des conditions suivantes survient :

- Le porteur ou une créature à 1,50 m réussit un jet de Charisme DC 18 (action) ;
- L'objet subit 30 dégâts radiants ou plus en une seule attaque (la moitié de ces dégâts traverse au porteur) ;
- Le porteur lâche l'objet ET aucune créature ne s'approche à moins de 9 m de l'objet pendant 1 round complet (l'objet devient inerte ; le Mire-faim peut re-cibler ce même objet plus tard) ;
- Un sort de *dissipation de la magie* lancé de niveau 3 ou supérieur réussit (test de caractéristique d'incantation DC 18 si le sort est lancé à un niveau inférieur).

Quand la Possession prend fin, le Mire-faim émerge à moins de 1,50 m de l'objet et est *Sonné* jusqu'à la fin de son prochain tour.

**Action bonus**

***Pas d'ombre.*** Le Mire-faim se téléporte jusqu'à 9 m vers un objet magique qu'il perçoit. Il apparaît à 1,50 m de l'objet. Il ne peut pas utiliser cette action bonus durant le tour où il libère une Possession.

**Réaction**

***Phase miroir.*** Quand une attaque qui n'est pas radiante touche le Mire-faim, il peut imposer le Désavantage à cette attaque ; si elle rate à cause de cela, l'attaquant subit 9 (2d8) dégâts psychiques. Inutilisable dans une lumière vive ou si le Mire-faim a déjà subi des dégâts radiants durant ce round.

---

## Écologie

### Origine et nature

Les Mire-faim sont des éclats survivants d'un démiplan-miroir effondré — un de ces espaces oniriques que de très anciens enchanteurs créaient pour stocker des reflets, des doubles, et des illusions assez stables pour vivre. Quand un tel démiplan meurt (l'enchanteur le néglige, ou il est rompu par un sort cataclysmique), ses fragments ne se dissipent pas : ils gardent un appétit, une faim de "soi" à occuper. Privés de leur source, ils dérivent vers le plan matériel et y reconnaissent dans les objets magiques quelque chose qui ressemble à ce qu'ils étaient — des réceptacles de pouvoir conscient, un endroit où s'incarner.

Ils ne sont ni morts-vivants ni démons. Ce sont des absences qui ont gardé la forme de la chose absente.

### Habitat

Les Mire-faim apparaissent partout où le plan matériel est devenu poreux à la magie ancienne : tombes de héros enterrés avec leur équipement, ruines de tours de mages, champs de bataille où une armée enchantée s'est éteinte sans qu'on récupère les corps. Plus rarement, ils s'invitent dans les marchés magiques d'envergure (les bazars d'Eldosse, les caravanes des Vendeurs du Sceau) où la densité d'objets magiques crée une lumière noire qu'ils sentent à plusieurs kilomètres.

### Comportement

Ils chassent en meutes de 4 à 8 individus reliés par une télépathie commune à courte portée. Cette télépathie n'est pas hiérarchique : il n'y a pas de chef. Le plus *vieux* — celui qui a hébergé le plus d'objets — guide par préséance, mais la meute fonctionne plus comme une faim partagée que comme une famille. Quand une cible portant un objet magique rare entre dans leur domaine sensoriel, la meute converge : chaque Mire-faim choisit un porteur différent, et l'attaque devient une chorégraphie où chacun travaille son propre objet sans interférer avec les autres.

Une meute privée d'objets magiques pendant plus d'une saison entre en torpeur : les individus se figent dans un miroir poli ou une eau dormante et y attendent. Cette torpeur peut durer des décennies.

### Régime

Les Mire-faim ne mangent rien d'organique. Ils métabolisent l'aura magique des objets qu'ils occupent : chaque jour de Possession ininterrompue laisse l'objet plus terne, plus froid, et grève l'une de ses propriétés mineures (un +1 devient un +0, un objet à charges perd 1 charge maximum, etc.). Cette dégradation est réversible — un sort de *restauration majeure* lancé sur l'objet le purifie — mais les marchands d'objets magiques savent reconnaître la "résonance d'ombre" et déprécient toujours un objet qui en porte la trace.

### Signes de présence

- Les reflets dans les surfaces polies (lames, casques, mares) **frémissent quand rien ne devrait les agiter**, et ne reflètent pas les bonnes formes.
- Les objets magiques portés à proximité deviennent **légèrement froids et plus lourds**, comme s'ils gagnaient en densité.
- De petits **graviers d'ombre** apparaissent dans les coins de la pièce ou aux pieds des statues — fragments noirs qui oscillent entre la solidité du caillou et la fumée.
- Les sorts à concentration vacillent à 18 m d'un Mire-faim : DC du jet de concentration **+2**.
- Les **animaux familiers et bêtes domestiques refusent d'approcher** de toute personne portant un objet magique dans la zone affectée.

### Relations

**Prédateurs.** Les illithides les détestent (toute conscience qu'ils ne contrôlent pas est une cible) et les chassent quand l'occasion se présente. Les créatures pleinement radiantes (planétaires, dévas, certains dragons d'or) les dissipent presque par leur seule présence.

**Proies.** Aventuriers, mages itinérants, ordres chevaleresques (les armures bénies sont des proies de choix), prêtres en pèlerinage portant des reliques.

**Symbioses.** Certaines liches très anciennes ont appris à "élever" une meute de Mire-faim autour de leur phylactère : la meute disperse les héros venus la chasser, et la lich nourrit la meute en achetant régulièrement des objets magiques mineurs qu'elle dispose en appât.

### Trésor

Aucun. Mais leur passage laisse dans les objets magiques une "résonance d'ombre" détectable par les mages enquêteurs, qui peut être suivie comme une piste pendant 7 à 30 jours.

---

## Faire vivre le Mire-faim à la table

**Ouverture.** Au tour 1, chaque Mire-faim choisit un PJ différent et tente *Possession* sur l'objet magique de plus haute rareté visible chez lui (focus du caster > arme +X du combattant > armure bénie du paladin). Vise d'abord les casters : neutraliser un focus arrête une classe entière, ce qui change le combat plus qu'une arme bloquée.

**Rounds 2-3.** Une fois la Possession placée, le Mire-faim *est* l'objet — il n'a pas à se défendre, et la faim continue. Les Mire-faim qui ont raté leur Possession harcèlent en *Caresse d'érosion* en évitant le corps-à-corps prolongé (Insubstantialité miroir leur coûte cher).

**Rounds 4+.** Si la meute a réussi 4-6 Possessions, les Mire-faim restent dormants dans les objets pendant que les "armes possédées" font le travail. Cela crée un moment de table très particulier : les PJ se battent contre leur propre matos.

**Retraite.** Si la moitié de la meute est détruite, les survivants utilisent leurs derniers tours pour téléporter *Pas d'ombre* vers leur objet le plus actif et tenter d'emmener cet objet (et son porteur, donc) hors du champ de bataille — vers un miroir, une mare, ou la prochaine pièce. Une meute en fuite avec un objet magique est un *hook* de poursuite en soi.

**Anti-pattern.** Ne jamais utiliser *Caresse d'érosion* contre un PJ déjà sous Possession — c'est gaspiller du DPR. Le rôle du Mire-faim n'est pas de tuer ; c'est de retourner la table. Si tous les Mire-faim ratent leur recharge en même temps, la rencontre devient soudain triviale : le MJ peut alors faire émerger un septième Mire-faim plus vieux, attiré par la concentration de signal, pour rééquilibrer.

---

## Accroches de table

1. **Le Reliquaire de Vorrann.** Un ordre chevaleresque rapporte que ses reliques deviennent "défectueuses" — trois chevaliers blessés par leur propre arme lors de duels d'honneur, deux étendards qui ont étouffé leur porteur. L'ordre offre 800 po pour résoudre le problème. Mais leur grande-prêtresse est déjà sous résonance d'ombre, et son anneau de commandement décide pour elle ce qu'elle doit révéler aux PJ et ce qu'elle doit cacher.

2. **La Vente aux enchères de la maison Astaer.** Une vente publique d'objets magiques tourne au massacre : les acquéreurs s'entretuent sans raison apparente trois jours après l'achat. Quand le groupe enquête, ils découvrent que tous les objets vendus provenaient d'une même collection — celle du mage Astaer, dont le démiplan-miroir s'est effondré il y a 70 ans. Quelqu'un est en train d'écouler systématiquement les éclats, et il faut découvrir qui (et pourquoi).

3. **Le Rêve récurrent.** Un PJ portant un objet magique-signature commence à rêver d'un endroit précis — une combe avec une mare noire — et de quelque chose qui l'y attend, déjà. Le rêve revient toutes les nuits, plus net à chaque fois. S'il y va, il déclenche la meute qui l'a marqué comme prochaine proie. S'il n'y va pas, la meute viendra à lui dans deux semaines. Le donjon à explorer n'est pas un lieu : c'est une décision.

---

**Notes mécaniques pour l'encounter source :**
- 6 Mire-faim × FP 11 = 43 200 PX bruts → ajusté pour groupe de 6 PJ niveau 13, c'est dans la zone *Hard* (Difficile) du DMG 2024.
- Vérifie avant la rencontre quel objet magique-signature chaque PJ porte et choisis la cible de Possession idéale par PJ ; note-le sur ton écran de MJ pour ne pas hésiter au tour 1.
- Prévois un "moment radiant" accessible : un autel à bénir, un sort de lumière du jour préparé en réserve, ou un PNJ allié avec *flamme sacrée*. Sans voie radiante évidente, la rencontre peut basculer en frustration totale.
- Si la rencontre vire trop facilement en faveur des PJ (mauvais rolls sur Possession), le 7e Mire-faim "ancien" attiré par le tumulte est une excellente carte en réserve.
