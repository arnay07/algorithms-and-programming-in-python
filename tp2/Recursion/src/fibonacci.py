from ap2_decorators import trace




dict_fibo = dict()


@trace
def fibo(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        if n in dict_fibo.keys():
            return dict_fibo[n]
        else:
            dict_fibo[n] = fibo(n-1)+fibo(n-2)
            return dict_fibo[n]
        
        #ne pas oublier de vider dict_fibo après
