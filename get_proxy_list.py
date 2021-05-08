import requests
from bs4 import BeautifulSoup
import pandas as pd


all_p = []

search_string = input("enter search query : ")
search_string.replace(' ', '+')

url = f'https://www.google.com/search?q={search_string}'
headers = {
    'User-agent':
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.19582"
}

all_data = [a.find('a').find('h3').text for a in BeautifulSoup(requests.get(url, headers=headers).text, 'lxml').find_all('div', class_='yuRUbf')]
print(all_data)

# for i in all_data:
#     try:
#         proxies = {
#             'ip-address' : i.find_all('td')[0].text,
#             'port' : i.find_all('td')[1].text,
#             'code' : i.find_all('td')[2].text,
#             'country' : i.find_all('td')[3].text,
#             'anonimity' : i.find_all('td')[4].text,
#             'Https' : i.find_all('td')[6].text,
#         }
#         all_p.append(proxies)
#         print(proxies)
#     except:
#         print('')


# df = pd.DataFrame(all_p)


# df.to_json('all_proxies.json')