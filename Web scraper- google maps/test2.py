import requests

url = "https://maps.googleapis.com/maps/api/place/details/json?place_id=ChIJXyPxkalbBEcRfK2UoxGJY4k&fields=name%2Cadr_address%2Cformatted_phone_number&key=AIzaSyAJmJPNuZtpBKN8lIPgDVI__1mIDMRbNWM"

payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)