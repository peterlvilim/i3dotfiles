#!/usr/bin/env python2
import commands


try:
    result = commands.getstatusoutput('gcalcli  --nocolor agenda "`date`" --calendar peter.vilim@delphix.com | head -2 | tail -1')
    if "Error" not in result[1] and "Exception" not in result[1]:
        print(result[1])
    else:
        print("No calendar")
except:
    print("No calendar")
