"""Gas, skrape, dip"""

import urllib2 as url
from bs4 import BeautifulSoup as bs

page = url.urlopen(
    'https://en.wikipedia.org/wiki/Beautiful_Soup_(HTML_parser)')

soup = bs(page, 'html.parser')

for h1 in soup.find_all('a'):
    print(h1)
