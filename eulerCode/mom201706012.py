import math
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
        return rawnum

def find_euler(a,e,num,dlist):
    for i in dlist:
        while True:
            if e%i:
                break
            e//=i
            if pow(a,e,num)!=1:
                e*=i
                break
    return e
mlist=[]
for a in range(3,1001):
    l=a-1
    r=a+1
    mo=a**2
    e=a*(a-1)
    tl=l
    tr=r
    leuler=find_euler(l,e,mo,denum(e))
    reuler=find_euler(r,e,mo,denum(e))
    lmolist=[]
    rmolist=[]
    for i in range(leuler):
        lmolist.append(l)
        l*=tl
        l%=mo
    for i in range(reuler):
        rmolist.append(r)
        r*=tr
        r%=mo
    g=leuler*reuler//math.gcd(leuler,reuler)
    lmolist=lmolist*(g//leuler)
    rmolist=rmolist*(g//reuler)
    mlist.append(max([(lmolist[i]+rmolist[i])%mo for  i in range(g)]))
print(sum(mlist))


raw=0
su=0
inlist=[6, 2, 12, 4, 18, 6, 24, 8, 30, 10]
innum=(30,10)
for i in range(998):
    raw+=inlist[i%10]
    inlist[i%10]=inlist[i%10]+innum[i%2]
    su+=raw
print(su)
