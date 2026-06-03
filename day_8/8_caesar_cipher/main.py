def caesar(code, text, shift):
    result_text = ""
    for letter in text:
        index = alphabet.index(letter)
        if code == "encode":
            new_index = index + shift
            if new_index>25:
                new_index = new_index-25-1
            result_text+=alphabet[new_index]
        elif code == "decode":
            new_index = index - shift
            if new_index<0:
                new_index = new_index+25+1
            result_text+=alphabet[new_index]
    print(f"The resulted text is {result_text}")

import art
print(art.logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 
            'y', 'z']
choice = True
while choice:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26
    caesar(direction,text,shift)
    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.").lower()
    if restart == "no":
        choice = False