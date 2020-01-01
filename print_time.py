#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 31 17:11:34 2019

@author: sam
"""

#this function will print the current time in hours, minutes, and seconds
import time

t = time.localtime()
current_time = time.strftime("%l:%M:%S %p", t)
print(current_time)