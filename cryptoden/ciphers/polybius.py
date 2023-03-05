field = {
    '0': ' ', '11': 'A', '12': 'B', '13': 'C', '14': 'D', '15': 'E', '21': 'F', '22': 'G', '23': 'H', '24': 'I' or 'J',
    '25': 'K', '31': 'L',
    '32': 'M', '33': 'N', '34': 'O', '35': 'P', '41': 'Q', '42': 'R', '43': 'S', '44': 'T', '45': 'U', '51': 'V',
    '52': 'W', "53": 'X',
    '54': 'Y', '55': 'Z'
}

values = []
keys = []
for k, v in field.items():
    values.append(v)
    keys.append(k)

def encrypt(text, key='null'):
    try:
        text = text.upper()
        keys = []
        for i in text:
            if i not in values:
                keys.append(i)
            else:
                if i == " ":
                    row = 0
                    cipher = row
                else:
                    row = int((ord(i) - ord('A')) / 5) + 1
                    col = int((ord(i) - ord('A')) % 5) + 1
                    cipher = str(row) + str(col)
                    if int(cipher) >= 25:
                        cipher = int(cipher) - 1
                        if int(cipher) == 30 or int(cipher) == 40 or int(cipher) == 50 or int(cipher) == 60:
                            cipher = int(cipher) - 5

                keys.append(int(cipher))

        return ' '.join(str(x) for x in keys)
    except ValueError:
        return "Error!"


def decrypt(cipher, key='null'):
    cipher = cipher.split()
    try:
        res = []
        for i in cipher:
            if i in keys:
                res.append(field[i])
            else:
                res.append(i)

        return ''.join(res)
    except ValueError:
        return "Error!"