#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 21 22:50:46 2019

@author: bikram
"""

import os

"""
def test():
    os.chdir("C:/Users/David/Files")
    files = os.listdir(".")
    for x in files:
        inputFile = open(x, "r")
        content = inputFile.read()
        with open(x, "wb") as outputFile:
                str.lower(content)
                
                """
                
file1 = open("14.txt")
line = file1.read()
words = line.lower()
#str.lower(line)
#for r in words:
appendFile = open('14.txt','a')
appendFile.write(" "+r)