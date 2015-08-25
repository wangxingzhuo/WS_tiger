#!/usr/bin/python

###########################
#
# tiger 1.0
# (C) 2014 WatsonSoft
# made by JamesWatson
#
###########################

#encoding=utf-8

import sys
import os
import inspect
import threading
from socket import *
from time import sleep
sys.path.append(os.getcwd()+"/../lib")
sys.path.append(os.getcwd()+"/../lib/WS_tiger")
from HttpDict import *
from debug import *
from HttpDispatcher import *
from SessionManager import *
from webServerKernel import *

def HttpServCtrl(dispatcher, sm, addr, max):
	logPuts("ctrl thread running...")
	ss = socket(AF_INET, SOCK_STREAM)
	ss.bind(addr)
	ss.listen(max)
	while(True):
		csfd, Caddr = ss.accept()
		break
	csfd.recv(65535)
	head = "HTTP/1.1 200 OK\r\n"
	head+= "Content-Type: text/html; UTF-8\r\n"
	head+= "Server: WS_Tiger/1.0\r\n"
	head+= "Content-Encoding: identity\r\n"
	head+= "Accept-Ranges: bytes\r\n\r\n\r\n"
	page = "<!DOCTYPE html>\n<html>\n<head><title>Server Control</title></head>\n<body>\n\t<h1>Server will Close"
	application.setAttr('Head', head)
	application.setAttr('Page', page + "d!</h1>\n</body>\n</html>")
	shutTime = cfg['shutTime']
	page += ", out time is "+ shutTime +"s!</h1>\n</body>\n</html>"
	csfd.send(head)
	csfd.send(page)
	csfd.close()
	application.setAttr('ServState', "shutDown")
	ss.close()

def main():
	this_file = inspect.getfile(inspect.currentframe())
	here = os.path.abspath(os.path.dirname(this_file))
	try:
		os.chdir( "../etc/WS_tiger" )
		fd = open( 'config.ini' )
		text = fd.read()
		fd.close()
		cfgText(cfg, text, "\n", " = ")
		for i in cfg:
			if( '\r' == cfg[ i ][-1] ):
				cfg[ i ] = cfg[ i ][:-1]
		os.chdir( cfg['webApp'] )
		cwd = os.getcwd()
		sys.path.append( cwd )
		sys.path.append( cwd+"/lib" )
		os.chdir( "ROOT" )
	except Exception as e:
		print(e)
		exit(1)
	dispatcher = HttpDispatcher()
	sm = SessionManager()
	logPuts("init finish...")
	if( "true" == cfg['WEB'] ):
		tPro= threading.Thread( target=HttpServCore, args=(dispatcher, sm, ('', int(cfg['proPort'])),  5) )
		tPro.setDaemon(True)
		tPro.start()
		logPuts("core thread running...")
	if( "true" == cfg['SSL'] ):
		tPros=threading.Thread( target=HttpServSafe, args=(dispatcher, sm, ('', int(cfg['prosPort'])), 5) )
		tPros.setDaemon(True)
		tPros.start()
		logPuts("safe thread running...")
	HttpServCtrl(dispatcher, sm, (cfg['ctrlAddr'], int(cfg['ctrlPort'])),  5)
	shutTime = cfg['shutTime']
	sleep(int(shutTime))
	return

def version():
	print('WS_tiger 1.0')
	print('(C) 2014 WatsonSoft')
	print('made by JamesWatson')
	print('This is free software; see the source for copying conditions.')
	print('There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.\n')

def help():
	print('Usage: WS_tiger [options]')
	print('Options:')
	print('  --help                   Display this information')
	print('  --version                Display compiler version information\n')

if '__main__' == __name__:
	if( 1 < len(sys.argv) ):
		try:
			com = sys.argv[1][2:]+"()"
			exec(com)
			exit(0)
		except Exception as e:
			help()
			exit(1)
	logPuts("Server is launching...")
	main()
	logPuts("Server has been terminated.")
	exit(0)
