# Partie 1 : Fondamentaux

Vous êtes gestionnaire de contenu ou locataire d'une **Machine à Lire / Makina Bellet**, une **borne interactive** de consultation et d'impression de textes (complets ou extraits). Ce guide vous explique comment ajouter et supprimer des articles sur la machine, pas à pas.

## Comment ça marche (vue d'ensemble)
1. Vous préparez des fichiers texte et leurs illustrations sur votre ordinateur
2. Vous les mettez sur une **clé USB nommée "AJOUT"**
3. Vous insérez la clé dans la machine
4. La machine traite automatiquement et ajoute les textes
5. Vous retirez la clé USB après
6. Les visiteurs peuvent consulter et imprimer

---

Pour le formatage des textes vous allez utiliser un fichier appelé "markdown".

## Qu'est-ce qu'un fichier Markdown ?

### Définition simple

**Markdown** est un format de texte très simple qui ressemble à du texte brut, mais avec quelques symboles spéciaux pour faire de la mise en forme (gras, italique, titres, listes, etc.).

Exemple :
```markdown
# Ceci est un titre de niveau 1

## Ceci est un titre de niveau 2

Ceci est du texte normal.

**Ceci est du texte en gras**

_Ceci est du texte en italique_

- Item 1 dans une liste
- Item 2
- Item 3
```

### Pourquoi Markdown ?

- ✅ **Universel/interopérable** : fonctionne sur n'importe quel ordinateur (Windows, Mac, Linux) et compatible avec de nombreux logiciels d'édition de texte.
- ✅ **Lisible** : même en version "brute", le markdown est facile à lire
- ✅ **Simple** : pas besoin de logiciel compliqué (un simple bloc-notes suffit)
- ✅ **Fiable** : aucun risque de corruption liée aux formats propriétaires (Word, etc.)

### Comment éditer un fichier Markdown ?

#### Option 1 : Bloc-notes Windows (gratuit, fourni avec Windows)

1. Clic droit sur le Bureau
2. Sélectionner "Nouveau" → "Document texte"
3. Renommer en `001.md` (attention au `.md` à la fin)
4. Double-clic pour ouvrir
5. Écrire votre contenu
6. Fichier → Enregistrer sous → Codage : UTF-8

**Avantages** : Simple, aucune installation  
**Inconvénients** : Pas de coloration syntaxique (mise en valeur par la couleur de certains éléments formatés), basique, vu 1 fichier à la fois

#### Option 2 : Sublime Text (gratuit, minimaliste, recommandé)

1. **Télécharger** : https://www.sublimetext.com/ (gratuit pour l'évaluation illimitée)
2. **Installer** : Suivre les instructions
3. **Utiliser** :
   - Ouvrir Sublime Text
   - File → Open Folder → Sélectionner votre dossier de travail (dans notre cas, créez un dossier appelé "Collections")
   - File → New File
   - Écrire votre contenu
   - File → Save As → retrouvez votre dossier de travail → Nom : `001.md` → Format : UTF-8

**Avantages** : Bonne coloration syntaxique (aide à la rédaction), vue d'ensemble de tous les fichiers
**Inconvénients** : Doit être téléchargé/installé

---

#### Vous n'arrivez pas à ouvrir les .md ?

Vous pouvez utiliser l'extension `.txt` malgré tout (la machine a été conçue pour être tolérente sur le sujet), mais il faudra tout de même respecter le formatage interne du fichier.

## Structure d'un article

### Composition générale

Chaque article a **deux parties** :

1. **Frontmatter YAML** (en haut, entre `---`)
   - Les **métadonnées** : titre, auteur, catégorie, URL, image, biographie
   
2. **Contenu Markdown** (en bas, après le second `---`)
   - Le **texte réel** de l'article en format markdown

### Exemple complet

```markdown
---
titre: "LaCommune de Malenpis"
auteur: "André Léo"
categorie: "Autrices"
url: https://example.com/article-andre-leo
image: andre-leo-portrait.jpg
bio: |-
  André Léo était à la fois Romancière et journaliste
---

Comme ceux qui avaient fait les chartes étaient morts depuis cent ans, il n'était pas facile de savoir d'eux les raisons qu'ils avaient eues de chasser les gens couronnés. On aurait pu du moins, comme le proposait Lavisé, envoyer deux ou trois des plus fins de la commune savoir un peu ce qui se passait dans le royaume, et si vraiment les gens étaient si contents de ceux qui les gouvernaient.

## Extrait 2

Le navire quitte le port de Marseille par une belle journée d'automne.

**Important à noter :** Les premiers jours en mer furent difficiles.

- Beaucoup de passagers étaient malades
- La nourriture était mauvaise
- Mais l'équipage était professionnel
```

### Pourquoi deux parties ?

- **Frontmatter** = Métadonnées pour la machine (titre, auteur, etc.)
- **Contenu** = Texte pour les visiteurs

La machine utilise le frontmatter pour :
- Afficher le titre et l'auteur correctement
- Générer un QR code (depuis l'URL)
- Lier l'image au bon article
- Organiser les articles par catégorie

---

## Prochaine étape

Maintenant que vous comprenez le format, passons aux **métadonnées détaillées** → [Partie 2: Métadonnées](./guide-utilisateurs-02-metadonnees.md)
