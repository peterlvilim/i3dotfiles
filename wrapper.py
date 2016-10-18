#!/usr/bin/env python2
# -*- coding: utf-8 -*-

# This script is a simple wrapper which prefixes each i3status line with custom
# information. It is a python reimplementation of:
# http://code.stapelberg.de/git/i3status/tree/contrib/wrapper.pl
#
# To use it, ensure your ~/.i3status.conf contains this line:
#     output_format = "i3bar"
# in the 'general' section.
# Then, in your ~/.i3/config, use:
#     status_command i3status | ~/i3status/contrib/wrapper.py
# In the 'bar' section.
#
# In its current version it will display the cpu frequency governor, but you
# are free to change it to display whatever you like, see the comment in the
# source code below.
#
# © 2012 Valentin Haenel <valentin.haenel@gmx.de>
#
# This program is free software. It comes without any warranty, to the extent
# permitted by applicable law. You can redistribute it and/or modify it under
# the terms of the Do What The Fuck You Want To Public License (WTFPL), Version
# 2, as published by Sam Hocevar. See http://sam.zoy.org/wtfpl/COPYING for more
# details.

import sys
import json
import commands
import subprocess

storedresult = dict()


def get_mpc():
    result = commands.getstatusoutput("mpc current")
    output = "N/A"
    if "error" not in result[1] and result[1] != "":
        output = result[1]
    return output


def get_cal(counter):
    if counter % 60 == 0:
        subprocess.Popen(["/bin/sh", "-c", "/home/pvilim/.i3/getcalstatus.py > /home/pvilim/.i3/getcalstatus.out"])
    try:
        f = open("/home/pvilim/.i3/getcalstatus.out")
        result = f.readline()
        result = result.replace("\n", "")
        return result
    except:
        return ""


def get_spotify():
    result = commands.getstatusoutput("~/.i3/getspotifystatus.py")
    return result[1]


def get_sab(counter):
    subprocess.Popen("/home/pvilim//.i3/getsabstatus.py")
    result = commands.getstatusoutput("cat ~/.i3/sab.status")
    return result[1]


def get_nzbget(counter):
    if counter % 10 == 0:
        result = commands.getstatusoutput("~/.i3/nzbgetstatus.sh")
        storedresult['nzbget'] = result
    else:
        result = storedresult['nzbget']
    return result[1]


def get_mail(counter):
    if counter % 60 == 0:
        subprocess.Popen(["/bin/sh", "-c", "/home/pvilim/.i3/mailcount.sh > /home/pvilim/.i3/mailcount.out"])
    try:
        f = open("/home/pvilim/.i3/mailcount.out")
        result = f.readline()
        result = result.replace("\n", "")
        return result
    except:
        return ""


def get_vpn():
    result = commands.getstatusoutput("~/.i3/vpnstatus.sh")
    return result[1]


def get_dunst(counter):
    if counter % 2 == 0:
        result = commands.getstatusoutput(
            "BLOCK_I3=true BLOCK_INSTANCE=NEWEST ~/.i3/dunst.py")
        storedresult['dunst'] = result
    else:
        result = storedresult['dunst']
    return result[1]


def get_speed():
    result = commands.getstatusoutput("~/.i3/speed.sh")
    return result[1]


def print_line(message):
    """ Non-buffered printing to stdout. """
    sys.stdout.write(message + '\n')
    sys.stdout.flush()


def read_line():
    """ Interrupted respecting reader for stdin. """
    # try reading a line, removing any extra whitespace
    try:
        line = sys.stdin.readline().strip()
        # i3status sends EOF, or an empty line
        if not line:
            sys.exit(3)
        return line
    # exit on ctrl-c
    except KeyboardInterrupt:
        sys.exit()


def monitor_hotplug(counter):
    commands.getstatusoutput("/home/pvilim/bin/dohotplug")


def monitor_doscreenlock():
    commands.getstatusoutput("/home/pvilim/bin/doscreenlock")


if __name__ == '__main__':
    # Skip the first line which contains the version header.
    print_line(read_line())

    # The second line contains the start of the infinite array.
    print_line(read_line())

    counter = 60
    while True:
        if counter == 0:
            counter = 60

        line, prefix = read_line(), ''
        # ignore comma at start of lines
        if line.startswith(','):
            line, prefix = line[1:], ','

        j = json.loads(line)

        # insert information into the start of the json, but could be anywhere
        j.insert(4, {'full_text': '%s' % " ".join(get_speed().split()),
                     'name': 'speed', 'color': '#859900'})
        j.insert(4, {'full_text': '%s' % " ".join(get_vpn().split()),
                     'name': 'speed', 'color': '#fdf6e3'})
        # j.insert(0, {'full_text': '%s' % get_mail(counter), 'name': 'nzbget',
                     # 'color': '#268bd2'})
        monitor_hotplug(counter)
        monitor_doscreenlock()

        # and echo back new encoded json
        print_line(prefix+json.dumps(j))
        counter = counter - 1
