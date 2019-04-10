#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 21 19:21:55 2019

@author: bikram
"""

count = 0

import random

x = random.randrange(0,100)
y = random.randrange(0,100)
numbers = x + y
print (x, "+", y)
guess = eval(input("Enter your guess: "))

if guess == numbers:
    count = count + 1
    print("Correct.")
else:
    print("Incorrect")
 