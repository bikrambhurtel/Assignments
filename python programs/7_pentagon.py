#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 21 19:00:16 2019

@author: bikram
"""
from math import pi,sin,sqrt
r = float(input('Enter the length from center of the pentagon to the vertex : '))
side = 2*r * sin(pi/5)
area = ((3 * sqrt(3))/2)*(side*side)
print('The area of the pentagon is ',area)
