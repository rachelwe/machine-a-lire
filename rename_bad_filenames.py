import os

dossier= '/home/pi/Documents/machine-a-lire/input'

for f in os.listdir(dossier):
	os.rename(os.path.join(dossier, f), os.path.join(dossier, f).replace(' ', '-'))

