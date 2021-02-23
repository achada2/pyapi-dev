#!/usr/bin/python3

import requests
import json

# define the URL we want to use
GETURL = "http://ip.jsontest.com"

def main():

    # use requests library to send an HTTP GET
    resp = requests.get(f"{GETURL}")

    # strip off JSON response
    # and convert to PYTHONIC LIST / DICT
    respjson = resp.json()

    # display our PYTHONIC data (LIST / DICT)
    print(respjson["ip"])

if __name__ == "__main__":
    main()

