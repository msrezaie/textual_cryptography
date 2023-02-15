def encrypt(text, key='null'):
    try:
        res = [text[::-1]]
        return ''.join(res)
    except ValueError:
        print("Invalid Entry", "Error!")

def decrypt(text, key):
    return encrypt(text, key)