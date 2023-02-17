def encrypt(text, key):
    try:
        encrypted = []
        for char in text:
            if char.isalpha():
                base = ord('A') if char.isupper() else ord('a')
                encrypted.append(chr((ord(char) - base + int(key)) % 26 + base))
            else:
                encrypted.append(char)
        return ''.join(encrypted)
    except ValueError:
        return "Error!"

def decrypt(text, key):
    try:
        decrypted = []
        for char in text:
            if char.isalpha():
                base = ord('A') if char.isupper() else ord('a')
                decrypted.append(chr((ord(char) - base - int(key)) % 26 + base))
            else:
                decrypted.append(char)
        return ''.join(decrypted)
    except ValueError:
        return "Error!"