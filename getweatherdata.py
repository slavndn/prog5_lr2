from owm_key import owm_api_key
import json
import requests
import os

def get_weather_data(place, api_key=None):
    if api_key is None:
        return None

    if not place:
        return None

    url = f'https://api.openweathermap.org/data/2.5/weather?q={place}&appid={api_key}&units=metric'
    response = requests.get(url)

    if response.status_code != 200:
        return None

    data = response.json()

    # Extract required information
    city_name = data.get("name")
    country_code = data.get("sys", {}).get("country")
    coordinates = data.get("coord", {})
    latitude = coordinates.get("lat")
    longitude = coordinates.get("lon")
    feels_like = data.get("main", {}).get("feels_like")
    timezone_offset = data.get("timezone") // 3600  # Convert seconds to hours

    # Format timezone
    timezone = f"UTC{'+' if timezone_offset >= 0 else '-'}{abs(timezone_offset)}"

    return json.dumps({
        "name": city_name,
        "coord": {"lon": longitude, "lat": latitude},
        "country": country_code,
        "feels_like": feels_like,
        "timezone": timezone
    })

if __name__ == '__main__':
    
    moscow_weather = (get_weather_data('Moscow', api_key=owm_api_key))
    spb_weather = (get_weather_data('Saint Petersburg', api_key=owm_api_key))
    dhaka_weather = (get_weather_data('Dhaka', api_key=owm_api_key))
    
    term_size = os.get_terminal_size()
    
    print()
    print()
    print('-' * term_size.columns)
    print(moscow_weather)
    print('-' * term_size.columns)
    print(spb_weather)
    print('-' * term_size.columns)
    print(dhaka_weather)
    print('-' * term_size.columns)
    print()
    print()
    