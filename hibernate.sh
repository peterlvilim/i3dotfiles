#~/.i3/lock.sh &
dbus-send --system --print-reply \
    --dest="org.freedesktop.UPower" \
    /org/freedesktop/UPower \
    org.freedesktop.UPower.Hibernate
#~/.i3/lock.sh
