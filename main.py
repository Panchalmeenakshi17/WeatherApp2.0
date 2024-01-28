import requests
import json


city = input("enter the name of the city: ")
url = f"https://api.weatherapi.com/v1/current.json?key=ec445270b25f4ea4bf5162047242601&q={city}"
r = requests.get(url)
# print(r.text)
# print(type(r.text))
try:
    dict = json.loads(r.text)
    print(dict['current']['temp_c'])
    # print(dict)
except:
    print("City not found! Please enter correct city name")

