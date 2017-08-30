import random
import math
from functools import reduce
dectextleng=9
enctextleng=4

def mypow(ori,inde,mo):
    inde=bin(inde)[2:]
    resu=1
    for i in range(-1,-len(inde)-1,-1):
        if int(inde[i]):
            resu=(resu*ori)%mo
        ori=(ori**2)%mo
    return resu

def bytestoint(bytesstream,leng):
    tbytesstream=bytesstream[:]
    while tbytesstream:
        aintbytes=tbytesstream[0:leng]
        tbytesstream=tbytesstream[leng:]
        yield reduce(lambda  x,y:x*256+y,aintbytes)

def encrp(bytesstream,e,n):
    global enctextleng,dectextleng
    result = b''
    for i in bytestoint(bytesstream,enctextleng):
        result+=mypow(i,e,n).to_bytes(dectextleng,'big')
    return result

def decrp(bytesstream,d,n):
    global dectextleng ,enctextleng
    numbers=list(bytestoint(bytesstream,dectextleng))
    length=len(numbers)
    result=b''
    for i in range(length):
        i=numbers[i]
        result +=mypow(i,d,n).to_bytes(enctextleng,'big',signed=False)
    return result

def is_prime(p):
    for i in range(2,int(math.sqrt(p))+1):
        if not p%i:
            return False
    return True


def big_prime():
    mi=256**4
    ma=256**4*16
    while True:
        i=random.randint(mi,ma)
        if is_prime(i):
            return i

def get_e( e_n):
    while True:
        e=random.randint(2**20,e_n)
        if coprime(e_n,e):
            return e

def eulid(a,b,gcd=1):
    li1=[1,0,a]
    li2=[0,1,b]
    while li2[2]!=gcd:
        q=li1[2]//li2[2]
        templist=[li1[i]-li2[i]*q for i in range(3)]
        li1,li2=li2,templist
    return li2[0]%b

def coprime(a,b):
    if a<b:
        a,b=b,a
    while b!=0:
        t=a%b
        a=b
        b=t
    if a==1:
        return True
    return False

def get_key():
    p=big_prime()
    q=big_prime()
    n=q*p
    e_n=n-q-p+1
    e=get_e(e_n)
    d=eulid(e,e_n)
    print(e_n,p,q)
    return [e,d,n]
