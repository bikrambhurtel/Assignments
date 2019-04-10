#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 07:29:12 2019

@author: bikram
"""

file1 = open("13_split.txt")
line = file1.read()
words = line.split()
for r in words:
    appendFile = open('13_split.txt','a')
    appendFile.write(" "+r)