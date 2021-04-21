#Write a python script to create the homogeneous tuple from hetrogeneous tuple.
t=eval(input("Enter Tuple: "))
print(t)
u=()
for i in t:
    if type(i)==int:
     u=u+(i,)
     print("Frequency of",i,"is",t.count(i))
print("Tuple with homogeneous elements:")     
print(u)
