# Partie 4 : Clés USB et Configuration

## Les deux clés USB : AJOUT vs SUPPR

Machine à Lire utilise **deux clés USB distinctes** :

| Clé | Fonction | Nom | Contenu |
|---|---|---|---|
| **AJOUT** | Ajouter/mettre à jour articles | `AJOUT` | Dossier `Collections/` avec articles |
| **SUPPR** | Supprimer TOUS les articles | `SUPPR` | Fichier `suppression.txt` |

⚠️ **Important** : Chaque clé a un **rôle bien défini**. Ne les confondez pas!

---

## Clé USB AJOUT (Ajouter du Contenu)

### Pourquoi la renommer "AJOUT" ?

La machine **détecte automatiquement** les clés USB en **lisant leur nom**. Quand une clé nommée `AJOUT` est insérée, la machine déclenche le traitement.

### Comment renommer une clé USB ?

#### Sur Windows

1. **Brancher la clé USB** dans un port USB de l'ordinateur
2. Ouvrir l'Explorateur de Fichiers (icône dossier sur la barre des tâches)
3. **Localiser la clé** (generalement `Disque amovible` ou `Lecteur E:`, `F:`, etc.)
4. **Clic droit** sur la clé → "Renommer"
5. **Taper `AJOUT`** (en majuscule)
6. **Appuyer sur Entrée**

#### Sur Mac

1. **Brancher la clé USB**
2. La clé apparaît sur le Bureau et dans le Finder
3. **Clic droit** sur le nom de la clé → "Renommer"
4. **Taper `AJOUT`** (en majuscule)
5. **Appuyer sur Entrée**

### Contenu : Structure AJOUT

(Voir détails complets dans [Partie 3: Organisation](./guide-utilisateurs-03-organisation-fichiers.md))

```
AJOUT/
└── Collections/
    ├── config.yml
    ├── Autrices/
    │   ├── config.yml (optionnel)
    │   ├── articles/
    │   │   ├── 001.md
    │   │   └── 002.md
    │   └── images/
    │       └── ...
```

**Avant d'insérer la clé USB, vérifiez localement** :

### ✅ Checklist de Vérification

- [ ] **Frontmatter valide** : Chaque `.md` commence par `---` et a tous les champs obligatoires
- [ ] **Pas d'accents dans les noms de champs** : `categorie`, pas `catégorie`
- [ ] **Pas d'accents dans les noms de fichiers** : `001.md`, pas `article_à_ajouter.md`
- [ ] **Pas d'espaces dans les noms de fichiers** : `sand-portrait.jpg`, pas `sand portrait.jpg`
- [ ] **Fichiers sauvegardés en UTF-8** : (paramètre lors de la sauvegarde)
- [ ] **Images existent** : Chaque `image: filename.jpg` existe dans le dossier `images/`
- [ ] **Dossier articles existe** : Chemin correct : `Autrices/articles/001.md`

### Insertion dans la Machine

