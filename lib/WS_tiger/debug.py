#!/usr/bin/python

###########################
#
# tiger 1.0 debug
# (C) 2014 WatsonSoft
# made by JamesWatson
#
###########################

import time

def logPuts( str ):
	now = time.strftime("%a, %d %b %Y %H:%M:%S GMT", time.gmtime(time.time()))
	print( now+" "+str+"\n" )

def cfgText(defaultDict, text, cflf, kv):
	rows = text.split(cflf)
	for i in rows:
		if '' == i or "#" == i[0] or "\r" == i:
			continue
		tmp = i.split(kv)
		print(tmp[0]+": "+tmp[1]+"\n")
		defaultDict[tmp[0]] = tmp[1]
	return defaultDict

def debugRequest(request):
	print( "\r\n--start debug--\r\n" )
	for item in request.head:
		print( item +": "+ request.head[item] )
	for item in request.parameter:
		print( item +" := "+ request.parameter[item] )
	print( "\r\n--end debug--\r\n" )
	return

def sendNull(csfd, response):
	response.setHead("Content-Length", "0")
	gram = response.getGram()
	csfd.send( gram )
	csfd.send( "\0" )
