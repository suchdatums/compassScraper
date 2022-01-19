#!/usr/bin/env python3

import sys
import time, csv, math, pprint
from bs4 import BeautifulSoup

# myca
#sys.path.append(r'./myca')
sys.path.append(r'../myca')

import DOMinate
import my_notify
import unit_criteria

import compass_scrape
import toList # toList=["...@gmail.com", "..."]

DEBUG_QUICKRUN = False

URL = "https://compassmining.io/hardware"
baseURL = "https://compassmining.io"
filename_DOM = '_DOM'
csv_filename = "scraped.csv"
csv_goodunits = "good_units.csv"

subjectline = f"compass scraper - criteria match (Hosted: '{unit_criteria.hosted}' | eff: {unit_criteria.eff})"

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
        "Link",
        "price/hash"
        ]





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
    print("running SCRAPE.py")

    if DEBUG_QUICKRUN:
        print("DEBUG MODE\nDEBUG MODE\nDEBUG MODE\nDEBUG MODE\nDEBUG MODE\n")

    print(f"finding units hosted: {unit_criteria.hosted}")
    print(f"eff must be {unit_criteria.eff} or less")

    print(f"creating {csv_filename} (every unit found will be placed in here)")
    with open(csv_filename, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
        writer.writeheader()

    starttime = time.time()

    ### 0 - get the DOM
    if DEBUG_QUICKRUN: # LOAD FROM FILE (DEBUG ONLY FOR FASTER RUN)
        theDOM = DOMinate.loadDOM( filename_DOM )
    else: # SCRAPE THE ACTUAL WEBSITE
        theDOM = DOMinate.getDOM( URL )
        DOMinate.saveDOM( theDOM, filename_DOM )
        
    soup = BeautifulSoup(theDOM, 'lxml')




    ### easy... get a list links to unit pages
    linkSHIT = ['w-full','relative','md:mt-0','h-230px','overflow-hidden','rounded-15px','cursor-pointer']
    links = DOMinate.scrapeLinks( soup, linkSHIT, baseURL=baseURL )
    
    print("found these links:")
    pprint.pprint( links )

    ### GO TO EACH PAGE AND SCRAPE UNITS
    units = []
    for l in links:
        found = compass_scrape.gatherUnits( l )

        if found == []: # solana miner, etc
            continue
        
        with open(csv_filename, 'a') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
            for f in found:
                writer.writerow( f )
                units.append( f )
        
        # TODO debug only (only scrape and process first unit page... then continue to matching/email and exit)
        if DEBUG_QUICKRUN:
            break

    goodUnits = []
    for u in units:
        y = compass_scrape.doesUnitMeetCriteria( u )
        if y != 0:
            goodUnits.append( y )

    if len(goodUnits):
        ### SAVE GOOD_UNITS.SCV
        print(f'writing units to {csv_goodunits}')
        with open(csv_goodunits, 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
            writer.writeheader()
            for y in goodUnits:
                writer.writerow( y )
        
        # TODO - THIS IS MESSY... MAKE INTO A FUNCTION
        try:
            msgFile = open("last_msg.txt", "r")
            last_msg = msgFile.read()
            msgFile.close()

            csvfile = open(csv_goodunits, 'r')
            this = csvfile.read()

            if last_msg != this:
                print("NEW MATCHES :: updating last_msg.txt and sending email!")
                # TODO - MAKE INTO FUNCTION
                #  BUG FIX - this needs to come first!  If the message didn't get out.. then don't make a file saying last_msg... it makes a bug if/WHEN the email program FAILS after first-run/install...
                for t in toList.toList:
                    easy_notify.sendcsv( subjectline, csv_goodunits, t )

                with open('last_msg.txt', 'w') as csvfile:
                    writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
                    writer.writeheader()
                    for y in goodUnits:
                        writer.writerow( y )
            else:
                print("no new matches found... NOT emailing.")
        except:
            print("last_msg.txt not found... making file and emailing!")
            # TODO - MAKE INTO FUNCTION
            #  BUG FIX - this needs to come first!  If the message didn't get out.. then don't make a file saying last_msg... it makes a bug if/WHEN the email program FAILS after first-run/install...
            for t in toList.toList:
                easy_notify.sendcsv( subjectline, csv_goodunits, t )

            with open('last_msg.txt', 'w') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
                writer.writeheader()
                for y in goodUnits:
                    writer.writerow( y )
    else:
        print("NO UNITS MEET CRITERIA")
        print(f"deleting {csv_goodunits}")
        with open(csv_goodunits, 'w') as csvfile:
            pass

    endtime = time.time()
    sec = int( (endtime - starttime) / 60 )
    secsleep = len( links ) * DOMinate.sleepfor
    print(f"execution took < { sec } > minutes")
    print(f"{math.floor( secsleep/60 )} minutes spent sleeping")
    print("SCRAPE.py done")






    ### SAVE SCRAPED.SCV
    # print('writing units to scraped.csv')
    # with open('scraped.csv', 'w') as csvfile:
    #     writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
    #     writer.writeheader()
    #     for u in units:
    #         writer.writerow( u )
    