#write a python script to printa set of three words in dictionary order.Words are given by the user.
a=input("Enter first word:");
b=input("Enter second word:");
c=input("Enter third word:");
if a>b:
    if a>c:
        if b>c:
            print(c,b,a)
        else:
             print(b,c,a)
    else:
        print(b,a,c)
             
else:
     if b>c:
         if a>c:
             print(c,a,b)
         else:
            print(a,c,b)

     else:
          print(a,b,c)
