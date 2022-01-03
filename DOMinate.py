#!/usr/bin/env python3

import os, time, csv, re

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup

# import DOMinate_options








#############################################################
####### options
#############################################################
#chromedriverpath = '/usr/bin/chromedriver' # RPI
chromedriverpath = '/Users/noone/Downloads/chromedriver'# MAC

# What do you want to name the CSV file?
csv_file = "scraped_latest.csv"      # Allowed: anything inside single or double quotes

# this will strip the units (100 TH/s) --> (100), ($19,000) --> (19000) ...technically all non-numeric characters
# I THINK I NEED THIS... BECAUSE I'M GOING TO BE USING THE NUMBERS IN MATH.. AND IDON'T WANT TO HAVE TO SCRAPE THAT SHIT OFF LATER
stripUnits = True     # Allowed: True / False

# who will DOMinate.py email?
emailTO="digsec.oregon@gmail.com"

# subject line of email
alertSubject="SCRAPER: criteria match list"










#############################
def DOMinate(URL, sleeptime):
    # NO TOUCH OR PAPA NO KISS!
    FLAG_USA = """viewBox='0 0 7410"""
    FLAG_RUS = """viewBox='0 0 9"""
    FLAG_CAN = """viewBox='0 0 1000"""

    csv_columns = ["Certified Reseller:","Hosted in:","Second Hand:","Name","Price:","Hashrate:","Energy Cons:","Minimum Order:","Online date:","Shipping date:"]

    opts = Options()
    opts.add_argument(" --headless")
    driver = webdriver.Chrome( chromedriverpath , options=opts)
    #driver = webdriver.Chrome('/usr/bin/chromedriver', options=opts) # pi baby
    #driver = webdriver.Chrome('/Users/noone/Downloads/chromedriver', options=opts) # mac daddy

    driver.get(URL)
    #TODO - log success here

    time.sleep( sleeptime )

    html = driver.execute_script("return document.getElementsByTagName('html')[0].innerHTML")
    soup = BeautifulSoup(html, 'lxml') # or html
    driver.quit()

    allUnits = []

    # MEAT AND POTATOES OF THE FUNCTION
    try:
        with open(csv_file, 'w') as csvfile:

            writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
            writer.writeheader()

            for g in soup.find_all(lambda tag: tag.name == 'div' and tag.get('class') == ['flex','flex-col','w-full','lg:pr-4','pb-4','pt-6','h-full']):

                unit = {"Certified Reseller:":False,
                        "Hosted in:":"at home",
                        "Second Hand:":'new', # should be undetermined... but it works for now
                        "Name":0,
                        "Price:":0,
                        "Hashrate:":0,
                        "Energy Cons:":0,
                        "Minimum Order:":0,
                        "Online date:":0,
                        "Shipping date:":0}

                if "Compass Certified Reseller" in g.text:
                    unit["Certified Reseller:"] = True

                if "Hand" in g.text: # && "Second" (logical, not bitwise operand?)
                    unit["Second Hand:"] = 'used'

                # <p class="pt-1 text-sm font-bold leading-none font-sans">Hosted in </p>
                a = g.find(lambda tag: tag.name == 'p' and tag.get('class') == ['pt-1','text-sm','font-bold','leading-none','font-sans'])
                if "Hosted in" in a.text:
                    if FLAG_USA in str(a.next_sibling.next):
                        unit['Hosted in:'] = "USA"
                    if FLAG_RUS in str(a.next_sibling.next):
                        unit['Hosted in:'] = "RUS" #putin is a bitch
                    if FLAG_CAN in str(a.next_sibling.next):
                        unit['Hosted in:'] = "CAN"

                # UNIT NAME
                #<h3 class="text-xl font-bold font-sans">Antminer S19j Pro 100 TH </h3></div>
                #['text-xl','font-bold','font-sans']
                a = g.find(lambda tag: tag.name == 'h3' and tag.get('class') == ['text-xl','font-bold','font-sans'])
                unit['Name'] = a.text

                # Price:
                # Hashrate:
                # Energy Cons:
                # Minimum Order:
                #<p class="text-sm leading-none font-sans text-graphite mr-2 w-29">
                #['text-sm','leading-none','font-sans','text-graphite','mr-2','w-29']
                for a in g.find_all(lambda tag: tag.name == 'p' and tag.get('class') == ['text-sm','leading-none','font-sans','text-graphite','mr-2','w-29']):
                    if stripUnits == True:
                        unit[a.text] = int( re.sub("[^0-9]","",a.next_sibling.text) ) # REMOVE UNITS (ALL NON NUMERALS)
                    else:
                        unit[a.text] = a.next_sibling.text

                a = g.find(lambda tag: tag.name == 'p' and tag.get('class') == ['mr-2','text-sm','leading-none','pt-2px','font-sans','w-29','text-graphite'])
                unit[a.text] = a.next_sibling.text

                #print(unit)
                writer.writerow(unit)
                allUnits.append(unit)
    except IOError:
        # TODO CATCH EVERYTHING..
        # TODO - IF THERE IS A BREAK IN THE WEB SCRAPING (PERHAPS FROM COMPASS UPDATING THEIR WEBSITE), THEN IT NEEDS TO REFLECT IN A DEBUG LOG
        print("yo dog, your code borked.. ok man?\n")

    return allUnits









###############################
def evaluate( units, emailTo ):
    """
    - This takes in list of unit dict

    - matches according to what we want

    - then asks an email module to email a message to the given list

    """
    print("eval...")

    # pick out ones with adequate price per hash
    for u in units:
        # guardian, only look for USA hosted miners
        if u['Hosted in:'] != "USA":
            continue

        prime = u['Price:'] / u['Hashrate:']

        # TODO - make 100 a variable and put it in settings
        if u['Price:'] / u['Hashrate:'] >= 100:
            emailThese.append( u )
    

    for i in emailThese:
        print(i['Name'], i['Price:'] / i['Hashrate:'], i['Hashrate:'] / i['Energy Cons:']) #TODO - round numbers only please

        # unit = {"Certified Reseller:":False,
        # "Hosted in:":"at home",
        # "Second Hand:":'new', # should be undetermined... but it works for now
        # "Name":0,
        # "Price:":0,
        # "Hashrate:":0,
        # "Energy Cons:":0,
        # "Minimum Order:":0,
        # "Online date:":0,
        # "Shipping date:":0}











########################################
def notify_ifmatch( units, emailThese ):
    return 0

    # TRY AND EXCEPT GO HERE!!!














##########################
if __name__ == "__main__":
    #TODO log that it's running
    print(f"{__file__} running.")
    
    # CHANGE IF YOU HAVE INTERNET OR NOT
    #units = DOMinate(file='out.txt', sleeptime=1)
    units = DOMinate(URL = "https://compassmining.io/hardware", sleeptime=3) # add criteria parameter

    #emailThese = []

    #notify_ifmatch( units, emailThese )
    
    #evaluate( units )



##########################
# NOTES ##################
##########################
#
#
#
#
#
#
#