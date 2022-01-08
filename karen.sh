# Karen gets triggered a lot
# sh karen.sh >> ./karen.log 2>&1

echo
echo
echo "!!!!!!!!!!!!!!!!!!"
echo "karen is triggered $(date +%s)"
# TODO what the fuck karen.. speak english... change this date format to human readable
echo "running DOMinate.py"
# stderr to stdout so it shows up in karen.log when run.sh calls karen.sh
python3 ./DOMinate.py 2>&1
#TODO make a timer, inside DOMinate.py... to see how LONG it takes to load the page
echo "./DOMinate.py DONE : ERROR: $?"
#echo "running diff"
#echo
# or use                                         "^\+"
#diff -u scraped.csv scraped_latest.csv | grep -E "^\+"
#echo
echo "karen is done $(date +%s)"
