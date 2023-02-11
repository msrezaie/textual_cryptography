import string

field = string.ascii_uppercase


def encrypt(text, key):
    text = text.upper()
    encrypted = []
    for i in text:
        ind = field.find(i)
        if ind != -1:
            if i in text:
                index = (field.find(i) + key) % len(field)
                encrypted.append(field[index])
        else:
            encrypted.append(i)

    return ''.join(encrypted)


def decrypt(text, key):
    text = text.upper()
    decrypted = []
    for i in text:
        ind = field.find(i)
        if ind != -1:
            if i in text:
                index = (field.find(i) - key) % len(field)
                decrypted.append(field[index])
        else:
            decrypted.append(i)

    return ''.join(decrypted)