def LCM(a,b):
    c= a if a>b else b 
    for i in range(c,a*b):
        if(i%a==0 and i%b==0):
            break;
    return i
def HCF(a,b):
    z= a if a<b else b
    for i in range(z,0,-1):
        if(a%i==0 and b%i==0):
            break
    return i
    
print("Enter two number:")
a=int(input())
b=int(input())
c=LCM(a,b)
z=HCF(a,b)
print("Lcm of {} and {}={}".format(a,b,c))
print("Hcf of {} and {}={}".format(a,b,z))

        
