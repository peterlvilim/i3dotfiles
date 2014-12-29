# xset r rate 200 30
xrandr --output DisplayPort-0 --left-of DVI-0
xrandr --output DVI-1 --right-of DVI-0
exec i3
