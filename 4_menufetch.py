import requests
import os
from dotenv import load_dotenv
load_dotenv()

APIKEY = os.getenv('APIKEY')
APISECRET = os.getenv('APISECRET')
INSTANCE = os.getenv('INSTANCE')
ESTABLISHMENT = os.getenv('ESTABLISHMENT')


headersGlobal = {
    'API-AUTHENTICATION': APIKEY + ':' + APISECRET,
    'Content-Type': 'application/json',
    'Accept': 'application/json'
}

menuFetchURL = f"https://{INSTANCE}.revelup.com/weborders/menu"

x = requests.get(menuFetchURL, params={
                 'establishment': ESTABLISHMENT}, headers=headersGlobal)

z = x.json()
data = z['data']
categories = data['categories']
productList = {}
for category in categories:
    products = category['products']
    for product in products:
        prodName = product['name']
        prodPrice = product['price']
        productList.update({prodName: prodPrice})

sortedProducts = sorted(productList.items(), key=lambda x: x[1], reverse=True)

for product in sortedProducts:
    print(f'{product[0]} - ${product[1]}')