#!/usr/env/python

#simple rysnc script for Projects and tasks

import subprocess
import sys

owner = 'aikidouke'
machine = 'aikidouke@greyman.info:'
sshmachine = 'aikidouke@greyman.info'
ploc = '/home/aikidouke/Projects/'
tloc = '/home/aikidouke/.task/'
sloc = '/home/aikidouke/lastsync.txt'
stampfile = '/home/greyman/lastsync.txt'

def stamp():
	date = subprocess.Popen(['date'], stdout=subprocess.PIPE)
	dateout = date.communicate()[0]                                    
	print (dateout) 
	stamping = open(stampfile, 'w')                        
	stamping.write(dateout)                                       
	stamping.close()                                            

stamp()

try:
#	subprocess.call(['rsync', '-ar', '/home/greyman/Projects/', 'aikidouke@greyman.info:/home/aikidouke/Projects/'])
#	subprocess.call(['rsync', '-ar', '/home/greyman/.task/' , 'aikidouke@greyman.info:/home/aikidouke/.task/'])
#	subprocess.call(['ssh', 'aikidouke@greyman.info', 'chown', '-R ', 'aikidouke', '/home/aikidouke/'])
#	print 'complete'
#	stamp()
	subprocess.call(['rsync', '-ar', (stampfile), (machine)+(sloc)])
	subprocess.call(['rsync', '-ar', '/home/greyman/Projects/', (machine)+(ploc)])
	subprocess.call(['rsync', '-ar', '/home/greyman/.task/' , (machine)+(tloc)])
	subprocess.call(['ssh', sshmachine, 'chown', '-R ', owner, '/home/aikidouke/'])

	print 'complete'

except Exception, e:
	print 'error'




