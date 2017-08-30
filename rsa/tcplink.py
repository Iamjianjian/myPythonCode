from socket import *
from pq import *

host=''
port=21567
bufize=2**21
addr=(host,port)
tcpsersock=socket(AF_INET,SOCK_STREAM)
tcpsersock.bind(addr)
tcpsersock.listen(1)

print('waiting for connection')
tcpclisock,addr=tcpsersock.accept()
print('connected from ',addr)
data=tcpclisock.recv(bufize)
with open (r'C:\Users\huangjy\Downloads\nodecrp.jpg','wb') as f:
    f.write(data)
data=decrp(data, 624039451334071694081, 3500680269784890683963)
with open (r'C:\Users\huangjy\Downloads\1.jpg','wb') as f:
    f.write(data)

tcpclisock.close()
tcpsersock.close()
