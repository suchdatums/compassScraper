#!/bin/bash -i

echo
echo "====================="
# Karen gets triggered a lot
echo "KAREN IS TRIGGERED!!!"
echo $(date)
# stderr to stdout so errors are caught in the log file
python3 ./SCRAPE.py 2>&1
echo "exit(): $?"
echo "karen is done"
echo "$(date)"
echo
