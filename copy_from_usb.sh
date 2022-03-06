#!/bin/bash

# Those 2 lines make the notifications work, don't know why but not going to complain.
export DISPLAY=:0
export DBUS_SESSION_BUS_ADDRESS=unix:path=/run/user/1000/bus

if [ -d "/media/pi/AJOUT/articles" ] # Si le dossier /articles existe sur la clé AJOUT
then 
	echo "Directory ./articles/ exists!"
	usb='/media/pi/AJOUT/articles/*'
	#usb='/home/pi/Documents/machine-a-lire/articles/*'
	# On crée les trois dossiers
	#mkdir '/Users/leabelzunces/code/machine-a-lire/input'
	#mkdir '/Users/leabelzunces/code/machine-a-lire/output'
	#mkdir '/Users/leabelzunces/code/machine-a-lire/images'
	mkdir '/home/pi/Documents/machine-a-lire/input'
	mkdir '/home/pi/Documents/machine-a-lire/output'

	if  [ ! -d "/home/pi/Documents/machine-a-lire/images" ]
	then
		mkdir '/home/pi/Documents/machine-a-lire/images'
	fi
	
	# On les stocke dans des variables
	#input_folder='/Users/leabelzunces/code/machine-a-lire/input'
	#output_folder='/Users/leabelzunces/code/machine-a-lire/output'
	#images_folder='/Users/leabelzunces/code/machine-a-lire/images'
	input_folder='/home/pi/Documents/machine-a-lire/input/'
	output_folder='/home/pi/Documents/machine-a-lire/output/'
	images_folder='home/pi/Documents/machine-a-lire/images/'

	python3 -c 'from led import turnOnGreen; turnOnGreen()' #Allume la led verte au début de la copie et pendant l'encoding
	echo "leds allumées"
	
	# On copie récursivement les fichiers de la clé usb dans le dossier input
	zenity --notification --text="Copie des fichiers..." --display=:0
	cp -r $usb $input_folder
	
	#On corrige les noms de fichiers qui contiennent des espaces 
	python3 rename_bad_filenames.py
	
	#On réencode les fichiers txt qui ne sont pas encodés en utf-8 en appelant le script encoding.sh
	zenity --notification --text="Encoding..." --display=:0
	source /home/pi/Documents/machine-a-lire/encoding.sh
	echo "encoding terminé"
	
	python3 -c 'from led import turnOnYellow; turnOnYellow()' #Allume la led blue au début de la conversion txt>HTML>images

	# On exécute le script python qui convertit les fichiers du dossier input en HTML dans ./output puis en jpg dans ./images
	zenity --notification --text="Conversion..." --display=:0
	python3 file_converter.py
	echo "conversion finie"
	
	python3 -c 'from led import turnOffGreen; turnOffGreen()' #Eteint la led verte 
	python3 -c 'from led import turnOffYellow; turnOffYellow()' # et la led bleue à la fin de la conversion
	python3 -c 'from led import tranferEnded; tranferEnded()' # transfert terminé avec succès
	python3 -c 'from led import cleanLed; cleanLed()' # On nettoie les ports utilisés par les leds
	echo "leds éteintes"
	
	# On supprime les dossiers input et output
	rm -r $input_folder
	# rm -r $output_folder
	echo "tout est fini"
	zenity --notification --text="Traitement terminé !" --display=:0
	
else # Si le dossier articles sur AJOUT n'existe pas 
	echo "Directory ./articles/ doesn't exists!"
	python3 -c 'from led import errDirMissing; errDirMissing()' # Lance la fonction errDirMissing() dans led.py (fait clignoter la led rouge)
	zenity --error --text="La clé USB ne contient pas de dossier \"articles\"" --display=:0
fi
