# Karen gets triggered a lot

# trigger her by crontab -e
# 0 * * * *
# sh karen.sh >> ./karen.log 2>&1

echo
echo "karen is triggered $(date +%s)"
asdfg
echo "running DOMinate.py"
#command > file 2>&1
python3 ./DOMinate.py > ./pythonerr.log 2>&1

echo "running diff"
diff scraped.csv scraped_latest.csv

echo "karen is done $(date +%s)"
