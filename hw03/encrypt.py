def encrypt(str):
    string = ""
    if len(str) == 0:
        return "error in encryption, try again"
    for letter in str:
        if letter == "a" or letter == "A":
            string += "$"
        elif letter == "e" or letter == "E":
            string += "&"
        elif letter == "i" or letter == "I":
            string += "^"
        elif letter == "o" or letter == "O":
            string += "*"
        elif letter == "u" or letter == "U":
            string += "%"
        elif letter == " ":
            string += " "
        else:
            string += letter
    return string
        
