#!/usr/bin/python3
'''
Code created by Matt Richardson 
for details, visit:  http://mattrichardson.com/Raspberry-Pi-Flask/inde...
'''
from flask import Flask, render_template
import datetime
import subprocess
import os
app = Flask(__name__)
@app.route("/")
def hello():
   
   # Get the list of all files and directories
   path = "/home/pi/Documents/machine-a-lire/images/"
   dir_list = os.listdir(path)
   now = datetime.datetime.now()
   timeString = now.strftime("%d/%m/%Y %H:%M")
   templateData = {
      'title' : 'Machine à lire',
      'time': timeString,
      'files': dir_list
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
