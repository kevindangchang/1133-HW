
def short_encode(list_of_words):
    string = ""
    for word in list_of_words:
        string += word[0] + word[len(word)-1] + " "
    return string

short_encode(["hello", "world"])