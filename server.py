#!/usr/bin/python3
'''
Code created by Matt Richardson 
for details, visit:  http://mattrichardson.com/Raspberry-Pi-Flask/inde...
'''
from flask import Flask, render_template
import subprocess
import os
import json
app = Flask(__name__)
@app.route("/")
def hello():
   
   # Get the list of all files and directories
   path = "/home/pi/Documents/machine-a-lire/images/list.json"

   with open(path) as f:
      data = json.load(f)

   templateData = {
      'title' : 'Machine à lire',
      'description': 'Lorem ipsum dolor sit amet consectetur, adipisicing elit. Vel cumque, facilis vitae accusantium voluptatem quae consequatur alias accusamus nemo autem modi totam sequi mollitia quas earum enim cum minima harum.',
      'files': data
   }
   return render_template('index.html', **templateData)

@app.route("/print/<url>")
def print(url):
    cmd = ["python3","test.py", url]
    p = subprocess.Popen(cmd, stdout = subprocess.PIPE,
                            stderr=subprocess.PIPE,
                            stdin=subprocess.PIPE)
    out,err = p.communicate()
    return out

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=8888, debug=True)
