def func(mo,inde,orgin,ba,an):
       inde=bin(inde)[2:]
       ba=ba%mo
       orgin=orgin%mo
       for i in range(-1,-len(inde)-1,-1):
              if int(inde[i]):
                     orgin=(orgin*ba)%mo
              ba=ba**2%mo
       orgin=(orgin+an)%mo
       return orgin


print(func(10**10,7830457,28433,2,1))
