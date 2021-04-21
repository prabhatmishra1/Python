# Write a python script to cheack wether number is prime or not":

x=int(input("Enter a number to cheack wether prime or not.\n"))
for i in range(2,x):
      if(x%i==0):
          break;
if i==x-1:
   print("{} is prime number:".format(x))

else:
    print("{} is not prime number:".format(x))
