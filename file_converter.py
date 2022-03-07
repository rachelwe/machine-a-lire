import os
import json
import imgkit # à installer à la main via `sudo apt-get install wkhtmltopdf`

# Importation des sous fichiers python dont on a besoin :
import qrcodegenerator # on importe le fichier qrcodegenerator.py, ce qui nous permet d'accéder à la fonction extractURL
import meta_extractor # on importe le fichier qrcodegenerator.py, ce qui nous permet d'accéder à la fonction extractURL
import txt_to_html # on importe le fichier txt_to_html.py, ce qui nous permet d'accéder à la fonction layout

# On customise la largeur par défaut créée par wkhtmltopdf qui est de base 1024
options = {
	'enable-local-file-access':'',
	#"xvfb": "",
    'crop-w': '576', # On veut une largeur de 576 pixels
	'quality': '100'
}

# On définit le dossier où sont les fichiers (textes et images) importés
input_folder = './input'
metadatas_list = {}

def addLogging(filename, logDict:dict):
		loggingsFile = './images/list.json'
		data = {}

		if os.path.isfile(loggingsFile) :
				with open(loggingsFile) as f:
						data = json.load(f)

		data[filename] = logDict

		with open(loggingsFile, 'w') as f:
				json.dump(data, f)

# B- On s'occupe des fichiers .txt
for subdir, dirs, files in os.walk(input_folder): # Pour chaque chemin, dossiers et fichiers dans ./input_folder
	for filename in files: # et pour chaque nom de fichier pour chaque fichier
		fullpath = subdir + os.sep + filename # on enregistre le chemin du fichier, son nom et son extension dans une variable de type str 

		print(fullpath)

		if fullpath.endswith(".txt"): # Si le fichier finit par .txt
			
			# 1- On extraie l'URL pour générer un QRCode
			with open(fullpath, 'r') as myfile: # on ouvre le fichier

				metadatas = meta_extractor.extractMETA(myfile) # Récupération des métadonnées
				metadatas_list[os.path.splitext(filename)[0]] = metadatas

				qrcodegenerator.createQrCode(metadatas['url'], filename) # Génération du QR code
			
			# 2- On convertit 'input/filename.txt' > 'output/filename.html'
			txt_to_html.layout(fullpath, input_folder, subdir, metadatas)

# C- On s'occupe ensuite de convertir /output/*.html en ./images/*.jpg
for subdir, dirs, files in os.walk('./output'): # Pour chaque chemin, dossiers et fichiers dans ./output/
	for filename in files: # et pour chaque nom de fichier
		
		outputfile = subdir + os.sep + filename # on aggrège le chemin d'accès du fichier dans ./output/ avec son nom et extension
		jpgfile = './images/' + os.path.splitext(filename)[0] + '.jpg' # on retire .html du filename pour mettre .jpg et on ajoute le chemin vers ./images/
		#print(type(outputfile))
		#print(type(jpgfile))
		imgkit.from_file(outputfile, jpgfile, options=options) # on convertit outputfile en jpgfile
		print(jpgfile + " > converted!")
		addLogging(os.path.splitext(filename)[0], metadatas_list[os.path.splitext(filename)[0]])
		#imgkit.from_file('./output/'+filename+'.html', './images/'+filename+'.jpg')

