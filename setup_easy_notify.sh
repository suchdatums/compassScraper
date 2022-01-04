#!/bin/bash

echo
echo

# TODO - the location for this needs to change; use environment variable, which means... it has to be setup FIRST, before running this script
# TODO - this should be rewritten... I should use environment variables instead


fname="credentials.py"
fullpath="./$fname"


if [ -f "$fullpath" ]; then
    echo "$fullpath already exists"
    echo "delete it to continue:"
    echo "rm $fullpath"
    exit
fi

touch $fullpath

echo
echo "enter email address for SENDING account:"
read send
echo
echo "enter password for SENDING account:"
read psk
echo
echo "enter email address for RECEIVEING account:"
read rec
echo
echo "done."
echo "delete this file with:"
echo "rm $0"

echo "easynotify_SENDER = \"$send\"" >> $fullpath
echo "easynotify_SENDER_psk = \"$psk\"" >> $fullpath
echo "easynotify_RECEIVER = \"$rec\"" >> $fullpath
