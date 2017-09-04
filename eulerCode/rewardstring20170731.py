def func(n):
    lone=3
    ltwo=1
    lzero=8
    one=2
    two=1
    zero=4
    day=3
    while day<n:
        day+=1
        temp=lone,ltwo,lzero,one,two,zero
        lone=temp[2]#lzero
        ltwo=temp[0]#lone
        lzero=temp[5]+temp[3]+temp[4]+temp[1]+temp[0]+temp[2]#zero+ltwo+lone
        one=temp[5]#zero
        two=temp[3]#one
        zero=temp[3]+temp[4]+temp[5]#one+two
    return one+two+zero+lone+ltwo+lzero
print(func(30))
