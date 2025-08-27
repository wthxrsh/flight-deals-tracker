from xmlrpc.client import MAXINT
import os
from dotenv import load_dotenv
load_dotenv()

from flight_data import FlightSearch
from pprint import pprint
from datetime import datetime
from datetime import timedelta


import requests
SHEETY_TOKEN = os.getenv("SHEETY_TOKEN")
url = os.getenv("SHEET")
flight_endpoint = "https://test.api.amadeus.com/v1"
headers = {
    "Authorization": f"Bearer {SHEETY_TOKEN}"
}

def get_data():
    response = requests.get(url=url, headers=headers)

    sheet_data = response.json()
    return sheet_data

sheet_data = get_data()
print(sheet_data)

a = FlightSearch()
token = a._token


def search_city(city):
    header = {
        "Authorization": f"Bearer {token}"
    }
    parameters = {
        "keyword": city,
        "max": 2,
        "include": "AIRPORTS"
    }
    location = requests.get(url=f"{flight_endpoint}/reference-data/locations/cities", headers=header, params=parameters)
    location = location.json()
    return location

def assign_iata():
    for i in range(len(sheet_data["prices"])):
        found_city = search_city(sheet_data["prices"][i]["city"] )
        if found_city["data"][0]["iataCode"]:
            body = {
                "price":{
                    "iataCode": found_city["data"][0]["iataCode"]
                }
            }
            response = requests.put(url=f"{url}/{sheet_data["prices"][i]["id"]}", json=body, headers=headers)
        else:
            print("No IATA found")

def search_flight(origincode, destcode, deptdate, returndate,adults):
    flight_endpoint = "https://test.api.amadeus.com/v2"
    search_url = f"{flight_endpoint}/shopping/flight-offers"

    parameters = {
        "originLocationCode": origincode,
        "destinationLocationCode": destcode,
        "departureDate": deptdate,
        "returnDate": returndate,
        "currencyCode": "INR",
        "nonStop": "true",
        "adults": adults
    }

    header = {
        "Authorization": f"Bearer {token}"
    }

    details = requests.get(url=search_url, params=parameters, headers=header)
    data = details.json()
    return data

tomorrow = datetime.now().date() + timedelta(days=1)
six_months_later = datetime.now().date() + timedelta(days=(6*30))

def prices():
    for i in range(len(sheet_data["prices"])):
        flight = search_flight("DEL", sheet_data["prices"][i]["iataCode"],tomorrow , six_months_later ,1)
        lowestPrice = sheet_data["prices"][i]["lowestPrice"]
        if flight is None or not flight["data"]:
            print("No flight data")
            body = {
                "price":{
                    "lowestPrice": "N/A"
                }
            }
            res = requests.put(url=f"{url}/{sheet_data["prices"][i]["id"]}", json=body, headers=headers )
            print(res.status_code)
            continue

        for f in flight["data"]:

            price = float(f["price"]["grandTotal"])
            if lowestPrice == "N/A":
                lowestPrice = MAXINT
            if price < float(lowestPrice):
                lowestPrice = price
                body = {
                    "price": {
                        "lowestPrice": lowestPrice
                    }
                }
                res = requests.put(url=f"{url}/{sheet_data["prices"][i]["id"]}", json=body, headers=headers)
                print(res.status_code)


        print(f"Lowest price to destination {sheet_data["prices"][i]["iataCode"]} is: Rs. {lowestPrice}")




