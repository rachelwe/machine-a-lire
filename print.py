from escpos.printer import Usb # import Usb class
import os
import sys
import json
import random
from PIL import Image
from get_config_files import get_config

# vendor and product ID allow us to communicate with the printer
printers = {
	"TM-T20III": [0x04b8, 0x0e28],
	"TM-T20IV": [0x04b8, 0x0e39]
}
config = get_config()
try:
	p = Usb(printers[config['imprimante']][0], printers[config['imprimante']][1], 0)
except KeyError:
	print("Imprimante non configurée")
	sys.exit(1)

collection = sys.argv[1]

# Get the list of all files and directories
path = "/home/pi/Documents/machine-a-lire/images/" + collection + "/list.json"

with open(path) as f:
		data = json.load(f)

# Function that prints a selected article when it is called;
def printFile():
	# RANDOM PRINTING
	if len(sys.argv) > 2:
		if sys.argv[2] == 'random':			
			random_index = random.randint(0, len(data) - 1);
			selected = list(data)[random_index]

			article = Image.open("/home/pi/Documents/machine-a-lire/images/" + collection + "/" + selected + ".jpg")
			article = article.rotate(180)
			p.image(article) # article is the fullpath of the selected article
			p.cut()

			print(data[selected]['titre'])
		else:
			try:
					article = Image.open("/home/pi/Documents/machine-a-lire/images/" + collection + "/" + sys.argv[2] + ".jpg")
					article = article.rotate(180)
					p.image(article) # article is the fullpath of the selected article
					p.cut()

					print(data[sys.argv[2]]['titre'])
			except OSError:
					print('')
	else:
		print('')


printFile()