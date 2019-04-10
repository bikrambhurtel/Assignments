#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 22 11:22:57 2019

@author: bikram
"""

fh = open("14.txt","r")
rd = fh.read()
lower_fh = str.lower(rd)
print(lower_fh)
fh.close
fh = open("14.txt","a")
fh.write(lower_fh)
fh.close