import requests

pokemon_url = "https://pokeapi.co/api/v2/pokemon"
pokemon_data = requests.get(pokemon_url)
data_json = pokemon_data.json()

