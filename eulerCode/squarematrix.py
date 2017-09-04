def func(quantity):
    lim=int(pow(quantity,0.5))
    k=lim//2
    result=((2*k-1)//2+1)*(k-1)
    if lim&1:
        result+=k
        for i in range(lim+1,quantity//4,2):
            r=int(pow(lim**2-quantity,0.5))
#            if r&1:
#                r+=1
#            else:
#                r+=2
            r+=2
            r//=2
            result+=i//2-r
        for i in range(lim+2,quantity//4,2):
            r=int(pow(lim**2-quantity,0.5))
            r//=2
            r+=1
            result+=i//2-r
    else:
        for i in range(lim+1,quantity//4,2):
            r=int(pow(lim**2-quantity,0.5))
            r//=2
            r+=1
            result+=i//2-r
        for i in range(lim+1,quantity//4,2):
            r=int(pow(lim**2-quantity,0.5))
#            if r&1:
#                r+=1
#            else:
#                r+=2
            r+=2
            r//=2
            result+=i//2-r
        return result
        
