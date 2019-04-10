#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 21 23:04:47 2019

@author: bikram
"""

#directory = '/path/to/the/directory'


f = open('14.txt', 'r')
text = f.read()
        
lines = [text.lower() for line in f]
with open('14.txt', 'a') as out:
    out.writelines(lines)
    
