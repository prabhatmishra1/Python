#Write a python script to accept marks of five subjects from user maximum marks is 100, calculate  fail,pass and grade also.
print("Enter marks of five subjects:\n");
a=float(input());
b=float(input());
c=float(input());
d=float(input());
e=float(input());
per=(a+b+c+d+e)/5
print("Total Percentage:%f"%per);
if per<=32:
    print("Fail")
elif per>=33 and per<=49:
    print("Third Division:");
elif per>=50 and per<=59:  
    print("second Division:");

elif per>60:   
    print("First Division:");    
