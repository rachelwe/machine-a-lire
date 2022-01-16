from escpos.printer import Usb # import Usb class
import os
import sys
from PIL import Image

# vendor and product ID allow us to communicate with the printer
p = Usb(0x04b8, 0x0e28, 0)


# Function that prints a selected article when it is called;
# uses random_article.py and its selectRandomArticle function to pick a random article
def printFile():
	
	# RANDOM PRINTING
	if len(sys.argv) > 1:
		article = Image.open("/home/pi/Documents/machine-a-lire/images/" + sys.argv[1])
		article = article.rotate(180)
		p.image(article) # article is the fullpath of the selected article
		p.cut()
		#p.image("/home/pi/Documents/machine-a-lire/assets/marge-ticket.jpg")
		print('ticket imprimé !')
	else:
		print('pas de nom de fichier renseigné')


printFile()