import requests
response = requests.get("http://api.weatherapi.com/v1/current.json?key=7f58f399e78f430b92195359232103&q=Abuja&aqi=no")

# print(response.json())
data = response.json()
print(data['current']['humidity'])