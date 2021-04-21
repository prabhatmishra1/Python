def display1(n,a):
    if(a>n):
       return
    print(a,end=" ")
    display1(n,a+1)
   
def display2(n):
    if(n==0):
        return
    print(n,end=' ')
    display2(n-1)

def even(n,a):
    if(a>n):
       return
    if(a%2==0):
     print(a,end=" ")
    even(n,a+1)

    


def squar(n):
    if(n==0):
        return
    print(n*n,end=' ')
    squar(n-1)

def cube(n,a):
    if(a>n):
       return
    print(a*a*a,end=" ")
    cube(n,a+1)

    
while(1):    
 print("Menu Driven:")
 print("1:print natural number:\n2:print reverse natural number:")
 print("3:Evan natural number:\n4:Odd natural number:\n5:Square natural number:\n6:cube natural number:")
 ch=int(input("Enter your choice:\n"))
 if(ch==1):
    
  a=1    
  n=int(input("Enter the value of n for display the natural numbers: "))
  display1(n,a)
  print()
  
 if(ch==2):
     
  n=int(input("Enter the value of n for display the natural numbers in reverse order: "))
  display2(n)
  print()

 if(ch==3):

     
  a=1   
  n=int(input("Enter the value of n for display the even number: "))
  even(n,a)
  print()

 if(ch==4):

     
  a=1   
  n=int(input("Enter the value of n for display the odd number: "))
  odd(n,a)
  print()
          
 if(ch==5):
     
  n=int(input("Enter the value of n for display the square of natural numbers in reverse order: "))
  squar(n)
  print()
  
 if(ch==6):
  a=1   
  n=int(input("Enter the value of n for display the cube of natural numbers:"))
  cube(n,a)
  print()
