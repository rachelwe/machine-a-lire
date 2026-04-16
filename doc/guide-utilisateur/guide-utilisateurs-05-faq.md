# Partie 5 : FAQ

## Questions Fréquentes

### Contenu & Articles

#### Q: "Puis-je modifier un article après l'avoir mis sur la machine?"

**R:** Oui, facilement.

1. Modifier le fichier `.md` sur votre ordinateur (même numéro, ex: `001.md`)
2. Insérer clé AJOUT
3. L'article existant sera **remplacé** par la nouvelle version

---

#### Q: "Puis-je ajouter des articles sans supprimer les anciens?"

**R:** Oui, c'est le comportement par défaut d'AJOUT.

- Vous insérez clé AJOUT avec articles `001.md`, `002.md`
- Machine a déjà `001.md`, `002.md`, `003.md`
- Après traitement : `001.md` (mis à jour), `002.md` (mis à jour), `003.md` (inchangé)
- Rien n'a été supprimé

---

#### Q: "Combien d'articles puis-je ajouter?"

**R:** Limité par l'espace disque du Raspberry Pi.

- La machine a environ **16 GB de stockage libre** (selon configuration)
- Chaque article JPG fait ~200-500 KB

---

#### Q: "Les images sont-elles obligatoires?"

**R:** Non. Le champ `image` est **optionnel**.

- Article sans image : OK
- La machine ignorera simplement l'absence d'image
- L'article s'affichera quand même

---

#### Q: "Puis-je ajouter du HTML ou du CSS dans le contenu?"

**R:** Oui.

Favorisez la **syntaxe Markdown** pour mise en forme, mais vous pouvez agrémenter de balises html si besoin (ex courant : <br> quand on souhaite faire un retour à la ligne sans espace pour les poèmes et dialogues par exemple)

**syntaxes utiles** :
- `## Titre de niveau 2`
- `**gras**`
- `*italique*`
- `- liste`
- `[lien](url)`
- `saut de ligne sans espace<br>`

---

#### Q: "Puis-je utiliser des accents dans le contenu (pas les noms de champs)?"

**R:** **Oui dans le contenu.**

✅ OK :
```markdown
titré: "L'Été à Marseille"
auteur: "André Maurois"

Texte avec des accents : café, élève, etc.
```

❌ Pas OK :
```markdown
catégorié: "..."  ← Pas d'accents dans le nom de champ!
```

---

### Collections

#### Q: "Je peux avoir plusieurs collections?"

**R:** Oui, autant que vous voulez.

Structure sur clé AJOUT :
```
AJOUT/Collections/
├── Autrices/
├── Voyages/
├── Poesie/
└── Politique/
```

Toutes les collections seront ajoutées ou mises à jour.

---

#### Q: "Puis-je modifier les collections après les avoir mises?"

**R:** Oui. Utilisez AJOUT avec les données modifiées.

Exemples :
- Renommer une collection : Changer `collectionNom` dans son `config.yml`
- Ajouter articles à une collection existante : Insérer clé AJOUT avec nouveaux articles
- Changer les logos : Mettre à jour `config.yml` avec nouveaux noms de fichiers

---

#### Q: "Qu'est-ce que je fais si je veux supprimer juste une collection?"

**R:** Actuellement, il n'y a pas de fonction "supprimer une collection".

Options :
1. **Utiliser SUPPR** (supprime tout, puis recréer les autres collections)
2. **Contacter votre contact technique** pour une suppression manuelle

---

### Clés USB

#### Q: "Qu'est-ce qu'il se passe si la clé reste dans la machine au redémarrage ?"

**R:** La clé se **re-traitera à chaque redémarrage**.

- ✅ Pas de catastrophe (les articles ne se dupliquent généralement pas)
- ⚠️ Mais elle se re-traitera, ce qui peut causer des conflits
- **Règle** : Toujours retirer la clé après traitement

---

#### Q: "Comment savoir si la clé a été bien détectée?"

**R:** L'écran montre des signes de traitement : Des messages de statut apparaissent

![traitement](/doc/captures/notification-traitement-temporaire.png)

Si **rien ne se passe** après 1-2 minutes :
- Clé peut ne pas être bien nommée (vérifier `AJOUT` ou `SUPPR`)
- Clé peut ne pas être bien insérée (retirer/réinsérer)
- Cliquer sur le logo en haut à gauche pour mettre à jour la page : un message d'erreur s'affichera peut-être avec plus d'informations

---

### Images

#### Q: "Quels formats d'images sont supportés?"

**R:** JPG, JPEG, PNG.

---

#### Q: "Puis-je utiliser des images très grandes?"

**R:** Techniquement oui, mais pas recommandé.

Idéalement redimensionnez les images à 600px de large pour optimiser les performances.

---

#### Q: "Mon image ne s'affiche pas. Pourquoi?"

**R:** Causes courantes :

1. **Nom mal épelé** : Dans `.md` vous écrivez `image: sand.jpg` mais fichier s'appelle `Sand.jpg` (casse différente)
2. **Accents dans le nom** : `portrait_Ampère.jpg` au lieu de `portrait_Ampere.jpg`
3. **Fichier n'existe pas** : Vous avez référencé une image qui n'est pas dans le dossier `images/`
4. **Mauvais format** : Format non supporté (GIF etc.)

**Solution** :
- Vérifier **exactement** le nom du fichier image
- S'assurer qu'il existe dans `images/`
- Vérifier pas d'accents ni d'espaces
- Utiliser JPG ou PNG

---

### Métadonnées

#### Q: "Que faire si j'oublie un champ obligatoire?"

**R:** La machine **rejette l'article**.

Champs obligatoires : `titre`, `auteur`, `categorie`

Si l'un manque :
- l'article ne s'ajoute pas
- Corriger le fichier, réinsérer la clé AJOUT

---

#### Q: "Comment vérifier les erreurs de validation?"

**R:** Après avoir cliqué sur le logo en haut à gauche pour recharger la page, s'il y a des erreurs elles seront listées dans un tableau.


![config.yml](/doc/captures/erreur-conversion.png)

---

### Configuration

#### Q: "Puis-je changer la collection par défaut après setup?"

**R:** Oui, via AJOUT ou accès direct à la machine.

- Modifier `AJOUT/Collections/config.yml` et réinsérer
- Ou modifier directement sur la machine (au démarrage uniquement)

![config.yml](/doc/captures/accueil-admin-defaut-collection.png)

---

### Impression & Affichage

#### Q: "J'ai un texte cryptique qui s'affiche et rien ne s'imprime"

**R:** Assurez-vous d'avoir bien connecté l'imprimante au raspberry et de l'avoir branchée. Elle doit être de l'un des 2 modèles supportés et ce modèle doit être celui sélectionné dans la congfiguration globale.

---

### Autre

#### Q: "Puis-je éditer les fichiers directement sur la machine?"

**R:** Non, les fichiers qui restent sur la machine sont des versions converties et non éditables de vos fichiers.