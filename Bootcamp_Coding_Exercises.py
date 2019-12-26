# -*- coding: utf-8 -*-
"""
Created on Mon Dec 23 14:35:25 2019

@author: dadlamk
"""

# Exercise 1
from datetime import datetime
current_time = datetime.now()
current_time = current_time.strftime("%m/%d/%y %H:%M:%S")
print(current_time)
print(datetime.now())

# Exercise 2
from datetime import datetime
start_time = datetime.now()
x=3
y=5
x+y
x-y
x*y
x//y
end_time = datetime.now()
elapsed_time = end_time - start_time
print(elapsed_time)

# Exercise 3
word = input("Enter a word")
print(word)

# Exercise 4
word = input("Enter a word")
if word.isalpha():
    print(word)
else:
    input("Enter another word")
    
# Exercise 5
first_name = input("Enter your first name")
last_name = input("Enter your last name")
college = input("Enter the name of your college")
degree = input("Enter degree pursuing")
residence = input("Enter your city of residence")    
student_info = [first_name,last_name,college,degree,residence]
for i in student_info:
    print(i)