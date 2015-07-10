#!/usr/env/python

import requests
import html2text
import argparse
import duckduckgo as ddg
import time

def pageget(link):

	try:
		print link
		page = requests.get(link)
		text = html2text.html2text(page.text)
		text = text.encode('ascii','ignore')
		print text
		doc = open('/home/shadow/Documents/Query_Results/'+query, 'a')
		doc.write(text)
		doc.close
		print('Results saved as /home/shadow/Documents/Query_Results/'+query)
	except Exception, error:
		raise Exception
		time.sleep(10)
		print('Bogus! Get Page failed. ')


def linkget(query):

	try:
		link = ddg.get_zci(query)
		return link
		print link
	except Exception, error:
		print ' Bogus! No Results. '


def querynormalizer(link):

	link = link.encode('ascii','ignore')
	if link.startswith('http'):
		return link
	else:
		trash, link = link.split('(')
		link = link[:-1]
		return link

while True:

	query = raw_input('Enter search term or string -->   ')
	if query == 'stop':
		print('Thanks for using pageget bro')
		break
	link = linkget(query)
	normallink = querynormalizer(link)
	print normallink
	pageget(normallink)






