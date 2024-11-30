# write a python script to find LCM.
print("Enter two number:")
a=int(input())
b=int(input())

for i in range(1,a*b):
    if i%a==0 and i%b==0:
       break
print("LCM of %d and %d= %d"%(a,b,i))
