# write a python script to print squares of numbers from a to b.values of a and b are given by user.
print("Enter two value:");
a=int(input())
b=int (input())
print("Square from %d to %d"%(a,b))
for i in range(a,b+1,1):
        c=i*i;
        print(c);
