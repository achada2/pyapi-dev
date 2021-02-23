import requests
poke_api="https://pokeapi.co/api/v2/pokemon/bulbasaur/"

def json_conv(poke_api):
    json2python = requests.get("poke_api").json()
    return json2python
print(json_conv(poke_api))
#poke_api=https://pokeapi.co/api/v2/pokemon/bulbasaur/)

