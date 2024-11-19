file = open('data/dom-casmurro.txt', mode='r+', encoding='utf-8')

characters_dict = {}

for line in file:
    lower_line = line.lower().strip()
    line_characters = list(lower_line)
    for character in line_characters:
        n = characters_dict.get(character, 0) + 1
        characters_dict[character] = n

print(characters_dict)