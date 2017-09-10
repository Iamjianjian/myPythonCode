def eulid(a,b,gcd=1):
    li1=[1,0,a]
    li2=[0,1,b]
    while li2[2]!=gcd:
        q=li1[2]//li2[2]
        templist=[li1[i]-li2[i]*q for i in range(3)]
        li1,li2=li2,templist
    return li2[0]%b

def f(string):
    if string[-1]=='d':
        b=1
        c=2
    elif string[-1]=='U':
        b=-2
        c=4
    else:
        b=0
        c=1
    a=3
    for i in range(-2,-1*len(string)-1,-1):
        a*=3
        b*=3
        if string[i]=='d':
            b+=c
            c*=2
        elif string[i]=='U':
            b-=2*c
            c*=4
    t=eulid(a,c)*-1*b%c
    while (t*a+b)//c<10**15:
        t+=c
    return (t*a+b)//c
print(f('UDDDUdddDDUDDddDdDddDDUDDdUUDd'))

def ff(i,ss):
    temp=i
    while 10**15<temp:
        temp-=1
        i=temp
        t=0
        while i!=1:
            if not i%3:
                i=i//3
                s='D'
            elif i%3==1:
                i=(4*i+2)//3
                s='U'
            else:
                i=(2*i-1)//3
                s='d'
            if ss[t]!=s:
                break
            t+=1
        if i==1:
            return False
    return i

            
