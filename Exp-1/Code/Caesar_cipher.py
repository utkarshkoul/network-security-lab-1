def caesar_encrypt(text, shift):
    result = ""

    for char in text:
        if char.isalpha():
            if char.isupper():
                base = ord('A')
            else:
                base = ord('a')

            new_position = (ord(char) - base + shift) % 26
            result += chr(new_position + base)
        else:
            result += char

    return result


def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)


# Taking input from user
plaintext = input("Enter the message: ")
shift = int(input("Enter the shift: "))

# Encryption
ciphertext = caesar_encrypt(plaintext, shift)

# Decryption
decrypted = caesar_decrypt(ciphertext, shift)

# Output
print("Encrypted :", ciphertext)
print("Decrypted :", decrypted)
print("Correct?  :", decrypted == plaintext)