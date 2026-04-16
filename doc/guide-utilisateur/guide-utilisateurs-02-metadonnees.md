# Partie 2 : Métadonnées

## Vue d'ensemble

Le **frontmatter** (bloc `--- ... ---` en haut de chaque article) contient les métadonnées. Il y a des champs **obligatoires** (sans lesquels la machine rejettera l'article) et des champs **optionnels** (qui enrichissent l'affichage si présents).

---

## Règle d'Or : Pas d'Accents dans les Noms de Champs

**TRÈS IMPORTANT** : Les noms des champs (comme `titre`, `auteur`, `categorie`) **ne doivent JAMAIS avoir d'accents ou de majuscules**.

| ❌ Incorrect | ✅ Correct |
|---|---|
| `catégorie` | `categorie` |
| `Auteur` | `auteur` |
| `Titre` | `titre` |

La machine est sensible à la casse et aux accents. Si vous écrivez `catégorie` au lieu de `categorie`, la machine renvoie une **erreur de validation** et ne génèrera pas l'article.

![erreur de métadonnée](/doc/captures/erreur-conversion.png)

---

## Champs Obligatoires

Sans ces trois champs, l'article **sera rejeté** et génèrera une erreur.

### 1. `titre` (texte sur une ligne)

![titre](/doc/captures/titre.png)

Le titre complet de l'article.

```yaml
titre: "Avant de partir"
```

**Exemples** :
- `titre: "Mémoires d'une suffragette"`
- `titre: "La Nuit étoilée"`
- `titre: "Compte rendu de l'Assemblée Nationale, 15 juillet 1832"`

**Avec guillemets** : Recommandé (surtout s'il y a des caractères spéciaux)

---

### 2. `auteur` (texte sur une ligne)

![auteur](/doc/captures/auteur.png)

Le nom complet de l'auteur.

```yaml
auteur: "Antoine d'Abbadie"
```

**Exemples** :
- `auteur: "George Sand"`
- `auteur: "Jules Michelet"`
- `auteur: "Anonyme"` (si auteur inconnu)

**Avec guillemets** : Recommandé

---

### 3. `categorie` (texte sur une ligne)


![categorie](/doc/captures/categorie.png)

Classification ou catégorie pour organiser les articles dans l'interface.

```yaml
categorie: "Préparatifs"
```

**Exemples** :
- `categorie: "Scientifique"`
- `categorie: "Politique"`
- `categorie: "Littérature"`
- `categorie: "XVIII siècle"`

**Points clés** :
- ❌ **Pas d'accent pour "categorie"** : `categorie`, pas `catégorie`
- ✅ **Peut avoir des espaces** : `"Belles lettres"` (avec guillemets)
- ✅ **Peut avoir des chiffres** : `"XIX eme siecle"`

---

### 4. `url` (lien vers un site, une page, un article)

![qr-code](/doc/captures/qr-code.png)

Lien internet vers l'article original ou une source externe. **Génère un QR code** sur le ticket imprimé.

```yaml
url: https://example.com/article-ampere
```

**Exemples** :
- `url: https://gallica.bnf.fr/ark:/12148/bpt6k5845682z`
- `url: https://en.wikipedia.org/wiki/Andre-Marie_Ampere`
- `url: https://archive.org/details/memoires1850george`

**Points clés** :
- Doit être une URL complète (avec `https://` ou `http://`)
- Sur le ticket imprimé, un **QR code** sera généré pointant vers cette URL et l'adresse sera écrite en clair en dessous
- Les visiteurs peuvent scanner le QR code pour accéder au lien

---

## Champs Optionnels

Ces champs enrichissent l'affichage mais ne sont pas obligatoires.

### 5. `image` (nom de fichier avec son extension)

![image](/doc/captures/image.png)

Nom du fichier image (portrait, illustration, etc.) à afficher en haut de l'article.

```yaml
image: ampere-portrait.jpg
```

**Points clés** :
- ❌ **Pas d'accents dans le nom de fichier** : `leo-portrait.jpg`, pas `léo-portrait.jpg`
- ❌ **Pas d'espaces** : `Portrait_Leo.jpg`, pas `Portrait Leo.jpg`
- ✅ **Formats supportés** : JPG, JPEG, PNG
- ⚠️ **Doit exister** : Le fichier image doit être présent dans le dossier `images/` de la collection

**Exemple de structure** :
```
autrices/
├── articles/
│   ├── 001.md (avec image: ampere-portrait.jpg)
│   └── 002.md
└── images/
    ├── ampere-portrait.jpg ← Le fichier doit être ici!
    └── sand-portrait.jpg
```

---

### 6. `bio` (Un ou plusieurs paragraphes)


![bio](/doc/captures/bio.png)

Courte biographie de l'auteur. **Accepte les sauts de ligne**.

```yaml
bio: |-
  André-Marie Ampère (1775-1836) était un physicien
  et mathématicien français. Il a notamment étudié
  l'électromagnétisme et les lois du magnétisme.
```

**Points clés** :
- **`|-` est obligatoire** au début pour indiquer du texte multi-ligne
- **Chaque ligne doit être indentée** (2 espaces ou une tabulation)
- Les sauts de ligne sont préservés à l'affichage

**Exemple complet** :
```yaml
bio: |-
  George Sand (1804-1876) était une romancière française.
  Elle était célèbre pour ses romans champêtres.
  Elle a aussi été une figure importante du féminisme.
```

---

## Exemple Complet : Article Complet

Voici un article avec **tous** les champs (obligatoires + optionnels) :

```yaml
---
titre: "Mémoires de voyage aux Indes"
auteur: "André-Marie Ampère"
categorie: "Voyages"
url: https://gallica.bnf.fr/ark:/12148/bpt6k5845682z
image: ampere-portrait.jpg
bio: |-
  André-Marie Ampère (1775-1836) était un physicien
  et mathématicien français. Il a découvert les lois
  fondamentales de l'électromagnétisme.
---

En 1822, un navire quitta Marseille...

## Chapitre 1 : La Traversée

La Méditerranée était calme ce jour-là.

**Note importante** : Le voyage a duré trois mois.
```

---

## Exemple Minimal : Article sans image, lien ou bio

Vous pouvez omettre les champs optionnels :

```yaml
---
titre: "Poème sans Titre"
auteur: "Anonyme"
categorie: "Poesie"
---

Sous le ciel étoilé,
J'entends l'écho du temps qui passe...

Pour les retours charriot sans espace<br>
utilisez "<br>" à la fin de la ligne
```

**La machine accepte cet article** car tous les champs obligatoires sont présents.

---

## ✅ Checklist Métadonnées

Avant de passer à l'étape suivante, vérifiez votre article :

- [ ] **Les 3 champs obligatoires sont présents** : `titre`, `auteur`, `categorie`
- [ ] **Pas d'accents dans les noms de champs** (ex: `categorie`, pas `catégorie`)
- [ ] **Guillemets autour des valeurs** si elles contiennent des caractères spéciaux ou des espaces
- [ ] **`|-` présent** si la bio a plusieurs lignes
- [ ] **Images** (si utilisées) sont nommées **sans accents ni espaces**
- [ ] **Les images référencées existent** dans le dossier `images/`
- [ ] **Fichier sauvegardé en UTF-8** (important pour les accents dans le contenu)

---

## Prochaine étape

Maintenant que vous connaissez les métadonnées, apprenons à **organiser les fichiers sur USB** → [Partie 3: Organisation des Fichiers](./guide-utilisateurs-03-organisation-fichiers.md)
