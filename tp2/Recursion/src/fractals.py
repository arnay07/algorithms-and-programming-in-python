#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
:mod:`fractals` module 

:author: ` Arnaud Kaderi, BAH Elhadj ibrahima
         Univ. Lille <http://portail.fil.univ-lille1.fr>`_

:date: 2019, September. Last revision: 2019, september


"""






from turtle import *
from math import sin



def zig_zag(n):
    """
    Draws n zig zags with turtle
    
    :param n: number of zig zag
    :type n: int
    :CU: n > 0

    """
    assert n > 0,'n must be at least 1'
    
    left(45)
    fd(75)
    right(90)
    fd(75)
    left(45)
    if n>1:
        zig_zag(n-1)
        
        


def courbe_von_koch(l,n):
    """
    Draws the curve of von koch of length l to the nth order
    
    :param l: the length of the curve
    :param n: the nth order
    :CU: l > 0 and n >= 0

    """
    assert l>0 and n >= 0,'l must be positive and n must be superior or equal to 0'
    
    if n==0:
        forward(l) 
    else:
        courbe_von_koch(l//3, n-1)
        left(60)
        courbe_von_koch(l//3, n-1)
        right(120)
        courbe_von_koch(l//3, n-1)
        left(60)
        courbe_von_koch(l//3, n-1)



        

def flocon_von_koch(l,n):
    """
    Draws the von koch flake of length l to the nth order

    :param l: the biggest radius of the flake
    :param n: the nth order
    :CU: l > 0 and n >= 0
    
    """
    assert l>0 and n >= 0,'l must be positive and n must be superior or equal to 0'
    
    if n==0:
        forward(l)
    else:
        courbe_von_koch(l//3, n-1)
        right(120)
        courbe_von_koch(l//3, n-1)
        right(120)
        courbe_von_koch(l//3, n-1)


        


def courbe_cesaro(l,n):
    """
    Draws the cesaro curve of length l to the nth order

    :param l: the length of the curve
    :param n: the nth order
    :CU: l > 0 and n >= 0
    
    """
    assert l>0 and n >= 0,'l must be positive and n must be superior or equal to 0'
    
    if n==0:
        forward(l+ (l-2*sin(5)*l)//2)

    else:
        courbe_cesaro(l//3,n-1)
        left(85)
        courbe_cesaro(l//3,n-1)
        right(170)
        courbe_cesaro(l//3, n-1)
        left(85)
        courbe_cesaro(l//3, n-1)


def carre_cesaro(l,n):
    """
    Draws the cesaro square of length l to the nth order

    :param l: the length of one side the square
    :param n: the nth order
    :CU: l > 0 and n >= 0
    
    """
    
    assert l>0 and n >= 0,'l must be positive and n must be superior or equal to 0'
    
    if n==0:
        forward(l+ (l-2*sin(5)*l)//2)
    else:
        courbe_cesaro(l//3, n-1)
        left(90)
        courbe_cesaro(l//3, n-1)
        left(90)
        courbe_cesaro(l//3, n-1)
        left(90)
        courbe_cesaro(l//3, n-1)




def sierpinski(l,n):
    """
    Draws the sierpinski  of length l to the nth order

    :param l: the length of one side the triangle
    :param n: the nth order
    :CU: l > 0 and n >= 0
    
    """
    assert l>0 and n >= 0,'l must be positive and n must be superior or equal to 0'
    
    if n==0:
        for i in range(3):
            forward(l)
            left(120)

    else:
        sierpinski(l//2,n-1)
        forward(l//2)
        sierpinski(l//2,n-1)
        backward(l//2)
        left(60)
        forward(l//2)
        right(60)
        sierpinski(l//2,n-1)
        left(60)
        backward(l//2)
        right(60)
        
             
        
        
        
if __name__=='__main__':
    zig_zag(6)
    clearscreen()
    speed(0)
    courbe_von_koch(600,3)
    clearscreen()
    speed(0)
    flocon_von_koch(600,4)
    clearscreen()
    speed(0)
    courbe_cesaro(600,4)
    clearscreen()
    speed(0)
    carre_cesaro(600,4)
    clearscreen()
    penup()
    goto(0,-300)
    pendown()
    speed(0)
    sierpinski(600,4)
    
    
