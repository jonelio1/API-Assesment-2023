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

paramsOrderFetch = {
    'establishment': ESTABLISHMENT,
    'order_by': '-created_date',
    'dining_option': 1,
    'limit': 1
}
orderFetchURL = f"https://{INSTANCE}.revelup.com/resources/Order/"

x = requests.get(orderFetchURL, headers=headersGlobal, params=paramsOrderFetch)
z = x.json()
objects = z['objects']
try:
    order = objects[0]
except:
    print('No orders found for specified parameters, exiting')
    exit()
orderID = order['id']

paramsItemFetch = {
    'establishment': ESTABLISHMENT,
    'order': orderID
}

orderItemFetchURL = f"https://{INSTANCE}.revelup.com/resources/OrderItem/"

x = requests.get(orderItemFetchURL, headers=headersGlobal,
                 params=paramsItemFetch)

z = x.json()
orderItems = z['objects']
currentHighestPrice = 0
mostExpensiveProduct = {
    'name': '',
    'price': '',
    'tax': '',
    'quantity': ''
}
for item in orderItems:
    if item['price'] > currentHighestPrice:
        currentHighestPrice = item['price']
        mostExpensiveProduct['name'] = item['product_name_override']
        mostExpensiveProduct['price'] = item['price']
        mostExpensiveProduct['tax'] = item['tax_amount']
        mostExpensiveProduct['quantity'] = item['quantity']

print(f"{mostExpensiveProduct['name']} - Price {mostExpensiveProduct['price']} - Tax {mostExpensiveProduct['tax']} - Quantity {mostExpensiveProduct['quantity']}")
