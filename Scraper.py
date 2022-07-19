#Necessary libraries 
import pandas as pd
from requests import Request
from bs4 import BeautifulSoup
import time
from urllib.request import Request, urlopen
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

#get the soup 
def get_soup(url):
    req = Request(url, headers={'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7','Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'})
    webpage = urlopen(req).read().decode('utf-8')
    soup = BeautifulSoup(webpage, 'lxml')
    return soup


list_product_name = []
reviews_info = []
list_price = []
list_url = []

baseurl = "https://www.amazon.com"

for i in range(1, 200):
    try:
        soup = get_soup(
            f'https://www.amazon.com/s?k=data+science&i=stripbooks&page={i}&crid=2CIKKG7G2UMAJ&qid=1657878871&sprefix=%2Cstripbooks%2C646&ref=sr_pg_1')
        product_name = soup.find_all('span', {'class': 'a-size-base-plus a-color-base a-text-normal'})
        for i in product_name:
            text = str(i.get_text())
            list_product_name.append(text)
        reviews_count = soup.find_all('div', {'class': 'a-row a-size-small'})
        for i in reviews_count:
            text = i.get_text()
            reviews_info.append(text)
        price = soup.find_all('span', {'class': 'a-offscreen'})
        for i in price:
            text = i.get_text()
            list_price.append(text)
        link_to_reviews = soup.find_all('a', {
            'class': 'a-size-base a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal'})
        for i in link_to_reviews:
            links = i.get('href')
            complete_link = baseurl + links
            list_url.append(complete_link)
            time.sleep(0.2)
    except Exception as e:
        print(e)
        pass
    print(len(list_product_name))
    print(len(reviews_info))
    print(len(list_price))
    print(len(list_url))
    list_stars = []
    reviews_count = []
    for i in reviews_info:
        strings = i.split('stars')
        list_stars.append(strings[0][:3])
        reviews_count.append(strings[1])
    df_dict = {"Product name": list_product_name, "Product price": list_price,
               "Urls": list_url, "Reviews count": reviews_info, "Star": list_stars, "Reviews count": reviews_count}
#create dataframe of the extracted data
df = pd.DataFrame.from_dict(df_dict, orient='index')
#Transpose the dataframe to get each column as a row
df = df.transpose()
#Save dataframe into a csv file
df.to_csv("data/Data_science_book.csv", index = False)