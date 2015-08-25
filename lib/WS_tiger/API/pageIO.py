#!/usr/bin/python

###########################
#
# tiger 1.0 pageIO
# (C) 2014 WatsonSoft
# made by JamesWatson
#
###########################

import StringIO

class PgOut(object):

	def __init__(self):
		self.pageOut = StringIO.StringIO()

	def prints(self, txt):
		self.pageOut.write(txt)

	def setErr(self, txt):
		self.pageOut.seek(0)
		self.pageOut.write(txt)

	def getInner(self):
		self.pageOut.seek(0)
		text = self.pageOut.read()
		self.pageOut.seek(0)
		return text

	def close(self):
		self.pageOut.close()