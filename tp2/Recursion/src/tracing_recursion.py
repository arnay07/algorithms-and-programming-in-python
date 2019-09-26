from ap2_decorators import trace




@trace
def add(a,b):
    if b==0:
        return a
    else:
        if b>0:
            return add(a+1,b-1)
        else:
            return add(a-1,b+1)


        


@trace
def binomial(n,p, dict_binomial={}):    
     
    if (p==0 or p==n):
        return 1
    else:
        if (n,p) in dict_binomial.keys():
            return dict_binomial[(n,p)]
            
        else:           
            dict_binomial[(n,p)] = binomial(n-1, p-1, dict_binomial) + binomial(n-1,p, dict_binomial)
            return dict_binomial[(n,p)]
        

        
        
@trace
def is_palindromic(word):  
     n = len(word)
     return (n <= 1 or word[0] == word[-1] and is_palindromic(word[1:n-1]))
    
    
    
if __name__=='__main__':
    binomial(10,5)
    binomial(5,3)
   

