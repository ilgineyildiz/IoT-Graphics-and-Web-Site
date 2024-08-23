#field_1 temperature field 2 wind field 3 humiditiy field 4 color 
#field 5 light field 6 weight field 7 mems and tilt field 8 de current/voltage  
import requests
API_KEY = 'b5d91b83c85276cddc84eb67' # demo account #100 Demo Data HTTP random test

url = 'http://iothook.com/api/device/?api_key=' + API_KEY + "&results=1"

response = requests.get(url)
data = response.json()
print(data)
print(len(data))
print(data[0]['id'])