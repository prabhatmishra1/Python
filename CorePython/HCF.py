#Write a python script to calculate HCF of two number by using Division method. 
a=int(input("Enter first number:"));
b=int(input("Enter first number:"));

if a>b:  #Swaping for two number;
    temp=0;
    temp=b;
    b=a;
    a=temp;

while(a>1):
     c=a;
     a=b%a;
     if(a==0):
       break
     c=c%a
print(c)   
        
    
