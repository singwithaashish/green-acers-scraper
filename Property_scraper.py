from bs4 import BeautifulSoup
import requests 
import threading
import pandas as pd


all_properties_data = []


def get_properties(page_no):
    url = f'https://www.green-acres.pt/property-for-sale/loule?p_n={page_no}'
    properties = BeautifulSoup(requests.get(url).text, 'lxml').find_all('figure', class_='item-main')
    print(f'scraping {url}')
    
    for ppt in properties:
        try:
            data = {
                'property-price' : ppt.find('p', class_='item-price').text.strip() if ppt.find('p', class_='item-price') != None else '',
                'title' : ppt.find('h3', class_='item-title').text.strip() if ppt.find('h3', class_='item-title') != None else '',
                'Land' : f"{ppt.find('li', class_='details-component').text.strip()} m^2" if ppt.find('li', class_='details-component') != None else '',
                'Images' : [i.get('data-lazy-load-src') for i in ppt.find_all('img', class_='item-img')],
                
            }
            all_properties_data.append(data)
        except:
            print('connection refused')
        


thrds = [threading.Thread(target=get_properties, args=(i,)) for i in range(226)] #threading magic
[x.start() for x in thrds] #creates threads
[x.join() for x in thrds] #waits for them to finish


df = pd.DataFrame(all_properties_data) #save it into a .csv file
df.to_csv('Properties.csv')
print(df.head())



