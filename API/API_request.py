# import requests
# response = requests.get("http://api.weatherapi.com/v1/current.json?key=7f58f399e78f430b92195359232103&q=Abuja&aqi=no")

# # print(response.json())
# data = response.json()
# print(data['location']['localtime'])

# import requests
# response = requests.get("https://dummyjson.com/products")

# data = response.json()
# print(data['products'][1]['images'][1])

# a = ['a', {4: 'books', 'b': ['hand', 'toes', 'legs', {'c': 'pencil'}, 'head']}]
# print(a[1]['b'][4])

import requests

url = "https://dummyjson.com/products/1"
json = {'title': 'Harry Potter', 'description': 'This is a book', 'stock': 69}
response = requests.put(url, data=json)

print(response.json())