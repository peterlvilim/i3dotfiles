#!/usr/bin/env python
from sabnzbd import SABnzbd
from stopifalreadyrunning import *;
import sys
import os
stop_if_already_running(os.path.basename(__file__));
time.sleep(5);
s = SABnzbd('hydrogen.local', 8080, 'f78a3823cf2853e0702f8970b4947713')
try:
        status=s.status();
except:
	f = open("/home/pvilim/.i3/sab.status", "w");
	f.write("No connection");
	f.close();
        sys.exit();

if len(status["jobs"])>0:
	timeleft=status["jobs"][0]["timeleft"]
	name=status["jobs"][0]["filename"]
	if len(name)>20:
		name=name[0:20]+"..."
	if len(timeleft)>5:
		timeleft=timeleft[:-3]
	f = open("/home/pvilim/.i3/sab.status", "w");
	f.write(name+" "+timeleft);
	f.close();
else:
	f = open("/home/pvilim/.i3/sab.status", "w");
	f.write("No downloads");
	f.close();
