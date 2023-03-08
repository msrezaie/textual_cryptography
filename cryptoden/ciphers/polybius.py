# Create a dictionary to map characters to cipher values
field = {
    '0': ' ', '11': 'A', '12': 'B', '13': 'C', '14': 'D', '15': 'E', '21': 'F', '22': 'G', '23': 'H', '24': 'I' or 'J',
    '25': 'K', '31': 'L',
    '32': 'M', '33': 'N', '34': 'O', '35': 'P', '41': 'Q', '42': 'R', '43': 'S', '44': 'T', '45': 'U', '51': 'V',
    '52': 'W', "53": 'X',
    '54': 'Y', '55': 'Z'
}

# Extract values and keys from the dictionary
values = [v for v in field.values()]
keys = [k for k in field.keys()]

def encrypt(text, key='null'):
    try:
        text = text.upper()
        # Create an empty list to store the cipher values
        keys = []
        # Iterate over each character in the input text
        for i in text:
            # If the character is not in the field values, append it as is to the list
            if i not in values:
                keys.append(i)
            else:
                # If the character is a space, append 0 as the cipher value
                if i == " ":
                    cipher = '0'
                else:
                    # Calculate the row and column values based on the character's position in the alphabet
                    cipher = str((ord(i) - ord('A')) // 5 + 1) + str((ord(i) - ord('A')) % 5 + 1)
                    # If the cipher value is greater than or equal to 25, subtract 1 from it
                    if int(cipher) >= 25:
                        cipher = str(int(cipher) - 1)
                        # If the new cipher value is 30, 40, 50 or 60, subtract 5 from it
                        if cipher in ['30', '40', '50', '60']:
                            cipher = str(int(cipher) - 5)

                keys.append(int(cipher))
        # Join the cipher values into a string and return it
        return ' '.join(str(x) for x in keys)
    except ValueError:
        return "Error!"


def decrypt(cipher, key='null'):
    cipher = cipher.split()
    try:
        # Create a dictionary to map cipher values back to characters
        cipher_map = {k: v for k, v in field.items()}
        # Iterate over each cipher value in the list and map it back to a character using the cipher_map dictionary
        result = [cipher_map.get(i, i) for i in cipher]
        # Join the characters into a string and return it
        return ''.join(result)
    except ValueError:
        return "Error!"