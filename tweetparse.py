#!/usr/env/python

import time

searchfile = open('tweets.txt', 'r')
linuxtweets = open('linuxtwt.txt', 'a')
bsdtweets = open('bsdtwt.txt', 'a')
search = searchfile.readlines()
ltcount = 0
btcount = 0
for line in search:
#	print line[1]
#	time.sleep(30)
	if 'linux' in line:
		ltcount = ltcount + 1
		linuxtweets.write(line)
	elif 'bsd' in line:
		btcount = btcount + 1
		bsdtweets.write(line)

print 'complete'
print 'Total linux tweets = ', ltcount
print 'Total BSD tweets = ', btcount

linuxtweets.close()
bsdtweets.close()
searchfile.close()
	

