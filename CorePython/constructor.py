# write a program to accept name and age and print that with classes.
class student:
    def __init__(self):
        print("Enter a value to check its palindromor not.")
        self.l=tuple(input())
        
    def palindrom(self):
        l=self.l
        print(l)
        for i in range(0,len(l)//2):
            if l[i]!=l[len(l)-1-i]:
                print("Not palindrom")
                break
        else:
            print("palindrom")
            
obj1=student()
obj1.palindrom()
        
