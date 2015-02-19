pkill -9 -f mopidy
mopidy -q -o spotify/password=`pass spotify`  &>/dev/null &
