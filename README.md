# setup the pi to scrape on...

- START WITH FRESH INSTALL
    - use Ctrl-Shift-Z trick...
- Enable SSH and VNC
- Setup Wifi


```
sudo raspi-config

sudo apt update -y
sudo apt upgrade -y

sudo apt-get install chromium-chromedriver
```

# get the repo!
```
repo="DOMinate"
url="https://github.com/suchdatums/$repo"
git clone --depth=1 $url
rm -rf ./$repo/.git
rm ./$repo/.gitignore
mv -f ./$repo/* ~/
rm -r ./$repo/
```

# setup the software to scrape... 
```
# MAC ONLY:
python3 -m pip install --upgrade pip

python3 -m venv .venv
source .venv/bin/activate

pip install bs4 selenium lxml requests
```

# configure it to run...

crontab -e is used to run karen.sh every 15-or-so minutes

karen does a lot:

- run DOMinatrix.py to scrape the DOM and place it into scraped.csv
- run evaluate.py to evaluate the items and email



