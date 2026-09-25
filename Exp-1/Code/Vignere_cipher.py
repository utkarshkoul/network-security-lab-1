def vigenere_encrypt(text, key):
    result = ""
    key_index = 0

    for char in text:
        if char.isalpha():
            if char.isupper():
                base = ord('A')
            else:
                base = ord('a')

            shift = ord(key[key_index % len(key)].lower()) - ord('a')

            new_position = (ord(char) - base + shift) % 26
            result += chr(new_position + base)

            key_index += 1
        else:
            result += char

    return result


def vigenere_decrypt(text, key):
    result = ""
    key_index = 0

    for char in text:
        if char.isalpha():
            if char.isupper():
                base = ord('A')
            else:
                base = ord('a')

            shift = ord(key[key_index % len(key)].lower()) - ord('a')

            new_position = (ord(char) - base - shift) % 26
            result += chr(new_position + base)

            key_index += 1
        else:
            result += char

    return result


# Taking input from user
plaintext = input("Enter the message: ")
key = input("Enter the key: ")

# Checking the key
if not key.isalpha():
    print("Error: Key must contain alphabets only.")
    exit()

# Encryption
ciphertext = vigenere_encrypt(plaintext, key)

# Decryption
decrypted = vigenere_decrypt(ciphertext, key)

# Output
print("Encrypted :", ciphertext)
print("Decrypted :", decrypted)
print("Correct?  :", decrypted == plaintext)