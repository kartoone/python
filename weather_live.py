import json
import urllib.parse
import urllib.request


def get_json(url, params):
    """Fetch a URL with query parameters and return the parsed JSON."""
    full_url = f"{url}?{urllib.parse.urlencode(params)}"
    with urllib.request.urlopen(full_url, timeout=10) as response:
        return json.load(response)


def get_temp_f(city):
    """Look up a city, then return its current temperature in Fahrenheit."""
    geo = get_json(
        "https://geocoding-api.open-meteo.com/v1/search",
        {"name": city, "count": 1},
    )
    if not geo.get("results"):
        raise ValueError(f"Couldn't find a place called '{city}'.")

    place = geo["results"][0]
    weather = get_json(
        "https://api.open-meteo.com/v1/forecast",
        {
            "latitude": place["latitude"],
            "longitude": place["longitude"],
            "current": "temperature_2m",
            "temperature_unit": "fahrenheit",
        },
    )
    return place["name"], weather["current"]["temperature_2m"]


def main():
    city = input("what city? ")
    try:
        name, degF = get_temp_f(city)
    except (ValueError, OSError) as err:
        print(f"Couldn't get the temperature: {err}")
        return

    print(f"It's {degF:.0f}°F in {name}.")
    if degF > 80:
        print("shorts")
    elif degF >= 50:
        print("long sleeves")
    else:
        print("jacket")


if __name__ == "__main__":
    main()