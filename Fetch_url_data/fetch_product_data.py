import requests
from bs4 import BeautifulSoup
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def check_product_data():
    HEADERS = {'User-Agent': 'Mozilla/5.0'}
    url = "https://www.snapdeal.com/product/edifier-black-leather-casual-belt/669192816736"
    page = requests.get(url, headers=HEADERS, verify=False)
    #print("Page data is: {}".format(page.content))
    soup = BeautifulSoup(page.content, 'html.parser')
    data = soup.find_all('div',class_='col-xs-18')
    for i in data:
        test_data = i.find('h1', class_='pdp-e-i-head')
        if test_data is not None:
            print("Prodcut name: {}".format(test_data.get('title')))
    price_data = soup.find_all('span', class_='payBlkBig')
    for j in price_data:
        print("Price: {}".format(j.text))


check_product_data()
