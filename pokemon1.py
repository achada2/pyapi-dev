
import requests
import wget
#poke_api="https://pokeapi.co/api/v2/pokemon/bulbasaur/"

def api_pull():
    choice = input("What Pokemon picture would you like?")
    url= "https://pokeapi.co/api/v2/pokemon/" + choice + "/"
    return url

def json_conv(poke_api):
    json2python = requests.get("poke_api").json()
    return json2python


def api_slice(json2python):
    poke_pic = json2python["sprites"]["front_default"]
    return poke_pic

def wget_pic(imagelink):
    wget.download(imagelink, '/home/student/static/')

def main():
    wget_pic(api_slice(json_conv(api_pull())))
main()

