#2 332 3 209 5 143
def binary_find_index(array,n,l=334):
    begin=0
    end=l-1
    while True:
        mid=(begin+end)//2
        if array[mid]<=n:
            if n<array[mid+1]:
                return mid
            begin=mid
        else:
            end=mid
            
x=1
fiveAndThree=[1]
for i in range(144):
    x*=5
    fiveAndThree.append(x)
two=[1]
x=1
for i in range(333):
    x=x<<1
    two.append(x)

result=0
for i in range(210):
    j=0
    while fiveAndThree[j]<=10**100:
        x=fiveAndThree[j]
        index=binary_find_index(two,x)
        if x<<(332-index)<=10**100:
            result+=333-index
        else:
            result+=332-index
        fiveAndThree[j]=x*3
        j+=1
        
print(result)

