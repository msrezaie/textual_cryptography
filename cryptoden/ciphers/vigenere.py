def encrypt(text, key):
    try:
        encrypted = ''
        key_index = 0
        for char in text:
            if char.isalpha():
                base = ord('A') if char.isupper() else ord('a')
                shift = ord(key[key_index % len(key)]) - base
                encrypted += chr((ord(char) - base + shift) % 26 + base)
                key_index += 1
            else:
                encrypted += char
        return ''.join(encrypted)
    except ValueError:
        return "Error!"

def decrypt(text, key):
    try:
        decrypted = ''
        key_index = 0
        for char in text:
            if char.isalpha():
                base = ord('A') if char.isupper() else ord('a')
                shift = ord(key[key_index % len(key)]) - base
                decrypted += chr((ord(char) - base - shift) % 26 + base)
                key_index += 1
            else:
                decrypted += char
        return ''.join(decrypted)
    except ValueError:
        return "Error!"