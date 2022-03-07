def extractMETA(myfile):  # On récupère comme argument le fichier et le nom du fichier
	# On formate le nom du fichier pour pouvoir nommer notre qrcode de la même façon avec extension différente
	# print(formatted_filename)
	#line = myfile.readline()  # On stocke ligne par ligne myfile dans line
	meta = {}
	for line in myfile.readlines(): # tant qu'il y a des lignes
		#line = myfile.readline() # On les lit**
		if line.startswith("# "): # Si on détecte une ligne qui commence par 4#,
			meta["title"] = line.replace('# ', '') # On supprime les #### de cette ligne
			
		elif line.startswith("AUTEUR "):
			meta["author"] = line.replace('AUTEUR ', '')
		elif line.startswith("CATEGORIE "):
			meta["category"] = line.replace('CATEGORIE ', '')
		elif line.startswith("BIO "):
			meta["bio"] = line.replace('BIO ', '')
		elif line.startswith("URL "):
			meta["url"] = line.replace('URL ', '')
		elif line.startswith("IMAGE "):
			imgLine = line.replace('IMAGE ', '')
			meta["img"] = imgLine.replace('\n', '')
	return meta