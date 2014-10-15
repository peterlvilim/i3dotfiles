#!/usr/bin/env python
"""Spit out the currently playing song."""
import dbus
import sys

try:
    bus = dbus.Bus(dbus.Bus.TYPE_SESSION)
    spotify = bus.get_object('com.spotify.qt','/')
    info = spotify.GetMetadata()
except dbus.exceptions.DBusException:
    print('Spotify is not running')
    sys.exit(1)

track = {}
trackMap = { 'artist'    : 'xesam:artist',
             'album'     : 'xesam:album',
             'title'     : 'xesam:title'
             }

for key, value in trackMap.items():
    if not value in info:
        continue
    piece = info[value]
    if isinstance(piece, list):
        piece = ', '.join(piece)

    track[key] = piece.encode('utf-8')

if track.has_key('title') and track.has_key('artist'):
    print('%s - %s' % (track['title'], track['artist']))
else:
    print('No song playing')
