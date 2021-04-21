#Exception handling.

'''a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
try:
    x=a/b
    print("a/b=",x)
except ZeroDivisionError:#Exception class
    print("Invalid attempt of Division:")
print("Hello  this is last lins:")

#When class is not match

a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
try:
    x=a/b
    print("a/b=",x)
except TypeError:# Wrong Exception class
    print("Invalid attempt of Division:")
print("Hello  this is last lins:")#not print bcz program is break

#Finally:

a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
try:
    x=a/b
    print("a/b=",x)
except TypeError:# Wrong Exception class
    print("Invalid attempt of Division:")

finally:
     print("We are in finally:")# finally reuns always
     print("Hello  this is last lins:")

#One or more the classes in except:

a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
try:
  if b==0:
     x=a/b
     print("a/b=",x)
except (TypeError,ValueError,ZeroDivisionError):# Wrong Exception class
    print("Invalid attempt of Division:")
except:
    print("Error")
else:#when no exception
    print("No error")'''

#Raised:

a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
if b==0:
     raise ZeroDivisionError("Denominator can not be Zero:")
     x=a/b
     print("a/b=",x)
