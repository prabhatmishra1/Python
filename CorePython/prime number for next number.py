# write a python script to find next prime number  to given number:
print("Enter a umber to find next prime number:")
a=int(input())

for i in range(a+1,a+10):
    flag=True
    for j in range(2,i):
        if(i%j==0):
         #print("%d is not prime number:"%i)
         flag=False
         break

    if flag:
         print("%d is prime number:"%i);
         break
