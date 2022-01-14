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

    # BRAND
    # H3 CLASS
    # text-sm font-normal font-family-inter text-center text-gray-60
    DOMbrand = ['text-sm','font-normal','font-family-inter','text-center','text-gray-60']
    a = g.find(lambda tag: tag.name == 'h3' and tag.get('class') == DOMbrand)
    print(f"Brand: {a.text}")
