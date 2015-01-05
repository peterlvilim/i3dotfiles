xset -b &
xautolock -time 10 -locker ~/.i3/suspend.sh &
redshift -l 40.659:88.1435 -t 5000:6500 &
xinput disable 11 &
~/.i3/music.sh &
unclutter -grab &
pkill -9 -f
dunst &
