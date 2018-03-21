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
	<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">
	<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap-theme.min.css" integrity="sha384-rHyoN1iRsVXV4nD0JutlnGaslCJuC7uwjduW9SVrLvRYooPp2bWYgmgJQIXwl/Sp" crossorigin="anonymous">
	<style type="text/css">
		.but{
			background: #ff9900;
			border: none;
			padding: 20px;
			color: #fff;
			margin-top: 40px;
			font-size: 30px;
		}
		.but1{
			background: rgba(0,255,0,0.5);
			width: 80%;
		}
	</style>
</head>

<body>
	<center>
		<form action="save.cgi" method="post" enctype="multipart/form-data">
			Select music to upload:
			<input class="but but1" type="file" name="filename" value="">
			<input class="but" type="submit" value="Upload Music" name="submit">
		</form>
		<p>%s</p>
	</center>
	<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
	<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js" integrity="sha384-Tc5IQib027qvyjSMfHjOMaLkfuWVxZxUPnCJA7l2mCWNIpG9mGCD8wGNIcPD7Txa" crossorigin="anonymous"></script>
</body>
</html>"""

