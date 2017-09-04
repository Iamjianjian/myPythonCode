import math
def isprime(a):
    for i in range(2,int(math.sqrt(a))+1):
        if not a%i:
            print(i)
            return False
    return True

def reser(a,p):
    n1=a
    n2=p
    q=a//p
    r=a-q*p
    n1,n2=n2,r
    res1=[1,0]
    res2=[0,1]
    while r!=0:
        res1=[res1[0]-res2[0]*q,res1[1]-res2[1]*q]
        res1,res2=res2,res1
        q=n1//n2
        n1,n2=n2,n1-n2*q
        r=n2

    return res2
