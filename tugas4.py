def encrypt(text, shift):
    text = text.lower()
    encrypted_text = ""
    for char in text:
        if char.islower():
            encrypted_text += chr((ord(char) - 97 + shift) % 26 + 97)
        else:
            encrypted_text += char
    return encrypted_text


# Contoh penggunaan Caesar Cipher
originalMessage = "Subscribe To Max ODidily 428 69 111"
encryptedMessage = encrypt(originalMessage, 2)
print(encryptedMessage)  # u w d u e t d g v q o z p f k n a