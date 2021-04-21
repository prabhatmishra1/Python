# Write a python script to reverse a string.
s=input("Enter a string:-")
print("Given string is:",s)
print("Reverse string:")
print(s[::-1])#1st way

#2nd  way
m=len(s)
l=[]
c=[]
for i in  s:
     l.append(i)
    
for i in range(m-1,-1,-1):
    c.append(l[i])

for i in c:
    print(i,end="")
#3rd  way
print()    
for i  in reversed(s):
          print(i,sep="",end="")
#Sort   string
print("\nSorted string is:")
for i in sorted(s):
        print(i,sep="",end="")
