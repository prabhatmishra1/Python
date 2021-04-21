#Write a pyton script to find the greatest number from List.
n=int(input("Enter the Size of List:\n"))
l=[]
for i in range(0,n):
    l.append(int(input("Enter Integers")))
print("List is:",l)

m=l[0]
for i in l:
    if(m<i):
        m=i
print(" %d is  the greatest number in the List"%m)
