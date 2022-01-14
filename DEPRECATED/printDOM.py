# she bang
# TODO's
# put __name__ here to pass URL parameter into script
# ALSO... name of outfile.
# also.. help if you do it wrong

# python3 printDOM.py > out.txt

import os

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome import options
# https://stackoverflow.com/questions/64717302/deprecationwarning-executable-path-has-been-deprecated-selenium-python
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

from time import sleep

#chromedriverpath = '/usr/bin/chromedriver' # RPI
#chromedriverpath = '/Users/noone/Downloads/chromedriver'# MAC

URL = "https://compassmining.io/hardware"

filename = './theDOM'

opts = Options()
# options.add_argument("start-maximized")
opts.add_argument(" --headless")
#driver = webdriver.Chrome( chromedriverpath , options=opts)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=opts)
driver.get( URL )
sleep(3) # COOK THE DOM
html = driver.execute_script("return document.getElementsByTagName('html')[0].innerHTML")
#print( html )
driver.quit()

print(f'writing the DOM to file: {filename}')
with open(filename, 'w') as outfile:
    outfile.write( html )
    outfile.close()
