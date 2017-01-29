# -*- coding: utf-8 -*-

from urllib.request import urlopen
from bs4 import BeautifulSoup

r = urlopen('http://stackoverflow.com/questions/3969726/attributeerror-module-object-has-no-attribute-urlopen')
soup = BeautifulSoup(r)
print(type(soup))

print(soup.prettify())


#print(soup.prettify().encode("utf-8"))


# https://www.analyticsvidhya.com/blog/2015/10/beginner-guide-web-scraping-beautiful-soup-python/

# https://www.thorlabs.com/thorproduct.cfm?partnumber=WP25M-VIS

# https://www.thorlabs.com/images/large/TTN006777-lrg.jpg