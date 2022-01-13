from bs4 import BeautifulSoup

import DOMinate

def gatherUnits( URL ):
    allUnits = []
    
    # unit = {"Certified Reseller:":"No",
    #                     "Hosted in:":"at home",
    #                     "Second Hand:":'new', # should be undetermined... but it works for now (do not assume state)
    #                     "Name":0,
    #                     "Price:":0,
    #                     "Hashrate:":0,
    #                     "Energy Cons:":0,
    #                     "Minimum Order:":0,
    #                     "Online date:":0,
    #                     "Shipping date:":0,
    #                     "Link:":0}

    print(f"gathering all COMPASS units for url: {URL}")

    theDOM = DOMinate.getDOM( URL )
    soup = BeautifulSoup(theDOM, 'lxml')

    # INFO BLOCK
    # DIV CLASS
    # inline-block relative rounded-16px w-full lg:shadow-sm text-left bg-white bg-white p-8 p-5
    #lookFOR = ['inline-block','relative','rounded-16px','w-full','lg:shadow-sm','text-left','bg-white','bg-white','p-8','p-5']
    #lookFOR = ['text-sm','leading-none','font-sans','text-graphite','mr-2','w-29']
    # for g in soup.find_all(lambda tag: tag.name == 'p' and tag.get('class') == lookFOR):
    #     print(g.text)
    #     #print(g.next)
    
    # NAME
    # h3 class
    # font-family-roobert-semi-bold cred leading-none text-4xl lg:text-5xl mb-5
    lookFOR = ['font-family-roobert-semi-bold','cred','leading-none','text-4xl','lg:text-5xl','mb-5']
    g = soup.find(lambda tag: tag.name == 'h3' and tag.get('class') == lookFOR)
    name = g.text
    
    # The WhatsMiner M32 by MicroBT is a SHA256 ASIC miner that was released in March 2020. This mining machine has a maximum hashrate of 66 TH/s for a power consumption of 3300 watts, and is a popular choice for Bitcoin miners.Hashrate:66 TH/s Power:3300 Watts Algorithm:SHA256 View Buying Options
    lookFOR = ['inline-block','relative','rounded-16px','w-full','lg:shadow-sm','text-left','bg-white','bg-white','p-8','p-5']
    g = soup.find(lambda tag: tag.name == 'div' and tag.get('class') == lookFOR)
    hashrate = g.text.split("Hashrate:")[1].split()[0]
    #print( hashrate )

    wattage = g.text.split("Power:")[1].split()[0]
    #print( wattage )

    algo = g.text.split("Algorithm:")[1].split()[0]
    #print( algo )

    if algo != "SHA256":
        print("these miners don't mine Bitcoin...")
        return 0

    # LOOP THRU TABLE

    unit = {"name":name,
             "hash rate":hashrate,
             "wattage":wattage
             }



    return unit
    #return allUnits


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