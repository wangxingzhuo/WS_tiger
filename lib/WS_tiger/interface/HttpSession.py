#!/usr/bin/python

###########################
#
# tiger 1.0 HttpSession
# (C) 2014 WatsonSoft
# made by JamesWatson
#
###########################

import time
import os

class HttpSession(object):
	def __init__(self):
		self.map = dict()

	def session(self, createTime):
		self.createTime = time.time()
		self.OutTime = 0

	def set(self, key, value):
		self.map[key] = value

	def get(self, key):
		try:
			return self.map[key]
		except Exception as e:
			return None

	def setOutTime(self, s):
		self.OutTime = s

	def getOutTime(self):
		return self.OutTime

	def getCreateTime(self):
		return createTime