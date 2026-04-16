#!/usr/bin/python3
from flask import Flask, render_template, request, redirect, send_from_directory
from get_config_files import get_config
import subprocess
import os
import json
import datetime
import yaml
app = Flask(__name__)

def get_image_folders():
   images_path = "/home/pi/Documents/machine-a-lire/images"
   folders = []
   try:
      if os.path.isdir(images_path):
         for folder_name in os.listdir(images_path):
            folder_path = os.path.join(images_path, folder_name)
            
            # Traiter uniquement les dossiers
            if not os.path.isdir(folder_path):
               continue
            
            # Compter les fichiers JPG dans le dossier
            jpg_files = [file for file in os.listdir(folder_path) 
                        if file.lower().endswith('.jpg')]
            jpg_count = len(jpg_files)
            
            # Charger la configuration de la collection
            config = get_config(folder_name)
            collection_name = (config.get('collectionNom', folder_name) 
                              if isinstance(config, dict) else folder_name)
            
            # Ajouter à la liste
            folders.append({
               'path': folder_name,
               'textCount': jpg_count,
               'collectionNom': collection_name
            })
   except FileNotFoundError:
      folders = []
   return folders

def load_errors():
   errors_file = "/home/pi/Documents/machine-a-lire/images/errors.json"
   try:
      if os.path.isfile(errors_file):
         with open(errors_file, 'r') as f:
            return json.load(f)
   except Exception as e:
      print(f"Erreur lors du chargement de errors.json: {str(e)}")
   return []

@app.route("/")
def hello():
   
   # Get the list of all files and directories
   collections = get_image_folders()
   config = get_config()
   all_errors = load_errors()

   templateData = {
      'title' : 'Machine à lire',
      'collections': collections,
      'current_datetime': datetime.datetime.now(),
      'config': config,
      'all_errors': all_errors
   }
   return render_template('index.html', **templateData)


@app.route("/<collection>")
def collection(collection):
   
   # Get the list of all files and directories
   path = "/home/pi/Documents/machine-a-lire/images/" + collection + "/list.json"
   config_global = get_config()
   config_collection = get_config(collection)
   all_errors = load_errors()

   try:
      with open(path) as f:
         data = json.load(f)
   except FileNotFoundError:
      data = []

   templateData = {
      'title' : 'Machine à lire' + " - " + collection,
      'files': data,
      'collection': collection,
      'current_datetime': datetime.datetime.now(),
      'config_global': config_global,
      'config_collection': config_collection,
      'all_errors': all_errors
   }
   return render_template('collection.html', **templateData)

@app.route("/print/<collection>/<url>")
def print(collection, url):
    cmd = ["python3","print.py",collection,url]
    p = subprocess.Popen(cmd, stdout = subprocess.PIPE,
                            stderr=subprocess.PIPE,
                            stdin=subprocess.PIPE)
    out,err = p.communicate()
    return out + err

@app.route('/articles-images/<collection>/<path:filename>')
def download_file(collection, filename):
   return send_from_directory("articles-images/" + collection, filename, as_attachment=True)

@app.route('/config', methods=['POST'])
def edit_config():
   data1 = request.form.get('changementCollectionPossible') == 'on'
   data2 = request.form['collectionParDefaut']
   data3 = request.form['imprimante']

   config_file = "/home/pi/Documents/machine-a-lire/images/config.yml"
   
   with open(config_file, 'r') as f:
      config = yaml.safe_load(f)
   
   config['changementCollectionPossible'] = data1
   config['collectionParDefaut'] = data2
   config['imprimante'] = data3
   
   with open(config_file, 'w') as f:
      yaml.dump(config, f, default_flow_style=False, allow_unicode=True)
   
   return redirect("/")

@app.route('/archive-errors', methods=['POST'])
def archive_errors():
   """Archive le fichier errors.json avec un timestamp"""
   errors_file = "/home/pi/Documents/machine-a-lire/images/errors.json"
   try:
      if os.path.isfile(errors_file) and os.path.getsize(errors_file) > 0:
         timestamp = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
         archive_file = f"/home/pi/Documents/machine-a-lire/images/errors_{timestamp}.json"
         os.rename(errors_file, archive_file)
         return json.dumps({'status': 'success', 'message': f'Erreurs archivées vers {archive_file}'}), 200
      else:
         return json.dumps({'status': 'error', 'message': 'Aucune erreur à archiver'}), 400
   except Exception as e:
      return json.dumps({'status': 'error', 'message': str(e)}), 500
   


if __name__ == "__main__":
   app.run(host='0.0.0.0', port=8888, debug=True)
