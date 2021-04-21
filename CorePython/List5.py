#Write a python script to create a List of Nth Square Number.
n=int(input("Enter the value of nth natural number:"))
l=[]
for i in range(1,n+1):
        l.append(i*i)
print("List of %dth square number:"%n,l)    

      
