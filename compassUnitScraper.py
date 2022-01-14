from pprint import pprint
import re

from bs4 import BeautifulSoup

import DOMinate

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

    print(f"gathering all COMPASS units for url: {URL}")
    
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
            "Link": URL
        }

        allUnits.append( u )

    print("gatherUnits returning:")
    pprint( allUnits )
    return allUnits







# csv_columns = [
#         "Name",
#         "Hashrate",
#         "Wattage",
#         "Facility",
#         "Hosting Rate",
#         "Estimated Online Date",
#         "Condition",
#         "Available Quantity",
#         "Price",
#         "Link"]
#######################
def stripUnits( units ):
    tidied = units

    # REMOVE ALL NON NUMERALS (SO WE CAN DO MATH WITH THEM...)
    for t in tidied:
        t["Hashrate"] = int( re.sub("[^0-9]","", t["Hashrate"]) )
        t["Wattage"] = int( re.sub("[^0-9]","", t["Wattage"]) )
        t["Price"] = int( re.sub("[^0-9]","", t["Price"]) )

    return tidied



# csv_columns = [
#         "Name",
#         "Hashrate",
#         "Wattage",
#         "Facility",
#         "Hosting Rate",
#         "Estimated Online Date",
#         "Condition",
#         "Available Quantity",
#         "Price",
#         "Link"]
#############################
def doesUnitMeetCriteria( u ):
    if not "Home" in u["Facility"]:
        return 0










    #return unit

    # Algorithm:SHA256 
    #print(g.text)
    #exit()

        # DOMlink = ['w-full','relative','md:mt-0','h-230px','overflow-hidden','rounded-15px','cursor-pointer']
        # a = g.find(lambda tag: tag.name == 'div' and tag.get('class') == DOMlink).get('href')
        # URL = "https://compassmining.io" + a
        # scrapePage( URL )

        # BRAND
        #DOMbrand = ['text-sm','font-normal','font-family-inter','text-center','text-gray-60']
        #a = g.find(lambda tag: tag.name == 'h3' and tag.get('class') == DOMbrand)
        #print(f"Brand: {a.text}")

        # NAME
        #DOMname = ['text-24px','font-bold','font-family-inter','text-center']
        #a = g.find(lambda tag: tag.name == 'h3' and tag.get('class') == DOMname)
        #print(f"Name: {a.text}")




# def gatherUnits( URL ):
#     allUnits = []
    
#     # unit = {"Certified Reseller:":"No",
#     #                     "Hosted in:":"at home",
#     #                     "Second Hand:":'new', # should be undetermined... but it works for now (do not assume state)
#     #                     "Name":0,
#     #                     "Price:":0,
#     #                     "Hashrate:":0,
#     #                     "Energy Cons:":0,
#     #                     "Minimum Order:":0,
#     #                     "Online date:":0,
#     #                     "Shipping date:":0,
#     #                     "Link:":0}

#     print(f"gathering all COMPASS units for url: {URL}")

#     theDOM = DOMinate.getDOM( URL )
#     soup = BeautifulSoup(theDOM, 'lxml')

#     # INFO BLOCK
#     # DIV CLASS
#     # inline-block relative rounded-16px w-full lg:shadow-sm text-left bg-white bg-white p-8 p-5
#     #lookFOR = ['inline-block','relative','rounded-16px','w-full','lg:shadow-sm','text-left','bg-white','bg-white','p-8','p-5']
#     #lookFOR = ['text-sm','leading-none','font-sans','text-graphite','mr-2','w-29']
#     # for g in soup.find_all(lambda tag: tag.name == 'p' and tag.get('class') == lookFOR):
#     #     print(g.text)
#     #     #print(g.next)
    
#     # NAME
#     # h3 class
#     # font-family-roobert-semi-bold cred leading-none text-4xl lg:text-5xl mb-5
#     lookFOR = ['font-family-roobert-semi-bold','cred','leading-none','text-4xl','lg:text-5xl','mb-5']
#     g = soup.find(lambda tag: tag.name == 'h3' and tag.get('class') == lookFOR)
#     name = g.text

#     # The WhatsMiner M32 by MicroBT is a SHA256 ASIC miner that was released in March 2020. This mining machine has a maximum hashrate of 66 TH/s for a power consumption of 3300 watts, and is a popular choice for Bitcoin miners.Hashrate:66 TH/s Power:3300 Watts Algorithm:SHA256 View Buying Options
#     lookFOR = ['inline-block','relative','rounded-16px','w-full','lg:shadow-sm','text-left','bg-white','bg-white','p-8','p-5']
#     g = soup.find(lambda tag: tag.name == 'div' and tag.get('class') == lookFOR)
#     #hashrate = g.text.split("Hashrate:")[1].split()[0]
#     #wattage = g.text.split("Power:")[1].split()[0]
#     algo = g.text.split("Algorithm:")[1].split()[0]

#     if algo != "SHA256":
#         print("these miners don't mine Bitcoin...")
#         return 0


#     # table header
#     # <th scope="col" class="px-6 py-3 text-left text-sm font-medium text-black tracking-wider cursor-pointer hover:bg-gray-70">
#     # GET THE HEADER INFO

#     tablecolheaders = []    
#     headerSHIT = ['px-6','py-3','text-left','text-sm','font-medium','text-black','tracking-wider','cursor-pointer','hover:bg-gray-70']
#     for hrows in soup.find_all((lambda tag: tag.name == 'th' and tag.get('class') == headerSHIT)):
#         tablecolheaders.append( hrows.text )

#     tablecolheaders.append("add to cart link")
#     # TABLE ROW
#     # <tr class="hover:bg-gray-70">
#     # ['hover:bg-gray-70']

#     # United States, Nebraska
#     # 0.065 / kWh
#     # Jan 18, 2022
#     # Second Hand
#     # 1
#     # $8,195

#     rowSHIT = ['hover:bg-gray-70']
#     for rows in soup.find_all((lambda tag: tag.name == 'tr' and tag.get('class') == rowSHIT)):

#         u = {"name":name}

#         # TABLE DATA
#         datumSHIT = ['px-6','py-4','whitespace-nowrap']
#         datumSHIT2 = ['px-6','py-4','whitespace-nowrap','text-sm']
#         for n, d in enumerate( rows.find_all((lambda tag: tag.name == 'td' and (tag.get('class') == datumSHIT or tag.get('class') == datumSHIT2)))):

#             #u.update( { tablecolheaders[r], d.text } )

#             u[ tablecolheaders[n] ] = d.text

#         allUnits.append( u )


#     return allUnits