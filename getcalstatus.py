#!/usr/bin/env python
import sys
import commands
import os
import time
from stopifalreadyrunning import *;

stop_if_already_running(os.path.basename(__file__));
time.sleep(30);
try:
    result=commands.getstatusoutput("gcalcli --nc --ignore-started agenda \"`date`\" | head -2 | tail -1")
    if "Error" not in result[1] and "Exception" not in result[1]:
        f = open("/home/pvilim/.i3/cal.status", "w");
        f.write(result[1]);
        f.close();
    else:
        f = open("/home/pvilim/.i3/cal.status", "w");
        f.write("No calendar");
        f.close();
except:
    f = open("/home/pvilim/.i3/cal.status", "w");
    f.write("No calendar"); 
    f.close();

