import random
import string

chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
key = chars.copy()

random.shuffle(key)

#ENCRYPT
plain_text = input("Enter a message to encrypt: ")
cipher_text = ""

for letter in plain_text:
    index = chars.index(letter)
    cipher_text += key[index]

print(f"original message {plain_text}")
print(f"Encrypted message {cipher_text}")

#DECRYPT

cipher_text = input("Enter a message to decrypt: ")
plain_text = ""

for char in cipher_text:
    index = key.index(char)
    decrypted_msg += chars[index]

print(f"encrypted message: {cipher_text}")
print(f"original message : {plain_text}")