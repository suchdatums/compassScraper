# one-click install...


sudo apt update -y
sudo apt upgrade -y

sudo apt-get install chromium-chromedriver


# DELETE STUPID SHIT


# GET THE REPO
repo="DOMinate"
url="https://github.com/suchdatums/$repo"
git clone --depth=1 $url
rm -rf ./$repo/.git
rm ./$repo/.gitignore
mv -f ./$repo/* ~/
rm -r ./$repo/


chmod +x scrape





clear
echo
echo "now setup toList.py"
echo "put all emails you want to be notified"
# PROJECT SETUP...

#echo "toList=['@gmail.com', '@gmail.com', '@gmail.com']" > ~/toList.py
#nano toList.py

goal="toList=['"
first="yaaasss"

while true ; do
    read inp
    if [ -z $inp ]; then
        echo "NO INPUT"
        break
    fi
    if [ ! -z "${first}" ];
        goal+="', '"
        first=""
    fi
    goal+=inp
done
goal+="']\"""

echo $goal > toList.py



# This will return true if a variable is unset or set to the empty string ("").
# if [ -z "${VAR}" ];