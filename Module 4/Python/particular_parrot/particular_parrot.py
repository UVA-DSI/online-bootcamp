notWord = True
while notWord: 
    word = input("Give me a word to repeat\n")
    if word.isalpha():
        print(word)
        notWord = False
    else:
        print("That's not a word! Try again.")
