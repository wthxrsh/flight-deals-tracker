from sheet_data import get_data, assign_iata,prices
from flight_data import FlightSearch
from pprint import pprint


# for i in range(len(sheet_data["prices"])):
#     city = sheet_data["prices"][i]["city"]
#     id = sheet_data["prices"][i]["id"]
#     price = sheet_data["prices"][i]["lowestPrice"]
#     flight = FlightSearch(city)
#     print(flight.found_city)

sheet_data = get_data()
pprint(sheet_data)

iataStatus = assign_iata()
print(iataStatus)

prices()

