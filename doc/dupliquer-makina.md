# Dupliquer une makina

Vous avez déjà une machine à lire et vous souhaitez la dupliquer ? Voici la marche à suivre (cela évite une configuration longue). Autrement suivez les étapes d'installation du [README](../README.md).

## matériel utilisé

Pour la partie technique :

- Raspberry 3B (minimum, 4 de préférence) avec caisse de protection.
- Ecran tactile 7" 1024x600 capacitif HDMI.
- 2 clefs USB 16G
- Carte MicroSD 32GB
- Bobines papier thermique SBPA pour caisses et
imprimantes 80x75x12
- Imprimante POS Epson TM-T20III OU TM-T20IV

Vous êtes libres dans vos choix d'enveloppe pour la coque de la borne !

## Duplication de l'OS

Si vous avez déjà une Makina, vous pouvez suivre les étapes suivantes

Tutoriel repris de [Raspberry Tips - Comment Créer une Image de votre Raspberry Pi ?](https://raspberrytips.fr/creer-image-raspberry-pi/)

- Téléchargez [Win32 Disk Imager](https://sourceforge.net/projects/win32diskimager/).
- Dans le champ "image file" choisissez un emplacement où le raspberry sera sauvegardé (prévoyez 30Go ~) de stockage.
- insérez la carte sd de l'ancienne Makina dans votre PC et sélectionnez là dans le champ "Device".
- Cliquez sur "Read" et attendez qu'il ait terminé.
- insérez la carte SD de la prochaine Makina
- Choisissez l'image que vous venez de récupérer sur votre PC dans le champ "Image file"
- Sélectionnez la nouvelle carte SD dans le champ "Device".
- Cliquez sur "Write", attendez qu'il ait terminé.
- branchez la nouvelle carte sd dans le raspberry, démarrez et branchez tout : tout devrait fonctionner comme l'ancienne !