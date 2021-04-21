# Write a python script to product of odd nth natural  number.
x=int(input("Enter a number:\n"))
n=1
while x>1:
       if(x%2!=0):
        n=n*x;
       x=x-1;  

print("prodduct of given odd number:\n%d"%n);
