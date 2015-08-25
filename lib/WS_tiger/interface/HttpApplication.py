#!/usr/bin/python

###########################
#
# tiger 1.0 HttpApplication
# (C) 2014 WatsonSoft
# made by JamesWatson
#
###########################

class HttpApplication(object):
	def __init__(self):
		self.attr = dict()
		self.attr['num'] = 0

	def setAttr(self, key, value):
		self.attr[key] = value

	def getAttr(self, key):
		try:
			return self.attr[key]
		except Exception as e:
			return None
