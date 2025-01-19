import json
import requests

#api to fetch the temperature of a city
city_name=input('Enter a city name:')
api_key='a34ba2e905d8676c0ffcb8ab6c2ceaea'

#to build api url
api_url=f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}'
get_server_information=requests.get(api_url)
data=get_server_information.json()
print (data)

import matplotlib.pyplot as plt

# Weather data
data = {
    'coord': {'lon': 78.4744, 'lat': 17.3753},
    'weather': [{'id': 721, 'main': 'Haze', 'description': 'haze', 'icon': '50d'}],
    'base': 'stations',
    'main': {
        'temp': 302.38,
        'feels_like': 301.22,
        'temp_min': 302.38,
        'temp_max': 302.88,
        'pressure': 1011,
        'humidity': 30,
        'sea_level': 1011,
        'grnd_level': 948
    },
    'visibility': 5000,
    'wind': {'speed': 4.12, 'deg': 10},
    'clouds': {'all': 20},
    'dt': 1737282903,
    'sys': {
        'type': 1,
        'id': 9214,
        'country': 'IN',
        'sunrise': 1737249570,
        'sunset': 1737290020
    },
    'timezone': 19800,
    'id': 1269843,
    'name': 'Hyderabad',
    'cod': 200
}

# Extracting necessary information
city = data['name']
country = data['sys']['country']
temperature = data['main']['temp'] - 273.15  # Convert Kelvin to Celsius
feels_like = data['main']['feels_like'] - 273.15
humidity = data['main']['humidity']
wind_speed = data['wind']['speed']
weather_main = data['weather'][0]['main']
weather_desc = data['weather'][0]['description']

# Display extracted data
print(f"City: {city}, Country: {country}")
print(f"Temperature: {temperature:.2f}°C")
print(f"Feels Like: {feels_like:.2f}°C")
print(f"Humidity: {humidity}%")
print(f"Wind Speed: {wind_speed} m/s")
print(f"Weather: {weather_main} ({weather_desc})")

# Visualizing the data
labels = ['Temperature (°C)', 'Feels Like (°C)', 'Humidity (%)', 'Wind Speed (m/s)']
values = [temperature, feels_like, humidity, wind_speed]

plt.figure(figsize=(8, 5))
plt.bar(labels, values, color=['blue', 'green', 'orange', 'purple'])
plt.title(f"Weather Data for {city}, {country}")
plt.ylabel("Values")
plt.tight_layout()
plt.show()
