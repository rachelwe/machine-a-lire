import os
import sys
import json
import imgkit # à installer à la main via `sudo apt-get install wkhtmltopdf`
import re

# Importation des sous fichiers python dont on a besoin :
import qrcodegenerator # on importe le fichier qrcodegenerator.py, ce qui nous permet d'accéder à la fonction extractURL
import meta_extractor # on importe le fichier meta_extractor.py, ce qui nous permet d'accéder à la fonction extractMETA
import txt_to_html # on importe le fichier txt_to_html.py, ce qui nous permet d'accéder à la fonction layout
import error_handler # on importe le module de gestion centralisée des erreurs

# On customise la largeur par défaut créée par wkhtmltopdf qui est de base 1024
options = {
	'enable-local-file-access':'',
	#"xvfb": "",
    'crop-w': '576', # On veut une largeur de 576 pixels
	'quality': '100'
}

# On définit le dossier où sont les fichiers (textes et images) importés
input_folder = './input/' + sys.argv[1]
metadatas_list = {}
errors_file = './images/errors.json'

def addLogging(filename, logDict:dict):
		loggingsFile = './images/' + sys.argv[1] + '/list.json'
		data = {}

		if os.path.isfile(loggingsFile) :
				with open(loggingsFile) as f:
						data = json.load(f)

		data[filename] = logDict

		with open(loggingsFile, 'w') as f:
				json.dump(data, f)

# B- On s'occupe des fichiers .txt et .md
for subdir, dirs, files in os.walk(input_folder): # Pour chaque chemin, dossiers et fichiers dans ./input_folder
	for filename in files: # et pour chaque nom de fichier pour chaque fichier
		fullpath = subdir + os.sep + filename # on enregistre le chemin du fichier, son nom et son extension dans une variable de type str 

		print(fullpath)

		# Accepter .txt et .md
		if re.search(r'\.(txt|md)$', fullpath, re.IGNORECASE):
			
			# 1- On extraire l'URL pour générer un QRCode et les métadonnées
			try:
				with open(fullpath, 'r', encoding='utf-8') as myfile:
					metadatas, body = meta_extractor.extractMETA(myfile, sys.argv[1]) # Récupération des métadonnées ET body
					metadatas_list[os.path.splitext(filename)[0]] = metadatas
			except ValueError as e:
				# Extraction des infos d'erreur du message d'erreur
				error_msg = str(e)
				# Passer le filename AVEC extension
				error_handler.log_error(sys.argv[1], filename, 'format', error_msg)
				continue  # Passer au fichier suivant
			except Exception as e:
				error_handler.log_error(sys.argv[1], filename, 'lecture', f"Erreur lors de la lecture du fichier: {str(e)}")
				continue
			
			# 2- Génération du QR code
			try:
				qrcodegenerator.createQrCode(metadatas['url'], filename, sys.argv[1])
			except Exception as e:
				error_handler.log_error(sys.argv[1], filename, 'qrcode', f"Erreur lors de la génération du QR code: {str(e)}")
				continue
			
			# 3- On convertit 'input/filename.txt|md' > 'output/filename.html'
			try:
				txt_to_html.layout(fullpath, sys.argv[1], metadatas, body)
			except Exception as e:
				error_handler.log_error(sys.argv[1], filename, 'mise en page', f"Erreur lors de la conversion HTML: {str(e)}")
				continue

# C- On s'occupe ensuite de convertir /output/*.html en ./images/*.jpg
for subdir, dirs, files in os.walk('./output/' + sys.argv[1]): # Pour chaque chemin, dossiers et fichiers dans ./output/
	for filename in files: # et pour chaque nom de fichier
		
		outputfile = subdir + os.sep + filename # on aggrège le chemin d'accès du fichier dans ./output/ avec son nom et extension
		jpgfile = './images/' + sys.argv[1] + '/' + os.path.splitext(filename)[0] + '.jpg' # on retire .html du filename pour mettre .jpg et on ajoute le chemin vers ./images/
		# Recomposer le nom original du fichier source (article.md ou article.txt)
		filename_without_html = os.path.splitext(filename)[0]  # Retirer .html
		
		try:
			imgkit.from_file(outputfile, jpgfile, options=options) # on convertit outputfile en jpgfile
			print(jpgfile + " > converted!")
			addLogging(filename_without_html, metadatas_list[filename_without_html])
		except Exception as e:
			# Chercher le fichier original pour récupérer son extension
			original_filename = None
			for fn in files:
				if os.path.splitext(fn)[0] == filename_without_html and re.search(r'\.(txt|md)$', fn, re.IGNORECASE):
					original_filename = fn
					break
			if original_filename is None:
				original_filename = filename_without_html  # Fallback si pas trouvé
			error_handler.log_error(sys.argv[1], original_filename, 'conversion', f"Erreur lors de la conversion JPG: {str(e)}")

