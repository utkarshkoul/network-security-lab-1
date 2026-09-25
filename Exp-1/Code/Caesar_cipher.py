def ceaser_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            shifted = chr((ord(char) - base + shift) % 26 + base)
            result += shifted
        else:
            result += char
    return result
text = "ui"
shift = 3

encrypted = ceaser_encrypt(text, shift)

print(f"Original: {text}")
print(f"Encrypted: {encrypted}")
def ceaser_decrypt(text, shift):
    return ceaser_encrypt(text, -shift)
print(f"Decrypted: {ceaser_decrypt(encrypted, shift)}")
