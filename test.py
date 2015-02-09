#!/usr/env/python

import subprocess

stuff = list()

proc = subprocess.Popen(["find",".","-iname",".git"])
for line in proc.stdout:
	 stuff = stuff.append(line)
print stuff(2)


