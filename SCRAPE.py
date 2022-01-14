#!/usr/bin/env python3

import time, csv, re, math

import pprint

from bs4 import BeautifulSoup

import DOMinate
import compassUnitScraper

import easy_notify
import toList # toList=["...@gmail.com", "..."]

URL = "https://compassmining.io/hardware"
baseURL = "https://compassmining.io"
filename_DOM = 'theDOM'
csv_filename = "scraped.csv"
csv_goodunits = "good_units.csv"

# THIS MUST BE IDENTIAL TO u = in compassUnitScraper
csv_columns = [
        "Name",
        "Hashrate",
        "Wattage",
        "Facility",
        "Hosting Rate",
        "Estimated Online Date",
        "Condition",
        "Available Quantity",
        "Price",
        "Link"]





# GET THE DOM...
# GET ALL THE LINKS FOR THE UNITS
# SCRAPE LINK BY LINK AND MAKE SCRAPED.CSV
# REMOVE DUPLICATES AND OTHER __SHIT__ WE DON'T WANT
# SORT UNITS ACCORDING TO EFF:
# EVALUATE IF ANY OF THE UNITS MEET CRITERIA
# IF CHANGED from last emailing
# EMAIL THOSE THAT DO
# LOG EVERYTHING
##########################
if __name__ == "__main__":
    print("\n\n\n\n\n\n\n\n\n\n\n\n")
    print("running SCRAPE.py")

    print(f"creating {csv_filename}")
    # with open('scraped.csv', 'w') as csvfile:
    #     csvfile.writelines("")

    with open(csv_filename, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
        writer.writeheader()

    starttime = time.time()

    ### 0 - get the DOM
    # TODO - DEBUGGING ONLY...
    if False:
        theDOM = DOMinate.getDOM( URL )
        DOMinate.saveDOM( theDOM, filename_DOM )
    else:
        theDOM = DOMinate.loadDOM( filename_DOM )
    soup = BeautifulSoup(theDOM, 'lxml')




    ### easy... get a list of unit pages
    linkSHIT = ['w-full','relative','md:mt-0','h-230px','overflow-hidden','rounded-15px','cursor-pointer']
    links = DOMinate.scrapeLinks( soup, linkSHIT, baseURL=baseURL )
    
    print("found these links:")
    pprint.pprint( links )

    ### GO TO EACH PAGE AND SCRAPE UNITS
    units = []
    for l in links:
        found = compassUnitScraper.gatherUnits( l )

        if found == []: # solana miner, etc
            continue
        
        with open(csv_filename, 'a') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
            for f in found:
                writer.writerow( f )
                units.append( f )
        
        # TODO debug only
        break
    
    units = compassUnitScraper.stripUnits( units )

    goodUnits = {}
    for u in units:
        y = compassUnitScraper.doesUnitMeetCriteria( u )
        if y != 0:
            goodUnits.append( y )

    ### SAVE GOOD_UNITS.SCV
    print(f'writing units to {csv_goodunits}')
    with open(csv_goodunits, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
        writer.writeheader()
        for y in goodUnits:
            writer.writerow( y )

    endtime = time.time()
    sec = int( (endtime - starttime) / 60 )
    secsleep = len( links ) * DOMinate.sleepfor
    print(f"execution took < { sec } > minutes")
    print(f"{secsleep} seconds slept sleeping")
    print("SCRAPE.py done")


















    ### SAVE SCRAPED.SCV
    # print('writing units to scraped.csv')
    # with open('scraped.csv', 'w') as csvfile:
    #     writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
    #     writer.writeheader()
    #     for u in units:
    #         writer.writerow( u )
    