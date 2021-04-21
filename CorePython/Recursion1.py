import os
#waps to find the factorial and summation of given number.
def fact(n):
    if(n==0 or n==1):
        return 1
    else:
        return(n*fact(n-1))
def add(n):
    if(n==0 or n==1):
        return 1
    else:
        return(n+fact(n-1))
def fib(n):
    if(n==1 or n==2):
        return 1
    else:
        return(fib(n-1)+fib(n-2))
def  gcd(a,b):
    if(a==b):
        return a
    if(a%b==0):
        return b
    if(b%a==0):
        return a
    if(a>b):
        return(gcd(a%b,b))
    else:
        return(gcd(a,b%a))
    
while(1):

 print("Menu Driven:")
 print("1:Factorial\n2:Summation\n3:Fibnacci\n4:GCD\n5:Exit")
 print("Enter your Choice:")
 ch=int(input())
 if(ch==1):
  n=int(input("Enter the value of n:"))
  f=fact(n)
  print("Factorial of %d = %d"%(n,f))
  
 if(ch==2):
  n=int(input("Enter the value of n:"))
  a=add(n)
  print("Sum of %d = %d"%(n,a))

 if(ch==3):
  n=int(input("Enter the value of n:"))
  print("fibonacci series for %d is: "%(n))
  for i in range(1,n+1):
     c=fib(i)
     print(c,end=' ')
 if(ch==4):
    print("Enter two number to calculate the gcd.")
    a=int(input())
    b=int(input())
    g=gcd(a,b)
    print("Hcf of %d and %d = %d"%(a,b,g))
 if(ch==5):
     exit()
 
