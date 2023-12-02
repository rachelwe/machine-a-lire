import re
import os

def createHeader(currentFile, metadatas):
	
	divEntete = '<header class="entete">\n<p class="tag">'+metadatas['category']+'</p>\n</header>'
	return(divEntete)

# POUR REMETTRE LES BONNES BALISES
def rearrangeMardownOrder(myfile, metadatas):			
	fin = open(myfile, 'r') # On ouvre le fichier en lecture
	data = fin.read() # On copie le contenu lu dans la variable data
	fin.close() # On ferme le fichier
	
	fin = open(myfile, 'w') # On réouvre ce fichier avec les droits d'écriture

	data = re.sub(r"^AUTEUR.*\n?|^CATEGORIE.*\n?|^BIO.*\n?|^URL.*\n?|^IMAGE.*\n?|^# .*\n?", "", data, flags=re.MULTILINE)
	
	fin.write('\n'+data) # On insert une ligne vide au début du document et le contenu de la variable data
	fin.close() # On ferme le fichier
	
	fin = open(myfile, 'r') # On le réréouvre 
	data = fin.read() # On le relit (avec la nouvelle ligne en haut du coup)

	title = '<h1 class="title">'+metadatas['title']+'</h1>'
	author = '<p class="author">'+metadatas['author']+'</p>'
	bio = '<figure class="blocplus">\n<img src="../assets/spacer-2.png">\n</figure><p class="bio">'+metadatas['bio']+'</p>'

	if 'img' in metadatas:
		thumbnail = '<figure class="thumbnail">\n<img src="../articles-images/'+metadatas['img']+'">\n</figure>\n<div class="blocplus">\n<img src="../assets/spacer-1.png">\n</div>'
	else:
		thumbnail = ''
	
	# On stocke dans data les nouveaux changements de markdown sans que ça change le texte du fichier initial
	
	#POUR CREER DIV AVEC TAG + DATE
	# ON APPELLE NOTRE SUPER METHODE ICI
	header = createHeader(myfile, metadatas)
	
	fin.close() # On referme le fichier

	fin = open(myfile, 'w') # On l'ouvre une dernière fois avec les privilèges d'écriture
	fin.write(header+thumbnail+title+author+data+bio) # On  écrit toutes les modifications contenues dans data
	fin.close() # On ferme, ce qui enregistre

#rearrangeMardownOrder('/home/alca/Documents/machine-a-lire/articles/ALIMENTATION-18860115-ARROSOIR-p1-la-republique-est-morte.txt')
