#Write a python script to manage the tuples.

t=eval(input("Enter tuple: "))
s=0
y=0
for i  in t:
    s=s+i
    y=t.count(i)
    print("%d=%d"%(i,y))
print("Sum of Tuple:",s)    
print("Average of Tuple:",s/len(t))
print("Sorted Tuple:",tuple(sorted(t)))
print("Reverse Tuple:",t[::-1])
print("Max number in the Tuple:",max(t))
u=eval(input("Enter tuple: "))
if t==u:
 print("Both tuple are in same oreder:")
else:
 print("Both tuple are not in same oreder:")    
t=t+(u)
print("Two merge Sorted Tuple:",tuple(sorted(t)))



