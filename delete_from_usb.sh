#!/bin/bash

# Those 2 lines make the notifications work, don't know why but not going to complain.
export DISPLAY=:0
export DBUS_SESSION_BUS_ADDRESS=unix:path=/run/user/1000/bus

if [ -f "/media/pi/SUPPR/suppression.txt" ] # si on détecte un fichier suppression.txt dans la clé SUPPR
then
	echo "Suppression en cours..."
	zenity --notification --text="Suppression en cours..." --display=:0
	sudo rm -rf '/home/pi/Documents/machine-a-lire/images' # on supprime le dossier images/ sur le raspberry
	sudo rm -rf '/home/pi/Documents/machine-a-lire/articles-images' # on supprime le dossier articles-images/ sur le raspberry
	zenity --info --text="Tous les fichiers ont bien été supprimés ! \nVous pouvez cliquer sur le logo en haut à gauche pour recharger la page une fois cette notification fermée." --width=400 --display=:0
else # Si le fichier suppression.txt n'existe pas sur SUPPR
	echo "File suppression.txt doesn't exists!"
	zenity --error --text="Les fichiers n'ont pas pu être supprimés :\nla clé usb ne contient pas le fichier suppression.txt \net/ou n'est pas correctement renommée en SUPPR." --width=400 --display=:0
fi
