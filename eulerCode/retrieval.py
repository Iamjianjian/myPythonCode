''' scanf 顾名思义就是扫描
    例如  scanf('(apple | others) & two',0,len('(apple | others) & two'))
    就返回 (apple | others)的索引范围
    scanf('(apple | others) & two',16,len)
    就返回 & 的索引范围
    scanf('(apple | others) & two',18,len)
    就返回 two 的索引范围
'''
def scanf(string,findex,rindex):
    t=0
    while string[findex]==' ':
        findex+=1
    temp=findex
    while findex<rindex:
        if string[findex]=='(':
            t-=1
        elif string[findex]==')':
            t+=1
        elif string[findex]==' ':
            if t==0:
                break
        findex+=1
    return (temp,findex)

def calc(string,findex,rindex,txt):
    positive=True #开头是否有！可以跳过多个！
    while string[findex]=='!':
        positive=not positive
        findex+=1#掉过！
    bracket=False #括号有括号就说明这个字符串可能有运算符
    if string[findex]=='(':
        findex+=1
        rindex-=1
        bracket=True
    #没有括号 那就是一个没有运算符的字符串了 可以直接查找了
    if not bracket:
        if not positive:
            result=not string[findex:rindex] in txt
        else :
            result =string[findex:rindex] in txt
        return result
    index=findex#好像这个index是多余的 直接用findex就好了
    '''
    cl保存扫描的返回值 必然是
    一段可以转为bool值的字符串 和 一个运算符轮流出现
'''
    cl=[]
    while index<rindex:
        cl.append(scanf(string,index,rindex))
        index=cl[-1][1]
    '''
    拿到可以转为bool值的字符串 和 运算符
    cl只有一个元素 那么
    这个元素必然是可以转为bool值的字符串
'''
    if len(cl)==1:
        return calc(string,cl[0][0],cl[0][1],txt)

    '''
    cl 不止一个值,一个个弹出来计算
'''
    temp=cl.pop()
    result=calc(string,temp[0],temp[1],txt)
    while cl:
        symbol=string[cl.pop()[0]]#运算符
        if symbol=='|':
            if result==True:#或运算 一个是真后面不用算了
                return True
            else:#或运算 一个值是假 直接计算下一个字符串
                temp=cl.pop()
                result=calc(string,temp[0],temp[1],txt)
                continue
        '''
        因为& 和 | 的优先级问题
        为了防止cl里面还有 | 所以只好 & 一个个算了
'''
        temp=cl.pop()
        temp=calc(string,temp[0],temp[1],txt)
        if temp==False:
            result=False
            
    if not positive:
        result = not result
    return result
        
def func(string,txt):
    '''
    去掉两边的空格
    加上括号是为了兼容
    如果没有括号会出错
    例如 'one & yellow'
    会被calc看作是一个没有运算符的字符串了
    但是里面还有个 &
'''
    string=string.strip()
    string='('+string+')'
    return calc(string,0,len(string),txt)
    
txt = 'one apple with two leaves, one is green and the other is yellow.'
s1 = '!!(!three | one & four) & !five'
a=func(s1,txt)
print(a)
s1 ='!!(apple | others) & two'
a=func(s1,txt)
print(a)
s1 ='one & yellow & leaf'
a=func(s1,txt)
print(a)
s1 ='!green & (ones | two)' 
a=func(s1,txt)
print(a)
s1 ='(big | !apple | the) & ((!yellow | !green) | others)'
a=func(s1,txt)
print(a)
