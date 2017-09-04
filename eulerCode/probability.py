import math

def EandD(a):
    E=0
    for i in a:
       E+=i[0]*i[1]

    D=0
    for i in a:
        D+=(i[0]-E)**2*i[1]

    return (E,D)


def H(l,b=2):
    s=0
    for i in l:
        s+=-1*i*math.log(i,b)

    return s


def sn(l):
    g=0
    for i in l:
        lo=-1*math.log2(i)
        le=math.ceil(lo)
        print(i,g,bin(int(g*2**le))[2:],lo,le)
        g+=i
def pindex(base,mo):
    for i in range(2,mo+1):
        if  not (mo-1)%i and base**i%mo==1:
            return i
            
            
def miu(a):
    l=len(a)
    su=sum(a)
    x=su/l
    s2=0
    for i in a:
        s2+=(i-x)**2
    s2/=l
    s=math.sqrt(s2)
    return x,s,s2


def isprime(a):
    for i in range(2,int(pow(a,0.5)+1)):
        if not a%i:
            print(i)
            return False
    return True


