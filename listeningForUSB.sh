#!/bin/bash

# Those 2 lines make the notifications work, don't know why but not going to complain.
export DISPLAY=:0
export DBUS_SESSION_BUS_ADDRESS=unix:path=/run/user/1000/bus

# nettoyer la zone de notifications
killall notification-daemon 2>/dev/null || true

MOUNT_FOLDER='/media/pi'

inotifywait --monitor --quiet --event create $MOUNT_FOLDER | \
while read event; do
	folder=$(echo $event|cut --delimiter ' ' --field 3)

	zenity  --info --text="Une clé usb vient d'être connectée !\n\nSi vous l'avez nommée \"AJOUT\" elle commencera automatiquement le processus d'ajout de textes.\n\nSi vous l'avez nommée \"SUPPR\" elle commencera automatiquement le processus de suppression des textes." --width=400  --display=:0
	
	if [[ $folder == "AJOUT" ]]; then
		sleep 5
		source /home/alca/Documents/machine-a-lire/copy_from_usb.sh
	elif [[ $folder == "SUPPR" ]]; then
		sleep 5
		source /home/alca/Documents/machine-a-lire/delete_from_usb.sh
	else
		zenity --error --text="La clé n'est pas reconnue.\n\nla clé usb n'a pas été renommée correctement \n(\"AJOUT\" ou \"SUPPR\", selon l'usage souhaité)." --width=400 --display=:0
		echo "clé usb non reconnue"
	fi
done
