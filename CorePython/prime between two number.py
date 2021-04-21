# write a python script to find prime number between to number:
print("Enter two number to find prime number:")
a=int(input())
b=int(input())

for i in range(a,b+1):
    flag=True
    for j in range(2,i):
        if(i%j==0):
         #print("%d is not prime number:"%i)
         flag=False
         break

    if flag:
         print("%d is prime number:"%i);
