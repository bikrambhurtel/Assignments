#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 21 18:49:52 2019

@author: bikram
"""

v0 = float(input('Enter the initial velocity in m/s : '))
v1 = float(input('Enter the final velocity in m/s : '))
time = int(input('Enter the time span t in seconds : '))
a = (v1 - v0)/time
print('The average acceleration is : ',a)
