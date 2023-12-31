
from IPython.display import Image, display

from pgeocode import Nominatim
import requests
import json

degree_sign = u"\N{DEGREE SIGN}"

print(f"THE TEMPERATURE IS 90 {degree_sign}F")

def display_forecast(zip_code, country_code="US"):
    """
    Displays a seven day weather forecast for the provided zip code.

    Params :

        country_code (str) a valid country code (see supported country codes list). Default is "US".

        zip_code (str) a valid US zip code, like "20057" or "06510".

    """
    try:

        nomi = Nominatim(country_code)
        geo = nomi.query_postal_code(zip_code)
        latitude = geo["latitude"]
        longitude = geo["longitude"]

        request_url = f"https://api.weather.gov/points/{latitude},{longitude}"
        response = requests.get(request_url)
        #print(response.status_code)
        parsed_response = json.loads(response.text)

        forecast_url = parsed_response["properties"]["forecast"]
        forecast_response = requests.get(forecast_url)
        #print(forecast_response.status_code)
        parsed_forecast_response = json.loads(forecast_response.text)

        periods = parsed_forecast_response["properties"]["periods"]
        daytime_periods = [period for period in periods if period["isDaytime"] == True]

        for period in daytime_periods:
            #print(period.keys())
            print("-------------")
            print(period["name"], period["startTime"][0:7])
            print(period["shortForecast"], f"{period['temperature']} {degree_sign}{period['temperatureUnit']}")
            #print(period["detailedForecast"])
            display(Image(url=period["icon"]))
        
        return response.status_code

        

    except requests.exceptions.RequestException as e:
        print(f"Error gathering data: {str(e)}")
        return None


if __name__ == "__main__":

    zip_code = input("Please input a zip code (e.g. '06510'): ") or "06510"
    print("ZIP CODE:", zip_code)

    display_forecast(zip_code)


    