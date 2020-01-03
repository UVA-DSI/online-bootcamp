#Write a program that asks the user to provide a word, validate that it is a word, and print the word.

#Step 1: Record that input in a variable.
#Step 2: Confirm that it is a word (if not, ask for another one).
#Step 3: Print that variable.

{
input <- readline(prompt="Type something here: ")
print(paste("You typed: ", input))
grepl("[A-z]", input)
}


#Tried to take this a step further but can't get it to work.

{
input <- readline(prompt="Type something here: ")
}
if (grepl("[A-z]", input)) {
  print(paste("You typed: ", input))
  } else {
    readline(prompt="Try again: ")
}