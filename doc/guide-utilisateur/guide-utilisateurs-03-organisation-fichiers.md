# Partie 3 : Organisation des Fichiers

## Structure complète sur clé USB

Quand vous préparez une clé USB nommée `AJOUT`, voici la structure **exacte** que la machine attend :

```
AJOUT/
├── Collections/
│   ├── config.yml (configuration globale)
│   ├── Autrices/
│   │   ├── config.yml (configuration collection)
│   │   ├── articles/
│   │   │   ├── 001.md (ou 001.txt)
│   │   │   ├── 002.md
│   │   │   ├── 003.md
│   │   │   └── ...
│   │   └── images/
│   │       ├── ampere-portrait.jpg
│   │       ├── sand-portrait.jpg
│   │       └── ...
│   ├── Voyages/
│   │   ├── config.yml
│   │   ├── articles/
│   │   │   ├── 001.md
│   │   │   ├── 002.md
│   │   │   └── ...
│   │   └── images/
│   │       └── ...
│   └── (autres collections...)
```

---

## Explication des Niveaux

### Niveau 1 : Racine de la clé USB

```
AJOUT/
└── Collections/
```

- **Clé nommée `AJOUT`** (c'est son nom qui déclenche la conversion !)
- **Dossier `Collections/`** à la racine (obligatoire, c'est le point d'entrée)

---

### Niveau 2 : Configuration Globale

```
AJOUT/Collections/
└── config.yml
```

Contrôle les **paramètres d'administration**:

```yaml
changementCollectionPossible: true
collectionParDefaut: "autrices"
texteChoixCollection: "Choisissez une collection"
imprimante: TM-T20III
```

(Détails complets dans [Partie 4: Clés USB](./guide-utilisateurs-04-cles-usb.md))

---

### Niveau 3 : Collections

```
AJOUT/Collections/
├── Autrices/
├── Voyages/
├── Litterature/
└── ...
```

**Chaque dossier = une collection / un corpus** (un groupe d'articles organisé sur un thème commun).

**Règles de nommage** :
- ✅ Pas d'espaces : `Autrices`, pas `Autrices modernes`
- ✅ Pas d'accents : `Litterature`, pas `Littérature`
- ✅ Peut avoir des tirets : `Belles-Lettres`
- ✅ Peut avoir des underscores : `Belles_Lettres`
- ❌ Pas de caractères spéciaux : `@`, `#`, `!`, `?`, etc.

**Exemples corrects** :
- `Autrices`
- `Voyages`
- `Journaux_Anciens`
- `Belles-Lettres`
- `XVIII_siecle`

---

### Niveau 4 : Configuration Collection

```
AJOUT/Collections/Autrices/
└── config.yml
```

**Fichier optionnel** qui personnalise **cette collection seulement** :

```yaml
collectionNom: "Les Autrices du XIXe siècle"
collectionDescription: |-
  Poèmes et textes de femmes écrivains. 
  Cliquez sur un texte pour l'imprimer !
collectionLogos:
  - logo-institution.png
ticketDescription: |-
  Une collection crée par la Bibliothèque Municipale
ticketAvertissement: |-
  À conserver - ne pas jeter sur la voie publique
ticketLogos1:
  - logo-bib.png
ticketMentionsLegales: |-
  © 2024 Bibliothèque Municipale
```

(Détails complets dans la [Partie 4](./guide-utilisateurs-04-cles-usb.md))

---

### Niveau 5 : Dossier Articles

```
AJOUT/Collections/Autrices/
└── articles/
    ├── 001.md
    ├── 002.md
    ├── 003.md
    └── ...
```

**Les fichiers articles DOIVENT être dans le dossier `articles/`** (pas directement dans la collection).

**Règles de nommage** :
- ✅ Format : `001.md`, `texte4.md`, `article_5_juillet.md`, etc.
- ✅ Extension : `.md` ou `.txt` (selon vos préférences, les 2 sont interprétés pareil)
- ❌ Pas d'accents : `article_a_ajouter.md`, pas `article_à_ajouter.md`
- ❌ Pas d'espaces : `article-01`, pas `article 01.md`

**Exemples corrects** :
- `001.md`, `texte4.md`, `article_a_ajouter.md`, ... (recommandé)
- `001.txt`, `article_5_juillet.txt`, `article-01.txt` (aussi valide)

---

### Niveau 5-bis : Dossier Images

```
AJOUT/Collections/Autrices/
└── images/
    ├── ampere-portrait.jpg
    ├── sand-portrait.jpg
    └── ...
```

**Images associées aux articles**.

**Règles de nommage** :
- ✅ Format : JPG, JPEG, PNG
- ❌ **Pas d'accents** : `ampere-portrait.jpg`, pas `ampère-portrait.jpg`
- ❌ **Pas d'espaces** : `Portrait_Ampere.jpg`, pas `Portrait Ampère.jpg`
- ✅ Peut avoir des underscores : `Portrait_Andre_Leo.jpg`
- ✅ Peut avoir des tirets : `portrait-andre-leo.jpg`

**Exemples corrects** :
- `ampere-portrait.jpg`
- `sand_portrait.jpeg`
- `leoAndrePortrait.png`

**Exemples incorrects** :
- `ampère-portrait.jpg` (accent)
- `Portrait d'André.jpg` (apostrophe + accent + espace)
- `andré léo.jpg` (accents + espace)

---

## Exemple Complet : Pas à Pas

Vous avez **2 articles** dans une collection **Autrices** :

### Étape 1 : Créer la structure

```
AJOUT/
└── Collections/
    └── Autrices/
        ├── config.yml
        ├── articles/
        └── images/
```

### Étape 2 : Ajouter les fichiers

```
AJOUT/
└── Collections/
    └── Autrices/
        ├── config.yml (contient le nom affichage, logos, etc.)
        ├── articles/
        │   ├── 001.md (Article sur George Sand)
        │   └── 002.md (Article sur Jane Austen)
        └── images/
            ├── sand-portrait.jpg
            └── austen-portrait.jpg
```

### Étape 3 : Contenu du fichier `001.md`

```markdown
---
titre: "George Sand, une vie de passion"
auteur: "André Maurois"
categorie: "Biographie"
url: https://gallica.bnf.fr/sand-maurois
image: sand-portrait.jpg
bio: |-
  André Maurois (1885-1967) était un écrivain français. 
  Il était spécialisé dans les biographies.
---

George Sand (1804-1876) était une écrivaine française...
```

### Étape 4 : Contenu du fichier `002.md`

```markdown
---
titre: "Jane Austen : La Jeunesse"
auteur: "Margaret Kennedy"
categorie: "Biographie"
url: https://example.com/jane-austen
image: austen-portrait.jpg
---

Jane Austen naquit en 1775 dans le Hampshire...
```

---

## ⚠️ Pièges Courants

| ❌ Problème | ✅ Solution |
|---|---|
| Fichiers dans `Autrices/` au lieu de `Autrices/articles/` | Créer dossier `articles/` et y mettre les `.md` |
| Images dans `images/` mais nom erroné dans `.md` | Vérifier que le nom dans `image: ...` existe exactement dans `images/` |
| Noms de fichiers avec accents : `article_à_ajouter.md` | Renommer en `article_a_ajouter.md` |
| Noms avec espaces : `article final.md` | Renommer en `article_final.md` ou `article-final.md` |
| Collection nommée `Belles Lettres` (espaces) | Renommer en `Belles_Lettres` |
| Fichier `.txt` sans encodage UTF-8 | Sauvegarder avec encodage UTF-8 |

---

## ✅ Checklist Organisation

Avant d'insérer la clé USB, vérifiez :

- [ ] Clé USB nommée exactement `AJOUT` (majuscule)
- [ ] Dossier `Collections/` à la racine de la clé
- [ ] Chaque collection a un dossier sans espaces ni accents
- [ ] **Tous les articles** sont dans un sous-dossier `articles/` dans la collection qui leur est propre
- [ ] Tous les fichiers `.md` contiennent un frontmatter (les métadonnées) valide
- [ ] Toutes les **images** sont dans un sous-dossier `images/` dans la collection qui leur est propre
- [ ] Les noms d'images **dans les `.md`** correspondent aux noms d'images **dans le dossier `images/`**
- [ ] **Pas d'accents** dans les noms de fichiers ou de dossiers
- [ ] **Pas d'espaces** dans les noms de dossiers (utiliser `_` ou `-`)

---

## Prochaine étape

Maintenant que vous connaissez la structure, parlons des **clés USB AJOUT et SUPPR** → [Partie 4: Clés USB](./guide-utilisateurs-04-cles-usb.md)
