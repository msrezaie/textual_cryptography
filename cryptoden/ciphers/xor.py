def encrypt(text, key):
    try:
        enc = []
        for i in text:
            enc.append(chr(ord(i) ^ int(key)))
        encrypted = ''.join(enc)
        return encrypted
    except ValueError:
        return "Error!"

def decrypt(text, key):
    return encrypt(text, key)