#Create a function to check that user input is only letters with no numbers or special characters
def is_this_a_word(word_to_check):
    return word_to_check.isalpha()

#Ask the user for an input
print('Please input a word')

#Take user input
user_input = input()

#Create a loop which only breaks if the user's input matches our specifications
check = is_this_a_word(user_input)

while check is False:
    print('That is not a word, please input a word with no numbers or special characters only.')
    user_input = input()
    check = is_this_a_word(user_input)
    
#Once we have determined the input is a word, print it
print(user_input)