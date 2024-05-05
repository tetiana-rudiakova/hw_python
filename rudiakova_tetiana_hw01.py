import json

soubor = {}

with open('alice.txt', 'r', encoding='utf-8') as file:
    for line in file:
        for char in line:
            if char not in ' \n':
                char = char.lower()
                if char in soubor:
                    soubor[char] += 1
                else:
                    soubor[char] = 1

with open('hw01_output.json', 'w', encoding='utf-8') as json_file:
    json.dump(soubor, json_file, indent=4)