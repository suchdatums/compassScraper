clear
echo
echo "now setup toList.py"
echo "put all emails you want to be notified"
# PROJECT SETUP...

#echo "toList=['@gmail.com', '@gmail.com', '@gmail.com']" > ~/toList.py
#nano toList.py

goal="toList=["
notfirst="no"

while true ; do
read inp
if [ -z $inp ]; then
echo "NO INPUT"
break
fi
if [ -z $notfirst ]; then
goal+=", '"
echo "wherr"
notfirst=""
else
goal+="'"
fi
goal+=$inp
goal+="'"
done
goal+="]"

echo $goal > toList.py
