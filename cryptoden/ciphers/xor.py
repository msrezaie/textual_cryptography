def encrypt(text, key):
    try:
        if text == "":
            print("No text entered", "Error!")
        elif not key.isdigit() or int(key) > 127 or int(key) < 0:
            print("Invalid Key", "Error!", 0)
        else:
            enc = []
            for i in text:
                enc.append(chr(ord(i) ^ int(key)))

            return ''.join(enc)
    except ValueError:
        return "Error!"

def decrypt(text, key):
    return encrypt(text, key)