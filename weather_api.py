import requests

def get_weather(api_key, location):
    # Construct the API request URL for OpenWeatherMap
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric"

    # Send the request
    response = requests.get(url)
    data = response.json()

    # Extract the weather and temperature
    weather = data['weather'][0]['main']  # e.g., 'Rain'
    temp = data['main']['temp']  # Current temperature

    return weather, temp
