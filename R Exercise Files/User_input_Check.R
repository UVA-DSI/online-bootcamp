#Brackets used here to stop the code so a user has the option to input when all code is run as a block
{
  
{
#accept input and store it in a variable
user_input <- readline(prompt = "Enter any word: ")
}

#Checks to see if user input is a word and continues to ask for one if it isn't
repeat{
  if (grepl("^[A-Za-z]+$", user_input, perl = T)) {
    break
  } else {
    user_input <- readline(prompt = "That is not a word.  Enter a word: ")
  }
}

paste("Thank you, your word is: ", user_input)
}