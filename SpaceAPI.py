import requests
import json
import time

#Get the response from the API endpoint.
response = requests.get("http://api.open-notify.org/astros.json")
data = response.json()

print(data["number"])
print(data)

#ISS Location
while 1 == 1: #Uses a simple loop to constantly update the location of the ISS
    time.sleep(1.0) #Delay so response doesn't overflow
    response2 = requests.get("http://api.open-notify.org/iss-now.json") #ISS Information
    data2 = response2.json()
    print('Location update:')
    print(data2) #Prints location of ISS




