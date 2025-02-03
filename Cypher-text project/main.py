from art import logo
print(logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt(original_text,shift_amount):
    encrypted_text=""
    for i in range(len(original_text)):
        if original_text[i].isalpha():
            idx=alphabet.index(original_text[i])
            encrypted_text+=alphabet[(idx+shift_amount)%len(alphabet)]
        else:
            encrypted_text+=original_text[i]
    return encrypted_text

def decrypt(original_text,shift_amount):
    decoded_text = ""
    for i in range(len(original_text)):
        if original_text[i].isalpha():
            idx = alphabet.index(original_text[i])
            decoded_text += alphabet[(len(alphabet)+(idx - shift_amount)) % len(alphabet)]
        else:
            decoded_text+=original_text[i]
    return decoded_text

def caeser(mode,original_text,shift_amount):
    if mode=='encode':
        cypher_text = encrypt(original_text=original_text,shift_amount= shift_amount)
        print(f"Cypher text: {cypher_text}")
    elif mode=='decode':
        original=decrypt(original_text=original_text,shift_amount=shift_amount)
        print(f"Original text: {original}")
while True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caeser(original_text=text,shift_amount=shift,mode=direction)
    option=input("Type 'yes' if you want to go again. Otherwise, type 'no'.\n")
    if option=='no':
        break
