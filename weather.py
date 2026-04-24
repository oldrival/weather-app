import requests

API_KEY = "5f26d55c38efcf36fb7f0ded0a195ef0"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }
    response = requests.get(BASE_URL, params=params)
    data = response.json()

    if data["cod"] != 200:
        print(f"City not found: {city}")
        return

    name = data["name"]
    country = data["sys"]["country"]
    temp = data["main"]["temp"]
    feels_like = data["main"]["feels_like"]
    humidity = data["main"]["humidity"]
    description = data["weather"][0]["description"]

    print(f"\n📍 {name}, {country}")
    print(f"🌡  Temperature: {temp}°C (feels like {feels_like}°C)")
    print(f"💧 Humidity: {humidity}%")
    print(f"☁️  Conditions: {description.capitalize()}")

def main():
    while True:
        city = input("\nEnter city name (or 'quit' to exit): ")
        if city.lower() == "quit":
            print("Goodbye!")
            break
        get_weather(city)

main()