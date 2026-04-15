#!/bin/bash

# Those 2 lines make the notifications work, don't know why but not going to complain.
export DISPLAY=:0
export DBUS_SESSION_BUS_ADDRESS=unix:path=/run/user/1000/bus

collections_folder="/media/pi/AJOUT/Collections"

if [ -d $collections_folder ] # Si le dossier /Collections existe sur la clé AJOUT
then 
	echo "Directory ./Collections/ exists!"

	target_folder="/home/pi/Documents/machine-a-lire"

	# On crée les trois dossiers
	mkdir "$target_folder/input"
	mkdir "$target_folder/output"

	if  [ ! -d "$target_folder/images" ]
	then
		mkdir "$target_folder/images"
	fi

	if  [ ! -d "$target_folder/articles-images" ]
	then
		mkdir "$target_folder/articles-images"
	fi

	# Récupération de la config globale
	if [ -f "$collections_folder/config.yml" ]
	then
		cp "$collections_folder/config.yml" "$target_folder/images/"
	fi

	# Function to archive existing error log before processing
	archive_error_log() {
		local errors_file="$target_folder/images/errors.json"
		if [ -f "$errors_file" ] && [ -s "$errors_file" ]; then
			# File exists and is not empty
			local timestamp=$(date '+%Y-%m-%d_%H-%M-%S')
			local archive_file="$target_folder/images/errors_$timestamp.json"
			mv "$errors_file" "$archive_file"
			echo "Error log archived to $archive_file"
		fi
	}
	archive_error_log
	
	for dir in /media/pi/AJOUT/Collections/*; do
    if [ -d "$dir" ]; then

			# cd "$dir"
			collection="$(basename $dir)"
			zenity --notification --text="Traitement de la collection $collection…" --display=:0

			usb_articles="$dir/articles/*"
			usb_images="$dir/images/*"

			# On crée les trois dossiers
			mkdir "$target_folder/input/$collection"
			mkdir "$target_folder/output/$collection"

			if  [ ! -d "$target_folder/images/$collection" ]
			then
				mkdir "$target_folder/images/$collection"
			fi

			# On stocke dans des variables les chemins
			input_folder="$target_folder/input/$collection"
			output_folder="$target_folder/output/$collection"
			images_folder="$target_folder/images/$collection"
			articles_images_output="$target_folder/articles-images/$collection"

			# Récupération de la config de chaque collection
			if [ -f "$dir/config.yml" ]
			then
				cp "$dir/config.yml" "$images_folder"
			fi

			if  [ -d "$dir/images" ]
			then
				if  [ ! -d "$articles_images_output" ]
				then
					mkdir "$articles_images_output"
				fi

				# On copie récursivement les fichiers de la clé usb dans le dossier input
				zenity --notification --text="Copie des images et articles (peut durer plusieurs minutes)..." --display=:0
				cp -r $usb_images $articles_images_output
			fi
			
			
			# On copie récursivement les fichiers de la clé usb dans le dossier input
			cp -r $usb_articles $input_folder
			
			#On corrige les noms de fichiers qui contiennent des espaces 
			python3 rename_bad_filenames.py "$input_folder"
			
			#On réencode les fichiers txt qui ne sont pas encodés en utf-8 en appelant le script encoding.sh
			zenity --notification --text="Encodage et conversion des fichiers (peut durer plusieurs minutes)..." --display=:0
			source "$target_folder/encoding.sh" "$input_folder"
			echo "encoding terminé"

			# On exécute le script python qui convertit les fichiers du dossier input en HTML dans ./output puis en jpg dans ./images
			python3 file_converter.py "$collection"
			echo "conversion finie"
			
			# nettoyer la zone de notifications
			killall notification-daemon 2>/dev/null || true
    fi
	done

	# On supprime les dossiers input et output
	rm -r "$target_folder/input"
	rm -r "$target_folder/output"
	
	echo "tout est fini"
	zenity  --info --text="Traitement terminé ! \nVous pouvez cliquer sur le logo en haut à gauche pour recharger la page une fois cette notification fermée." --width=400  --display=:0
	
else # Si le dossier articles sur AJOUT n'existe pas 
	echo "Directory ./Collections/ doesn't exists!"
	zenity --error --text="Les fichiers n'ont pas pu être copiés :\nLa clé USB ne contient pas de dossier \"Collections\" \net/ou n'est pas correctement renommée en AJOUT." --width=400 --display=:0
	 
fi