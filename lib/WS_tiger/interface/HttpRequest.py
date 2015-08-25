#!/usr/bin/python

###########################
#
# tiger 1.0 HttpRequest
# (C) 2014 WatsonSoft
# made by JamesWatson
#
###########################

def getURLarg(args):
	parameter = dict()
	try:
		items = args.split( "&" )
		for item in items:
			i = item.split( "=" )
			parameter[ i[0] ] = i[1]
	except Exception as e:
		pass
	return parameter

def multipart(formData, boundary, txt):
	boundary = "--" + boundary
	vector = txt.split(boundary)
	for one in vector:
		if( 3 > len(one) or "--" == one[:2] ):
			continue
		one = one[2:]
		kv = one.split("\x0D\x0A\x0D\x0A")
		keys = kv[0]
		value = kv[1]
		fields = keys.split("\x0D\x0A")
		content = (fields[0].split(": "))[1]
		tmp = content.split("; ")
		for x in tmp:
			y = x.split("=")
			if("name" == y[0]):
				formData[y[1][1:-1]] = value[:-2]
	return formData

class HttpRequest(object):
	def __init__(self, text):
		self.ExceptionNo = 0
		self.ExceptionMessage = ""
		self.session = None
		self.head = dict()
		blk = text.split("\r\n\r\n", 1)
		rows = blk[0].split("\r\n")
		tmp = rows[0]
		i = tmp.split(" ")
		self.head["Method"] = i[0]
		path = i[1]
		self.head["Protocol"] = i[2]
		off = path.find("?")
		if( -1 != off ):
			self.head["Path"] = path[:off]
			self.parameter = getURLarg( path[off+1:] )
		else:
			self.head["Path"] = path
			self.parameter = dict()
		rows = rows[1:]
		for tmp in rows:
			i = tmp.split(": ")
			self.head[i[0]] = i[1]
		#parameter begin
		boundary = None
		try:
			contentType = self.head["Content-Type"]
			boundary = contentType.split("boundary=")[1]
		except Exception:
			pass
		if( None == boundary ):
			try:
				rows = blk[1].split("&")
				for tmp in rows:
					i = tmp.split("=")
					self.parameter[i[0]] = i[1]
			except Exception:
				pass
		else:
			multipart(self.parameter, boundary, blk[1])
		return

	def setHead(self, key, value):
		self.head[key] = value

	def getHead(self, key):
		try:
			return self.head[key]
		except KeyError:
			return None

	def setParameter(self, key, value):
		self.parameter[key] = value

	def getParameter(self, key):
		try:
			return self.parameter[key]
		except Exception as e:
			return None

	def setSession(self, session):
		self.session = session

	def getSession(self):
		return self.session

	def getException(self):
		return (self.ExceptionNo, self.ExceptionMessage)

	def setException(self, num, message):
		self.ExceptionNo = num
		self.ExceptionMessage = message
