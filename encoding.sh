#!/bin/bash

input_folder="${1:-.}"

utf="utf-8"

# Sans cela on a une erreur lorsqu'il n'y a pas de .txt par exemple, alors qu'on essaye juste de rester compatible avec les 2 formats.
shopt -s nullglob

for files in $input_folder/*.md $input_folder/*.txt
do
	sed -i "s/\’/\'/g" $files #remplace les quotations marks en cp1252 par des apostrophes ce qui évite les problèmes réencodage cp1252>utf-8
	sed -i "s/\œ/\oe/g" $files
	sed -i "s/\—/\-/g" $files
	sed -i "s/\ /\ /g" $files
	sed -i "s/\–/\-/g" $files
	
	encoding=$(file -i "$files" | sed "s/.*charset=\(.*\)$/\1/") 
	# -i display file's encoding
	# sed is a stream editor that enables you to modify text
	# the rest, idk
	
	if [ ! "$utf" == "${encoding}" ] # if the encoding is != from utf-8
	then
	echo "recoding from ${encoding} to $utf file : $files" #debug
	recode ${encoding}..$utf $files #recode file with the utf-8 encoding
	fi

done



