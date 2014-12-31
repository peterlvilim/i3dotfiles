# xset r rate 200 30
xrandr --output DisplayPort-0 --left-of DVI-0
xrandr --output DVI-1 --right-of DVI-0
autocutsel -fork &
autocutsel -selection PRIMARY -fork &
exec i3
