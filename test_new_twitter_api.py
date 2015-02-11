#twitter api keys

#Consumer API Key - KPKwlP2k0KK7Xaeqk30gjyz2g
#Consumer Secret Key -
#	idN673oFMvbfuadk8hbShrgJk5LaJsPnZTsmzWMPGsKMrYwHL4

#Access token
#	- 34135168-06tArGgx1qhLJXePZXlXXqocGVUSACDHUm9vOZ3Nm
#Secret Access token
#	- 3tUcMecQ5pvVghXNRNz5Yi1E7PgzDIMD5H2uF4spXfKZM

#### using twitter api####

import twitter
api = twitter.Api(consumer_key='KPKwlP2k0KK7Xaeqk30gjyz2g', consumer_secret='idN673oFMvbfuadk8hbShrgJk5LaJsPnZTsmzWMPGsKMrYwHL4', access_token_key='34135168-06tArGgx1qhLJXePZXlXXqocGVUSACDHUm9vOZ3Nm', access_token_secret='3tUcMecQ5pvVghXNRNz5Yi1E7PgzDIMD5H2uF4spXfKZM')

#print api.VerifyCredentials()



def streamcap():
	for tweet in api.GetStreamFilter(track=['Harkaway', 'Linux', 'Fedora', 'FreeBSD', 'Gaiman', 'Seanan McGuire']):	
		try:
			if tweet.has_key('text'):
				print tweet['text']
#				sleep.time(30)
		except:
			continue


streamcap()


