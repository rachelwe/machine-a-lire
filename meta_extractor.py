import frontmatter
import os
from error_handler import format_error


def extractMETA(myfile, collection=""):
	# myfile est un file object déjà ouvert
	filename = myfile.name
	filename = filename.split('/')[-1]  # Garder juste le nom
	
	try:
		# Lire le contenu
		content = myfile.read()
		myfile.seek(0)  # Reset pour future utilisation
		
		# Parser comme markdown front-matter
		if not content.startswith('---'):
			raise ValueError(format_error('format', "Le fichier doit respecter la syntaxe markdown front-matter (doit commencer par ---, suivi des métadonnées, puis --- et enfin le contenu)"))
		
		try:
			post = frontmatter.loads(content)
			meta = dict(post.metadata)  # Copier les métadonnées du front-matter
			body = post.content  # Extraire le contenu (body) sans le frontmatter
			
			# Valider les clés requises
			required_keys = ['titre', 'auteur', 'categorie', 'url']
			optional_keys = ['image', 'bio']
			valid_keys = set(required_keys + optional_keys)
			
			# Vérifier les clés non supportées
			found_keys = set(meta.keys())
			unsupported_keys = found_keys - valid_keys
			if unsupported_keys:
				unsupported_list = ', '.join(sorted(unsupported_keys))
				valid_list = ', '.join(sorted(valid_keys))
				raise ValueError(format_error('Métadonnées', 
					f"<br>Clés non supportées trouvées: <br><strong>{unsupported_list}</strong><br>"
					f"(les clés valides autorisées sont : {valid_list})\n"))
			
			# Vérifier les clés requises
			for key in required_keys:
				if key not in meta or not meta[key]:
					raise ValueError(format_error(key, f"clé requise manquante"))
			
			# Nettoyer les valeurs (retirer espaces/newlines)
			for key in meta:
				if isinstance(meta[key], str):
					meta[key] = meta[key].strip()
			
			# image et bio sont optionnels, mettre à '' par défaut si absent
			if 'image' not in meta:
				meta['image'] = ''
			else:
				# Vérifier que le fichier image existe si spécifié
				if meta['image']:  # Si image n'est pas vide
					img_filename = meta['image']
					# Le fichier img doit être dans le dossier articles-images de la collection
					img_path = os.path.join('./articles-images', collection, img_filename)
					
					if not os.path.isfile(img_path):
						raise ValueError(format_error('image', f"Le fichier image '{img_filename}' n'existe pas (vérifiez que vous avez bien renseigné la bonne casse (majuscule, minuscule) et extension de fichier (.png, .jpg, .jpeg))"))
			
			if 'bio' not in meta:
				meta['bio'] = ''
			else:
				# la bio est le seul endroit où on peut avoir des retours à la ligne.
				# \n ne suffit pas pour la génération html 
				# donc on entre les paragraphes en dur
				meta['bio'] = meta['bio'].replace("\n", "</p><p class=\"bio\">") 
			
			return (meta, body)  # Retourner (metadata, body)
		except ValueError:
			raise  # Re-lever les ValueError (validations échouées)
		except Exception as e:
			raise ValueError(format_error('Métadonnées', f"markdown front-matter invalide: {str(e)}"))
		
	except ValueError:
		raise
	except Exception as e:
		raise ValueError(format_error('unknown', f"Erreur lors de la lecture: {str(e)}"))