from escpos.printer import Usb # import Usb class
import os
import sys
import json
import random
from PIL import Image

# vendor and product ID allow us to communicate with the printer
p = Usb(0x04b8, 0x0e28, 0)

# Get the list of all files and directories
path = "/home/pi/Documents/machine-a-lire/images/list.json"

with open(path) as f:
		data = json.load(f)

# Function that prints a selected article when it is called;
def printFile():
	
	# RANDOM PRINTING
	if len(sys.argv) > 1:
		if sys.argv[1] == 'random':			
			random_index = random.randint(0, len(data) - 1);
			selected = list(data)[random_index]

			article = Image.open("/home/pi/Documents/machine-a-lire/images/" + selected + ".jpg")
			article = article.rotate(180)
			p.image(article) # article is the fullpath of the selected article
			p.cut()

			print(data[selected]['title'])
		else:
			try:
					article = Image.open("/home/pi/Documents/machine-a-lire/images/" + sys.argv[1] + ".jpg")
					article = article.rotate(180)
					p.image(article) # article is the fullpath of the selected article
					p.cut()

					print(data[sys.argv[1]]['title'])
			except OSError:
					print('')
	else:
		print('')


printFile()