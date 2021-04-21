# write a python script to cheack it is coprime or not:
print("Enter two number to cheack  whether coprime or not:");
x=int(input());
y=int(input());
m= x if x<y else y

for i  in range(2,m+1):
    if(x%i==0 and y%i==0):
      print("%d and %d are not Coprime:"%(x,y))
      break    
if(i==m):
 print("%d and %d are  Coprime:"%(x,y))
 
