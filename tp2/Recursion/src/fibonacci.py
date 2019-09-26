from ap2_decorators import *






@count
def fibo(n, dict_fibo={}):
    
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        if n in dict_fibo.keys():
            return dict_fibo[n]
        else:
            dict_fibo[n] = fibo(n-1, dict_fibo) + fibo(n-2, dict_fibo)
        return dict_fibo[n]
        
        
      



