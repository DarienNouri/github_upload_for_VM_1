
from requests_html import HTMLSession
import re
from bs4 import BeautifulSoup
import pandas as pd
import openpyxl
import csv
import time
import html
import cloudscraper

import requests


import urllib.request



from selenium import webdriver
import time
from bs4 import BeautifulSoup

#browser = webdriver.Edge("C:\Program Files (x86)\iedriver\msedgedriver.exe")

url = "https://www.floridabar.org/about/cmtes/profile/?num=177946"


from urllib.request import Request, urlopen
from bs4 import BeautifulSoup


req = Request(url,headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()
print(webpage)


'''
sada = browser.get(url)
time.sleep(3)
source = browser.page_source
soup = BeautifulSoup(source, 'html.parser')

for item in soup.findAll('div', attrs={'class': 'name'}):
    print(item.text)


url = "https://www.floridabar.org/about/cmtes/profile/?num=177946"
user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.101 Safari/537.36'

# header variable
headers = { 'User-Agent' : user_agent }

# creating request
req = urllib.Request(url, None, headers)

# getting html
html = urllib.urlopen(req).read()











req_headers = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'en-US,en;q=0.8',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
        }
        

r = requests.get(url, headers=req_headers)
session = HTMLSession()
s = session.get(url, headers=req_headers)

print(r.json())
import cloudscraper

scraper = cloudscraper.create_scraper()  # returns a CloudScraper instance
# Or: scraper = cloudscraper.CloudScraper()  # CloudScraper inherits from requests.Session
a =scraper.get("https://www.floridabar.org/about/cmtes/profile/?num=177946").text  # => "<!DOCTYPE html><html><head>..."


import cloudscraper
import json
scraper = cloudscraper.create_scraper(interpreter='nodejs')
r = scraper.get("https://www.facebook.com/tr/?id=2020368528109326&ev=Microdata&dl=https%3A%2F%2Fwww.floridabar.org%2Fabout%2Fcmtes%2Fprofile%2F%3Fnum%3D177946&rl=https%3A%2F%2Fwww.google.com%2F&if=false&ts=1654222521957&cd[DataLayer]=%5B%5D&cd[Meta]=%7B%22title%22%3A%22Committee%20Member%20Profile%20%E2%80%93%20James%20Grier%20Pressly%20%E2%80%93%20The%20Florida%20Bar%22%7D&cd[OpenGraph]=%7B%7D&cd[Schema.org]=%5B%5D&cd[JSON-LD]=%5B%5D&sw=1504&sh=1003&v=2.9.61&r=stable&a=tmgoogletagmanager&ec=1&o=30&fbp=fb.1.1654216799935.745376549&it=1654222520348&coo=false&es=automatic&tm=3&rqm=GE").text 
print(r)

y = json.loads(r)
print (y)
'''

'''

from bs4 import BeautifulSoup

soup = BeautifulSoup(s.content, 'html5lib')

emails = re.findall(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", 'body'.text)
print(emails)

#r.select_one('icon-email')
'''