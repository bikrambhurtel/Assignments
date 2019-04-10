#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 21 18:17:26 2019

@author: bikram
"""

number = int(input('Enter the number between 0 and 1000: '))
if number<=0 or number>=1000:
    print('Please enter the number between 0 and 1000')
else:
    sum=0
    while(number>0):
         temp = number % 10
         sum = sum + temp
         number = number //10

    print('The sum of the digits is : ',sum)