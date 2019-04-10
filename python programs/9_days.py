#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 21 19:42:19 2019

@author: bikram
"""

year = int(input('Enter the year :'))
month = int(input('Enter the month :'))

if month in [4,6,9,11]:
    days = 30
elif month in [1,3,5,7,8,10,12]:
    days = 31
elif month is 2:
    if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
        days = 29
    else:
        days = 28
else:
    print('Enter the valid month and year ')
    days = 'invalid'
if year > 0:   
    print('The number of days in month ',month,' of the year',year,' is ',days)
else:
    print('Invalid year!!!')