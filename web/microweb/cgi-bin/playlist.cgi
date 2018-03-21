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
itemnext = form.getvalue("itemnumber", "")

activenumber = -1
if itemnext:
    itemnext = int(itemnext) + 1
#    cm.update_state('song_to_play', str(itemnext -1))
    cm.update_state('play_now', str(itemnext))
    activenumber = itemnext

print "Content-type: text/html"
print

print """
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <title>LightShowPi Web Controls</title>
        <meta name="description" content="A very basic web interface for LightShowPi">
        <meta name="author" content="Ken B">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link rel="shortcut icon" href="/favicon.png">
        <meta name="mobile-web-app-capable" content="yes">
        <link rel="icon" sizes="196x196" href="/favicon.png">
        <link rel="apple-touch-icon" sizes="152x152" href="/favicon.png">
        <link rel="stylesheet" href="/css/playlist.css">
        <link href="//maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css" rel="stylesheet">
	<script src="//maxcdn.bootstrapcdn.com/bootstrap/3.3.6/js/bootstrap.min.js"></script>
    </head>
    <body>
        <center>
            <h2> LightShowPi Web Controls </h2>
            <h3> Playlist </h3>

            <form method="post" action="web_controls.cgi">
                <input id="playlist" type="submit" value="Back">
            </form>
            <div class="container">
		<h3>Playlist</h3>
		<ul id="playlist list-group">
            

     
""" 

if itemnext:
    itemnext -= 1
else:
    itemnext = int(cm.get_state('song_to_play', "0"))

with open(cm.lightshow.playlist_path, 'rb') as playlist_fp:
    fcntl.lockf(playlist_fp, fcntl.LOCK_SH)
    playlist = csv.reader(playlist_fp, delimiter='\t')
    
    itemnumber = 0
    for song in playlist:
        if itemnumber == activenumber-1:
            playClass = "active "
        else:
            playClass = ""
        if itemnumber == itemnext:
            input_id = 'playnext'
        else:
            input_id = 'playitem'
        print """<li class="%s list-group-item clearfix">
                <span>Active %s item%s %s</span>
                <span class="pull-right button-group">
                        <a href="" class="btn btn-danger"><span class="glyphicon glyphicon-trash"></span>Delete</a>
                </span>
                <span class="pull-right button-group">
                <form method="post" action="playlist.cgi?itemnumber=%s">
                        <button type="submit class="btn btn-success" name="item%s" value="%s">
                                <span class="glyphicon glyphicon-play"></span> Play
                        </button>
                </form>
        </li>"""%(playClass,activenumber, itemnumber, song[0],str(itemnumber), str(itemnumber), song[0])
	
        itemnumber += 1

    fcntl.lockf(playlist_fp, fcntl.LOCK_UN)
print activenumber
print "</body></html>"
