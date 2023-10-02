from translator import Translator

def main():
    text = input("enter text to be converted :")

    translator = Translator()

    encoded_text = translator.encoder(text)
    decoded_text = translator.decoder(encoded_text)

    print(decoded_text)


if __name__ == "__main__":
    main()