1. **Localiser le port USB** sur la machine
2. **Insérer la clé**
3. **La machine démarre le traitement** automatiquement (peut durer plusieurs minutes selon le nombre d'articles et la taille des images)
4. Quand le traitement est terminé, une notification s'affiche

### Important : JAMAIS de Suppression d'Articles Existants

**La clé AJOUT ne supprime JAMAIS les articles existants.** Elle les **ajoute ou met à jour**.

Exemple :
- Avant : Articles 001, 002, 003 dans la collection "Autrices"
- Vous insérez AJOUT avec : Articles 001 (modifié), 002 (inchangé), 004 (nouveau)
- Après : Articles 001, 002, 003, 004 (rien ne disparaît)

**Pour supprimer des articles**, utilisez la clé **SUPPR** (voir ci-après).

### ⚠️ OBLIGATION : Retirer la Clé USB Après Traitement

**TRÈS IMPORTANT** :

- Après le traitement, la clé **doit être retirée immédiatement**
- Si vous la laissez, elle **re-traitera à chaque redémarrage** de la machine
- Cela peut créer des doublons ou des conflits

**Comment retirer** :
1. Vérifier que le traitement est terminé (notification de traitement terminé)
2. **Tirer la clé**

### Vérification : Articles Apparaissent-ils ?

Après retrait de la clé :

1. **Cliquer sur le logo** en haut-à-gauche de l'interface
   - Cela **recharge la page** et l'index des articles
   - Les nouveaux articles devraient apparaître

2. **Vérifier les erreurs** :
   - En cas d'erreur de traitement sur les fichiers un tableau avec les fichiers problématiques devrait vous donner plus d'informations.
   - **Si rien n'apparaît** : redémarrez la machine (sans clé usb branchée) et retentez d'insérer la clé AJOUT.

---

## Clé USB SUPPR (Supprimer Tout)

### ⚠️ ATTENTION : Opération Destructive et Irréversible

La clé SUPPR **supprime TOUS les articles et toutes les images** de la machine. **Il n'y a pas de récupération possible.**

### Quand utiliser SUPPR ?

- Machine doit être complètement réinitialisée
- Tous les anciens articles sont obsolètes
- Changement majeur de contenu/direction

### Contenu : Structure SUPPR

La clé SUPPR est très simple :

```
SUPPR/
└── suppression.txt (fichier vide)
```

**C'est tout!** Le fichier `suppression.txt` peut être **complètement vide**. C'est juste un marqueur.

### Comment créer le fichier suppression.txt

1. Ouvrir Bloc-notes (Windows)
2. **Ne rien écrire** (laisser vide)
3. Fichier → "Enregistrer sous"
4. Nom : `suppression.txt`
6. Localisation : **racine de la clé SUPPR**
7. Clic sur "Enregistrer"

### Insertion dans la Machine

**Processus identique à AJOUT** :

1. Renommer clé en `SUPPR` (majuscule)
2. Insérer dans le port USB de la machine
3. La machine détecte `SUPPR` et **supprime tous les articles et images** automatiquement
5. ⚠️ **Pas de récupération** — les données sont perdues, prévoyez une sauvegarde de vos fichiers d'origine hors de la machine !

### ⚠️ OBLIGATION : Retirer la Clé USB Après Traitement

Même chose que pour AJOUT :
- Vérifier que traitement est terminé
- Retirer physiquement la clé

---

## Fichiers de configuration (config.yml)

### Global Config : `AJOUT/Collections/config.yml`

Ce fichier à la racine de `Collections/` contrôle **tout le système** :

```yaml
# Permettre aux visiteurs de basculer entre collections
# true = affiche "voir toutes les collections" dans chaque collection
# false = pas de sélection possible (collection verrouillée)
changementCollectionPossible: true

# Charger automatiquement une collection au démarrage
# Laisse 60 secondes pour l'utilisateur de choisir une autre
# Mettez le nom du dossier de collection, ex: "autrices"
# Ou laissez vide / false pour afficher l'écran de sélection
collectionParDefaut: "autrices"

# Texte affiché dans l'interface de choix de collection
texteChoixCollection: "Choisissez la collection que vous souhaitez explorer"

# Modèle d'imprimante installée
# Valeurs possibles: "TM-T20III" ou "TM-T20IV"
imprimante: TM-T20III
```

### Configuration par collection : `AJOUT/Collections/{collection}/config.yml`

Ce fichier **optionnel** personnalise **une collection spécifique** :

```yaml
# Nom affiché de la collection dans l'interface
collectionNom: "Les Autrices du XIXe siècle"

# Description affichée sur la page d'accueil de la collection
# Utiliser "|-" pour multi-ligne (voir exemple)
collectionDescription: |-
  Une collection de poèmes et textes de femmes écrivains
  du XIXe siècle. Cliquez sur un titre pour l'imprimer!

# Logos affichés sous les catégories (largeur: 256px)
# Liste de noms de fichiers images dans le dossier images/
# Peut être vide si aucun logo
collectionLogos:
  - logo-machine.png
  - logo-admin.png

# --- Contenu des Tickets Imprimés ---

# Texte de description sur les tickets
ticketDescription: |-
  Une collection curatée par la Bibliothèque Municipale.
  Pour plus de découvertes, visitez: example.com

# Avertissement affiché sous la description
ticketAvertissement: |-
  Ticket lecteur à conserver.
  Ne pas jeter sur la voie publique.

# Logos entre les séparateurs (généralement logos d'institutions)
ticketLogos1:
  - logo-institution.png

# Mentions légales/crédits (texte final du ticket)
ticketMentionsLegales: |-
  © 2024 Bibliothèque Municipale.
  Tous droits réservés.

# Logos à la fin du ticket
ticketLogos2:
  - logo-partner.png
```

---

## ✅ Checklist Clés USB

Avant d'insérer une clé :

**Pour AJOUT** :
- [ ] Clé nommée exactement `AJOUT` (majuscule)
- [ ] Dossier `Collections/` à la racine
- [ ] Articles dans des sous-dossiers `articles/`
- [ ] Images dans des sous-dossiers `images/`
- [ ] Fichiers de configuration au bon endroit

**Pour SUPPR** :
- [ ] Clé nommée exactement `SUPPR` (majuscule)
- [ ] Fichier `suppression.txt` à la racine (**vide**, OK)
- [ ] **Vous avez compris que TOUT va être supprimé**

---

## Prochaine étape

Maintenant que vous comprenez les clés et la configuration vous êtes entièrement autonome !

Pour des **questions fréquentes**, consultez [Partie 5: FAQ](./guide-utilisateurs-05-faq.md)
