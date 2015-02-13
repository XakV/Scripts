#!/usr/env/python

import pywordcloud

file = open('linuxtwt.txt', 'r')
text = file.read()
pywordcloud.create(text, outfile='lnxtwtcld.html', showfreq=False, colorlist = ["blue", "white", "black", "yellow", "orange"])


