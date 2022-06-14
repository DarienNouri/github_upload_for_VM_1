
from h11 import SWITCHED_PROTOCOL
from requests_html import HTMLSession
import re
from bs4 import BeautifulSoup
import pandas as pd
import csv
import time

link = 'https://www.floridabar.org/about/cmtes/profile/?num=37489'

from bs4 import BeautifulSoup
import urllib3
from seleniumwire import webdriver

moon_url = 'https://www.floridabar.org/directories/find-mbr/profile/?num=564737'


import lxml.html as html
import lxml.html.clean as clean
from seleniumwire import webdriver
import requests
import lxml
from lxml import etree
import xml.etree.ElementTree as ET 
from googlesearch import search
from pyvirtualdisplay import Display
from selenium.webdriver import DesiredCapabilities
import pandas as pd
from selenium.webdriver.common.by import By
import openpyxl


options = webdriver.ChromeOptions()

def interceptor(request):
    del request.headers['Referer']  # Delete the header first
    request.headers['Referer'] = 'some_referer'
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)
# Set the interceptor on the driver
driver.request_interceptor = interceptor

# All requests will now use 'some_referer' for the referer
driver.get(link)

content = driver.page_source

cleaner = clean.Cleaner()
content = cleaner.clean_html(content)

doc = html.fromstring(content)

content1 = content
html = content1
soup = BeautifulSoup(html,features="lxml")
'''
root = ET.parse(content1).getroot()
for type_tag in soup.findall('class=col-xs-12 col-sm-8'):
    value = type_tag.get('p')

    print(value)

'''
a_tags = soup.select("a[href^=tel]")
title = soup.find("h4", class_="col-xs-12 col-sm-8")

details = soup.find ('div', {'class':"col-xs-12 col-sm-8"}).text
print(details)
# address = soup.findall_(class_="col-xs-12 col-sm-8").text
#print(address)

#print(title)
from pprint import pprint as pp

dom = etree.HTML(str(soup))
p = dom.xpath("//p")[0]
#print(etree.tostring(p, method="text"))
#mProfile > div.container-narrow > div:nth-child(3) > div.col-xs-12.col-sm-8
print()
#yes = driver.find_element_by_class_name('row').text

#print(str(dom))
#print(dom.xpath('//*[@id="mProfile"]/div[2]/div[3]/div[2]')[0].text)
#addy = dom.xpath("//*[@id="mProfile"]/div[2]/div[3]/div[2]/p[1]")[0].text
#print(addy)
profile = driver.find_element(By.ID, 'mProfile').text
#print(profile)




#a = driver.find_element_by_xpath('//div[@id="mProfile"]/div[@class="col-xs-12 col-sm-8"]/br')

df = pd.DataFrame(columns= ['city',
                        'circut',
                        'date_licenced',
                        '10-yr',
                        'school',
                        'practice',
                        'firm',
                        'size_firm',
                        'position',
                        ])

row = 2

dict= {1:['city','date_licenced','school',
        'practice','firm','size_firm','fd']}  
df = pd.DataFrame(dict)

name = soup.find("h1", class_="full").text
addy = driver.find_elements(By.CLASS_NAME,'col-sm-8')
email = driver.find_elements(By.CLASS_NAME, 'icon-email')[0].text
bar_url = driver.find_elements(By.CLASS_NAME, 'col-sm-9')
addy_list = []
fin_list = []



for x in bar_url:  # remove unwanted
    if 'Committee' or 'www' in x.text:
        bar_url.remove(x)
        

addy_list.append(['Address',addy[0].text,addy[1].text])
fin_list.append(['Name', name])
fin_list.append(['Address',addy_list])
bar_profile = bar_url[0].text 
city = bar_url[1].text
year_bar = bar_url[2].text
school = bar_url[3].text
area =  bar_url[4].text
firm_size =  bar_url[5].text
home_site =  bar_url[6].text
fin_list.append(['Bar Profile',bar_profile])
fin_list.append(['City', city])
fin_list.append(['Year Bar', year_bar])
fin_list.append(['School', school])
fin_list.append(['Firm Size', firm_size])
fin_list.append(['Home Site', home_site])
for x in bar_url: # apend bar_url
    #print((x)[1].text)
    break
print(fin_list)

    


print()




'''
for x in addy:
   print(x.text)
   print("f")
   '''
#final = [x for x in addy if addy == x.text]
#print(final)

#print(addy)

#print(username)
#//*[@id="mProfile"]/div[2]/div[3]/div[2]/p[1]/text()[2]
