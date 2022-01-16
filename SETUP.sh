#!/bin/bash -i

# one-click install..., ya bish?

# SYSTEM
sudo apt update -y
sudo apt upgrade -y
sudo apt-get install chromium-chromedriver

# PYTHON
python3 -m venv venv
source venv/bin/activate
# (MAC ONLY!!!)
# python3 -m pip install --upgrade pip
pip install bs4 selenium lxml requests
pip3 install webdriver_manager

# INSTALL FILES
chmod +x run

# RUN SETUP OTHER SCRIPTS
python3 setup_toList.py

echo
echo "NOW SETUP CRONTAB:"
echo "run:"
echo "crontab -e"
echo
echo "delete everything in the file and paste in this:"
echo "0 * * * * /home/pi/run"
