
import requests


def pokedex(choice):
    pokedex = requests.get("https://pokeapi.co/api/v2/pokemon/" + choice).json()
    return pokedex["name"]

print(pokedex("salamence"))

#print(pokedex("pikachu"))
