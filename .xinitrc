autocutsel -fork &
autocutsel -selection PRIMARY -fork &
xmodmap ~/.Xmodmap &
xbindkeys &
export TZ=/etc/localtime
xsetroot -solid '#8e908c'
exec i3
