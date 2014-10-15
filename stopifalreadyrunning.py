import commands
import os
import time
import sys
 
def stop_if_already_running(script_name):
	l = commands.getstatusoutput("ps aux | grep -e '%s' | grep -v grep | awk '{print $2}'| awk '{print $2}'" % script_name)
	if l[1] != "":
		sys.exit(0);
