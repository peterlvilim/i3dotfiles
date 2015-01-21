if [ $(ip link | grep tap0 | wc -l) -gt 0 ]; then
    echo "VPN: UP"
else
    echo "VPN: DOWN"
fi
