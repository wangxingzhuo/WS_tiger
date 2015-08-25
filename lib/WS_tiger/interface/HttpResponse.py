#!/usr/bin/python

###########################
#
# tiger 1.0 HttpResponse
# (C) 2014 WatsonSoft
# made by JamesWatson
#
###########################

import time
import os
from HttpDict import webLang

class HttpResponse(object):
	def __init__(self):
		self.head = dict()
		self.head["Protocol"] = "HTTP/1.1"
		self.head["State"] = webLang.getState(200)
		self.head["Server"] = "WS_Tiger/1.0"
		self.head["Content-Encoding"] = "identity"
		self.head["Accept-Ranges"] = "bytes"
		self.head["Content-Type"] = "text/html; utf-8"
		self.head["Date"] = time.strftime("%a, %d %b %Y %H:%M:%S GMT", time.gmtime(time.time()) )

	def setHead(self, key, value):
		self.head[key] = value

	def getHead(self, key):
		try:
			return self.head[key]
		except KeyError:
			return None

	def getGram(self):
		gram = self.head.pop("Protocol") +" " +repr(self.head["State"][0]) +" " +self.head["State"][1] +"\r\n"
		self.head.pop("State")
		for k in self.head:
			gram += k + ": " + self.head[k] +"\r\n"
		return gram + "\r\n"
