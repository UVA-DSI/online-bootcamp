#1 Define User Input and Data Entry Code
Userinput <- function(){
  User.Input <- readline(prompt="Enter Text: ")
  #2 Validate Data Entry
  Letters.Only <- function(x) !grepl("[^A-Za-z]", x)
  while (isFALSE(Letters.Only(User.Input))){
    {User.Input <- readline(prompt="Enter New Text: ")
    }
  }
  {
   print(User.Input)
  }
  }
Userinput()
