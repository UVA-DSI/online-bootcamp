# Author: Maurizio Boano (mb6fs@virginia.edu)
library(tidyverse)

# Exercise 1

print(Sys.time())

# Exercise 2

start <- Sys.time()

difference <- Sys.time() - start

print(difference)

# Exercise 3

user_input <- readline("type something and hit enter")

print(paste("you entered: ", user_input))

# Exercise 4

user_input <- readline("type something and hit enter")

while (grepl("\\d", user_input)) {
  
  user_input <- readline("sorry, please enter a value without numbers")
  
}

print(paste("you entered: ", user_input))

# Exercise 5

user_number <- as.integer(readline("enter number of elements in your list : "))

x <- 1

while (x<user_number+1) {
  
  value <- readline(prompt="input a value then hit enter: ")
  user_list[x] <- value
  x <- x+1
}

print(user_list)

