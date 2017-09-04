def func(leng,block=50):
    quantitylist=[]
    i=0
    while i<51:
        if i<leng:
            quantitylist.append(0)
        elif i==leng:
            quantitylist.append(1)
        else:
            quantitylist.append(quantitylist[i-1]+1+quantitylist[i-leng])
        i+=1
    return quantitylist[50]
sum([func(i) for i in (2,3,4)])
