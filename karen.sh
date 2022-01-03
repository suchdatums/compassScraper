# Karen gets triggered a lot
# sh karen.sh >> ./karen.log 2>&1

echo
echo "karen is triggered $(date +%s)"
echo "running DOMinate.py"
# command > file 2>&1
# python3 ./DOMinate.py > ./pythonerr.log 2>&1
python3 ./DOMinate.py 2>&1
echo "running diff"
echo
echo
# or use                                         "^\+"
diff -u scraped.csv scraped_latest.csv | grep -E "^\-"
echo
echo
echo "karen is done $(date +%s)"
echo
