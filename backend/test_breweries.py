import unittest

import requests


class TestBreweries(unittest.TestCase):

    def test_breweries(self):
        breweries = requests.get("https://api.openbrewerydb.org/breweries/autocomplete?query=lagunitas").json()
        filtered_breweries = [brewerie for brewerie in breweries if brewerie["name"] == "Lagunitas Brewing Co"]
        for b in filtered_breweries:
            details = requests.get(f'https://api.openbrewerydb.org/breweries/{b["id"]}').json()
            if details["state"] == "California":
                self.assertEqual(details["name"], "Lagunitas Brewing Co")
                self.assertEqual(details["street"], "1280 N McDowell Blvd")
                self.assertEqual(details["phone"], "7077694495")