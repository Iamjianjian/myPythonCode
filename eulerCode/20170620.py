def get_prime(l=6):
    #numlist=[True for i in range(10**l//2)]
    numlist=[True for i in range(10**5*3)]
    num=0
    prime_nums=[]
    ifneed=False
    while num<len(numlist):
        if numlist[num]:
            temp=3*num+3
            if ifneed:
                prime_nums.append(num*2+3)
            ifneed=ifneed^True
            while temp<len(numlist):
                numlist[temp]=False
                temp+=num*2+3
        num+=1
    return prime_nums

primes=get_prime()
def find(de=10**10):
    global primes
    leng=len(primes)
    be=0
    ed=leng-1
    ind=(be+ed)//2
    n=ind*2+3
    while True :
        if (primes[ind]*2*(ind*2+3)>de) and (primes[ind-1]*2*(2*ind+1)<de):
            return ind*2+3
        if primes[ind]*2*(ind*2+3)>de:
            ed=ind
            ind=(ind+be)//2
            continue
        be=ind
        ind=(ind+ed)//2
        
print(find())
