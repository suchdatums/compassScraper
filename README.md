# DOMinate
Take control of knowledge

# setup the pi to scrape on...
START WITH FRESH INSTALL

enable SSH from rpi-imager

SSH and enable VNC with "sudo raspi-config"

```
# enable SSH
sudo raspi-config

sudo apt update -y
sudo apt upgrade -y

sudo apt-get install chromium-chromedriver

```

# get the easy repo!

# get the repo!
```
ummm...
```

# setup the software to scrape... 
```
# MAC ONLY:
# python3 -m pip install --upgrade pip


python3 -m venv .venv
source .venv/bin/activate


pip install bs4 selenium lxml requests
```

# configure it to run...

crontab -e is used to run karen.sh every 15-or-so minutes

karen does a lot:

- run DOMinatrix.py to scrape the DOM and place it into scraped.csv
- run evaluate.py to evaluate the items and email



