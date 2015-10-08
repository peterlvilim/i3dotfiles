/home/pvilim/bin/macfanmedium
ponymix mute &
nm-applet &
xset -b &
xautolock -time 15 -locker ~/.i3/suspend.sh &
~/.i3/music.sh &
redshift -l 37.78:122.42 -t 4000:6500
unclutter -idle -grab 2
pkill -9 -f
dunst &
