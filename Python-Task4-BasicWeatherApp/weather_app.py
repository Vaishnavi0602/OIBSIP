import requests

# ======================================
# Replace with your OpenWeatherMap API Key
# ======================================
API_KEY = "YOUR_API_KEY"

BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


def get_weather(city):
    """Fetch weather data from OpenWeatherMap."""

    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    try:
        response = requests.get(BASE_URL, params=params, timeout=10)

        # Invalid API Key
        if response.status_code == 401:
            print("\n❌ Invalid API Key.")
            return

        # City Not Found
        if response.status_code == 404:
            print("\n❌ City not found.")
            return

        response.raise_for_status()

        data = response.json()

        city_name = data["name"]
        country = data["sys"]["country"]

        temp_c = data["main"]["temp"]
        temp_f = (temp_c * 9 / 5) + 32

        humidity = data["main"]["humidity"]

        weather = data["weather"][0]["description"].title()

        wind_speed = data["wind"]["speed"]

        print("\n" + "=" * 45)
        print("          WEATHER REPORT")
        print("=" * 45)
        print(f"City           : {city_name}")
        print(f"Country        : {country}")
        print(f"Temperature    : {temp_c:.2f} °C")
        print(f"Temperature    : {temp_f:.2f} °F")
        print(f"Humidity       : {humidity}%")
        print(f"Weather        : {weather}")
        print(f"Wind Speed     : {wind_speed} m/s")
        print("=" * 45)

    except requests.exceptions.Timeout:
        print("\n❌ Request timed out.")

    except requests.exceptions.ConnectionError:
        print("\n❌ Network error. Please check your internet connection.")

    except requests.exceptions.RequestException:
        print("\n❌ Unable to fetch weather data.")


def main():

    print("=" * 45)
    print("        BASIC WEATHER APP")
    print("=" * 45)

    while True:

        city = input("\nEnter City Name: ").strip()

        if city == "":
            print("❌ City name cannot be empty.")
            continue

        get_weather(city)

        choice = input("\nSearch another city? (Y/N): ").strip().lower()

        if choice != "y":
            print("\nThank you for using the Weather App!")
            break


if __name__ == "__main__":
    main()