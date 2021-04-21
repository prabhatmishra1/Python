#write a python script to calculate whether the given numbers is co-prime or not

def isCoprime(a,b):
    fact1=[]
    fact2=[]
    for i in range(2,a+1):
        if(a%i==0):
            fact1.append(i)
    print(fact1)        
    for j in range(2,b+1):
        if(b%j==0):
            fact2.append(j)
    print(fact2)        
    for k in fact2:
        if k in fact1:
             return False
    else:
         return True
print(isCoprime())
