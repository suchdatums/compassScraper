#!/usr/bin/env python3

from bs4 import BeautifulSoup

filename = "theDOM"
outfile = open( filename )
soup = BeautifulSoup(outfile, 'lxml')

# A UNIT
# div CLASS
# ["inline-block", "relative", "rounded-16px", "w-full", "lg:shadow-sm", "text-left", "bg-white", "bg-white", "xl:h-full", "h-2/5", "pt-3", "h-full", "overflow-hidden", "pb-0", "hover:shadow-3xl", "p-2"]
DOMfeaturedasic = ["inline-block", "relative", "rounded-16px", "w-full", "lg:shadow-sm", "text-left", "bg-white", "bg-white", "xl:h-full", "h-2/5", "pt-3", "h-full", "overflow-hidden", "pb-0", "hover:shadow-3xl", "p-2"]
for g in soup.find_all(lambda tag: tag.name == 'div' and tag.get('class') == DOMfeaturedasic):
    print("\nFEATURED UNIT")

    # NAME
    # h3 class
    # text-3xl font-bold font-family-inter text-center
    DOMname = ['text-3xl','font-bold','font-family-inter','text-center']
    a = g.find(lambda tag: tag.name == 'p' and tag.get('class') == DOMname)
    print(f"Name: {a}")

# OTHER UNITS
# div CLASS
# flex flex-col w-full pr-0 lg:pr-5 pb-10 h-full 
DOMotherasic = ['flex','flex-col','w-full','pr-0','lg:pr-5','pb-10','h-full']
for g in soup.find_all(lambda tag: tag.name == 'div' and tag.get('class') == DOMotherasic):
    print("\nNORMAL UNIT")

    a = g.find(lambda tag: tag.name == 'p' and tag.get('class') == DOMname)
    print(f"Name: {a}")







# for g in soup.find_all(lambda tag: tag.name == 'div' and tag.get('class') == ['flex','flex-col','w-full','lg:pr-4','pb-4','pt-6','h-full']):

#     unit = {"Certified Reseller:":"No",
#             "Hosted in:":"at home",
#             "Second Hand:":'new', # should be undetermined... but it works for now (do not assume state)
#             "Name":0,
#             "Price:":0,
#             "Hashrate:":0,
#             "Energy Cons:":0,
#             "Minimum Order:":0,
#             "Online date:":0,
#             "Shipping date:":0,
#             "Link:":0}

#     if "Compass Certified Reseller" in g.text:
#         unit["Certified Reseller:"] = "Yes"

#     if "Hand" in g.text: # && "Second" (logical, not bitwise operand?)
#         unit["Second Hand:"] = 'used'

#     # LINK
#     # ['w-full','relative','pb-5/10','overflow-hidden','rounded-15px','cursor-pointer']
#     lnk = g.find(lambda tag: tag.name == 'div' and tag.get('class') == ['w-full','relative','pb-5/10','overflow-hidden','rounded-15px','cursor-pointer']).get('href')
#     unit['Link:'] = "https://compassmining.io" + lnk

#     # <p class="pt-1 text-sm font-bold leading-none font-sans">Hosted in </p>
#     a = g.find(lambda tag: tag.name == 'p' and tag.get('class') == ['pt-1','text-sm','font-bold','leading-none','font-sans'])
#     if "Hosted in" in a.text:
#         if FLAG_USA in str(a.next_sibling.next):
#             unit['Hosted in:'] = "USA"
#         if FLAG_RUS in str(a.next_sibling.next):
#             unit['Hosted in:'] = "RUS" #putin is a bitch
#         if FLAG_CAN in str(a.next_sibling.next):
#             unit['Hosted in:'] = "CAN"

#     # UNIT NAME
#     #<h3 class="text-xl font-bold font-sans">Antminer S19j Pro 100 TH </h3></div>
#     #['text-xl','font-bold','font-sans']
#     a = g.find(lambda tag: tag.name == 'h3' and tag.get('class') == ['text-xl','font-bold','font-sans'])
#     unit['Name'] = a.text

#     # Price:
#     # Hashrate:
#     # Energy Cons:
#     # Minimum Order:
#     #<p class="text-sm leading-none font-sans text-graphite mr-2 w-29">
#     #['text-sm','leading-none','font-sans','text-graphite','mr-2','w-29']
#     for a in g.find_all(lambda tag: tag.name == 'p' and tag.get('class') == ['text-sm','leading-none','font-sans','text-graphite','mr-2','w-29']):
#         if stripUnits == True:
#             unit[a.text] = int( re.sub("[^0-9]","",a.next_sibling.text) ) # REMOVE UNITS (ALL NON NUMERALS)
#         else:
#             unit[a.text] = a.next_sibling.text

#     a = g.find(lambda tag: tag.name == 'p' and tag.get('class') == ['mr-2','text-sm','leading-none','pt-2px','font-sans','w-29','text-graphite'])
#     unit[a.text] = a.next_sibling.text





######### OLD CODE ############
#from selenium.webdriver.chrome.service import Service
#chromedriverpath = '/usr/bin/chromedriver' # RPI
#chromedriverpath = '/Users/noone/Downloads/chromedriver'# MAC

