#Write a python script to cheack nature of roots of given quadaratic equation.
print('"Enter the value of Ax^2+Bx+C quadaratic equation:"\n')
a=float(input("Enter the value of A:\n"))
b=float(input("Enter the value of B:\n"))
c=float(input("Enter the value of c:\n"))
d=(b*b)-(4*a*c)
print("The value of Discriminant is:%f\n"%d)

if d<0:
    print("Imaginary Roots:")
elif d==0:
    print("Equal Roots:")
elif d>0:
    print("Distinitic Roots:")
   


