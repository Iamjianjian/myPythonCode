'''
    对于无穷序列12345678910111213....（Infi）
    给出任意的字符串（s），返回它在无穷序列第一次出现的索引
    
    思路：
        1 s由至少3个数的不同部分组成
        从s的左边开始假设第一个完整的数字为x位
        再遍历每一个可能的开始位置
        返回这个数字，和偏移量
        2 有两部分组成

'''
import time

def func(s):
    l=len(s)
    '''
        处理第一个字符为0的情况
    '''
    if s[0]!='0':#第一个不是零,则最多可以去int(s)
        answer=(int(s),0)
    else:#第一个是零,则最多可以去int('1'+s)
        answer=(int('1'+s),-1)
    nl=1
    '''
    下面这部分为第一中情况，当s第一位是完整数字的第一位时有可能会是两个部分组成但是没影响
    '''
    while nl<l:
        for i in range(nl):
            if i+nl<l:
                #数字首位不能为0
                iszero=False
                for j in range(i,l,nl):
                    if s[j]=='0':
                        iszero=True
                        break
                #有数字首位为0跳过
                if iszero:
                    continue
                f=int(s[i:i+nl])
                if i and str(f-1)[-1:-1*i:-1]!=s[i-1::-1]:
                    continue
                nums=s[0:i+nl]
                t=f
                while len(nums)<l:
                    t+=1
                    nums+=str(t)
                if (nums[0:l]==s) and (f<answer[0]):
                    answer=(f,i)
        nl+=1
    '''
    下面是情况2
    '''
    # if(l&1) and (int(s[0:l//2])+1)==int(s[l//2:l]):#处理前后两个数的长度不一样的的情况 即9999 10000
    if '1' in s and s[0]=='9':
        temp=s.index('1')
        subs=s[0:temp]
        exnine=True
        for i in '123456780':#前面只有9
            if i in subs:
                exnine=False
                break
        if  exnine:
            for i in '123456789':#后面只有0或者没有
                if i in s[temp+1:]:
                    exnine=False
                    break
        if exnine :
            if (l-temp-1)<=temp:
                tempanswer=(int(s[0:temp])+1,temp)
            else:
                tempanswer=(int(s[temp:]),temp)
            if tempanswer[0]<answer[0]:
                answer=tempanswer
            return answer
    #排除9999100000的情况后，奇数偶数的nl最小值不一样
    if(l&1):
        nl=l//2+1
    else:
        nl=l//2
    #nl一直取值到l
    while nl<l:
        #第一个数字向前偏移的范围为0~2nl-L
        for i in range(2*nl-l+1):
            if (s[nl-i]=='0'):
                continue
            h=int(s[0:nl-i])#前面一部分
            h+=1#加一之后这部分和下一个数字的对应位的数字一样
            x=l-nl#x 为交叉位
            if str(h)[0:x]==s[l-x:l]:#第一个数交叉部分在前面 第二个在后面 交叉部分相同则数字符合
                t=int(s[nl-i:l-x]+s[0:nl-i])+1#组合出数字
                if (t<answer[0]):
                    answer=(t,nl-i)
        nl+=1
    if len(str(answer[0]))<l:
        return answer
    #数字长为l时
    for i in range(1,l):
        if s[i]=='0':
            continue
        if i<len(str(int(s[0:i])+1)):
            tempanswer=(int(s[i:])*10**i,i)
        else:
            tempanswer=(int(s[i:]+s[0:i]),i)
        if answer[0]>tempanswer[0]:
            answer=tempanswer
    return answer



def func2(answer):
    num=answer[0]
    l=len(str(num))
    count=0
    for i in range(0,l-1):
        count+=9*10**i*(i+1)
    count+=(num-10**(l-1))*(l)
    return count-answer[1]

def findposition(n):
    print(func2(func(str(n))))


findposition(91)
param=(456,454,91,9100,123456798,123459876,910000000)
an=(3,79,8,188,1000000071,1000027773,68888888)
for i in param:
    print(an[param.index(i)],end=' ')
    findposition(i)

print(time.process_time())