def encrypt(text, key):
    try:
        encrypted = []
        # Iterate through each character in the input "text" using a for loop
        for i in text:
            # Append the XOR value of the character's ASCII code and the input "key" to the "enc" list
            encrypted.append(chr(ord(i) ^ int(key)))
        # Join and return the elements of the "encrypted" list into a string
        return ''.join(encrypted)
    except ValueError:
        return "Error!"

def decrypt(text, key):
    # Call the "encrypt" function with the input "text" and "key" and return its output
    decrypted = encrypt(text, key)
    return decrypted
