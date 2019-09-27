from turtle import *
from math import sin



def zig_zag(n):
    """
    """
    left(45)
    pendown()
    fd(75)
    right(90)
    fd(75)
    left(45)
    if n==1:
        exitonclick()
    else:
        return zig_zag(n-1)


def courbe_von_koch(l,n):
    """
    """

    
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
    if n==0:
        forward(l)
    else:
        courbe_von_koch(l//3, n-1)
        right(120)
        courbe_von_koch(l//3, n-1)
        right(120)
        courbe_von_koch(l//3, n-1)


def courbe_cesaro(l,n):
    speed(0)
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
        
             
        
        
        
