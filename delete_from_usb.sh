#!/bin/bash

# Those 2 lines make the notifications work, don't know why but not going to complain.
export DISPLAY=:0
export DBUS_SESSION_BUS_ADDRESS=unix:path=/run/user/1000/bus

# POUR EFFACER LES ARTICLES-IMAGES PRESENTS SUR LE RASPBERRY

if [ -f "/media/pi/SUPPR/suppression.txt" ] # si on détecte un fichier suppression.txt dans la clé SUPPR
then
	sudo rm -rf '/home/pi/Documents/machine-a-lire/images' # on supprime le dossier images/ sur le raspberry
	python3 -c 'from led import dirImagesDeleted; dirImagesDeleted()' # Lance la fonction problem() dans led.py (allume les 3 led comme une guirlande)
	zenity --notification --text="Tous les fichiers ont bien été supprimés" --display=:0
else # Si le fichier suppression.txt n'existe pas sur SUPPR
	echo "File suppression.txt doesn't exists!"
	python3 -c 'from led import errFileMissing; errFileMissing()' # Lance la fonction errFileMissing() dans led.py (fait clignoter la led rouge)
	zenity --notification --text="Les fichiers n'ont pas pu être supprimés" --display=:0
fi
