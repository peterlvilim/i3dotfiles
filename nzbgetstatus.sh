if [ $($HOME/.i3//nzbgetserverstatus.sh) = "down" ]; then
    echo "Server down"
else
    if [ $($HOME/.i3/nzbgetname.sh) = "download" ]; then
        echo "No download queue"
    else
        if [ $($HOME/.i3/nzbgetpaused.sh) = "Paused" ] || [ $($HOME/.i3/nzbgetpaused.sh) = "Pausing" ]; then
            echo $($HOME/.i3/nzbgetname.sh)" - "$($HOME/.i3/nzbgetpaused.sh)
        else
            echo $($HOME/.i3/nzbgetname.sh)" - "$($HOME/.i3/nzbgettime.sh)
        fi
    fi
fi
