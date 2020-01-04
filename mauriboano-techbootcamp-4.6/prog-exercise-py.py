# -*- coding: utf-8 -*-
"""
Created on Sat Jan  4 09:53:01 2020

@author: Maurizio Boano (mb6fs@virginia.edu)
"""

# Exercise 1
import datetime
 
print(datetime.datetime.now().time())

# Exercise 2

import datetime

start = datetime.datetime.now()


difference = datetime.datetime.now() - start

print(difference)

# Exercise 3

user_input = input("type something and hit enter")

print("you entered: ", user_input)

# Exercise 4

def checkString(checkValue):
        return any(char.isdigit() for char in checkValue)

while True:
    user_input = input("type something and hit enter")

    if checkString(user_input) is False:
        break
    else:
        print("sorry, please enter a value without numbers")

print("you entered: ", user_input)

# Exercise 5

user_list = []

user_number = int(input("enter number of elements in your list : ")) 

for i in range(0, user_number): 
    value = input() 
  
    user_list.append(value)

for n in range(len(user_list)):
    print(user_list[n])
    
    