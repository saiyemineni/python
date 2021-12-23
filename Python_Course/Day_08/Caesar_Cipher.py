def caesar(text, shift, direction):
    end_text = ""
    if direction == "decode":
        shift *= -1
    for letter in text:
        if letter in alphabet:
            index = alphabet.index(letter)
            new_index = index + shift
            end_text += alphabet[new_index]
        else:
            end_text += letter
        # print(end_text)
    print(f"The {direction}d text is {end_text}")

# def encrypt(text, shift):
#     encrypted_word = ""
#     for letter in text:
#         index = alphabet.index(letter)
#         new_index = index+shift
#         encrypted_word += alphabet[new_index]
#     print(f"The encrypted text is {encrypted_word}")

# def decrypt(text, shift):
#     decrypted_word = ""
#     for letter in text:
#         index = alphabet.index(letter)
#         new_index = index-shift
#         decrypted_word += alphabet[new_index]
#     print(f"The decrypted text is {decrypted_word}")
import caesar_art
print(caesar_art.logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26

    caesar(text, shift, direction)
    reponse = input("Type 'yes' if you want to go again. Otherwise 'no' : ").lower()
    if reponse == 'no':
        should_continue = False
        print("Goodbye ...👋")
