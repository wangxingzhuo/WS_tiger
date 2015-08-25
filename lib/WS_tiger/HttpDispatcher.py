#!/usr/bin/python

###########################
#
# tiger 1.0 HttpDispatcher
# (C) 2014 WatsonSoft
# made by JamesWatson
#
###########################

import imp
import sys
import os
import gzip
#from io import BytesIO
import cStringIO
from hashlib import md5
from HttpDict import *
from API import HttpPYP
from debug import *
from RdXml import *
from HttpDict import *

class modelState(object):
	def __init__(self):
		self.mod = None
		self.state = False

def firstEncoding(encoding):
	return "gzip"

def textGzip(puredata):
	#buf = BytesIO()
	buf = cStringIO.StringIO()
	f = gzip.GzipFile(mode="wb", fileobj = buf)
	#f.write(puredata.encode('utf8'))
	f.write(puredata)
	f.close()
	cdata = buf.getvalue()
	buf.close()
	return cdata

def encode( request, response, page ):
	try:
		encoding = request.getHead("Accept-Encoding")
		if( None != encoding and None != page ):
			codeName = firstEncoding(encoding)
			response.setHead("Content-Encoding", codeName)
			page = textGzip(page)
			response.setHead("Content-Length", repr(len(page)))
	except Exception as e:
		print("in HTTPDispatcher encode: "+e)
	return page

class HttpModelManager(object):
	def __init__(self):
		self.models = dict()

	def appendModel( self, pname, state=False, globalNS=globals(), localNS=None, fromList=None ):
		self.models[pname] = modelState()
		self.models[pname].mod = __import__(pname, globalNS, localNS, fromList)
		self.models[pname].state = state

	def delModel(self, pname):
		del(self.models[pname].mod)
		del(self.models[pname])

	def setModelState( self, pname, state ):
		self.models[pname].state = state

	def flash( self, pname ):
		if( self.models[pname].state ):
			reload(self.models[pname].mod)

	def getModel(self, pname):
		return self.models[pname].mod
			

def cached(request, response, page):
	if( None == page ):
		response.setHead("State", webLang.getState(500))
		return None
	m = md5()
	try:
		#ETag = m.update( page.encode("utf8") )
		ETag = m.update( page )
	except Exception as e:
		print("in cache: "+e)
	fileHash = "W/\"" + m.hexdigest() + "\""
	if( request.getHead("If-None-Match") == fileHash ):
		response.setHead("State", webLang.getState(304))
		return None
	response.setHead("ETag",  fileHash)
	return page

class HttpDispatcher(object):
	def __init__(self):
		self.models = HttpModelManager()
		try:
			self.web = webInfo("../web.xml")
		except Exception as e:
			logPuts(str(e))
		return

	def mvc(self, request, response, pageName):
		packageName = ""
		if( '/' == pageName[0] ):
			pageName = pageName[1:]
		off = pageName.find('/')
		if( -1 == off ):
			return pageName
		#print "debug-pageName: "+pageName
		packageName = pageName[:off]
		try:
			#print "debug-packageName: "+packageName
			package = self.web[ packageName ]
		except Exception as e:
			print( str(e) )
			return pageName;
		pageName = pageName[off+1:]
#<filter>
		packfilter = package.filter
		for fltr in packfilter :
			print(fltr);
		print("do filter finish")
#</filter>
		while(True):
			try:
				action = package.action[pageName]
			except Exception as e:
				return packageName + "/" + pageName
			try:
				code = "action."+packageName+"."+action.code
				className = action.code
				self.models.appendModel(code, False, globals(), locals(), [className])
				self.models.flash(code)
				modl = self.models.getModel(code)
				aclass = getattr(modl, action.code)
				p = aclass()
				try:
					pageName = p.execute(request, response)
					pageName = action.result[pageName]
				except Exception as e:
					print("action execute: " + str(e) )
					response.setHead( "State", webLang.getState(500) )
					return None
			except Exception as e:
				print("import except: "+str(e))
				response.setHead( "State", webLang.getState(404) )
				return None
			print("to action "+pageName)

	def makeHead(self, request, response, typeName ):
#		if( None == page and 3 != response.getHead("State")[0]/100 ):
#			page = "<!DOCTYPE html>\n<html>\n<head>\n\t<title>" + response.getHead("State")[1] + "</title>\n</head>\n<body>\n"
#			page += "\t<h1>" + `response.getHead("State")[0]` + " " + response.getHead("State")[1]+"</h1>"
#			page += "\n</body>\n</html>"
		typeName = "."+typeName
		typeName = webLang.getMIME(typeName)
		if( None == typeName ):
			typeName = "text/html"
		if( "text" == typeName.split("/")[0] ):
			typeName += "; utf-8"
		response.setHead( "Content-Type", typeName )
		if( "HTTP/1.1" == request.getHead("Protocol") and "close" != request.getHead("Connection") ):
			pass#return page
		response.setHead("Connection", "close")
#		return page

	def runAction( self, request, response ):
		pageName = request.getHead("Path")
		if( os.path.isdir(pageName) ):
			if( "/" != pageName[-1] ):
				response.setHead( "State", webLang.getState(302) )
				location = "http://"+request.getHead("Host")+"/"+pageName+"/"
				response.setHead( "Location", location)
				return None
			pageName += cfg['index']
		return self.mvc(request, response, pageName)

	def getPage( self, request, response, pageName ):
		page = None
		if(None != pageName):
			try:
				fd = open(pageName, "rb")
				#page = fd.read().decode("utf8")
				page = fd.read()
				fd.close()
				page = HttpPYP.pyp(request, response, page)
				#print(page)    #debug content
				page = cached(request, response, page)
				#print(page)    #debug content
			except Exception as e:
				response.setHead( "State", webLang.getState(404) )
				page = getInfoPage(404, "")
			page = encode( request, response, page )
		return page
