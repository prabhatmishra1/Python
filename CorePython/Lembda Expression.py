#Lambda Expression

#first way
s=lambda a,b:a+b
r=s(10,20)
print("sum=",r)

#second way
s=(lambda a,b:a+b)(10,20)
print("sum=",s)

#second way
s=(lambda a,b:a+b)(int(input("Enter first value:\n")),int(input("Enter second value:\n")))
print("sum=",s)

#Recurstion
s=lambda a:1 if a==0 else a*s(a-1)
r=s(5)
print("factoroal=",r)
