#!/usr/bin/python

###########################
#
# tiger 1.0 SessionManager
# (C) 2014 WatsonSoft
# made by JamesWatson
#
###########################

class SessionManager(object):
	def __init__(self):
		self.lib = dict()

	def setSession(self, key, session):
		self.lib[key] = session

	def getSession(self, key):
		try:
			ids = key.split("id=", 1)
			id = ids[1]
			ids = id.split(";", 1)
			key = ids[0]
			print("SessionManager: cookie id is "+key)
			return self.lib[key]
		except Exception as e:
			return None

	def length(self):
		pass
