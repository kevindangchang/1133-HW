def count_words(sentence):
    space = 0
    if len(sentence) == 0:
        return 0
    for letter in sentence:
        if letter == " ":
            space += 1
    return print(space)

count_words("Hello world! ")


    
            
