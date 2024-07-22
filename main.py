# main.py

import json

def load_hero_data(filename):
    with open(filename, 'r') as file:
        data = json.load(file)
    return data

def get_hero_info(hero_name, data):
    return data.get(hero_name, 'Hero not found')

if __name__ == "__main__":
    hero_data = load_hero_data('heroes.json')
    hero_name = input("Enter hero name: ")
    info = get_hero_info(hero_name, hero_data)
    print(info)