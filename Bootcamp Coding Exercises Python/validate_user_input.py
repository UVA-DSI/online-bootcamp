#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  1 10:34:50 2020

@author: sam
"""

#Write a program that asks the user to provide a word, validate that it is a word, and print the word.
#Step 1: Record that input in a variable.
#Step 2: Confirm that it is a word (if not, ask for another one).
#Step 3: Print that variable.

while True:
    value = input("Type something here: ")
    if not value.isalpha():
        print("Sorry, you have to type a string")
        continue
    else:
        print("You typed: " + value)
        break
