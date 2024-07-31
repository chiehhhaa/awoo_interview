import requests

BASE_URL = "https://pokeapi.co/api/v2/pokemon/"

def get_pokemon_data(pokemon_id):
    """根據 ID 獲取寶可夢詳細資料"""
    response = requests.get(f"{BASE_URL}{pokemon_id}/")
    response.raise_for_status()  
    return response.json()

def get_pokemon_name_by_id(pokemon_id):
    """列出指定 ID 的寶可夢名稱"""
    pokemon_data = get_pokemon_data(pokemon_id)
    return pokemon_data['name']

def main():
    pokemon_id = 6
    name = get_pokemon_name_by_id(pokemon_id)
    print(f"ID {pokemon_id} 的寶可夢名稱為: {name}")


if __name__ == "__main__":
    main()