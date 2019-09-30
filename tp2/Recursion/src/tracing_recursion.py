#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
:mod:`tracing_recursion` module 

:author: ` Arnaud Kaderi, BAH Elhadj ibrahima
         Univ. Lille <http://portail.fil.univ-lille1.fr>`_

:date: 2019, September. Last revision: 2019, september


"""



from ap2_decorators import trace




@trace
def add(a,b):
    """
    adds a to b
    
    :param a: number a
    :param b: number b
    :type a: int
    :type b: int
    :return: the sum of a and b
    :rtype: int

    """
    if b==0:
        return a
    else:
        if b>0:
            return add(a+1,b-1)
        else:
            return add(a-1,b+1)


dict_binomial = {}


@trace
def binomial(n,p):    
    """
    Calculates the binomial of p in n
    
    :param p: number p that we are trying to find  in n
    :param n: n objects in the set
    :type p: int
    :type n: int 
    :return: the binomial of p in n
    :rtype: int
    :CU: p must be superior or equal to 0 and inferior or equal to n
    
    """

    assert p<=n and p>=0, "p must be superior or equal to 0 and inferior or equal to n"

    global dict_binomial
    
    if (p==0 or p==n):
        return 1
    else:
        if (n,p) in dict_binomial:
            return dict_binomial[(n,p)]
            
        else:           
            dict_binomial[(n,p)] = binomial(n-1, p-1) + binomial(n-1,p)
            return dict_binomial[(n,p)]
        

        
        
@trace
def is_palindromic(word):
    """
    return True if a word is palindromic or False if not
    
    :param word: the word that we want to test
    :type word: string
    :return: True if word is palindromic, False if not
    :rtype: boolean
    
    """
    n = len(word)
    return (n <= 1 or word[0] == word[-1] and is_palindromic(word[1:n-1]))






   

