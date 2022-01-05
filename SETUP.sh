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

echo "toList=['@gmail.com', '@gmail.com', '@gmail.com']" > ~/toList.py
nano toList.py

