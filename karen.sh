# Karen gets triggered a lot
# sh karen.sh >> ./karen.log 2>&1
echo
echo
echo "!!!!!!!!!!!!!!!!!!"
echo "karen is triggered $(date)"
# stderr to stdout so it shows up in karen.log when run.sh calls karen.sh
python3 ./SCRAPE.py 2>&1
echo "exit(): $?"
echo "karen is done $(date)"
