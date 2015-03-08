dirs=$(find ~/.mail/ -type d | grep INBOX/new)
mailcount=0
for dir in $dirs
do
    mails=$(find $dir -type f | wc -l)
    mailcount=$(($mailcount + $mails))
done
printf $mailcount"\n"
