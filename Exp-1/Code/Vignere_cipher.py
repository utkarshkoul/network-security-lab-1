def vigenere_encrypt(text, key, decrypt=False):
    result = ""
    key = key.upper()
    key_index = 0

    for char in text:
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - ord('A')

            if decrypt:
                shift = -shift

            encrypted = chr((ord(char.upper()) - ord('A') + shift) % 26 + ord('A'))
            result += encrypted
            key_index += 1
        else:
            result += char

    return result


plaintext = "HELLO"
key = "KEY"

encrypted = vigenere_encrypt(plaintext, key)

print(f"Original: {plaintext}")
print(f"Encrypted: {encrypted}")

print(f"Decrypted: {vigenere_encrypt(encrypted, key, True)}")
