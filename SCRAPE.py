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






##########################
if __name__ == "__main__":
    print("\n\n\n\n\n\n\n\n\n\n\n\n==============\nrunning SCRAPE.py")

    if False: # TODO - DEBUGGING ONLY...
        theDOM = DOMinate.getDOM( URL )
        DOMinate.saveDOM( theDOM, filename_DOM )
    else:
        theDOM = DOMinate.loadDOM( filename_DOM )

    soup = BeautifulSoup(theDOM, 'lxml')

    linkSHIT = ['w-full','relative','md:mt-0','h-230px','overflow-hidden','rounded-15px','cursor-pointer']
    links = DOMinate.scrapeLinks( soup, linkSHIT, baseURL=baseURL )
    units = []
    for l in links:
        unitsFound = compassUnitScraper.gatherUnits( l )

        if unitsFound == []: # solana miner, etc
            pass

        units.append( compassUnitScraper.tidyUnits(unitsFound) )
        break # TODO - DEBUG ONLY

    # for u in units:
    #     #print(u)
    #     pprint.pprint( u )



    # csv_columns = ["Certified Reseller:","Hosted in:","Second Hand:","Name",\
    #         "Price:","Hashrate:","Energy Cons:","Minimum Order:","Online date:",\
    #             "Shipping date:","Link:"]
    # with open(csv_file, 'w') as csvfile:
    #     writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
    #     writer.writeheader()
    #     writer.writerow(unit)



# GET THE DOM...
# GET ALL THE LINKS FOR THE UNITS
# SCRAPE LINK BY LINK AND MAKE SCRAPED.CSV
# REMOVE DUPLICATES AND OTHER __SHIT__ WE DON'T WANT
# SORT UNITS ACCORDING TO EFF:
# EVALUATE IF ANY OF THE UNITS MEET CRITERIA
# IF CHANGED from last emailing
# EMAIL THOSE THAT DO
# LOG EVERYTHING
