#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 31 17:11:34 2019

@author: sam
"""

#Write a program that prints out a time it takes to run.

#Step 1: Record the time at the start of the program.

import time

t0 = time.localtime()
start_time = time.strftime("%l:%M:%S %p", t0)
print(start_time)

#Run some code to pause for n seconds

snooze = 5
time.sleep(snooze)

#Step 2: Print the current time minus the time at the start of the program.

t1 = time.localtime()
end_time = time.strftime("%l:%M:%S %p", t1)
print(end_time)
print("Elapsed time is " + str(snooze) + " seconds")