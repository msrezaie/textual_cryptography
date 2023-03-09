alpha = list("ABCDEFGHIKLMNOPQRSTUVWXYZ")

def charIndex(letter, matrix):
    r, c = 0, 0
    for row in matrix:
        for chr in row:
            if chr == letter:
                return r, c
            c += 1
        r += 1
        c = 0


def encrypt(text, key):
    try:
        key1 = key['key-1'].replace(" ", "").upper()
        key2 = key['key-2'].replace(" ", "").upper()
        text = ''.join(filter(lambda char: char.isalpha() or char == ' ', text))
        mat1Val = []

        for c in key1:
            if c in alpha and c not in mat1Val:
                mat1Val.append(c)
        for c in alpha:
            if c not in mat1Val:
                mat1Val.append(c)

        matrix1 = []
        index = 0
        for rows in range(5):
            row = []
            for column in range(5):
                row.append(mat1Val[index])
                index += 1
            matrix1.append(row)

        mat2Val = []
        for c in key2:
            if c in alpha and c not in mat2Val:
                mat2Val.append(c)
        for c in alpha:
            if c not in mat2Val:
                mat2Val.append(c)

        mat2 = []
        index = 0
        for rows in range(5):
            row = []
            for column in range(5):
                row.append(mat2Val[index])
                index += 1
            mat2.append(row)

        plainText = text.replace(" ", "").upper().replace("J", "I")
        for s in range(0, len(plainText) + 1, 2):
            if s < len(plainText) - 1:
                if plainText[s] == plainText[s + 1]:
                    plainText = plainText[:s + 1] + 'X' + plainText[s + 1:]
        if len(plainText) % 2 != 0:  # To find the even or odd plainTexts
            plainText = plainText[:] + 'X'
        plainText = " ".join(plainText[i:i + 2]
                                for i in range(0, len(plainText), 2)).split(
            " ")
        cipherText = ""

        alphabet = [
            ["A", "B", "C", "D", "E"],
            ["F", "G", "H", "I", "K"],
            ["L", "M", "N", "O", "P"],
            ["Q", "R", "S", "T", "U"],
            ["V", "W", "X", "Y", "Z"]
        ]
        alphaMat1 = alphabet
        alphaMat2 = alphabet

        for pairVals in plainText:
            index1 = charIndex(pairVals[0], alphaMat1)
            index2 = charIndex(pairVals[1], alphaMat2)
            var1 = matrix1[index1[0]][index2[1]]
            var2 = mat2[index2[0]][index1[1]]
            cipherText += var1 + var2 + ""

        return cipherText

    except ValueError:
        return "Error!"

def decrypt(text, key):
    try:
        key1 = key['key-1'].replace(" ", "").upper()
        key2 = key['key-2'].replace(" ", "").upper()
        text = ''.join(filter(lambda char: char.isalpha() or char == ' ', text))
        mat1Val = []
        for char in key1:
            if char in alpha and char not in mat1Val:
                mat1Val.append(char)
        for char in alpha:
            if char not in mat1Val:
                mat1Val.append(char)
        mat1 = []
        index = 0
        for rows in range(5):
            row = []
            for columns in range(5):
                row.append(mat1Val[index])
                index += 1
            mat1.append(row)

        mat2Val = []
        for char in key2:
            if char in alpha and char not in mat2Val:
                mat2Val.append(char)
        for char in alpha:
            if char not in mat2Val:
                mat2Val.append(char)

        mat2 = []
        index = 0
        for rows in range(5):
            row = []
            for columns in range(5):
                row.append(mat2Val[index])
                index += 1
            mat2.append(row)

        cipherText = text.replace(" ", "").upper().replace("J", "I")
        for s in range(0, len(cipherText) + 1, 2):
            if s < len(cipherText) - 1:
                if cipherText[s] == cipherText[s + 1]:
                    cipherText = cipherText[:s + 1] + ' x ' + cipherText[s + 1:]
        if len(cipherText) % 2 != 0:
            cipherText = cipherText[:] + ' x '
        cipherText = " ".join(cipherText[i:i + 2]
                                for i in range(0, len(cipherText), 2)).split(" ")
        result = ""
        alphabet = [
            ["A", "B", "C", "D", "E"],
            ["F", "G", "H", "I", "K"],
            ["L", "M", "N", "O", "P"],
            ["Q", "R", "S", "T", "U"],
            ["V", "W", "X", "Y", "Z"]
        ]
        alphaMat1 = alphabet
        alphaMat2 = alphabet

        for pairVal in cipherText:
            index1 = charIndex(pairVal[0], mat1)
            index2 = charIndex(pairVal[1], mat2)
            var1 = alphaMat1[index1[0]][index2[1]]
            var2 = alphaMat2[index2[0]][index1[1]]
            result += var1 + var2 + ""

        return result

    except ValueError:
        return "Error!"