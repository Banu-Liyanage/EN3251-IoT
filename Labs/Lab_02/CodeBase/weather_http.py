import requests

API_KEY = "" #Replace with your API key  
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather(city, country_code=None, units="metric"):
    q = city if not country_code else f"{city},{country_code}"
    params = {"q": q, "appid": API_KEY, "units": units}
    r = requests.get(BASE_URL, params=params, timeout=10)
    r.raise_for_status()
    data = r.json()
    main = data.get("main", {})
    wind = data.get("wind", {})
    weather0 = (data.get("weather") or [{}])[0]
    print(f"City: {data.get('name')}, Country: {(data.get('sys') or {}).get('country')}")
    print(f"Weather: {weather0.get('main')} - {weather0.get('description')}")
    print(f"Temp: {main.get('temp')}°C  Feels: {main.get('feels_like')}°C")
    print(f"Humidity: {main.get('humidity')}%  Pressure: {main.get('pressure')} hPa")
    print(f"Wind: {wind.get('speed')} m/s")
    return data

if __name__ == "__main__":
    city = input("Enter City (e.g., Colombo): ").strip()
    cc   = input("Enter Country Code (optional, e.g., LK): ").strip() or None
    get_weather(city, cc)

