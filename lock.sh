#!/bin/sh
xinput disable bcm5974
( slock && xset dpms 0 0 240 && xinput enable bcm5974) &
xset dpms 0 0 2
xset dpms force off
# pgrep slimlock
# if [ $? -eq 1 ]; then
    # xinput disable bcm5974
    # ( slimlock && xinput enable bcm5974) &
# fi
