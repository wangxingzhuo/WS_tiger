#!/usr/bin/python

###########################
#
# tiger 1.0 webServerKernel
# (C) 2014 WatsonSoft
# made by JamesWatson
#
###########################

import sys
import os
import threading
import select
from ctypes import *
from socket import *

from HttpDict import *
from HttpDispatcher import *
from SessionManager import *
from debug import *
from interface.HttpApplication import *
from interface.HttpRequest import *
from interface.HttpResponse import *
from interface.HttpSession import *

def resetPath(request):
    ph = request.getHead("Path")
    if( "/" == ph ):
        request.setHead("Path", cfg['index'])
    else:
        request.setHead("Path", ph[1:])
    return

def HttpServCore(dispatcher, sm, addr, max):
    ss = socket(AF_INET, SOCK_STREAM)
    try:
        ss.bind(addr)
        ss.listen(max)
        print("Server is working...\n")
        while True:
            csfd, Caddr = ss.accept()
            print('new Connect\n')
            t = threading.Thread(target=waiter,args=(dispatcher, sm, csfd, Caddr))
            t.setDaemon(True)
            t.start()
            t.join(1)
    except Exception as e:
        print(e)
    ss.close()
    return

def HttpServSafe(dispatcher, sm, addr, max):
    ss = socket(AF_INET, SOCK_STREAM)
    try:
        ss.bind(addr)
        ss.listen(max)
        print("Safe Server is working...\n")
        inputs = []
        allAddr = dict()
        inputs.append(ss)
        while True:
            rs, ws, es = select.select(inputs, [], [])
            for r in rs:
                if r is ss:
                    csfd, Caddr = ss.accept()
                    print('new Safe Connect\n')
                    inputs.append(csfd)
                    allAddr[csfd] = Caddr
                else:
                    waiter(dispatcher, sm, r, allAddr[r])
                    inputs.remove(r)
    except Exception as e:
        print(e)
    ss.close()
    return

def onceInit( msg, sm ):
    request = None
    response = None
    session = None
    try:
        print("once service")
        print(msg)                                          #debug
        request = HttpRequest(msg)                          #request finish
        resetPath(request)
        #debugRequest(request)                              #debug
        cookie = request.getHead("Cookie")
        response = HttpResponse()                           #response init finish
        if( None != cookie ):
            session = sm.getSession(cookie)
        if( None == session ):
            session = HttpSession()
            num = application.getAttr("num")                #lock
            application.setAttr("num", num +1)              #unlock
            response.setHead("Set-Cookie", "id="+repr(num)+";") #rebiulding
            sm.setSession(repr(num), session)
        request.setSession(session)                         #session is in
    except Exception as e:
        print( "Once Init: " + str(e) )
    return request, response, session

def toInt(str):
    x = None
    try:
        x = int(str)
    except Exception as e:
        pass
    return x

def sendGram(csfd, response):
    gram = response.getGram()
    print( gram+"-"*64+"\n" )                           #response debug
    #return csfd.send(gram.encode("utf8"))
    return sendit(csfd, gram)

def sendFileBlocks(csfd, request, response, pageName, size):
    httpRange = request.getHead("Range")
    #response.setHead( "Content-Type", "application/octet-stream" )
    httpRange = httpRange[6:]
    blocks = httpRange.split(",")
    fd = open( pageName, "rb" )
    for i in blocks:
        i = " "+i+" "
        be = i.split("-")
        beg = toInt(be[0])
        end = toInt(be[1])
        if( None == end ):
            end = size
        length = 0
        if( None == beg ):
            beg = size-end
            length = end
            end = size
        length = end -beg
        #if( 0 != beg ):
        #   response.setHead( "State", webLang.getState(206) )
        response.setHead( "State", webLang.getState(206) )
        response.setHead( "Content-Range", "bytes " +str(beg)+"-"+str(end-1) +"/" +str(size) )
        response.setHead( "Content-Length", str(length) )
        fd.seek(beg)
        sendGram(csfd, response)
        #print( "debug: send block" )
        while(True):
            page = fd.read(65536)
            blockLen = len(page)
            if(length >= blockLen):
                if( 1 > blockLen ):
                    break
                sendit(csfd, page)
            else:
                sendit(csfd, page[:length])
                break
            length -= blockLen
    fd.close()
    return

