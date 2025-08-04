# weather.py

import requests
import os
from dotenv import load_dotenv


# Load environment variables from .env file
load_dotenv()
API_KEY = os.getenv("OPENWEATHER_API_KEY")  # Use the variable name, not the value

def get_weather(city):
    # Construct API endpoint
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=imperial"

    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise error for bad status
        data = response.json()

        # Extract relevant data
        temp = data['main']['temp']
        condition = data['weather'][0]['description'].title()
        humidity = data['main']['humidity']  # fixed typo: humanity ➝ humidity
        wind = data['wind']['speed']

        # Display weather
        print(f"\n🌤️  Weather in {city.title()}:")
        print(f"Condition: {condition}")
        print(f"Temperature: {temp}°F")
        print(f"Humidity: {humidity}%")
        print(f"Wind Speed: {wind} mph\n")

    except requests.exceptions.HTTPError:
        print("❌ Invalid city or failed to fetch weather.")
    except Exception as e:
        print(f"⚠️ Something went wrong: {e}")

if __name__ == "__main__":  # fixed typo: ++ ➝ ==
    city = input("Enter city name: ")
    get_weather(city)