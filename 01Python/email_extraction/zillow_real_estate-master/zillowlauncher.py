import requests
import re
import json
import pandas as pd
from bs4 import BeautifulSoup

input_link ='https://www.zillow.com/homes/The-Hamptons,-NY_rb/'
r = requests.get(input_link,headers = {'User-Agent':'Mozilla/5.0'})

data = json.loads(re.search(r'!--(\{"queryState".*?)-->', r.text).group(1))
df = pd.DataFrame()
df1 = pd.DataFrame()

for item in range(1,2):
    for item in data['cat'+str(item)]['searchResults']['listResults']:
        listing_url= 'https://www.zillow.com' +item['detailUrl'] 
        print(listing_url)
        #listings = requests.get(listing_url,headers = {'User-Agent':'Mozilla/5.0'})
        soup = BeautifulSoup(r.content, 'lxml')
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
            
            df['address'] = address
            df['prices'] = price
            broke = []
            broke += brokerage
            print(broke)
            
        print(df)
        #create empty url list
        urls = []
        #loop through url, pull the href and strip out the address tag
        #loop through url, pull the href and strip out the address tag
        '''
        for link in soup.find_all("article"):
            href = link.find('a',class_="list-card-link")
            addresses = href.find('address')
            addresses.extract()
            urls.append(href)
            print(urls)
        #import urls into a links column
        df['links'] = urls
        df['links'] = df['links'].astype('str')
        #remove html tags
        df['links'] = df['links'].replace('<a class="list-card-link" href="', ' ', regex=True)
        df['links'] = df['links'].replace('" tabindex="0"></a>', ' ', regex=True)
        '''
        print(urls)
                        
            
   



















   

        
'''
        price = soup.find('span', {'class': 'photo-card-price'}).text
        print(price)
        info = soup.find('span', {'class': 'zsg-photo-card-info'}).text
        address = soup.find('span', {'itemprop': 'address'}).text
        '''
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0",
    "Accept": "*/*",
    "Accept-Language": "en-US,en;q=0.5",
    "Pragma": "no-cache",
    "Cache-Control": "no-cache"
}
'''
def main(url):
    with requests.Session() as req:
        req.headers.update(headers)
        req.head('https://www.zillow.com/')
        for item in range(1, 2):
            # item can be used here to loop by refactoring `cat1` to be `cat2` and so on
            
            params = {
                "searchQueryState": '{"pagination":{"currentPage":2},"usersSearchTerm":"Orange County, CA","mapBounds":{"west":-118.84559473828126,"east":-116.68678126171876,"south":33.34208982842918,"north":33.99173886991076},"regionSelection":[{"regionId":1286,"regionType":4}],"isMapVisible":true,"filterState":{"isAllHomes":{"value":true},"sortSelection":{"value":"globalrelevanceex"}},"isListVisible":true,"mapZoom":9}',
                "wants": '{"cat1":["mapResults"]}'
            }
            r = req.get(url, params=params)
            df = pd.DataFrame(r.json()['cat1']['searchResults']['mapResults'])
            print(df)
            df.to_csv('data.csv', index=False)

main('https://www.zillow.com/search/GetSearchPageState.htm')


'''


























'''

import requests
import json

url = 'https://www.zillow.com/search/GetSearchPageState.htm'

headers = {
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9',
    'upgrade-insecure-requests': '1',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'
}

houses = []
for page in range(1, 3):
    params = {
        "searchQueryState": json.dumps({
            "pagination": {"currentPage": page},
            "usersSearchTerm": "35216",
            "mapBounds": {
                "west": -86.97413567189196,
                "east": -86.57244804982165,
                "south": 33.346263857015515,
                "north": 33.48754107532057
            },
            "mapZoom": 12,
            "regionSelection": [
                {
                    "regionId": 73386, "regionType": 7
                }
            ],
            "isMapVisible": True,
            "filterState": {
                "isAllHomes": {
                    "value": True
                },
                "sortSelection": {
                    "value": "globalrelevanceex"
                }
            },
            "isListVisible": True
        }),
        "wants": json.dumps(
            {
                "cat1": ["listResults", "mapResults"],
                "cat2": ["total"]
            }
        ),
        "requestId": 3
    }

    # send request
    page = requests.get(url, headers=headers, params=params)

    # get json data
    json_data = page.json()

    # loop via data
    for house in json_data['cat1']['searchResults']['listResults']:
        houses.append(house)


# show data
print('Total houses - {}'.format(len(houses)))

# show info in houses
for house in houses:
    if 'brokerName' in house.keys():
        print('{}: {}'.format(house['brokerName'], house['price']))
    else:
        print('No broker: {}'.format(house['price']))
'''