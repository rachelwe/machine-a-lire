import pyqrcode 
import os

def createQrCode(urlstr, filenameURL):
	# nouveaux réglages / L a moins de correction que le M / 
	url = pyqrcode.create(urlstr, 'L', 12, None, None)
	url.png('./input/'+filenameURL.replace('.txt', '.png'), scale=3)
	
	# anciens réglages :
	#url = pyqrcode.create(urlstr, 'M', 10, None, None) # On crée un qrcode avec l'url d'encodée
	#url.png('./input/'+filenameURL+'.png', scale=1) # On l'enregistre dans input sous nomformaté.png
	#print(url.terminal(quiet_zone=1)) # debug pour afficher le qrcode dans terminal
			
