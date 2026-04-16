# Partie 6 : Pense-bêtes et check-lists

## ⚠️ Règles Critiques

Ne pas oublier :

| Règle | Raison | Conséquence |
|---|---|---|
| **Pas d'accents dans les noms de champs** | La machine est stricte | Article rejeté |
| **Pas d'espaces ni accents dans les noms de fichiers** | Risque d'erreur encoding | Article rejeté ou image invisible |
| **Retirer la clé après traitement** | Évite les re-traitements | Conflits possibles |
| **Fichiers sauvegardés en UTF-8** | Support des accents en contenu | Encodage corrompu |

## Checklist Avant Insertion de nouveaux textes

Avant d'insérer votre clé USB, vérifiez :

**Fichiers** :
- [ ] Frontmatter (métadonnées) valides (3 champs obligatoires présents)
- [ ] Pas d'accents dans les noms de champs (`categorie`, pas `catégorie`)
- [ ] Sauvegardés en UTF-8
- [ ] Images nommées sans accents ni espaces

**Structure** :
- [ ] Dossier `Collections/` à la racine de la clé
- [ ] Collections sans espaces ni accents
- [ ] Articles dans `{collection}/articles/`
- [ ] Images dans `{collection}/images/`

**Clé USB** :
- [ ] Nommée `AJOUT` (majuscule)
- [ ] Images référencées dans les articles existent dans `images/`