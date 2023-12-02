#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
Code created by Matt Richardson 
for details, visit:  http://mattrichardson.com/Raspberry-Pi-Flask/inde...
'''
from flask import Flask, render_template, send_from_directory
import subprocess
import os
import json
app = Flask(__name__)
@app.route("/")
def hello():
   
   # Get the list of all files and directories
   path = "/home/alca/Documents/machine-a-lire/images/list.json"

   with open(path) as f:
      data = json.load(f)

   templateData = {
      'title' : 'Machine à lire',
      'description': 'Un ticket-voyage proposé par La Bibilothèque patrimoniale numérique d\'Alca en nouvelle-Aquitaine. Cliquez sur le titre qui vous intéresse pour l\'imprimer !',
      'files': data
   }
   return render_template('index.html', **templateData)

@app.route("/print/<url>")
def print(url):
    cmd = ["python3","print.py", url]
    p = subprocess.Popen(cmd, stdout = subprocess.PIPE,
                            stderr=subprocess.PIPE,
                            stdin=subprocess.PIPE)
    out,err = p.communicate()
    return out + err

@app.route('/articles-images/<path:filename>')
def download_file(filename):
   return send_from_directory('articles-images', filename, as_attachment=True)

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=8888, debug=True)
