#!/usr/bin/python

#
# Licensed under the BSD license.  See full license in LICENSE file.
# http://www.lightshowpi.org/
#
# Author: Ken B

import cgi
import cgitb
import os
import subprocess
from time import sleep
import json

filename = 'setting.json'

def readValue(key):
    with open(filename) as jsonfile:
        settings = json.load(jsonfile)
    value = settings[key]
    return value

def writeValue(key, value):
    with open(filename) as jsonfile:
        settings = json.load(jsonfile)
    settings[key] = value
    with open(filename, 'w') as jsonfile:
        json.dump(settings, jsonfile)

print(readValue('lightToggle'))

cgitb.enable()  # for troubleshooting
form = cgi.FieldStorage()
message = form.getvalue("message", "")

HOME_DIR = os.getenv("SYNCHRONIZED_LIGHTS_HOME")
volume = subprocess.check_output([HOME_DIR + '/bin/vol'])
lightIcon = "ion-ios-lightbulb-outline"
lightToggle = readValue('lightToggle')

if message:
    if message == "Volume -":
        if int(volume) - 5 < 0:
            volume = "0"
        else:
            volume = str(int(volume) - 5)
        os.system(HOME_DIR + '/bin/vol ' + volume)
    if message == "Volume +":
        if int(volume) + 5 > 100:
            volume = "100"
        else:
            volume = str(int(volume) + 5)
        os.system(HOME_DIR + '/bin/vol ' + volume)
    if message == "toggle":
        os.system('pkill -f "bash $SYNCHRONIZED_LIGHTS_HOME/bin"')
        os.system('pkill -f "python $SYNCHRONIZED_LIGHTS_HOME/py"')
        if lightToggle == True:
            lightIcon = "ion-ios-lightbulb-outline"
            writeValue('lightToggle', False)
            os.system("python ${SYNCHRONIZED_LIGHTS_HOME}/py/hardware_controller.py --state=off")
        else:
            lightIcon = "ion-ios-lightbulb"
            writeValue('lightToggle', True)
            os.system("python ${SYNCHRONIZED_LIGHTS_HOME}/py/hardware_controller.py --state=on")
    if message == "Off":
        lightIcon = "ion-ios-lightbulb-outline"
        writeValue('lightToggle', False)
        os.system("python ${SYNCHRONIZED_LIGHTS_HOME}/py/hardware_controller.py --state=off")
        os.system('pkill -f "bash $SYNCHRONIZED_LIGHTS_HOME/bin"')
        os.system('pkill -f "python $SYNCHRONIZED_LIGHTS_HOME/py"')
        os.system("python ${SYNCHRONIZED_LIGHTS_HOME}/py/hardware_controller.py --state=off")
    if message == "Next":
        os.system('pkill -f "python $SYNCHRONIZED_LIGHTS_HOME/py"')
        sleep(1)
    if message == "Start":
        os.system('pkill -f "bash $SYNCHRONIZED_LIGHTS_HOME/bin"')
        os.system('pkill -f "python $SYNCHRONIZED_LIGHTS_HOME/py"')
        os.system("${SYNCHRONIZED_LIGHTS_HOME}/bin/play_sms &")
        os.system("${SYNCHRONIZED_LIGHTS_HOME}/bin/check_sms &")
        sleep(1)

print "Content-type: text/html"
print

print """
<!DOCTYPE html>
<html>

<head>
	<title>Stage Light Controller</title>

	<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">
	<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap-theme.min.css" integrity="sha384-rHyoN1iRsVXV4nD0JutlnGaslCJuC7uwjduW9SVrLvRYooPp2bWYgmgJQIXwl/Sp" crossorigin="anonymous">
	<link rel="stylesheet" href="http://code.ionicframework.com/ionicons/2.0.1/css/ionicons.min.css" crossorigin="anonymous">
	<link rel="stylesheet" type="text/css" href="/css/teststyle.css">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body class="myContainer">
	<div class="container">
		<div class="row" align="center">
			<div class="col-lg-4 col-lg-push-4 col-sm-12">

				<div class="row">
                                    <form action="testcontrol.cgi" method="post">"""

cmd = 'pgrep -f "python $SYNCHRONIZED_LIGHTS_HOME/py/synchronized_lights.py"'
if os.system(cmd) == 0:
    print """
                                        <button type="submit" name="message" value="Play Next" id="playbutton" class="btn btn-default button1"><span id="playicon" class="glyphicon glyphicon-forward"></span></button>
"""
else:
    print """
                                        <button type="submit" name="message" value="Start" id="playbutton" class="btn btn-default button1"><span id="playicon" class="glyphicon glyphicon-play"></span></button>
    """
print """
                                        <button type="submit" name="message" value="Volume +" class="btn btn-default button1"> <span class="glyphicon glyphicon-volume-up"></span></button>
                                        <button type="submit" name="message" value="Volume -" class="btn btn-default button1"> <span class="glyphicon glyphicon-volume-down"></span></button>
                                        <button type="submit" name="message" value="toggle" class="btn btn-default button1"><i id="lighticon" class="ionicons %s"></i></button>
                                        <button type="submit" name="message" value="Off" class="btn btn-default button1"> <span class="glyphicon glyphicon-stop"></span></button>
                                    </form>
                                        
				</div>
				<div class="row">
					<form action="playlist.cgi" method="post">
						<button type="submit" class="btn btn-default button2"><span class="glyphicon glyphicon-list"></span>&nbsp Back To Playlist</button>
					</form>
				</div>
				<div class="row">
					<form action="upload_music.cgi" method="post">
						<button type="submit" class="btn btn-default button2"><span class="glyphicon glyphicon-cloud-upload"></span>&nbsp Upload Track</button>
					</form>
				</div>
				<div class="row">
					<div class="volume-label">
						Volume: %s %s %s
					</div>
				</div>
			</div>
		</div>
	</div>
	<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>
	<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js" integrity="sha384-Tc5IQib027qvyjSMfHjOMaLkfuWVxZxUPnCJA7l2mCWNIpG9mGCD8wGNIcPD7Txa" crossorigin="anonymous"></script>
</body>

</html>"""%(lightIcon, volume,cgi.escape(message),readValue('lightToggle'))
