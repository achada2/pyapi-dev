#!/usr/bin/env python3
import argparse
import time
import requests
import hashlib
import webbrowser

## Define the API here
MARVELCHAR = 'http://gateway.marvel.com/v1/public/characters'

## Calculate a hash to pass through to our MARVEL API call
## Marvel API wants md5 calc md5(ts+privateKey+publicKey)
def hashbuilder(timeywimey, pvkee, pubkee):
    return hashlib.md5((timeywimey+pvkee+pubkee).encode('utf-8')).hexdigest()

## Perform a call to MARVEL Character API
## http://gateway.marvel.com/v1/public/characters
## ?name=Spider-Man&ts=1&apikey=1234&hash=ffd275c5130566a2916217b101f26150
def marvelcharcall(stampystamp, hashyhash, pkeyz, lookmeup):
    r = requests.get(MARVELCHAR+"?name="+lookmeup+"&ts="+stampystamp+"&apikey="+pkeyz+"&hash="+hashyhash)

    print(MARVELCHAR+"?name="+lookmeup+"&ts="+stampystamp+"&apikey="+pkeyz+"&hash="+hashyhash)
    return r.json()

    
def main():           
    
    ## harvest private key
    with open(args.dev) as prvky:
        getprv = prvky.read().rstrip('\n')
    
    ## harvest public key
    with open(args.pub) as pubky:
        getpub = pubky.read().rstrip('\n')
    
    ## create an integer from a float timestamp (for our RAND)
        tmstmp = str(time.time()).rstrip('.')
    
    ## build hash with hashbuilder(timestamp, privatekey, publickey)
    hshbld = hashbuilder(tmstmp, getprv, getpub)

    ## call the API with marvelcharcall(timestamp, hash, publickey, character)
    marvelhero = marvelcharcall(tmstmp, hshbld, getpub, args.hero)
    
    ## display results
#    print(uncannyxmen)
    print(marvelhero["data"]["results"][0]["name"])
    print(marvelhero["data"]["results"][0]["description"])
    print(marvelhero["data"]["results"][0]["comics"]["collectionURI"])
    COMICLIST = (marvelhero["data"]["results"][0]["comics"]["collectionURI"])
    webbrowser.open('COMICLIST') 

## Define arguments to collect
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--dev', help='Provide the /path/to/file.priv \
      containing Marvel private developer key')
    parser.add_argument('--pub', help='Provide the /path/to/file.pub \
      containing Marvel public developer key')
    
    ## The line below is NEW! This allows us to pass the lookup character
    parser.add_argument('--hero', \
      help='Character to search for within the Marvel universe')
    args = parser.parse_args()
    main()

