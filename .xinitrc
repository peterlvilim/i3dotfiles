xrandr --output DP-4 --right-of DVI-I-1 --auto
xrandr --output DP-2 --left-of DVI-I-1 --auto
autocutsel -fork &
autocutsel -selection PRIMARY -fork &
xmodmap ~/.Xmodmap &
xbindkeys &
export TZ=/etc/localtime
xsetroot -solid '#8e908c'
exec i3
