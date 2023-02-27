def encrypt(text, key):
    try:
        a = int(key['a'])
        b = int(key['b'])
        encrypted = []
        for char in text:
            if char.isalpha():
                base = ord('A') if char.isupper() else ord('a')
                encrypted.append(chr((a * (ord(char) - base) + b) % 26 + base))
            else:
                encrypted.append(char)
        return ''.join(encrypted)
    except ValueError:
        return "Error!"

def decrypt(text, key):
    try:
        # a = int(key['a'])
        # b = int(key['b'])
        # decrypted = []
        # for char in text:
        #     if char.isalpha():
        #         base = ord('A') if char.isupper() else ord('a')
        #         decrypted.append(chr((a * (ord(char) - base) - b) % 26 + base))
        #     else:
        #         decrypted.append(char)
        # return ''.join(decrypted)
        return "Not yet implemented"
    except ValueError:
        return "Error!"