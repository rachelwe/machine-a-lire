#!/bin/bash

MOUNT_FOLDER='/media/alca'

inotifywait --monitor --quiet --event create $MOUNT_FOLDER | \
while read event; do
	folder=$(echo $event|cut --delimiter ' ' --field 3)
	
	if [[ $folder == "AJOUT" ]]; then
		sleep 5
		source /home/alca/Documents/machine-a-lire/copy_from_usb.sh
	elif [[ $folder == "SUPPR" ]]; then
		sleep 5
		source /home/alca/Documents/machine-a-lire/delete_from_usb.sh
	else
		echo "clé usb non reconnue"
	fi
done
