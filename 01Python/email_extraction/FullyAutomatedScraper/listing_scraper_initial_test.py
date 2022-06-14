import os
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import sys
import numpy as np
import pandas as pd
import regex as re
import requests
import lxml
from lxml.html.soupparser import fromstring
import prettify
import numbers
import htmltext

req_headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.8',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
}
with requests.Session() as s:
   city = 'new york/' #*****change this city to what you want*****
   url = 'https://www.zillow.com/homes/for_sale/'+city    
   r = s.get(url, headers=req_headers)
   
soup = BeautifulSoup(r.content, 'html.parser')
'''
soup1 = BeautifulSoup(r2.content, 'html.parser')
soup2 = BeautifulSoup(r3.content, 'html.parser')
soup3 = BeautifulSoup(r4.content, 'html.parser')
soup4 = BeautifulSoup(r5.content, 'html.parser')
soup5 = BeautifulSoup(r6.content, 'html.parser')
soup6 = BeautifulSoup(r7.content, 'html.parser')
soup7 = BeautifulSoup(r8.content, 'html.parser')
soup8 = BeautifulSoup(r9.content, 'html.parser')
soup9 = BeautifulSoup(r10.content, 'html.parser') 
'''
df = pd.DataFrame()
df1 = pd.DataFrame()
#all for loops are pulling the specified variable using beautiful soup and inserting into said variable
for i in soup:
    address = soup.find_all (class_= 'list-card-addr')
    price = list(soup.find_all (class_='list-card-price'))
    beds = list(soup.find_all("ul", class_="list-card-details"))
    details = soup.find_all ('div', {'class': 'list-card-details'})
    home_type = soup.find_all ('div', {'class': 'list-card-footer'})
    last_updated = soup.find_all ('div', {'class': 'list-card-top'})
    brokerage = list(soup.find_all(class_= 'list-card-brokerage list-card-img-overlay',text=True))
    link = soup.find_all (class_= 'list-card-link')
    
    #create dataframe columns out of variables
    df['prices'] = price
    df['address'] = address
    df['beds'] = beds
#create empty url list
urls = []
#loop through url, pull the href and strip out the address tag
for link in soup.find_all("article"):
    href = link.find('a',class_="list-card-link")
    addresses = href.find('address')
    addresses.extract()
    urls.append(href)
    #import urls into a links column
df['links'] = urls
df['links'] = df['links'].astype('str')
#remove html tags
df['links'] = df['links'].replace('<a class="list-card-link" href="', ' ', regex=True)
df['links'] = df['links'].replace('" tabindex="0"></a>', ' ', regex=True)
