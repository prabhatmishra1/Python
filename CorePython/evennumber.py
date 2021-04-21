#Write a python  script to print first N Even natural number in reverse order.
n=int(input("Enter a number:\n"))
print("List of Even numbers:")
for i in range(n,0,-1):
    if(i%2==0):
       print(i,end=",",sep=".")
