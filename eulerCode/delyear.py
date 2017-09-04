import os
import os.path

raw=r'D:\py\PyCharm Community Edition 2017.1.2\docu\leg'
def delyear(year):
    p=raw+'\\%d'%year
    for i in os.listdir(p):
        dp=p+'\\%s'%i
        for j in os.listdir(dp):
            if os.path.getsize(dp+'\\%s'%j)<90000:
                os.remove(dp+'\\%s'%j)
                

y=[2017,2016,2015]
for i in y:
    delyear(i)
