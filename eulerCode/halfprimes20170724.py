import time
b=time.time()
def func(n):
    m=n//2
    t=[False,False]+[True for i in range(m-1)]
    primes=[]
    count=0
    num=int(pow(n,.5))
    for i in range(2,m+1):
        if t[i]:
            primes.append(i)
            temp=i+i
            while temp<=m:
                t[temp]=False
                temp+=i
    leng=len(primes)
    result=leng
    t=1
    temp=int(pow(n,0.5))
    while primes[t]<=temp:
        result+=binary_find_index(primes,t,leng,n)-t+1
        t+=1
    return result

def binary_find_index(primes,numindex,leng,n):
    num=primes[numindex]
    begin=numindex
    end=leng
    while True:
        numindex=begin+end
        numindex//=2
        t=num*primes[numindex]
        if t>n:
            end=numindex
        elif num*primes[numindex+1]<=n:
            begin=numindex
        else:
            return numindex
#func(10**8)
#print(time.time()-b)


def fun2(n):
    m=n//2
    t=[False,False]+[True for i in range(m-1)]
    primes=[]
    num=int(pow(n,.5))
    for i in range(2,m+1):
        if i>num:
            break
        if t[i]:
            primes.append(i)
            temp=i+i
            while temp<=m:
                t[temp]=False
                temp+=i
    ind=len(primes)-1
    result=0
    num=n//primes[-1]
    j=i
    del i
    for i in range(j,m+1):
        if t[i]:
            primes.append(i)
            temp=i+i
            while temp<=m:
                t[temp]=False
                temp+=i
            if num<i:
                result+=len(primes)-ind-1
                ind-=1
                #print(result,num)
                num=n//primes[ind]
    return result+len(primes)


