#Write a python script to print all the prime number between two numbers.
print("Enter two number:");
l=int(input())
u=int(input())
x=0
for i in range(l,u+1):
    x=i;
    for j in range(2,x):
        if x%j==0:
           break
           
    else:    
     print("%d" %i)
     break 
