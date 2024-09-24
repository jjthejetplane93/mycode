#!/usr/bin/python3
"""Alta3 Research - Exploring OpenAPIs with requests"""
# documentation for this API is at
# https://anapioficeandfire.com/Documentation

import requests
import pprint

AOIF_CHAR = "https://www.anapioficeandfire.com/api/characters/"
houses = []
books = []
def main():
        ## Ask user for input
        got_charToLookup = input("Pick a number between 1 and 1000 to return info on a GoT character! " )

        ## Send HTTPS GET to the API of ICE and Fire character resource
        gotresp = requests.get(AOIF_CHAR + got_charToLookup)

        ## Decode the response
        got_dj = gotresp.json()
        pprint.pprint(got_dj)

        if got_dj["allegiances"]:
            print("this character belongs to the following hous(es)")
            for house in got_dj["allegiances"] :
                print(f'\t{requests.get(house).json()["name"]}')

        if got_dj["books"]:
            print("this character appears in the following book(s)")
            for book in got_dj["books"]:
                print(f'\t{requests.get(book).json()["name"]}')

if __name__ == "__main__":
        main()

