#!/usr/env/python

import os
import subprocess


#import functionality to navigate directories and call functions

p = os.getcwd()
list = os.listdir(p)

#store current working directory in p
#create a list of the directory listing of p

for dir in(list):
	if os.path.isdir(dir) == True:
		os.chdir(dir)
		print(os.getcwd())
		print(os.listdir())
		os.chdir(p)
	else:
		print('Not a directory')

# for each item in directory list, check to see if it is a directory
# if it is, change to the directory, print the new working directory and 
# directory listing, then change back to the original working directory
# print a message if an item in the directory list is not a directory
#######
# could also use subprocess.call to perform other actions in the directory


