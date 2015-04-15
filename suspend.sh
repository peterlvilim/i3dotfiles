pkill -9 -f unclutter
xinput disable bcm5974
i3lock -d -c 000000 -I 0 -e
sudo systemctl suspend
xinput enable bcm5974
unclutter -grab
