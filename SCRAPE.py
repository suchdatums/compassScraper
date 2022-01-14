#!/usr/bin/env python3

import os, time, csv, re, math

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





##########################
if __name__ == "__main__":
    print("\n\n\n\n\n\n\n\n\n\n\n\n")
    print("running SCRAPE.py")

    print(f"creating {f}")
    # with open('scraped.csv', 'w') as csvfile:
    #     csvfile.writelines("")

    with open(csv_filename, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
        writer.writeheader()

    starttime = time.time()

    ### 0 - get the DOM
    if True: # TODO - DEBUGGING ONLY...
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

        #for f in found:
            #units.append( f )
            #int( re.sub("[^0-9]","",a.next_sibling.text) ) # REMOVE UNITS (ALL NON NUMERALS)
        
        with open(csv_filename, 'a') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
            for f in found:
                writer.writerow( f )
                units.append( f )
        #break # TODO - DEBUG ONLY

    # units = compassUnitScraper.tidyUnits( units )



    endtime = time.time()
    sec = int( (endtime - starttime) / 60 )
    secsleep = len( links ) * DOMinate.sleepfor
    print(f"execution took < { sec } > minutes")
    print(f"{secsleep} seconds slept sleeping")
    print("SCRAPE.py done")



# GET THE DOM...
# GET ALL THE LINKS FOR THE UNITS
# SCRAPE LINK BY LINK AND MAKE SCRAPED.CSV
# REMOVE DUPLICATES AND OTHER __SHIT__ WE DON'T WANT
# SORT UNITS ACCORDING TO EFF:
# EVALUATE IF ANY OF THE UNITS MEET CRITERIA
# IF CHANGED from last emailing
# EMAIL THOSE THAT DO
# LOG EVERYTHING















    ### SAVE SCRAPED.SCV
    # print('writing units to scraped.csv')
    # with open('scraped.csv', 'w') as csvfile:
    #     writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
    #     writer.writeheader()
    #     for u in units:
    #         writer.writerow( u )
    