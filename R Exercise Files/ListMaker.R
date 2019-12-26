#Brackets used here to stop the code so a user has the option to input when all code is run as a block
{
#accept input and store it in a variable
x1 <- readline(prompt = "What is your favorite color?: ")
x2 <- readline(prompt = "What is your favorite dinner?: ")
x3 <- readline(prompt = "What is your favorite breed of dog?: ")
}

new_list = list(x1,x2,x3)

for(i in new_list){
  print(i)
}
