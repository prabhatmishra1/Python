#Write a python script to calculate the sum of List.
n=int(input("Enter the size of List"))
l=[]
print("Enter elements:")
for i in range(0,n):
    l.append(float(input()))

print("List is:",l)
s=0
for i in l:
    s=s+i
print("Sum of the List:",s)
