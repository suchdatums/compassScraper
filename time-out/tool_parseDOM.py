#!/usr/bin/env python3

import sys
from bs4 import BeautifulSoup

if len(sys.argv) == 1"
    print("no argument given, exitting\ngive filename as script argument to parse")

filename = sys.argv[1]
outfile = open( filename )
soup = BeautifulSoup(outfile, 'lxml')

lookFOR = ["inline-block", "relative", "rounded-16px", "w-full", "lg:shadow-sm", "text-left", "bg-white", "bg-white", "xl:h-full", "h-2/5", "pt-3", "h-full", "overflow-hidden", "pb-0", "hover:shadow-3xl", "p-2"]
for g in soup.find_all(lambda tag: tag.name == 'div' and tag.get('class') == lookFOR):
    print( g.text )
