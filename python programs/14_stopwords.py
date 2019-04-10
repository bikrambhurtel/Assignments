#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 21 22:17:41 2019

@author: bikram
"""

import nltk
from nltk.corpus import stopwords


stop_words = set(stopwords.words('english'))
file1 = open("13.txt")
line = file1.read()
words = line.split()
for r in words:
    if not r in stop_words:
        appendFile = open('13.txt','a')
        appendFile.write(" "+r)