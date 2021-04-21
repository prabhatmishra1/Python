#Write a python script to creat the set of n prime numbers:
n=int(input("Enter the value of N:"))
s={1,2,3}
for i in range(4,n+1):
     for j in range(2,i):
         if(i%j==0):
             break
         
     
     else:
        s.add(i)

print("Set of %d prime number:"%n,s)
