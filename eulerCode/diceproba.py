def func1(dice,num):
    A=[1]
    temp=1
    for i in range(num):
        temp*=(i+2)
        A.append(temp)
    pro=[1]
    distru=[]
    distru.append([1,num]+[0]*(dice-1))
    count=dice*num-num+1
    for i in range((count+1)//2-1):
        temp=[]
        for d in distru:
            for j in range(1,dice):
                if d[j]:
                    t=d[:]
                    t[0]=(t[j]*t[0])//(t[j+1]+1)
                    t[j]-=1
                    t[j+1]+=1
                    if t not in temp:
                        temp.append(t)
        distru=temp
        pro.append(sum([i[0] for i in distru]))
    return pro

def func2(dice1,num1,dice2,num2):
    pro1=func1(dice1,num1)
    pro2=func1(dice2,num2)
    count1=dice1*num1-num1
    if count1&1:
        pro1+=pro1[::-1]
    else:
        pro1+=pro1[:-1][::-1]
    count2=dice2*num2-num2
    if count2&1:
        pro2+=pro2[::-1]
    else:
        pro2+=pro2[:-1][::-1]
    numerator=0
    denominator=dice1**num1*dice2**num2
    if num2<=num1:
        for i in range(count1+1):
            numerator+=sum(pro2[0:i+num1-num2])*pro1[i]
    else:
        temp=num2-num1
        for i in range(temp,count+1):
            numerator+=sum(pro2[0:i+num1-num2])*pro1[i]
    return '%.7f'%(numerator/denominator)
    

print(func2(4,9,6,6))
