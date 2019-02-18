alphabet = "abcdefghijklmnopqrstuvwxyz"

def encode(word,key):
    new_word = ""
    pos_in_key = 0
    for char in word.lower():
        current_key = key[pos_in_key]
        offset = alphabet.index(current_key)
        try:
            index = alphabet.index(char)
            new_word += alphabet[(index+offset)%26]
            pos_in_key = (pos_in_key + 1)%len(key)
        except ValueError:
            new_word += char 
    return new_word

def decode(word,key):
    new_word = ""
    pos_in_key = 0
    for char in word.lower():
        current_key = key[pos_in_key]
        offset = alphabet.index(current_key)
        try:
            index = alphabet.index(char)
            new_word += alphabet[(index-offset)%26]
            pos_in_key = (pos_in_key + 1)%len(key)
        except ValueError:
            new_word += char 
    return new_word

