from turtle import *



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
    
    


if __name__=='__main__':
    zig_zag(3)
