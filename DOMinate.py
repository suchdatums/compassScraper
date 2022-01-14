from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
# https://github.com/SergeyPirogov/webdriver_manager

from time import sleep

import platform

sleepfor = 10


##################
def getDOM( URL ):
    print(f"DOMinating: {URL}")

    opts = Options()
    opts.add_argument(" --headless")

    p = None

    if platform.system() == 'Darwin':
        p = 1
        driver = webdriver.Chrome(service=Service(ChromeDriverManager(print_first_line=False, log_level=0).install()), options=opts)
    
    if platform.system() == 'Linux':
        p = 1
        # BUG - can't make it run on rpi the new way... just revert to old way *shrug*
        driver = webdriver.Chrome( '/usr/bin/chromedriver' , options=opts)

    if p == None:
        print("NOT RUNNING ON LINUX OR DARWIN (MAC)... CAN'T HANDLE.. EXITING(1)")
        exit(1)

    driver.get( URL )

    print(f"sleeping {sleepfor} seconds to cook the DOM...")
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


#driver.implicitly_wait(10) # seconds #TODO ugh... 


# TODO - fail better
#from selenium.common.exceptions import WebDriverException

