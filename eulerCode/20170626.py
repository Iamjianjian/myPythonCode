import math
from functools import reduce
def fun(x):
    t=1
    tt=x
    while tt<=10000:
        tt*=x
        t+=1
    return t

def denum(num):
    rawnum=num
    dlist=[]
    for i in range(2,int(math.sqrt(num))+1):
        if not num%i:
            while not num%i:
                num//=i
            dlist.append(i)
        if num==1:
            return dlist
    if rawnum!=num:
        dlist.append(num)
        return dlist
    else :
        return [1,rawnum]

def fun2(x):
    a=[reduce(lambda x,y:x*y,denum(i)) for i in range(1,1+x)]
    return list(set(a))
sqrt=[int (pow(10**5,1/i)) for i in range(2,17)]

e=1+16+10+6+7+8
be=7
a=fun2(1000)
a.sort()
for i in a[5:]:
    be=i
    if i>sqrt[0]:
        e+=1
        continue
    elif i>sqrt[1]:
        e+=2
        continue
    elif i>sqrt[2]:
        e+=3
        continue
    elif i>sqrt[3]:
        e+=4
        continue
    else:
        e+=5

        
