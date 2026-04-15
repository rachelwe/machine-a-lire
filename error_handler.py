import os
import json
from datetime import datetime


# Formate un message d'erreur.
# Exemple: format_error("url", "URL invalide")
def format_error(key, message):
	return f"{key} : {message}"


# Enregistre une erreur dans le fichier errors.json centralisé.
# Exemple: log_error('autrices', '001.md', 'url', 'URL invalide')
def log_error(collection, filename, key, message, errors_file='./images/errors.json'):
	try:
		# Initialiser le fichier d'erreurs s'il n'existe pas
		if not os.path.isfile(errors_file):
			with open(errors_file, 'w') as f:
				json.dump([], f)
		
		# Lire le fichier d'erreurs
		with open(errors_file, 'r') as f:
			errors_data = json.load(f)
		
		# Chercher ou créer l'entrée de la collection
		collection_entry = None
		for entry in errors_data:
			if entry.get('collection') == collection:
				collection_entry = entry
				break
		
		if collection_entry is None:
			collection_entry = {'collection': collection, 'errors': []}
			errors_data.append(collection_entry)
		
		# Ajouter l'erreur
		error_entry = {
			'filename': filename,
			'key': key,
			'message': message,
			'timestamp': datetime.now().isoformat()
		}
		collection_entry['errors'].append(error_entry)
		
		# Écrire le fichier d'erreurs
		with open(errors_file, 'w') as f:
			json.dump(errors_data, f, indent=2, ensure_ascii=False)
		
	except Exception as e:
		print(f"Erreur lors de l'enregistrement de l'erreur: {str(e)}")
