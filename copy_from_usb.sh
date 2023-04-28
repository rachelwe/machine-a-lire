#!/bin/bash

# Those 2 lines make the notifications work, don't know why but not going to complain.
export DISPLAY=:0
export DBUS_SESSION_BUS_ADDRESS=unix:path=/run/user/1000/bus

if [ -d "/media/pi/AJOUT/articles" ] # Si le dossier /articles existe sur la clé AJOUT
then 
	echo "Directory ./articles/ exists!"
	usb='/media/pi/AJOUT/articles/*'
	# On crée les trois dossiers
	mkdir '/home/pi/Documents/machine-a-lire/input'
	mkdir '/home/pi/Documents/machine-a-lire/output'

	if  [ ! -d "/home/pi/Documents/machine-a-lire/images" ]
	then
		mkdir '/home/pi/Documents/machine-a-lire/images'
	fi

	if  [ -d "/media/pi/AJOUT/images" ]
	then
		if  [ ! -d "/home/pi/Documents/machine-a-lire/articles-images" ]
		then
			mkdir '/home/pi/Documents/machine-a-lire/articles-images'
		fi

		articles_images='/media/pi/AJOUT/images/*'
		articles_images_output='/home/pi/Documents/machine-a-lire/articles-images/'

		# On copie récursivement les fichiers de la clé usb dans le dossier input
		zenity --notification --text="Copie des images (peut durer plusieurs minutes)..." --display=:0
		cp -r $articles_images $articles_images_output
	fi
	
	# On les stocke dans des variables
	input_folder='/home/pi/Documents/machine-a-lire/input/'
	output_folder='/home/pi/Documents/machine-a-lire/output/'
	images_folder='home/pi/Documents/machine-a-lire/images/'
	
	# On copie récursivement les fichiers de la clé usb dans le dossier input
	zenity --notification --text="Copie des articles..." --display=:0
	cp -r $usb $input_folder
	
	#On corrige les noms de fichiers qui contiennent des espaces 
	python3 rename_bad_filenames.py
	
	#On réencode les fichiers txt qui ne sont pas encodés en utf-8 en appelant le script encoding.sh
	zenity --notification --text="Encoding..." --display=:0
	source /home/pi/Documents/machine-a-lire/encoding.sh
	echo "encoding terminé"

	# On exécute le script python qui convertit les fichiers du dossier input en HTML dans ./output puis en jpg dans ./images
	zenity --notification --text="Conversion..." --display=:0
	python3 file_converter.py
	echo "conversion finie"
	
	# On supprime les dossiers input et output
	rm -r $input_folder
	rm -r $output_folder
	echo "tout est fini"
	zenity --notification --text="Traitement terminé !" --display=:0
	
else # Si le dossier articles sur AJOUT n'existe pas 
	echo "Directory ./articles/ doesn't exists!"
	zenity --error --text="La clé USB ne contient pas de dossier \"articles\"" --display=:0
fi
