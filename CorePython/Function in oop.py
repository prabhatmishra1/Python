class student:
    def swap(self,a,b):
        print("x=%d,y=%d"%(a,b))
        temp=a
        a=b
        b=temp
        print("After swapping:")
        print("x=%d,y=%d"%(a,b))

print("Enter two number:")
a=eval(input())
b=eval(input())
obj=student()
obj.swap(a,b)
