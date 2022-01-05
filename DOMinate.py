#!/usr/bin/env python3

import os, time, csv, re, math

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup

import easy_notify
import toList # toList=["...@gmail.com", "..."]

#############################################################
####### options
#############################################################
chromedriverpath = '/usr/bin/chromedriver' # RPI
#chromedriverpath = '/Users/noone/Downloads/chromedriver'# MAC

# What do you want to name the CSV file?
csv_file = "scraped.csv"      # Allowed: anything inside single or double quotes

# this will strip the units (100 TH/s) --> (100), ($19,000) --> (19000) ...technically all non-numeric characters
# I THINK I NEED THIS... BECAUSE I'M GOING TO BE USING THE NUMBERS IN MATH.. AND IDON'T WANT TO HAVE TO SCRAPE THAT SHIT OFF LATER
stripUnits = True     # Allowed: True / False

# subject line of email
alertSubject="Compass Hardware Scrape Criteria Match!"




#############################
def DOMinate(URL="", sleeptime=3, filen=None):

    # GET THE SOUP
    if filen != None:
        try:
            # TODO - if the file is not there, is still runs and gives a stupid error about soup variable...
            outfile = open(filen)
            soup = BeautifulSoup(outfile, 'lxml')
            sleeptime = 0 # no need to wait!
            print("getting the DOM from file")
        except:
            print(f"could not get DOM info from file: {filen}")

    else: # get it on the internet...
        print(f"Dominating {URL}")
        opts = Options()
        opts.add_argument(" --headless")
        driver = webdriver.Chrome( chromedriverpath , options=opts)
        driver.get(URL)
        #TODO - log success here
        print(f"napping for {sleeptime} seconds so the DOM can cook...")
        time.sleep( sleeptime )
        html = driver.execute_script("return document.getElementsByTagName('html')[0].innerHTML")
        soup = BeautifulSoup(html, 'lxml') # or html
        driver.quit()



    # MEAT AND POTATOES OF THE FUNCTION
    allUnits = []
    try:

        csv_columns = ["Certified Reseller:","Hosted in:","Second Hand:","Name",\
            "Price:","Hashrate:","Energy Cons:","Minimum Order:","Online date:",\
                "Shipping date:","Link:"]

        # NO TOUCH OR PAPA NO KISS!
        FLAG_USA = """viewBox='0 0 7410"""
        FLAG_RUS = """viewBox='0 0 9"""
        FLAG_CAN = """viewBox='0 0 1000"""
        with open(csv_file, 'w') as csvfile:

            writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
            writer.writeheader()

            for g in soup.find_all(lambda tag: tag.name == 'div' and tag.get('class') == ['flex','flex-col','w-full','lg:pr-4','pb-4','pt-6','h-full']):

                unit = {"Certified Reseller:":"No",
                        "Hosted in:":"at home",
                        "Second Hand:":'new', # should be undetermined... but it works for now (do not assume state)
                        "Name":0,
                        "Price:":0,
                        "Hashrate:":0,
                        "Energy Cons:":0,
                        "Minimum Order:":0,
                        "Online date:":0,
                        "Shipping date:":0,
                        "Link:":0}

                if "Compass Certified Reseller" in g.text:
                    unit["Certified Reseller:"] = "Yes"

                if "Hand" in g.text: # && "Second" (logical, not bitwise operand?)
                    unit["Second Hand:"] = 'used'

                # LINK
                # ['w-full','relative','pb-5/10','overflow-hidden','rounded-15px','cursor-pointer']
                lnk = g.find(lambda tag: tag.name == 'div' and tag.get('class') == ['w-full','relative','pb-5/10','overflow-hidden','rounded-15px','cursor-pointer']).get('href')
                unit['Link:'] = "https://compassmining.io" + lnk

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
def generate_message_by_eval( units ):
    
    msg = ""
    #msg += "found units with UNDER $100 per terahash:\n\n"

    for u in units:

        # guardian
        if u['Hosted in:'] != "USA":
            continue

        # TODO - BAD WAY TO DO THIS!... FIND A WAY TO INCLUDE ONLY BITCOIN MINERS
        if "Z15" in u['Name']:
            continue

        costEff = math.floor(u['Price:'] / u['Hashrate:'])
        if costEff > 100:
            continue
    
        print(u['Name'], "\teff:", costEff)
        msg += '[ ' + str(costEff) + " $/TH ] ---> "\
            + ' (' + str(u["Second Hand:"]) + ') ' \
            + str(u['Name']) \
            + '\n' \
            + '$' + str(u['Price:']) + " | " \
            + str(u['Hashrate:']) + " TH/s | " \
            + str(u["Energy Cons:"]) + " Watt | " \
            + "Hosted in " + str(u["Hosted in:"]) + " | " \
            + "Online date: " + str(u["Online date:"]) + " | " \
            + "Min Order: " + str(u["Minimum Order:"]) + " | " \
            + "Certified Reseller: " + str(u["Certified Reseller:"]) \
            + "\nLink: " + str(u['Link:']) \
            + "\n\n"

    return msg



###############################
def emailAndUpdate( msg ):
    #  BUG FIX - this needs to come first!  If the message didn't get out.. then don't make a file saying last_msg... it makes a bug if/WHEN the email program FAILS after first-run/install...
    easy_notify.sendalert(msg, alertSubject, toList.toList)

    msgFile = open("last_msg.txt", 'w')
    msgFile.write(msg)
    msgFile.close()



##########################
if __name__ == "__main__":

    #units = DOMinate(filen='out.txt', sleeptime=1)
    units = DOMinate(URL = "https://compassmining.io/hardware", sleeptime=3) # add criteria parameter
    
    msg = generate_message_by_eval( units )

    try:
        msgFile = open("last_msg.txt", "r")
        last_msg = msgFile.read()
        msgFile.close()

        if last_msg != msg:
            print("NEW MATCHES :: updating last_msg.txt and sending email!")
            emailAndUpdate( msg )
        else:
            print("no new matches found... NOT emailing.")
    except:
        print("last_msg.txt not found... making file and emailing!")
        emailAndUpdate( msg )
