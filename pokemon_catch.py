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

def list_pokemon_names_and_types(lower_id, upper_id):
    """列出 ID 範圍內的寶可夢名稱及屬性，依照 ID 由小至大排序"""
    names_and_types = []
    for pokemon_id in range(lower_id, upper_id):
        if pokemon_id > 0:
            pokemon_data = get_pokemon_data(pokemon_id)
            name = pokemon_data['name']
            types = [t['type']['name'] for t in pokemon_data['types']]
            names_and_types.append((pokemon_id, name, types))
    return sorted(names_and_types, key=lambda x: x[0])

def main():
    pokemon_id = 6
    name = get_pokemon_name_by_id(pokemon_id)
    print(f"【目標一】 ID {pokemon_id} 的寶可夢名稱為: {name}")

    names_and_types = list_pokemon_names_and_types(1, 20)
    print("【目標二】")
    for pokemon_id, name, types in names_and_types:
        print(f"ID: {pokemon_id} 寶可夢名稱: {name}, 屬性: {', '.join(types)}")


if __name__ == "__main__":
    main()