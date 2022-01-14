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

# THIS DOES NOT WORK YET ON RPI
#pip install webdriver-manager
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

# make toList.py
```
python3 setup_toList.py
```

# change permissions
```
chmod +x run
```

# setup the software to scrape... 
```
(MAC ONLY!!!)   python3 -m pip install --upgrade pip
```


```
python3 -m venv .venv
source .venv/bin/activate

pip install bs4 selenium lxml requests
pip3 install webdriver_manager
```

# configure it to run...

configure run.sh to run with:
```
crontab -e

0 * * * * /home/pi/run
```

# ensure variables in DOMinate.py are correct
most notably, chromedriverpath


# this is run by crontab -e
example:
*/30 * * * * /home/$USER/$PROJECT_FOLDER/scrape



# known bugs...

## squished and dead

https://stackoverflow.com/questions/65372252/selenium-python-page-down-unknown-error-neterr-name-not-resolved/65372437
