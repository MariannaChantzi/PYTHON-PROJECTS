# Libraries
import requests
import clipboard

API_KEY = '82977563a3fe28bffa14a0c7d3d433aa'
BASE_URL = 'https://api.openweathermap.org/data/2.5/weather'

lat = input("Enter the city's latitude coordinate: ")
lon = input("Enter the city's longitude cooridate: ")

request_url = f"{BASE_URL}?lat={lat}&lon={lon}&appid={API_KEY}&units=metric"
response = requests.get(request_url)

if response.status_code == 200:
    data = response.json()
    weather = data['weather'][0]['description']
    temperature = round(data['main']['temp'],1)
    print('Weather:',weather)
    print('Temperature:',temperature,'Celsius')
else:
    print('An error has occured.')
