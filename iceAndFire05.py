#!/usr/bin/python3
"""Alta3 Research - Exploring OpenAPIs with requests"""
# documentation for this API is at
# https://anapioficeandfire.com/Documentation

import requests
import pprint

AOIF_CHAR = "https://www.anapioficeandfire.com/api/characters/"
#AOIF_HOUSE = "got_dj["allegiances"]"
def char():
        ## Ask user for input
        got_charToLookup = input("Pick a number between 1 and 1000 to return info on a GoT character! " )

        ## Send HTTPS GET to the API of ICE and Fire character resource
        gotresp = requests.get(AOIF_CHAR + got_charToLookup)

        ## Decode the response

        # the got_dj variable is created inside a function... which means it only exists inside of this function
        # char_house() has NO IDEA what "got_dj" is

        got_dj = gotresp.json()
       # pprint.pprint(got_dj)
       # print(got_dj["allegiances"])
       # print(got_dj["books"])

        # if we add a "return" line, we'll have char() pass along the value
        return got_dj


def char_house(got_dj):
   # for x in got_dj["allegiances"]:
        AOIF_HOUSE = got_dj["allegiances"]
        # AOIF_HOUSE is a list... a list of all those links
        # you'll need to run each element in that list one at a time into requests.get
        # so you'll need to build a for loop

    ## Ask user for input
        for x in AOIF_HOUSE:
            gothouse = requests.get(x)
        ## Decode the response
            got_dj1 = gothouse.json()
            print("House: " + got_dj1["name"])

def char_book(got_dj):
   # for x in got_dj["allegiances"]:
        AOIF_BOOK = got_dj["books"]
        for x in AOIF_BOOK:
            gotbook = requests.get(x)
        ## Decode the response
            got_dj2 = gotbook.json()
            print("Book: " + got_dj2["name"])


def main():
    char_book(char())

if __name__ == "__main__":
        main()

