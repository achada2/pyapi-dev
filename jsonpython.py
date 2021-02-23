#!/usr/bin/python3

import json

def json_grab():
    with open("challenge.json", "r") as data:
        datastring = data.read()

    datadecoded = json.loads(datastring)
    return datadecoded

def contact_maker(datadecoded):

    #print(datadecoded)
   # print(type(datadecoded))           
#    print("Address: " + datadecoded[0]["address"])             
    for x in datadecoded:
        print("Name: " + x["name"])
        print("Email: " + x["email"])
        print("Phone: " + x["phone"])
        print("Address: " + x["address"])
        friendlist = []
#            print("Friends: " + y["name"])
        for y in x["friends"]:
            friendlist.append(y["name"])
        print("Friends: " + friendlist[])


def main():
    contact_maker(json_grab())
if __name__ == "__main__":
    main()

