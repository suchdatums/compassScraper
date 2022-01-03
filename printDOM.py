import os

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from time import sleep





#chromedriverpath = '/usr/bin/chromedriver' # RPI
chromedriverpath = '/Users/noone/Downloads/chromedriver'# MAC


URL = "https://compassmining.io/hardware"


opts = Options()
opts.add_argument(" --headless")
driver = webdriver.Chrome( chromedriverpath , options=opts)
driver.get( URL )

sleep(3)

html = driver.execute_script("return document.getElementsByTagName('html')[0].innerHTML")

print( html )


# put __name__ here to pass URL parameter into script
# ALSO... name of outfile.
# also.. help if you do it wrong

# python3 printDOM.py > out.txt