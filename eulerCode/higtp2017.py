count=0
i=11
def sumofs(s):
    su=0
    while s:
        su+=s%10
        s//=10
    return su

def is_find(inte):
    base=sumofs(inte)
    if base==1:
        return False
    while True:
        if inte%base:
            return False
        inte//=base
        if inte==1:
            return True

numlist=[]
def func(i):
    r=i
    global numlist
    t=0
    while len(str(r))<i and t<2*r:
        r*=i
        t=sumofs(r)
        if t==i:
            numlist.append(r)
            

i=2
while True:
    func(i)
    if len(numlist)>=30:
        numlist.sort()
        t=len(str(numlist[29]))
        if i>t*9:
            print(numlist[29])
            break
    i+=1
