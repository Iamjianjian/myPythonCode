txt = '''Hot work is one of the typical high risk work in work shop,
if out of control, it will cause tragedy. We manage our hot work basing on
the FM hot work permit system. Then, to make sure the fire risk are
eliminated before we start hot work, what should we do? Please refer
to this week's topic, hot work permit.'''

def adjust_txt(t,m):
    words=t.split()
    l=list(map(len,words))
    print(l)
    le=len(l)
    i=0
    j=0
    temp=0
    while i<le:
        temp+=l[i]+1# include blank
        i+=1
        if temp>m:
            if temp==m+1:
                for k in range(i-j-1):
                    words[j+k]+=" "
                words[i-1]+='\n'
                temp=0
                j=i
            else:
                temp-=l[i-1]+2
                r=m-temp
                if i-j-2==0:#only one word
                    words[j]+='\n'
                    j+=1
                    i=j
                    temp=0
                else:
                    x=r//(i-j-2)
                    d=r%(i-j-2)
                    for k in range(d):
                        words[j+k]+=" "*(2+x)
                    for k in range(i-j-d-2):
                        words[j+k+d]+=" "*(x+1)
                    words[i-2]+='\n'
                    temp=0
                    i-=1
                    j=i
    if 1<i-j:
        temp-=1
        r=m-temp
        x=r//(i-j-1)
        d=r%(i-j-1)
        for k in range(d):
            words[j+k]+=" "*(2+x)
        for k in range(i-j-d):
            words[j+k+d]+=" "*(x+1)
    return "".join(words)

print(adjust_txt(txt,16))
