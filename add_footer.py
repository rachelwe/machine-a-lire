
from get_config_files import get_config
def vertical(formatted_filename, output_file, metadatas, collection):
	config_collection = get_config(collection)
	output_file.write('<div class="blocplus">\n<img src="../../assets/spacer-2.png">\n</div>')
		
	output_file.write('<div class="ticket">\n<p>' + config_collection.get('ticketDescription', "").replace("\n", "</p><p>") + '</p>\n</div>')
	output_file.write('<div class="italic">\n<p>' + config_collection.get('ticketAvertissement', 'Ticket lecteur à conserver - ne pas jeter sur la voie publique').replace("\n", "</p><p>") + '</p>\n</div>')
	
	output_file.write('<div class="blocplus">\n<img src="../../assets/spacer-1.png">\n</div>') # ligne + + + + +

	if config_collection.get('ticketLogos1'):
		for logo in config_collection.get('ticketLogos1', []):
			output_file.write('<div class="logo">\n<img src="../../articles-images/' + collection + '/' + logo + '">\n</div>') # on insère le logo
		
		output_file.write('<div class="blocplus">\n<img src="../../assets/spacer-1.png">\n</div>') # ligne + + + + +
	
	# et les mentions légales

	if config_collection.get('ticketMentionsLegales'):
		output_file.write('<div class="mentions">\n<p>' + config_collection.get('ticketMentionsLegales', '').replace("\n", "</p><p>") + '</p>\n</div>')

		output_file.write('<div class="blocplus">\n<img src="../../assets/spacer-1.png">\n</div>') # ligne + + + + +
		
	if config_collection.get('ticketLogos2'):
		for logo in config_collection.get('ticketLogos2', []):
			output_file.write('<div class="bloclogo">\n<img src="../../articles-images/' + collection + '/' + logo + '">\n</div>')
	
		output_file.write('<div class="blocplus">\n<img src="../../assets/spacer-1.png">\n</div>') # ligne + + + + +
	
	
	# et le QRcode (seulement si une URL est présente)
	if metadatas['url']:
		qrcode = "../../input/" + collection + "/" + formatted_filename + ".png" # on recrée le chemin d'accès vers le qrcode depuis ./input/
		output_file.write('<div class="qrcode">\n<img src="' + qrcode + '">\n</div><p class="url">\n' + metadatas['url'] + '\n</p>') # on insère le chemin d'accès du qrcode dans une balise img et on affiche l'url en clair à la suite
		
	# F- On écrit la fin de notre balise body
	output_file.write("\n</body>")
				
	# G- On ferme le fichier .html
	output_file.close()
