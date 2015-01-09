xset -b &
xautolock -time 10 -locker ~/.i3/suspend.sh &
xinput disable 11 &
~/.i3/music.sh &
unclutter -grab &
pkill -9 -f
dunst &
