import json
import requests

def get_weather_data(location, units='metric'):
    api_key = "YOUR_API_KEY"
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": location,
        "appid": api_key,
        "units": units
    }
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()  
        return response.json()
    except requests.exceptions.RequestException as e:
        print("Error fetching weather data:", e)
        return None

def display_weather(weather_data):
    if weather_data:
        print("Current Weather: ")
        print(f"Weather: {weather_data['weather'][0]['description']}")
        print(f"Temperature: {weather_data['main']['temp']}")
        print(f"Humidity: {weather_data['main']['humidity']}%")
        print(f"Wind Speed: {weather_data['wind']['speed']} m/s")
    else:
        print("No weather data available.")

def main():
    location = input("Enter city name or zip code: ")
    units = input("Choose units (metric/imperial): ").strip().lower()
    if units not in ['metric', 'imperial']:
        print("Invalid units. Using metric by default.")
        units = 'metric'
    weather_data = get_weather_data(location, units)
    display_weather(weather_data)

if __name__ == "__main__":
    main()
