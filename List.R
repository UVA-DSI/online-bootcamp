#1 Define Function
Userinput <- function(){
  #2 Define User Input and Data Entry Code
  User.Input1 <- readline(prompt="What is your name: ")
  User.Input2 <- readline(prompt="Where are you from: ")
  User.Input3 <- readline(prompt="How old are you: ")
  User.Input4 <- readline(prompt="What is your favorite color: ")
  
  #3 Create List
  List = list(User.Input1,User.Input2,User.Input3,User.Input4)
  
  #4 Print 
  for(i in List)
    print(i)
}
Userinput()