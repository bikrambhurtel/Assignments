#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 21 18:32:22 2019

@author: bikram
"""

weight = float(input('Enter your weight in pounds : '))
height = float(input('Enter your height in inches : '))
wt_kg = weight / 0.45359237
ht_m = height / 0.0254
print('Your BMI is : ',wt_kg/(ht_m*ht_m))