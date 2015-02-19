#!/usr/bin/env python2
import commands


try:
    result = commands.getstatusoutput('gcalcli --pw `pass peter.vilim@delphix.com` --nocolor agenda "`date`" | head -2 | tail -1')
    if "Error" not in result[1] and "Exception" not in result[1]:
        print(result[1])
    else:
        print("No calendar")
except:
    print("No calendar")
