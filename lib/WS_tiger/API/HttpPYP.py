#!/usr/bin/python

###########################
#
# tiger 1.0 HttpPYP
# (C) 2014 WatsonSoft
# made by JamesWatson
#
###########################

import re
from API.pageIO import *
from HttpDict import webLang
from interface import *

class PyPage(object):

	def __init__(self, text):
		self.text = text
		self.pyr = re.compile(r"<py>(.*?)</py>", re.I|re.S)
		self.allpyr = self.pyr.finditer(text)

	def run(self, request, response, out):
		if None == self.allpyr:
			return self.text
		self.page = ""
		self.i = 0
		for self.m in self.allpyr:
			self.__code = self.m.group()
			self.off = self.text.find( self.__code )
			self.page += self.text[:self.off]
			self.text = self.text[self.off+len(self.__code):]
			try:
				exec(self.m.group(1))
				self.ret = True
			except Exception as err:
				out.setErr(err)
				self.ret = False

			if not self.ret :
				self.page = "<h1>Error 500</h1>\n"
				self.page += out.getInner()
				out.close()
				self.page += "\r\nin block " + str(self.i)+"\r\n"
				response.setHead( "State", webLang.getState(500) )
				return self.page
			self.page += out.getInner()
			self.i += 1
		return self.page+self.text

def pyp(request, response, text):    #python page
	out = PgOut()
	__CONTEXT = PyPage(text)
	page = __CONTEXT.run(request, response, out)
	out.close()
	return page
