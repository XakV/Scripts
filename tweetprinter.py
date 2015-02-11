#!/usr/env/python

import simplejson

tweets_data = []
tweets_file = file('testtwitgrab.txt', 'r')
lines = tweets_file.readlines()

for line in lines:
    try:
        tweet = simplejson.load(line)
	print tweet
	text = tweet['text'].lower()
        tweets_data.append(text)
    except:
        print 'no read'

	continue


