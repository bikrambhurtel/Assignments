#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 21 19:59:52 2019

@author: bikram
"""

import random
cpu = random.randrange(0,3)
user = int(input('Enter the number 0 for scissor, 1 for rock and 2 for paper : '))
if user == 0:
    print('your choice : scissor ')
elif user == 1:
    print('your choice : rock ')
elif user == 2:
    print('your choice : paper')
else:
    print('please enter valid choice!!')

if cpu == 0:
    print('opponent = scissor')
elif cpu == 1:
   print('opponent = rock')
elif cpu == 2:
   print('opponent = paper')

if user in [0,1,2]:
    if user == 0:
        if cpu == 1:
            print('you loose')
        elif cpu == 0:
            print('draw')
        else:
            print('you win')
    elif user == 1:
        if cpu == 2:
            print('you loose')
        elif cpu == 1:
            print('draw')
        else:
            print('you win')
    elif user == 2:
        if cpu == 0:
            print('you loose')
        elif cpu == 2:
            print('draw')
        else:
            print('you win')
else:
        print('invalid input!!')