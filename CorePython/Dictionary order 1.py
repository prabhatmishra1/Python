a=(input("Enter 1st name:"))
b=(input("Enter 2nd name:"))
c=(input("Enter 3rd name:"))

if a<b<c:
    print(a,b,c)
    
elif  a<c<b:
    print(a,c,b)


elif  b<a<c:
    print(b,a,c)

elif  b<c<a:
    print(b,c,a)
    

elif  c<a<b:
    print(c,a,b)
    
else:
    print(c,b,a)

    
    
