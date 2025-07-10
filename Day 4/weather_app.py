import requests

def weather_app(city_name, api_key):
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    
    params = {
        "q": city_name,
        "appid": api_key,
        "units": "metric"
    }

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        data = response.json()

        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        description = data["weather"][0]["description"]

        print(f"\nWeather in {city_name.title()}:")
        print(f"Temperature: {temp}°C")
        print(f"Humidity: {humidity}%")
        print(f"Description: {description.capitalize()}")
    else:
        print("Error fetching data. Please check the city name or API key.")

if __name__ == "__main__":
    api_key = "aa1e040a558d0fc18fad77b6d4eb2b07"
    city = input("Enter city name: ")
    weather_app(city, api_key)
