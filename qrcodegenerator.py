import pyqrcode 
import re

def createQrCode(urlstr, filenameURL, collection):
	print("Création du QR code pour l'URL : " + urlstr) # debug
	# nouveaux réglages / L a moins de correction que le M / 
	url = pyqrcode.create(urlstr, 'L', 7, None, None) # On crée un qrcode avec l'url d'encodée
	url.png('./input/' + collection + '/' + re.sub(r'\.(txt|md)$', '.png', filenameURL), scale=7) # On l'enregistre dans input sous nomformaté.png
	
	#print(url.terminal(quiet_zone=1)) # debug pour afficher le qrcode dans terminal
	
	# anciens réglages :
	#url = pyqrcode.create(urlstr, 'M', 10, None, None) 
	#url.png('./input/'+filenameURL+'.png', scale=1) 
	
			
