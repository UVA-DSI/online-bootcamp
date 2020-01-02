#Create a loop with a true condition
repeatLoop <- TRUE

while(repeatLoop){
  # Take user input and save to variable
  word <- readline(prompt = "What word would you like me to repeat?: ")
  # Verify that input is a word
  if (grepl("[A-Za-z]\\D", word)) {
    # Print word
    print(word)
    repeatLoop <- FALSE
  } else {
    # If not word, prompt for appropriate input
    print("That's not a word! Try again.")
  }
}