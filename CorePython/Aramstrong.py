#Write a python script to print  all the armstrong number from 1 to 1000.

x=0
r=0
s=0
print("Aramstrong number from 1 to 1000")
for i in range(1,1001,1):
 x=i;
 s=0;
 
 while(x!=0):
    
      r=x%10
      s=(s)+(r*r*r);
      x=x//10;
      
 if(s==i):
  print(i,end=" ");
