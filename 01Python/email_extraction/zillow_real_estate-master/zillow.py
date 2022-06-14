from lxml import html
import requests
import unicodecsv as csv
import argparse
import numpy as np
import regex as re
import htmltext
import requests
from bs4 import BeautifulSoup
from lxml.html.soupparser import fromstring

from requests_html import HTMLSession




url = "https://www.zillow.com/homedetails/718-Broadway-APT-7B-New-York-NY-10003/244755699_zpid/"


# try:
headers= {
			'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
			'accept-encoding':'gzip, deflate, sdch, br',
			'accept-language':'en-GB,en;q=0.8,en-US;q=0.6,ml;q=0.4',
			'cache-control':'max-age=0',
			'upgrade-insecure-requests':'1',
			'user-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
}
  #chage stop= to change how many links are searched
session = HTMLSession()
req_headers = {
	'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
	'accept-encoding': 'gzip, deflate, br',
	'accept-language': 'en-US,en;q=0.8',
	'upgrade-insecure-requests': '1',
	'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
}

try:
	r = session.get(url,  headers=req_headers)
except:
	print("badlink")
	

soup = BeautifulSoup(r.content, 'html5lib')
address = soup.find_all(class_= 'list-card-addr')
price = list(soup.find_all (class_= 'list-card-price'))
print(price)
print(address)
'''
# r.html.render()
#re.html.render()
print(url)
r.html.render()
soup = BeautifulSoup(r.content, 'html5lib')

                    #body = r.html.find("body")[0]

	response = session.get(url,headers=headers)
	print(response)
	soup = BeautifulSoup(response.content, 'html.parser')

	parser = html.fromstring(response.text)
	search_results = parser.xpath("//div[@id='search-results']//article")
	properties_list = []

	for i in soup:
		address = soup.find_all(class_= 'list-card-addr')
		print(str(address))
'''
'''
	raw_city = properties.xpath(".//span[@itemprop='address']//span[@itemprop='addressLocality']//text()")
	raw_state= properties.xpath(".//span[@itemprop='address']//span[@itemprop='addressRegion']//text()")
	raw_postal_code= properties.xpath(".//span[@itemprop='address']//span[@itemprop='postalCode']//text()")
	raw_price = properties.xpath(".//span[@class='zsg-photo-card-price']//text()")
	raw_info = properties.xpath(".//span[@class='zsg-photo-card-info']//text()")
	raw_broker_name = properties.xpath(".//span[@class='zsg-photo-card-broker-name']//text()")
	url = properties.xpath(".//a[contains(@class,'overlay-link')]/@href")
	raw_title = properties.xpath(".//h4//text()")
	
	address = ' '.join(' '.join(raw_address).split()) if raw_address else None
	city = ''.join(raw_city).strip() if raw_city else None
	state = ''.join(raw_state).strip() if raw_state else None
	postal_code = ''.join(raw_postal_code).strip() if raw_postal_code else None
	price = ''.join(raw_price).strip() if raw_price else None
	info = ' '.join(' '.join(raw_info).split()).replace(u"\xb7",',')
	broker = ''.join(raw_broker_name).strip() if raw_broker_name else None
	title = ''.join(raw_title) if raw_title else None
	property_url = "https://www.zillow.com"+url[0] if url else None 
	is_forsale = properties.xpath('.//span[@class="zsg-icon-for-sale"]')
	properties = {
					'address':address,
					'city':city,
					'state':state,
					'postal_code':postal_code,
					'price':price,
					'facts and features':info,
					'real estate provider':broker,
					'url':property_url,
					'title':title
	}
	if is_forsale:
		properties_list.append(properties)
return properties_list
# except:
# 	print ("Failed to process the page",url)

if __name__=="__main__":
	argparser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter)
	argparser.add_argument('zipcode',help = '')
	sortorder_help = """
    available sort orders are :
    newest : Latest property details,
    cheapest : Properties with cheapest price
    """
	argparser.add_argument('sort',nargs='?',help = sortorder_help,default ='Homes For You')
	args = argparser.parse_args()
	zipcode = args.zipcode
	sort = args.sort
	print ("Fetching data for %s"%(zipcode))
	scraped_data = parse(zipcode,sort)
	print ("Writing data to output file")
	with open("properties-%s.csv"%(zipcode),'wb')as csvfile:
		fieldnames = ['title','address','city','state','postal_code','price','facts and features','real estate provider','url']
		writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
		writer.writeheader()
		for row in  scraped_data:
			writer.writerow(row)

'''


