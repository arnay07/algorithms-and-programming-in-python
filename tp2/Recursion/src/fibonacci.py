#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
:mod:`fibonacci` module 

:author: ` Arnaud Kaderi, BAH Elhadj ibrahima
         Univ. Lille <http://portail.fil.univ-lille1.fr>`_

:date: 2019, September. Last revision: 2019, september


"""



from ap2_decorators import *



dict_fibo = {}


@count
def fibo(n):
    """
    Calculates the fibonacci number of the nth term.

    :param n: the nth term 
    :return: the fibonacci number to the nth term
    :rtype: int
    :CU: n >= 0
    
    :Example:
 
    >>> fibo(10)
    55
    >>> fibo(4)
    3
   
    
    """
    
    assert n >= 0, "n must be equal or superior to 0"

    global dict_fibo
    
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        if n in dict_fibo:
            return dict_fibo[n]
        else:
            dict_fibo[n] = fibo(n-1) + fibo(n-2)
        return dict_fibo[n]
        
        
      



if __name__=="__main__":
    import doctest
    doctest.testmod()
    dict_fibo = {}
    fibo.counter = 0
    fibo(40)
    print(fibo.counter)
    dict_fibo = {}
    fibo.counter = 0
    fibo(10)
    print(fibo.counter)
    
