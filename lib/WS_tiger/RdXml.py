#!/usr/bin/python

###########################
#
# tiger 1.0 RdXml
# (C) 2014 WatsonSoft
# made by JamesWatson
#
###########################

from xml.dom import minidom
import os

class WebAction(object):
	def __init__(self, name, code):
		self.name = name
		self.code = code
		self.interceptor = []
		self.result = dict()

	def appendInterceptor(self, lib):
		self.interceptor.append(lib)

	def appendResult(self, name, path):
		self.result[name] = path


class WebPackage(object):
	def __init__(self, name):
		self.filter = []
		self.action = dict()
		self.name = name
	
	def appendAction(self, name, action):
		self.action[name] = action

def getWebAction(node):
	anAction = WebAction(node.getAttribute('name'), node.getAttribute('code'))
	list = node.getElementsByTagName("interceptor")
	for element in list:
		anAction.appendInterceptor(element.getAttribute('lib'))
	list = node.getElementsByTagName("result")
	for element in list:
		anAction.appendResult(element.getAttribute('name'), element.childNodes[0].data)
	return anAction

def getWebPackage(node):
	package = WebPackage(node.getAttribute('name'))
	list = node.getElementsByTagName("filter-stack")[0].getElementsByTagName("filter-ref")
	for item in list:
		package.filter.append( item.getAttribute('lib') )
	list = node.getElementsByTagName("action")
	for item in list:
		anAction = getWebAction(item)
		package.appendAction(anAction.name, anAction)
	return package

def webInfo(xmlFile):
	packages = dict()
	xmlFile = os.path.abspath(xmlFile)
	doc = minidom.parse(xmlFile)
	node = doc.documentElement
	packageNodes = node.getElementsByTagName('package')
	#print "debug-xmlFile: "+xmlFile
	for node in packageNodes:
		package = getWebPackage(node)
		#print "debug-package.name: "+package.name
		packages[package.name] = package
	return packages

if "__main__" == __name__ :
	web = webInfo("../../home/watson/webApp/web.xml")
	print("Number of package: %d" % len(web))
	for pg in web:
		print( "packageName: " + pg.name )
		for f in pg.filter:
			print( "filter: " + f )
		for a in pg.action:
			print( "actionName: "+a.name )
			print( "actionCode: "+a.code )
			for i in a.interceptor:
				print("interceptor: "+i)
			print("result: ")
			print( a.result )
		print("")