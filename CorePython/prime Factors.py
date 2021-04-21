#Write a python script to find the prime factors of  given number:

x=int(input("Enter a number:\n"));
i=2
print("Prime Factors of given number:")
while x!=1:
    while x%i==0:
       print(i,end=" ")
       x=x/i;

    i+=1;
