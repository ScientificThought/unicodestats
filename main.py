file = open('data/dom-casmurro.txt', mode='r+', encoding='utf-8')

characters = {}

for line in file:
    lower_line = line.lower().replace('\n', '').replace(' ', '')
    line_characters = list(lower_line)
    for character in line_characters:
        if character not in characters.keys():
            characters[character] = 1

        else:
            characters[character] += 1

print(characters)

