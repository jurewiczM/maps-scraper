from fileinput import close
import requests
import json

url = "https://maps.googleapis.com/maps/api/place/textsearch/json?query=modular%20houses%20in%20Wielkopolskie&key=AIzaSyAJmJPNuZtpBKN8lIPgDVI__1mIDMRbNWM"

payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)


f = open("plik.json","w")
f.write(response.text)
