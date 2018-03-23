#!/usr/bin/python

import cgi
import cgitb
import os
import subprocess
from time import sleep

HOME_DIR = os.getenv("SYNCHRONIZED_LIGHTS_HOME")

print "Content-type: text/html"
print

print """
<!DOCTYPE html>
<html>
<head>
    <title>Upload Music</title>	
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap-theme.min.css" integrity="sha384-rHyoN1iRsVXV4nD0JutlnGaslCJuC7uwjduW9SVrLvRYooPp2bWYgmgJQIXwl/Sp" crossorigin="anonymous">
    <link rel="stylesheet" href="http://code.ionicframework.com/ionicons/2.0.1/css/ionicons.min.css" crossorigin="anonymous">
    <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
    <link rel="stylesheet" type="text/css" href="/css/style.css">
    <style type="text/css">
	.but{
		background: #ffffff;
		border: none;
		padding: 20px;
		color: #000000;
		margin-top: 40px;
		font-size: 30px;
	}
	h3 {
		color: white;
	}
	</style>
</head>

<body>
	<center>
		<form action="save.cgi" method="post" enctype="multipart/form-data">
			<h3>Select music to upload:</h4>
			<input class="btn btn-default but but1" type="file" name="filename" value="">
			<button class="btn btn-default button2" type="submit" name="submit"><span class="glyphicon glyphicon-cloud-upload"></span>&nbsp; Upload Music </button><br>
			
		</form>
		<form action="web_controls.cgi" method="post">
                    <button class="btn btn-default button3"><i class="material-icons">settings_remote</i>&nbsp; Back To Controls</button>
                </form>
	
	</center>
	<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
	<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js" integrity="sha384-Tc5IQib027qvyjSMfHjOMaLkfuWVxZxUPnCJA7l2mCWNIpG9mGCD8wGNIcPD7Txa" crossorigin="anonymous"></script>
</body>
</html>"""

