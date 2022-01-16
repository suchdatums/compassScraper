import sys
sys.path.append(r'./myca')

import re, math
from bs4 import BeautifulSoup
from pprint import pprint

# myca
import DOMinate

#########################################################
#### CRITERIA ####
#########################################################

import unit_criteria

# # leave blank with (hosted = '') if you don't care where it's hosted
# hosted = 'United States'

# # eff = (price / hash rate)
# eff = 130
#########################################################


loquacious = False




#######################
def gatherUnits( URL ):
    """
0 get the DOM of site
...
1 guardian: check the algorithm to ensure it's a CORN min3r
2 get unit name
3 name the ideal unit
3.1 (by looking at table headers)
    """

    print(f"gathering units: {URL}")
    
    allUnits = [] # WE RETURN THIS
    theDOM = DOMinate.getDOM( URL )
    soup = BeautifulSoup(theDOM, 'lxml')


    ### 111111111111111111111111111111111111111111111111111111
    # The WhatsMiner M32 by MicroBT is a SHA256 ASIC miner that was released in March 2020. This mining machine has a maximum hashrate of 66 TH/s for a power consumption of 3300 watts, and is a popular choice for Bitcoin miners.Hashrate:66 TH/s Power:3300 Watts Algorithm:SHA256 View Buying Options
    lookFOR = ['inline-block','relative','rounded-16px','w-full','lg:shadow-sm','text-left','bg-white','bg-white','p-8','p-5']
    g = soup.find(lambda tag: tag.name == 'div' and tag.get('class') == lookFOR)
    hashrate = g.text.split("Hashrate:")[1].split()[0]
    wattage = g.text.split("Power:")[1].split()[0]
    algo = g.text.split("Algorithm:")[1].split()[0]

    if algo != "SHA256":
        print("these miners don't mine Bitcoin...")
        return []
    
    ### 222222222222222222222222222222222222222222222222222222
    # h3 class
    # font-family-roobert-semi-bold cred leading-none text-4xl lg:text-5xl mb-5
    lookFOR = ['font-family-roobert-semi-bold','cred','leading-none','text-4xl','lg:text-5xl','mb-5']
    g = soup.find(lambda tag: tag.name == 'h3' and tag.get('class') == lookFOR)
    name = g.text

    # <tr> TABLE ROW
    rowSHIT = ['hover:bg-gray-70']
    for rows in soup.find_all((lambda tag: tag.name == 'tr' and tag.get('class') == rowSHIT)):

        # <td> TABLE DATUM
        datumSHIT = ['px-6','py-4','whitespace-nowrap']
        datumSHIT2 = ['px-6','py-4','whitespace-nowrap','text-sm']
        data = []
        for d in rows.find_all((lambda tag: tag.name == 'td' and (tag.get('class') == datumSHIT or tag.get('class') == datumSHIT2))):
            data.append( d.text )

        hash = int( re.sub("[^0-9]","", hashrate) )
        #watt = int( re.sub("[^0-9]","", wattage )
        price = int( re.sub("[^0-9]","", data[5]) )

        u = {
            "Name" : name,
            "Hashrate" : hashrate,
            "Wattage" : wattage,
            "Facility" : data[0],
            "Hosting Rate" : data[1],
            "Estimated Online Date" : data[2],
            "Condition" : data[3],
            "Available Quantity" : data[4],
            "Price" : data[5],
            "Link": URL,
            "price/hash" : math.floor(price / hash)
        }

        allUnits.append( u )

    if loquacious:
        print("gatherUnits returning:")
        pprint( allUnits )

    print(f"gathered <{len(allUnits)}> units")
    return allUnits







#############################
def doesUnitMeetCriteria( u ):

    if unit_criteria.hosted != '':
        if not unit_criteria.hosted in u["Facility"]:
            return 0
    
    if u["price/hash"] > unit_criteria.eff:
        return 0

    return u
