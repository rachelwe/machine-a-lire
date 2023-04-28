# Dupliquer une makina

## matériel utilisé
- Raspberry 3B avec caisse de protection.
- Ecran tactile 7" 1024x600 capacitif HDMI.
- 2 clefs USB 16G
- Carte MicroSD 32GB
- Bobines papier thermique SBPA pour caisses et
imprimantes 80x75x12
- Imprimante POS Epson TM-T20III - C31CH51011

## Duplication de l'OS

Si vous avez déjà une Makina, vous pouvez suivre les étapes suivantes, autrement suivez les étapes d'installation du [README](../README.md).

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