from socket import *
from pq import *
host='localhost'
port=21567
bufize=2**21
addr=(host,port)

tcpclisock=socket(AF_INET ,SOCK_STREAM)
tcpclisock.connect(addr)

f=open('1.jpg','rb')
a=f.read()
f.close()
file=encrp(a,2314256581650600217889, 3500680269784890683963)
tcpclisock.send(file)
tcpclisock.close()