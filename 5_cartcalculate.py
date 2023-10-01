import requests
import os
from dotenv import load_dotenv
load_dotenv()


def productList(x):
    z = x.json()
    data = z['data']
    categories = data['categories']
    productList = {}
    for category in categories:
        products = category['products']
        for product in products:
            prodID = product['id']
            prodPrice = product['price']
            productList.update({prodID: prodPrice})
    sortedProducts = sorted(productList.items(),
                            key=lambda x: x[1], reverse=True)
    return sortedProducts


APIKEY = os.getenv('APIKEY')
APISECRET = os.getenv('APISECRET')
INSTANCE = os.getenv('INSTANCE')
ESTABLISHMENT = os.getenv('ESTABLISHMENT')

headersGlobal = {
    'API-AUTHENTICATION': APIKEY + ':' + APISECRET,
    'Content-Type': 'application/json',
    'Accept': 'application/json'
}

menuFetchURL = f"https://{INSTANCE}.revelup.com/weborders/menu/"
cartCalculateURL = f"https://{INSTANCE}.revelup.com/specialresources/cart/calculate/"

sortedProducts = productList(requests.get(
    menuFetchURL, params={
        'establishment': ESTABLISHMENT,
        'mode': 6,
        'name': 'Online'
    }, headers=headersGlobal))

items = []
i = 0
while i < 3:
    product = sortedProducts[i]
    items.append({
        'product': product[0],
        'price': product[1],
        'quantity': 1
    })
    i += 1

request = requests.post(cartCalculateURL, json={
    'orderInfo': {
        'dining_option': 0,
        'asap': True
    },
    'establishment': ESTABLISHMENT,
    'items': items,
    "customMenuInfo": {
        "mode": 6,
        "name": "Online"
    }
}, headers=headersGlobal)
x = request.json()
data = x['data']
print(f"Subtotal: {data['subtotal']}")
print(f"Tax: {data['tax']}")
print(f"Total: {data['final_total']}")