alphabet = "abcdefghijklmnopqrstuvwxyz"

def encode(word,key):
    new_word = ""
    for char in word.lower():
        try:
            index = alphabet.index(char)
            new_word += alphabet[(index+key)%26]
        except ValueError:
            new_word += " "
    return new_word

def decode(word,key):
    return encode(word, -key)

