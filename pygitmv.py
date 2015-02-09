#!/usr/env/python

#Check to see if a directory is a git repo
#Add commits and push

import subprocess

def gitdirscan():
	subprocess.call("find . -maxdepth 1 -iname .git", shell=True)

def gitaddcommit():
	if gitdirscan() == "./.git":
		subprocess.call("git add *", shell=True)
		subprocess.call("git commit", shell=True)
	else:
		 print "No git found in directory " subprocess.call("pwd", shell=True)

def dirlist():
	
	
gitaddcommit()
	


