import re


class Translator:
    def __init__(self):
        self.beep_map = {
            'A': '.-', 'B': '-...', 'C': '-.-.',
            'D': '-..', 'E': '.', 'F': '..-.',
            'G': '--.', 'H': '....', 'I': '..',
            'J': '.---', 'K': '-.-', 'L': '.-..',
            'M': '--', 'N': '-.', 'O': '---',
            'P': '.--.', 'Q': '--.-', 'R': '.-.',
            'S': '...', 'T': '-', 'U': '..-',
            'V': '...-', 'W': '.--', 'X': '-..-',
            'Y': '-.--', 'Z': '--..', '1': '.----',
            '2': '..---', '3': '...--', '4': '....-',
            '5': '.....', '6': '-....', '7': '--...',
            '8': '---..', '9': '----.', '0': '-----',
            ', ': '--..--', '.': '.-.-.-', '?': '..--..',
            '/': '-..-.', '-': '-....-', '(': '-.--.',
            ')': '-.--.-'}
    
    # Gets the key and the value enterd
    def key_finder(self, data: str) -> str:
        for key, value in self.beep_map.items():
            if data == value:
                return key

    # takes text and converts it to morse code
    def encoder(self, text: str) -> str:
        encoded_text = ""
        # removes unknown chacters
        clean_text = re.sub("[^\w\s]+", "",text).split(" ")

        for word in clean_text:
            buffer = ""
            for char in word.upper():
                buffer = buffer + " " + self.beep_map.get(char)

            encoded_text = encoded_text + " " + buffer
            buffer = ""

        return encoded_text

    def decoder(self, encoded_text: str) -> str:
        list_of_tokens = encoded_text.split("  ")
        decoded_text = ""

        for token in list_of_tokens:
            if " " in token:
                word_buffer = ""
                for sub_token in token.split(" "):
                    if not sub_token.isspace() and len(sub_token) > 0:
                        word_buffer += self.key_finder(sub_token)

                decoded_text = decoded_text+" "+word_buffer
                word_buffer = ""
            else:
                if not token.isspace() and len(token) > 0:
                    decoded_text = decoded_text + " " + self.key_finder(token)

        return decoded_text.lower()
