#!/usr/bin/python

import cgi
import cgitb
import os
import subprocess
from time import sleep


cgitb.enable()  # for troubleshooting
form = cgi.FieldStorage()

def fbuffer(f, chunk_size=10000):
    while True:
        chunk = f.read(chunk_size)
        if not chunk: break
        yield chunk

fileitem = form['filename']

if fileitem.filename:
    fn = os.path.basename(fileitem.filename)
    f = open('files/' + fn, 'wb', 10000)

    for chunk in fbuffer(fileitem.file):
        f.write(chunk)
    f.close()
    message = 'The file "' + fn + '" was uploaded successfully'
else:
    message = 'No file was uploaded'


print "Content-type: text/html"
print

print """
<!DOCTYPE html>
<html>
<body>
    <p>%s</p>
</body>
</html>
"""%(message,)