def sendit(fd, content):
    try:
        length = len(content)
        sent = fd.send(content)
        while sent < length :
            sent += fd.send(content[sent:])
    except Exception as e:
        print "in sendit: " + str(e)
    return

def waiter( dispatcher, sm, csfd, Caddr ):
    csfd.settimeout(10000000)
    if( "shutDown" == application.getAttr('ServState') ):
        #msg = csfd.recv( 65536 ).decode('utf8')
        msg = csfd.recv( 65536 )
        csfd.send(application.getAttr('Head'))
        csfd.send(application.getAttr('Page'))
        csfd.close()
        return
    try:
        while(True):
            #msg = csfd.recv( 65536 ).decode('utf8')
            msg = csfd.recv( 65536 )
            if( 1 > len(msg) ):
                break
            request, response, session = onceInit(msg, sm)
            pageName = dispatcher.runAction(request, response)              #runAction!!!( main )
            if( None == pageName ):
                response.setHead("Connection", "keep-alive")
                sendGram(csfd, response)
                print( "once service over" )
                break
            typeName = ""
            try:
                typeName = pageName.split(".")[-1]
            except Exception as e:
                pass
            print("to page "+pageName)
            if( "py_" == typeName[:3] ):        #python page file
                typeName = typeName[3:]
                dispatcher.makeHead(request, response, typeName)
                #print("debug call page file: " + pageName)      #debug page path
                page = dispatcher.getPage(request, response, pageName)      #getPage!!!!!( main )
                #print(page.decode("utf8"))
                sendGram(csfd, response)
                if( "HEAD" != request.getHead("Method") ):
                    csfd.send(page)
            else:                               #another file
                dispatcher.makeHead(request, response, typeName)
                pageName = os.path.abspath(pageName)
                try:
                    size = os.path.getsize(pageName)
                except Exception as e:
                    response.setHead( "State", webLang.getState(404) )
                    sendGram(csfd, response)
                    csfd.send(getInfoPage(404, ""))
                    break
                print "debug: ",
                print request.getHead("Range")
                if( None != request.getHead("Range") ):     #send blocks
                    print "..."
                    sendFileBlocks(csfd, request, response, pageName, size)
                    print "OK sent blocks"
                    break
                else:                           #send once
                    response.setHead("Content-Length", str(size))
                    if( "HEAD" != request.getHead("Method") ):
                        fd = open(pageName, 'rb')
                        #tmpfd = open("/tmp/"+pageName.split("/")[-1],"wb+")
                        if( 65536 < size ):
                            sendGram(csfd, response)
                            #size -= 1;
                            print "debug: ready go"
                            while size > fd.tell():
                                #print "debug:" +str(fd.tell())
                                page = fd.read(65536)
                                #print(type(page))
                                print "have read: "+str(len(page))
                                print type(page)
                                sendit(csfd, page)
                                #tmpfd.write(page)
                            print "debug: sent"
                            #tmpfd.close()
                        else:
                            #page = fd.read().decode("utf8")
                            page = fd.read()
                            page = encode( request, response, page )
                            sendGram(csfd, response)
                            csfd.send(page)
                        #print pageName
                        fd.close()
                    print "OK closed"
            print("once service over")
            if( "close" == response.getHead("Connection") ):
                print("term connect by server")
                break
    except Exception as e:
        print("in waiter: ")
        err = str(e)
        if( '[Errno 10053]' == err[:-1] ):
            print( "\tterm a connect by client" )
        else:
            s = str(e)
            print("\t"+s)
    csfd.close()
    print("leave writer")
    return
