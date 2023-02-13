def atbash(text):
    result = ""
    try:
        for char in text:
            if char.islower():
                result += chr(219 - ord(char))
            elif char.isupper():
                result += chr(155 - ord(char))
            else:
                result += char
        return result
    except ValueError:
        return "Error!"