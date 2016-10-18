/home/pvilim/bin/macfanmedium
ponymix mute &
nm-applet &
blueman-applet &
xset -b &
xautolock -time 15 -locker ~/.i3/suspend.sh &
~/.i3/music.sh &
redshift &
unclutter -idle -grab 2
pkill -9 -f
dunst &
