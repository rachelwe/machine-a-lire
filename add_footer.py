def vertical(formatted_filename, output_file, metadatas):
	output_file.write('<div class="blocplus">\n<img src="../assets/spacer-2.png">\n</div>')
		
	output_file.write('<div class="ticket">\n<p>Un ticket-poème proposé par La Bibliothèque patrimoniale numérique d\'Alca en Nouvelle-Aquitaine. Pour plus de découvertes et pour télécharger des livres numériques gratuitement et librement : <u>alca-nouvelle-aquitaine.fr/fr/catalogue-numerique-patrimonial</u>\n</div>')
	output_file.write('<div class="italic">\n<p>Ticket lecteur à conserver - ne pas jeter sur la voie publique</p>\n</div>')
	
	output_file.write('<div class="blocplus">\n<img src="../assets/spacer-1.png">\n</div>') # ligne + + + + +
		
	output_file.write('<div class="logo">\n<img src="../assets/logos-machine.png">\n</div>') # on insère le logo
	
	output_file.write('<div class="blocplus">\n<img src="../assets/spacer-1.png">\n</div>') # ligne + + + + +
	
	# et les mentions légales
	# ATTENTION : toutes les apostrophes doivent être précédées d'un antislash \ pour ne pas être interprétées comme des guillemets fermant la fonction. Exemple : l\'agence.
	# Si cela n'est pas respecté, aucun fichier image ne sera généré.
	output_file.write('<div class="mentions">\n<p>Agence livre, cinéma et audiovisuel de la Région Nouvelle-Aquitaine, ALCA accompagne les professionnels de l\'image et de l\'écrit dans toutes les étapes de leur parcours et de leurs projets, de la création à la diffusion d\'oeuvres.</p><p>Interface privilégiée entre la stratégie culturelle de la Région Nouvelle-Aquitaine, la Drac et les professionnels concernés, Alca organise depuis ses sites d\'Angoulême, de Bordeaux, de Limoges et de Poitiers, le soutien aux industries du livre, du cinéma et de l\'audiovisuel. Les actions portées par ALCA visent un équilibre géographique en direction des industris culturelles de la région et le rayonnement de ses acteurs, en France et à l\'international.</p>\n</div>')
	output_file.write('<div class="mentions">\n<p>Un projet adapté de "L\'Exprimante" Lectura Plus</p>\n</div>')

	output_file.write('<div class="blocplus">\n<img src="../assets/spacer-1.png">\n</div>') # ligne + + + + +
		
	
	output_file.write('<div class="bloclogo">\n<img src="../assets/logos-admin.png">\n</div>')
	
	output_file.write('<div class="blocplus">\n<img src="../assets/spacer-1.png">\n</div>') # ligne + + + + +
	
	
	# et le QRcode
	qrcode = "../input/" + formatted_filename + ".png" # on recrée le chemin d'accès vers le qrcode depuis ./input/
	output_file.write('<div class="qrcode">\n<img src="' + qrcode + '">\n</div><p class="url">\n' + metadatas['url'] + '\n</p>') # on insère le chemin d'accès du qrcode dans une balise img et on affiche l'url en clair à la suite
		
	# F- On écrit la fin de notre balise body
	output_file.write("\n</body>")
				
	# G- On ferme le fichier .html
	output_file.close()
