from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import WebDriverException
from webdriver_manager.chrome import ChromeDriverManager
# https://github.com/SergeyPirogov/webdriver_manager

from bs4 import BeautifulSoup

from time import sleep

sleepfor = 3




##################
def getDOM( URL ):
    print(f"DOMinating: {URL}")

    opts = Options()
    opts.add_argument(" --headless")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager(print_first_line=False, log_level=0).install()), options=opts)
    driver.get( URL )

    #print(f"sleeping {sleepfor} seconds to cook the DOM")
    sleep( sleepfor )

    html = driver.execute_script("return document.getElementsByTagName('html')[0].innerHTML")
    driver.quit()

    return html









##############################################
def scrapeLinks( soup, linkSHIT, baseURL="" ):
    print("scraping links from DOM")

    links = []

    for g in soup.find_all(lambda tag: tag.name == 'div' and tag.get('class') == linkSHIT):
        links.append( baseURL + g.get('href') )

    return links






#############################
def saveDOM( DOM, filename ):
    print(f'writing the DOM to file: {filename}')

    with open(filename, 'w') as outfile:
        outfile.write( DOM )
        outfile.close()




########################
def loadDOM( filename ):
    print(f'loading DOM from file: {filename}')

    with open(filename, 'r') as outfile:
        theDOM = outfile.read()
        outfile.close()
    return theDOM




##########################
if __name__ == "__main__":
    print(f"running __main__")

    URL = input("URL : ")

    defaultfilename = URL.split('/')[-1] + "_DOM"

    filename = input(f"filename (default: {defaultfilename}) : ")

    if filename == '':
        filename = defaultfilename

    print(f"saving {URL} to {filename}")

    saveDOM( getDOM( URL ), filename )








##################
# she bang
# TODO's
# put __name__ here to pass URL parameter into script
# ALSO... name of outfile.
# also.. help if you do it wrong
# python3 printDOM.py > out.txt
#chromedriverpath = '/usr/bin/chromedriver' # RPI
#chromedriverpath = '/Users/noone/Downloads/chromedriver'# MAC
#driver = webdriver.Chrome( chromedriverpath , options=opts)
# https://stackoverflow.com/questions/64717302/deprecationwarning-executable-path-has-been-deprecated-selenium-python
