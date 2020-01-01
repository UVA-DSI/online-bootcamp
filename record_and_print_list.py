#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  1 12:26:55 2020

@author: sam
"""

#Write a program that asks the user to provide several inputs, and print them out.

#Step 1: Record the input in a list.
#Step 2: Loop over the list and print each element.

value0 = str(input("Type first value here: "))
value1 = str(input("Type second value here: "))
value2 = str(input("Type third value here: "))

value_list = (value0 + value1 + value2)
print(list(value_list))