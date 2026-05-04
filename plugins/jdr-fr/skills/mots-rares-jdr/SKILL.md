---
name: mots-rares-jdr
description: Génère des articles de mots rares français pour le glossaire jeuxderole.org. Utiliser quand l'utilisateur demande de créer un article de mot rare, un mot littéraire/archaïque pour le JDR, ou du contenu pour jeuxderole.org/mots-rares. Produit une définition étymologique, des inspirations ludiques par genre (médiéval-fantastique, SF, horreur/gothique, contemporain), des mécaniques de table, et des pistes d'approfondissement.
---

# Générateur d'articles — Mots rares pour le JDR

Génère des articles pour la section "Mots rares" du glossaire jeuxderole.org. Ces articles présentent des mots français littéraires, archaïques ou savants avec des applications concrètes en jeu de rôle.

## Format de sortie

Produire du Markdown structuré prêt à intégrer dans le CMS du site.

### Structure obligatoire

```markdown
# Mot rare : *[Mot]*

**Accroche** : *« [Citation évocatrice, poétique, ~10 mots] »*

---

## Définition

* **Sens principal** : [Définition concise et précise]
* **Étymologie** : [Origine grecque/latine/autre + composition]
* **Nuances** : [Registre, connotations, synonymes proches]

---

## Inspirations ludiques

### 1. Médiéval-fantastique

* **Artefact / Lieu / Créature** : [Exemple concret utilisant le mot]
* **Accroches rapides** :
  + Nom d'artefact/lieu : *[Nom évocateur]*
  + Pouvoir ou effet : *[Description mécanique/narrative]*
  + Intrigue liée : *[Amorce de scénario en une phrase]*

### 2. Science-fiction

* **Technologie / Monde / IA** : [Exemple concret]
* Exemple : *[Phrase d'ambiance ou description]*

### 3. Horreur / Gothique

* **Atmosphère / Rituel / Malédiction** : [Exemple concret]
* Exemple : *[Phrase d'ambiance]*

### 4. Contemporain / Post-apo / Autres genres

* **Usage narratif** : [Exemple concret]
* Exemple : *[Phrase d'ambiance]*

---

## À la table

* **Mini-mécanique** : [Règle simple, bonus/malus, jet spécial]
* **Question aux joueurs** : *« [Question ouverte pour engagement] »*
* **Mini-intrigue en 2 phrases** : *[Amorce de quête utilisant le mot]*

---

## Pour aller plus loin

* **Mots associés** : *[3-4 mots thématiquement liés]*
* **Référence** : [Source historique, littéraire ou culturelle]
* **Invitation** : *« [Question ouverte au lecteur] »*
```

## Directives de rédaction

### Ton et style
- Registre : cultivé mais accessible, jamais pédant
- Accroches : poétiques, évocatrices, mémorables
- Inspirations : concrètes et immédiatement utilisables en partie

### Sélection des mots
Privilégier les mots qui sont :
- Rares mais prononçables (éviter l'obscurité gratuite)
- Évocateurs visuellement ou phonétiquement
- Polyvalents (applicables à plusieurs genres)
- Français authentiques (pas de néologismes)

### Qualité des inspirations
Chaque inspiration doit :
- Être spécifique au genre concerné
- Proposer quelque chose d'actionnable (nom, lieu, mécanisme)
- Stimuler l'imagination sans imposer

### Mini-mécaniques
- Simples et génériques (compatibles D&D 5e, PbtA, etc.)
- Bonus/malus conditionnels ou jets spéciaux
- Éviter les mécaniques trop complexes

## Exemple complet

Voir `references/exemple-selenien.md` pour un article de référence.

## Métadonnées pour le CMS

L'article doit pouvoir générer ces métadonnées :
- **Titre** : Le mot
- **Description courte** : La définition (sens principal)
- **Tags** : `rare`, `mots-rares`
- **Date** : Date de génération

## Processus de génération

1. Vérifier que le mot est authentiquement français et rare
2. Rechercher l'étymologie précise
3. Créer une accroche poétique originale
4. Développer 4 inspirations variées par genre
5. Concevoir une mini-mécanique élégante
6. Proposer des mots associés thématiquement cohérents
