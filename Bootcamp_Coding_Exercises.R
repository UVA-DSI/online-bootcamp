# author: Monish Dadlani (mkd7q@virginia.edu)
# date : 12-26-2019

rm(list=ls())

# Exercise 1
current_time <- Sys.time()
print(current_time)

# Exercise 2
start <- Sys.time()
data(cars)
attach(cars)
cars$time <- cars$dist/cars$speed
end <- Sys.time()
elapsed_time <- end-start
print(elapsed_time)

# Exercise 3
word <- readline(prompt = "Enter a word")
print(word)

# Exercise 4
word <- readline(prompt = "Enter a word")
letters_only <- function(x) {!grepl("[^A-Za-z]", x)}
if (letters_only(word)) {
  print(word)
} else {
  readline(prompt = "Enter another word")
}

#Exercise 5
first_name <- readline(prompt = "Enter your first name")
last_name <- readline(prompt = "Enter your last name")
college <- readline(prompt = "Enter the name of your college")
degree <- readline(prompt = "Enter degree pursuing")
residence <- readline(prompt = "Enter your city of residence")    
student_info = list(first_name,last_name,college,degree,residence)
for(i in student_info){print(i)}