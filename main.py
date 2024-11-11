class Unicodestats:
    @staticmethod
    def open_file(filename):
        """
        Open the file and returns the contentt.
        The "filename" needs to be inside "data" folder.
        """
        try:
            with open(f'data/{filename}', mode='r', encoding='utf-8') as file:
                return file.read()
        except FileNotFoundError:
            print(f"O arquivo {filename} não foi encontrado. Cheque se o arquivo realmente está dentro da pasta 'data'.")
            return None

    @staticmethod
    def characters_count(text):
        """
        Counts the number of characters in the text, creating a histogram.
        """
        cleaned_text = text.lower().replace(' ', '').replace('\n', '')

        characters_dict = {}

        for char in cleaned_text:
            if char in characters_dict:
                characters_dict[char] += 1
            else:
                characters_dict[char] = 1

        return characters_dict

if __name__ == "__main__":
    file_content = Unicodestats.open_file('dom-casmurro.txt')
    characters = Unicodestats.characters_count(file_content)
    print(characters)

