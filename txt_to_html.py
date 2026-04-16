import os
import markdown # à installer à la main via `sudo apt-get install python3-markdown`
import add_footer

# Fonction qui convertit notre fichier .txt/.md dans ./input/ 
# avec du texte en markdown à l'intérieur,
# en fichier .html balisé dans ./output/
def layout(fullpath, collection, metadatas, body):
	print("layout :" + fullpath)
	# Récupérer le nom du fichier sans extension
	filename = os.path.basename(fullpath)
	formatted_filename = os.path.splitext(filename)[0]
	
	# Créer le fichier output HTML
	output_path = r'./output/' + collection + '/' + formatted_filename + '.html'
	output_file = open(output_path, 'w', encoding='utf-8')
	
	# 1- HEADER avec layout CSS
	header = (
		'<head><meta charset="UTF-8"><title>' + metadatas['titre'] + '</title>'
		'<link href="../../stylesheet.css" rel="stylesheet"></head>\n'
	)
	output_file.write(header)
	output_file.write('<body>\n')
	
	# 2- HEADER HTML avec catégorie
	header_html = '<header class="entete">\n<p class="tag">' + metadatas['categorie'] + '</p>\n</header>\n'
	output_file.write(header_html)
	
	# 3- THUMBNAIL (si image disponible)
	if metadatas['image']:
		thumbnail = (
			'<figure class="thumbnail">\n'
			'<img src="../../articles-images/' + collection + '/' + metadatas['image'] + '">\n'
			'</figure>\n<div class="blocplus">\n<img src="../../assets/spacer-1.png">\n</div>\n'
		)
		output_file.write(thumbnail)
	
	# 4- TITLE
	title_html = '<h1 class="title">' + metadatas['titre'] + '</h1>\n'
	output_file.write(title_html)
	
	# 5- AUTHOR
	author_html = '<p class="author">' + metadatas['auteur'] + '</p>\n'
	output_file.write(author_html)
	
	# 6- BODY (convertir le markdown en HTML)
	body_html = markdown.markdown(body.strip())
	output_file.write(body_html + '\n')
	
	# 7- BIO (si disponible)
	if metadatas['bio']:
		bio_html = (
			'<figure class="blocplus">\n<img src="../../assets/spacer-2.png">\n</figure>'
			'<p class="bio">' + metadatas['bio'] + '</p>\n'
		)
		output_file.write(bio_html)
	
	# 8- FOOTER (ticket, logos, mentions légales, QR code)
	add_footer.vertical(formatted_filename, output_file, metadatas, collection)
