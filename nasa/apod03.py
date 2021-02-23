#!/usr/bin/python3

import requests

NASAAPI = "https://api.nasa.gov/planetary/apod?"

# this function grabs our credentials
def returncreds():
    ## first I want to grab my credentials
    with open("/home/student/nasa.creds", "r") as mycreds:
        nasacreds = mycreds.read()
    ## remove any newline characters from the api_key
    nasacreds = "api_key=" + nasacreds.strip("\n")
    return nasacreds

# this is our main function
def main():
    ## first grab credentials
    nasacreds = returncreds()

    nasadate = input(" Enter Date to query in format YYYY-MM-DD \n")
    
    ## make a call to NASAAPI with our key
    apodresp = requests.get(NASAAPI + nasacreds + "&date=" + nasadate)

    ## strip off json
    apod = apodresp.json()

   # print(apod)
   # print(apod["url"])
    if (apod["media_type"] == "video"):
        print("Video Link:"  + apod["thumbnail_url"])
    else:
        print("Image Link:"  + apod["url"])
       
#    print()

 #   print(apod["media_type"])

 #   print(apod["date"] + "\n")

  #  print(apod["explanation"])

  #  print(apod["url"])

if __name__ == "__main__":
    main()

