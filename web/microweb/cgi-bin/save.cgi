#!/usr/bin/python

import cgi
import cgitb
import os
import subprocess
from time import sleep


HOME_DIR = os.getenv("SYNCHRONIZED_LIGHTS_HOME")
SAVE_DIR = HOME_DIR 
cgitb.enable()  
form = cgi.FieldStorage()

def fbuffer(f, chunk_size=10000):
    while True:
        chunk = f.read(chunk_size)
        if not chunk: break
        yield chunk

fileitem = form['filename']

if fileitem.filename:
    fn = os.path.basename(fileitem.filename)
    
    if os.path.exists(HOME_DIR+'/music/tracks'+fn):
        
        message = "File already exists"
    else:
        f = open(HOME_DIR + '/music/tracks/' + fn, 'wb')
        for chunk in fbuffer(fileitem.file):
          f.write(chunk)
        f.close()
        message = 'The file "' + fn + '" was uploaded successfully'
        file = open(HOME_DIR + '/music/' +'.playlist', "a")
        file.write(fn) 
        file.write('\t$SYNCHRONIZED_LIGHTS_HOME/music/tracks/' + fn + '\n')
        file.close()
        file = open(HOME_DIR + '/music/' +'.playlist', "r") 
        line = file.readline()
        file.close()
        
else:
    message = 'No file was uploaded'


print "Content-type: text/html"
print
print """
<!DOCTYPE html>
<html>
<body>
    <center>
    <h2> Web Controls </h2>
    <h3> %s uploaded </h3>
    <form method="post" action="web_controls.cgi">
    <input id="playlist" type="submit" value="Back">
    </form>
    </center>
</body>
</html>
"""%(message,)
