'''Define a class student with instance variable rollno,name,semester and branch and also define
 setvalue instance method and getvalueinstace method.'''

class Student:
    def __init__(self,r,n,s,b):
        self.rollno=r;
        self.name=n;
        self.sem=s;
        self.branch=b;
    def getvalue(self):
        print("ROllno=%d\nName=%s\nSem=%s\nBranch=%s"%(self.rollno,self.name,self.sem,self.branch))
obj=Student(101,"Prabhat","4th","MCA");
   
obj.getvalue()
print(obj.__dict__)#it checks how many instanse variable we have for object obj
