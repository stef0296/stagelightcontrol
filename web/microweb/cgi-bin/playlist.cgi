#!/usr/bin/python

import cgi
import cgitb
import os
import sys
import fcntl
import csv
from time import sleep

HOME_DIR = os.getenv("SYNCHRONIZED_LIGHTS_HOME")
sys.path.insert(0, HOME_DIR + '/py')
import hardware_controller as hc 
cm = hc.cm

cgitb.enable()  # for troubleshooting
form = cgi.FieldStorage()
delete_song = form.getvalue("message", "")
itemnext = form.getvalue("itemnumber", "")

###if delete_song:
   ### os.remove(HOME_DIR + '/music/tracks/' + delete_song)
###    f = open(HOME_DIR + '/music/' +'.playlist', "r")
    ###lines = f.readlines()
###    f.close()
    ###count = 0
    ###f = open(HOME_DIR + '/music/' +'.playlist', "w")
    ###for line in lines:
      ###  if count != itemnext:
         ###   f.write(line)
   ###     count += 1
###    f.close()
    

if itemnext:
    itemnext = int(itemnext) + 1
#    cm.update_state('song_to_play', str(itemnext -1))
    cm.update_state('play_now', str(itemnext))

print "Content-type: text/html"
print

print """
<html>

<head>
    <title>Playlist</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap-theme.min.css" integrity="sha384-rHyoN1iRsVXV4nD0JutlnGaslCJuC7uwjduW9SVrLvRYooPp2bWYgmgJQIXwl/Sp" crossorigin="anonymous">
    <link rel="stylesheet" href="http://code.ionicframework.com/ionicons/2.0.1/css/ionicons.min.css" crossorigin="anonymous">
    <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
    <link rel="stylesheet" type="text/css" href="/css/style.css">
</head>

<body>
	<div class="container">
		<div class="row">
			<div class="row" align="center">
				<form action="web_controls.cgi" method="post">
					<button class="btn btn-default button3"><i class="material-icons">settings_remote</i>&nbsp Back To Controls</button>
				</form>
			</div>
			<ul class="playlist list-group">"""

if itemnext:
    itemnext -= 1
else:
    itemnext = int(cm.get_state('song_to_play', "0"))

with open(cm.lightshow.playlist_path, 'rb') as playlist_fp:
    fcntl.lockf(playlist_fp, fcntl.LOCK_SH)
    playlist = csv.reader(playlist_fp, delimiter='\t')
    
    itemnumber = 0
    for song in playlist:
        if itemnumber == itemnext:
            list_class = 'list-group-item clearfix music-item active'
            header = '<h4 class="list-group-item-heading">Playing: </h4>'
            play_button_text = 'Stop'
            play_button_class = 'btn btn-warning btn-lg'
            play_glyphicon = 'glyphicon glyphicon-stop'
            input_id = 'playnext'
        else:
            input_id = 'playitem'
            list_class = 'list-group-item clearfix music-item'
            header = ''
            play_button_text = 'Play'
            play_button_class = 'btn btn-success btn-lg'
            play_glyphicon = 'glyphicon glyphicon-play'
        print """
				<li class="%s">
                                    %s
                                    <p class="list-group-item-text">%s</p>
                                    <div>
                                    <form method="post" action="playlist.cgi?itemnumber=%s">
                                        <span class="pull-right button-group">
                                        <button type="" name="message" value="%s" class="btn btn-danger btn-lg"><span class="glyphicon glyphicon-trash"></span> Delete</button>
                                        </span></form>
                                    """%(list_class, header, song[0],str(itemnumber), song[0])
        print """
                                    <form method="post" action="playlist.cgi?itemnumber=%s">
                                        <span class="pull-right button-group">
                                             <button type="submit" name="item%s" value="%s" class="%s"><span class="%s"></span> %s</button>
                                        </span>
                                    </form></div>
				</li>"""%(str(itemnumber), str(itemnumber), song[0], play_button_class,play_glyphicon, play_button_text,)
        itemnumber += 1

    fcntl.lockf(playlist_fp, fcntl.LOCK_UN)
print """
			</ul>
			<div class="row" align="center">
			<form action="upload_music.cgi" method="post">
				<button type="submit" class="btn btn-default button2"><span class="glyphicon glyphicon-cloud-upload"></span>&nbsp Upload Track</button>
			    </form>
			</div>
		</div>
	</div>
	<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>
	<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js" integrity="sha384-Tc5IQib027qvyjSMfHjOMaLkfuWVxZxUPnCJA7l2mCWNIpG9mGCD8wGNIcPD7Txa" crossorigin="anonymous"></script>
</body>
</html>     
"""
