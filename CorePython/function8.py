#wrt a python script to calculate fibonacci series.
def feb(n):
 x=0
 y=1
 l=[]
 while n>=1:
      z=x+y
      l.append(z)
      x=y
      y=z
      n-=1
 return l
n=int(input("Enter  the size of  n: "))
l=feb(n)
print(l)
    
    
