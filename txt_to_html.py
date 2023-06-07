import os
import markdown # à installer à la main via `sudo apt-get install python3-markdown`
import update_markdown
import add_footer

# Fonction qui convertit notre fichier .txt courant dans ./input/ avec du texte en markdown à l'intérieur,
# en fichier .html balisé dans ./output/
def layout(fullpath, input_folder, subdir, metadatas):
	print("layout :" + fullpath)
	update_markdown.rearrangeMardownOrder(fullpath, metadatas) # on reformate le markdown utilisé pour un autre plus lisible
	
	# A- On ouvre le fichier pour récupérer le contenu
	with open(fullpath, 'r') as myfile:

		contents = myfile.read() # on récupère le contenu dans la variable contents
		#print('le fichier contient : '+contents) # debug
		filename = os.path.basename(myfile.name) # on récupère le chemin d'accès au fichier

	formatted_filename = os.path.splitext(filename)[0] # on retire l'extension (.txt) du nom+chemin d'accès du fichier
				
	# B- On crée et ouvre un fichier .html avec le même nom formaté que le fichier .txt actuel dans le dossier ./output/
	output_file = open(r'./output/'+formatted_filename+'.html', 'w') # avec les droits d'écriture

	# C- On ajoute et/ou crée le contenu
	header = r"<head><meta charset='UTF-8'><title>"+formatted_filename+"</title><link href='../stylesheet.css' rel='stylesheet'>\n</head>\n" # on charge stylesheet.css / white background & v display

	output_file.write(header) # et on l'écrit dans le fichier                                                   	
	
	output_file.write("<body>\n")

	html = markdown.markdown(contents)

	
	output_file.write(html) # on insère le HTML converti

	add_footer.vertical(formatted_filename, output_file, metadatas)
