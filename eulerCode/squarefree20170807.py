import math
import time
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
        return [rawnum]
dnum={}
squarefree_nums=[1,2,3,5,6,7,10,15,21,35]
binomials=[[[3,7],[],21],[[5,7],[],35]]
n=7
while n<51:
    dlist=denum(n+1)
    if  n&1:
        temp=[]
        temp.append(binomials[-1][0][:])
        temp.append(binomials[-1][1][:])
        temp.append(binomials[-1][2])
    for i in range(len(binomials)):
        for j in dlist:
            if j in binomials[i][0]:
                binomials[i][0].remove(j)
                binomials[i][1].append(j)
            else:
                binomials[i][0].append(j)
        if n-i-1 in dnum:
            templist=dnum[n-i-1]
        else:
            templist=denum(n-i-1)
            dnum[n-i-1]=templist
        for j in templist:
            if j in binomials[i][0]:
                binomials[i][0].remove(j)
            else:
                binomials[i][1].remove(j)
                binomials[i][0].append(j)
        binomials[i][2]=(binomials[i][2]*(n+1))//(n-i-1)
        if not binomials[i][1] and binomials[i][2] not in squarefree_nums:
            squarefree_nums.append(binomials[i][2])
    if  n&1:
        temp[2]*=2
        if 2 in temp[0]:
            temp[0].remove(2)
            temp[1].append(2)
        else :
            temp[0].append(2)
            if not temp[1] and temp[2] not in squarefree_nums:
                squarefree_nums.append(temp[2])
        binomials.append(temp)
    if n in dnum:
        temp=dnum[n]
    else:
        temp=denum(n)
        dnum[n]=temp
    if len(set(temp))==len(temp):
        squarefree_nums.append(n)
    n+=1
print(sum(squarefree_nums))
print(time.process_time())
