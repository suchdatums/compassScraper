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

# make toList.py
```
echo "toList=['@gmail.com', '@gmail.com', '@gmail.com']" > ~/toList.py
nano toList.py
```
TODO write a script to do this... like setup_easy_notify.sh

# change permissions
```
chmod +x ~/run_DOMinate.sh
```

# setup the software to scrape... 
```
(MAC ONLY!!!)   python3 -m pip install --upgrade pip
```


```
python3 -m venv .venv
source .venv/bin/activate

pip install bs4 selenium lxml requests
```

# configure it to run...

configure run.sh to run with:
```
crontab -e

* * * * * /home/pi/run_DOMinate.sh
```

# ensure variables in DOMinate.py are correct
most notably, chromedriverpath