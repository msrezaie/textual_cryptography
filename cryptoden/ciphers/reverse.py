def encrypt(text, key='null'):
    try:
        # Initialize a list called "encrypted" with the input "text" reversed
        encrypted = [text[::-1]]
        # Convert the "encrypted" list into a string and return it
        return ''.join(encrypted)
    except ValueError:
        return "Error!"

def decrypt(text, key):
    # Call the "encrypt" function with the input "text" and "key" and return its output
    decrypted = encrypt(text, key)
    return decrypted
