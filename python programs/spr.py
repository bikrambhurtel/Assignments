#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 23 19:54:45 2019

@author: bikram
"""

import random
def printch():
		if(rand==0):
			print("my choice was Scissor!")
		elif(rand==1):
			print("my choice was Rock!")
		else:
			print("my choice was Paper!")
while(True):
	rand = random.randint(0,2)
	userch = eval(input("What's your choice, scissor-paper-rock (0-S, 1-R, 2-P): "))
	if((rand==0 and userch == 0) or (rand==1 and userch == 1) or (rand==2 and userch == 2)):
		print("draw!!\n")
		printch()
	elif((rand == 0 and userch == 2) or (rand == 1 and userch == 0) or (rand == 2 and userch == 1)):
		print("You loose!!\n")
		printch()
		
	else:
		print("you win!!\n")
		printch()
		
	anil=input("Do you want to play again (y,n): ")
	if(anil=='n'):
		break
	else:
		print("__________________________________________________________________________\n")
		continue