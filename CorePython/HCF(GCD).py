# write a python secript to find HCF(GCD).
print("Enter two number to find HCF:");
a=int(input())
b=int(input())
c= a if a<b else b
print(c)
for i in range(c,0,-1):
     if(a%i==0 and b%i==0):
         break
        
print("HCF of %d and %d= %d"%(a,b,i));
