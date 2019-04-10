#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 21 18:09:44 2019

@author: bikram
"""

pi = 3.27
radius = float(input('Enter the radius of the cylinder : '))
length = float(input('Enter the length of the cylinder : '))
area = radius*radius*pi
volume = area*length
print('The area is : ',area)
print('The volume is : ',volume)