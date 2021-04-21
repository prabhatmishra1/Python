#Write a pyton script to calculate  the sum of even and odd number.
n=int(input("Enter the Size of List:\n"))
l=[]
for i in range(0,n):
    l.append(int(input("Enter Integers")))
print("List is:",l)

s1=0
s2=0
for i in l:
    if(i%2==0):
     s1=s1+i
    else:
      s2=s2+i  
     
print("Sum of Even number:",s1)
print("Sum of odd number:",s2)
