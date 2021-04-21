# Write a python script to cheack greatest value in between real and imaginary part,value is given by user.

x=complex(input("Enter a complex number:\n"))
if x.real>x.imag:
    print("The real part %d is grater"%x.real)
else:
    print("The imaginary part %d is grater"%x.imag)
