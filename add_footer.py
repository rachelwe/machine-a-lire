def vertical(formatted_filename, output_file):
	output_file.write('<div class="blocplus">\n<img src="../assets/spacer-2.png">\n</div>')
		
	output_file.write('<div class="ticket">\n<p>Un ticket-poème proposé par La Bibliothèque patrimoniale numérique d\'Alca en nouvelle-Aquitaine. Pour plus de découvertes et pour télécharger des livres numériques gratuitement et librement : <u>alca-nouvelle-aquitaine.fr/fr/catalogue-numerique-patrimonial</u>\n</div>')
	output_file.write('<div class="italic">\n<p>Ticket lecteur à conserver - ne pas jeter sur la voie publique</p>\n</div>')
	
	output_file.write('<div class="blocplus">\n<img src="../assets/spacer-1.png">\n</div>') # ligne + + + + +
		
	output_file.write('<div class="logo">\n<img src="../assets/logos-machine.png">\n</div>') # on insère le logo
	
	output_file.write('<div class="blocplus">\n<img src="../assets/spacer-1.png">\n</div>') # ligne + + + + +
	
	# et les mentions légales
	output_file.write('<div class="mentions">\n<p>ALCA an Nouvelle-Aquitaine est une agence unique couvrant les industries du livre, du cinéma et de l’audiovisuel pour une politique territoriale cohérente, coordonnée et visant tout à la fois l’équilibre géographique des actions en direction des industries culturelles de la nouvelle Région, l’équilibre de sa politique du livre et de l’image animée au service de toutes les populations.</p><p>ALCA est aussi là pour prouver que dans un monde de plus en plus globalisé, numérisé, on peut tirer avantage de la disparition des barrières et rassembler le plus grand nombre autour d’un enjeu de civilisation : la préservation de nos singularités culturelles.</p>\n</div>')
	output_file.write('<div class="mentions">\n<p>Un projet adapté de "L\'Exprimante" Lectura Plus</p>\n</div>')

	output_file.write('<div class="blocplus">\n<img src="../assets/spacer-1.png">\n</div>') # ligne + + + + +
		
	
	output_file.write('<div class="bloclogo">\n<img src="../assets/logos-admin.png">\n</div>')
	
	output_file.write('<div class="blocplus">\n<img src="../assets/spacer-1.png">\n</div>') # ligne + + + + +
	
	
	# et le QRcode
	qrcode = "../input/" + formatted_filename + ".png" # on recrée le chemin d'accès vers le qrcode depuis ./input/
	output_file.write('<div class="qrcode">\n<img src="' + qrcode + '">\n</div>') # on insère le chemin d'accès du qrcode dans une balise img
		
	# F- On écrit la fin de notre balise body
	output_file.write("\n</body>")
				
	# G- On ferme le fichier .html
	output_file.close()
