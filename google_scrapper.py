import requests
import re
import urllib.request
from bs4 import BeautifulSoup

def google_scrape(search_item):
    search_item = search_item.replace(" ","+")
    search_link = 'http://www.google.com/search?q={}&num=10'.format(search_item)
    r = urllib.request.Request(search_link, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        html = urllib.request.urlopen(r).read()
        soup = BeautifulSoup(html)
    #print(type(soup))
    #content = str(soup.prettify()[0:-1])
        content = str(soup)
        
        pdf_re = re.compile(r'<a href="\S+.pdf')
        pdf_line = pdf_re.findall(content)
        pdf_link_re = re.compile(r'http://\S+.pdf')
        
        pdf_link = []
        for i in range(len(pdf_line)):
            temp_pdf_link = pdf_link_re.findall(pdf_line[i])
            pdf_link.append(temp_pdf_link[0])
        
        for i in range(len(pdf_link)):
            pdf_link[i] = pdf_link[i].replace("'","")
            pdf_link[i] = pdf_link[i].replace('"','')
        
        for i in range(len(pdf_link)):
            print(pdf_link[i])
    except:
        pass

    #<h3 class="r"><a href="/url?q=http://datasheets.maximintegrated.com/en/ds/DS18B20.pdf&amp;
