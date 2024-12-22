from django.shortcuts import render
import requests

def get_weather(city, url):
    try:
        r = requests.get(url.format(city)).json()
        temp_in_kelvin = r['main']['temp']
        temp_in_celsius = temp_in_kelvin - 273.15  # Convert Kelvin to Celsius
        
        return {
            'city': city,
            'temperature': round(temp_in_celsius, 1),  # Round to 1 decimal place
            'description': r['weather'][0]['description'],
            'icon': r['weather'][0]['icon'],
            'humidity': r['main']['humidity'],
            'pressure': r['main']['pressure'],
            'wind_speed': r['wind']['speed'],
            'feels_like': round(r['main']['feels_like'] - 273.15, 1)  # Convert feels_like to Celsius
        }
    except:
        return {
            'city': f'{city} (Not Found)',
            'temperature': None,
            'description': 'City not found',
            'icon': None,
            'humidity': None,
            'pressure': None,
            'wind_speed': None,
            'feels_like': None
        }

def index(request):
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid=08ffc4857013121418156ffc934a37da'
    
    if request.method == 'POST':
        main_city = request.POST['city']
    else:
        main_city = 'Kiambu'

    # Define neighbor cities (replace with actual neighboring cities)
    neighbor1 = 'Nairobi'
    neighbor2 = 'Thika'
    
    # Get weather for all cities
    city_weather = get_weather(main_city, url)
    neighbor1_weather = get_weather(neighbor1, url)
    neighbor2_weather = get_weather(neighbor2, url)
    
    context = {
        'city_weather': city_weather,
        'neighbor1_weather': neighbor1_weather,
        'neighbor2_weather': neighbor2_weather
    }
    
    return render(request, 'weather/weather.html', context)