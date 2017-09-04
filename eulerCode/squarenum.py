import time
f=int(19293949596979899**0.5)
print(f)
j=f%10
if 7<=j:
    f=f-j+7
    sort=True
elif 3<=j:
    f=f-j+3
    sort=False
else:
    f=f-j-3
    sort=True
an=False
if not sort:
    temp=str(i**2)
    if (temp[2],temp[4],temp[6],temp[8],temp[10],temp[12],temp[14],temp[16])==('2','3','4','5','6','7','8','9'):
        an=True
    else:
        f=f-6
if not an:
    while True:
        temp=str(f**2)
        if (temp[2],temp[4],temp[6],temp[8],temp[10],temp[12],temp[14],temp[16])==('2','3','4','5','6','7','8','9'):
            break
        f-=4
        temp=str(f**2)
        if (temp[2],temp[4],temp[6],temp[8],temp[10],temp[12],temp[14],temp[16])==('2','3','4','5','6','7','8','9'):
            break
        f-=6

print(f*10)

print(time.process_time())
