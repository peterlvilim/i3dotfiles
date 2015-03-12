autocutsel -fork &
autocutsel -selection CLIPBOARD -fork &
xmodmap ~/.Xmodmap &
xbindkeys &
export TZ=/etc/localtime
exec i3
