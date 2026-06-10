# feat-effect-library Expansion Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Ajouter trois familles de briques (Information / Bond & Companion / Debt & Observance) à `feat-effect-library.md` et publier ttrpg-creation 1.4.0.

**Architecture:** Une seule référence modifiée (insertion de 3 sections H2 entre « Magic Bricks » et « Scaling Knobs »), bump MINOR des deux manifests, entrée CHANGELOG, release (push + update marketplace/plugin installés). Aucun autre fichier ne bouge.

**Tech Stack:** Markdown, JSON. Vérifications : `scripts/validate.py`, parse JSON, Grep structurel.

**Spec (contenu normatif complet) :** `docs/superpowers/specs/2026-06-10-feat-effect-library-expansion-design.md` — le §4 contient tableaux, règles dures et scaling de chaque famille, **validés mot pour mot**. Les sections s'écrivent en **anglais** (langue du fichier existant), en traduisant fidèlement le §4 ; les termes de jeu restent en vocabulaire 2024 officiel (Long Rest, Proficiency Bonus, weal/woe…).

---

### Task 1: Les 3 sections dans `feat-effect-library.md`

**Files:**
- Modify: `plugins/ttrpg-creation/skills/feat-creator/references/feat-effect-library.md` (insertion entre la fin de « ## Magic Bricks » et « ## Scaling Knobs — One Concept, Three Power Levels »)

- [ ] **Step 1 : Écrire les 3 sections** (~110–130 lignes au total), dans cet ordre et avec cette structure par section — contenu = spec §4.1, §4.2, §4.3 traduit en anglais :

```markdown
## Information Bricks

(préambule : questions fermées par repos, 1 closed question/LR ≈ ½ feat)

| Brick | Mechanical template | Official benchmark | Indicative cost |
(4 lignes : Closed oracle / Detection at range / Intent reading / Diagnostic
 — reprendre exactement le tableau spec §4.1)

(détails par brique : les 4 blocs de règles dures de §4.1 — leviers du
 closed oracle avec sortie ambiguë OBLIGATOIRE, catégorie nommée et étroite,
 fait défini d'avance + jamais de DD fixe, plafond du diagnostic)

(ligne de scaling de famille + renvoi)
*Illustrations: see `examples/feat-creator-dons-zarathar.md` (Lecture des
vols, Sens des strates, Lire sous le masque, Sokoros's favor).*

## Bond & Companion Bricks

(préambule : a sensor and an angle, never an attacker)
| Brick | ... | (4 lignes : Shared senses / Telepathic tether /
 Positional rider / The bond's price — tableau spec §4.2)
(détails : 3 knobs des shared senses, paliers du tether portée vs contenu,
 angle de vue jamais l'avantage brut + compagnon intuable = anti-pattern,
 clauses de rupture écrites)
(scaling + renvoi : Ciel partagé, Serres jumelles, Fauconnier's curse)

## Debt & Observance Bricks

(préambule : ces régulateurs REMPLACENT les patterns standard, jamais
 d'empilement)
| Brick | ... | (4 lignes : Observance gate / Capped inventory /
 Non-gold currency / Debt hook — tableau spec §4.3)
(détails : acte scénique vérifiable + échec écrit sans punition empilée,
 contenu sans valeur mécanique + rétention scalant avec le stock jamais
 de DD fixe, fourchette de valeur obligatoire en Design Notes, la dette
 appartient au MJ et n'achète pas de puissance)
(scaling par gravité + renvoi : Voix de l'Autel's six observances,
 the Dream-Thief's itching inventory, the Pirates' debt)
```

- [ ] **Step 2 : Vérifier la structure**

Run (Grep sur le fichier) : les H2 dans l'ordre `Resource Patterns → Combat → Exploration → Social → Magic → Information → Bond & Companion → Debt & Observance → Scaling Knobs` ; 3 occurrences de `examples/feat-creator-dons-zarathar.md` ; aucune occurrence de « DC 1[0-9] » (pas de DD fixe introduit).

- [ ] **Step 3 : Commit**

```bash
git add plugins/ttrpg-creation/skills/feat-creator/references/feat-effect-library.md
git commit -m "feat(ttrpg-creation): expand feat-effect-library - information, bond, debt brick families"
```

### Task 2: Manifests + CHANGELOG (1.4.0)

**Files:**
- Modify: `plugins/ttrpg-creation/.claude-plugin/plugin.json` (`"version": "1.3.0"` → `"1.4.0"`, description inchangée)
- Modify: `.claude-plugin/marketplace.json` (`"version": "1.3.0"` → `"1.4.0"` dans metadata, descriptions inchangées)
- Modify: `CHANGELOG.md` (nouvelle entrée en tête, avant `## [1.3.0]`)

- [ ] **Step 1 : Bumper les deux versions** (Edit ciblés, rien d'autre ne change).

- [ ] **Step 2 : Entrée CHANGELOG** au format du dépôt :

```markdown
## [1.4.0] — 2026-06-10

### Ajouts

- Plugin `ttrpg-creation` (v1.4.0) : `feat-creator` — trois nouvelles familles de briques dans `references/feat-effect-library.md`, issues du premier corpus d'usage réel (les 10 dons Zarathar, `examples/feat-creator-dons-zarathar.md`) :
  - **Information Bricks** — closed oracle (étalon *Augury*, sortie ambiguë obligatoire), detection at range (catégorie nommée, passif seulement si rare), intent reading (fait défini d'avance, jet opposé, jamais de DD fixe), diagnostic (données mécaniques honnêtes). Monnaie de calibrage : questions fermées par repos (1/LR ≈ ½ feat).
  - **Bond & Companion Bricks** — shared senses (3 knobs : fréquence / action / cécité propre), telepathic tether (le contenu coûte plus que la portée), positional rider (vendre un angle, jamais l'avantage brut — anti-modèle Pack Tactics), the bond's price (clauses de rupture écrites, la moitié défensive du budget). Règle de famille : le compagnon de feat est un capteur, jamais un attaquant.
  - **Debt & Observance Bricks** — observance gate (acte scénique vérifiable), capped inventory (plafond PB, contenu sans valeur mécanique, rétention scalant avec le stock), non-gold currency (fourchette de valeur obligatoire en Design Notes), debt hook (zéro math, la dette appartient au MJ). Règle de famille : ces régulateurs remplacent les patterns standard, jamais d'empilement.

### Pourquoi (la boucle galerie → références)

C'est la première itération du mécanisme prévu par `examples/README.md` : un output curé qui sert de point d'ancrage à un enrichissement de `references/`. Les 10 dons Zarathar ont révélé que la bibliothèque d'effets ne couvrait ni l'information comme bénéfice, ni le compagnon-capteur, ni les régulateurs narratifs de ressource — trois familles que l'usage réel produit spontanément et que le homebrew calibre mal faute d'étalons (l'information ne se mesure pas en DPR). Chaque section se clôt sur un renvoi vers l'exemple curé. Les Drawback riders (malédictions), signature du format maison Zarathar, restent volontairement hors du skill générique.
```

- [ ] **Step 3 : Vérifier** — les deux JSON parsent (`ConvertFrom-Json`), `1.4.0` présent dans les 3 fichiers, plus aucune occurrence de `"version": "1.3.0"`.

- [ ] **Step 4 : Commit**

```bash
git add plugins/ttrpg-creation/.claude-plugin/plugin.json .claude-plugin/marketplace.json CHANGELOG.md
git commit -m "chore(ttrpg-creation): bump to 1.4.0 - feat-effect-library expansion"
```

### Task 3: Validation + release

**Files:** aucun nouveau.

- [ ] **Step 1 : `python scripts/validate.py`** — attendu : `OK 0 warning(s), no errors.`

- [ ] **Step 2 : Push** — `git push origin main` (autorisation push main déjà accordée cette session).

- [ ] **Step 3 : Rendre disponible** —

```powershell
claude plugin marketplace update ludomancien-skills
claude plugin update ttrpg-creation@ludomancien-skills
```

Attendu : marketplace à 1.4.0 ; plugin « updated from 1.3.0 to 1.4.0. Restart to apply changes. »

- [ ] **Step 4 : Vérifier le cache** — `Test-Path "$env:USERPROFILE\.claude\plugins\cache\ludomancien-skills\ttrpg-creation\1.4.0\skills\feat-creator\references\feat-effect-library.md"` → True.

---

## Self-review (fait à la rédaction)

- **Couverture spec** : §1–§4 → Task 1 ; §5 → Tasks 2–3 ; §6 critères → vérifications des Steps 2 de chaque tâche ; §7 hors scope respecté (aucune tâche ne touche SKILL.md, READMEs, power-budgets). Aucun écart.
- **Placeholders** : les squelettes renvoient au contenu normatif complet de la spec §4 (validé mot pour mot) — pas de TBD.
- **Cohérence** : version 1.4.0 partout ; ordre des H2 identique entre Task 1 Step 1 et Step 2.
