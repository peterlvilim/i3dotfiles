if [ $(nzbget -L | wc -l) -eq 1 ]; then
    echo down
else
    echo up
fi
