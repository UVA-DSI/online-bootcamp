

UserInput <- readline(prompt= "Enter a word: ")


repeat{
  if (grepl("[A-Z a-z]",UserInput,perl = TRUE)){
    print("It's a word!")
    print(UserInput)
    break
  } else {
    print("It is not a word")
    UserInput <- readline(prompt= "Enter a word: ")
    }
  }