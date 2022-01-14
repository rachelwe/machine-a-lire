'''
Code created by Matt Richardson 
for details, visit:  http://mattrichardson.com/Raspberry-Pi-Flask/inde...
'''
from flask import Flask, render_template
import datetime
import subprocess
app = Flask(__name__)
@app.route("/")
def hello():
   now = datetime.datetime.now()
   timeString = now.strftime("%d/%m/%Y %H:%M")
   templateData = {
      'title' : 'Données - qualité de l\'air',
      'time': timeString
      }
   return render_template('index.html', **templateData)

# @app.route("/screen")
# def screen():
#     cmd = ["sh","/home/pi/Documents/launcher-display.sh"]
#     p = subprocess.Popen(cmd, stdout = subprocess.PIPE,
#                             stderr=subprocess.PIPE,
#                             stdin=subprocess.PIPE)
#     out,err = p.communicate()
#     errcode = process.returncode
#     while process.returncode is None:
#     # handle output by direct access to stdout and stderr
#        for line in process.stdout:
#           return line
#     # set returncode if the process has exited
#     process.poll()
#     return out

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=8080, debug=True)
