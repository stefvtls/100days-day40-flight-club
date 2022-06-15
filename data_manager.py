from pprint import pprint
import requests
import os
from dotenv import load_dotenv
load_dotenv()

SHEETY_PRICES_ENDPOINT = os.getenv('SHEETY_API')
SHEETY_USERNAME = os.getenv('SHEETY_USER')
SHEETY_PASS = os.getenv('SHEETY_PASSWORD')


class DataManager:

    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=SHEETY_PRICES_ENDPOINT, auth=(SHEETY_USERNAME, SHEETY_PASS))
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data, auth=(SHEETY_USERNAME, SHEETY_PASS)
            )
            print(response.text)
