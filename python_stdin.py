#!/usr/env/python

import subprocess


proc = subprocess.Popen(['ls'], stdout=subprocess.PIPE,)
stdout_value = tuple(proc.communicate()[0])
print stdout_value[1]


