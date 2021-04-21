#Default argument.
def add(a=0,b=0,c=0):#default argument
    c=a+b+c
    print("sum=",c)
     
#add(10,20,None)#error comes
add(10,20,30)
add(10,20)
add(10)
add()
