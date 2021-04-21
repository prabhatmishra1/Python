'''Define a class Employee with instance variable empid,name,salary.Define a constructor
   to initilize the member variable.Define a function to show employee data.
'''
class Employee:
    def __init__(self,empno,name,salary):
        self.empid=empno
        self.name=name
        self.salary=salary
    def getdata(self):
        print("EmpId=%g\nName=%s\nsalary=%g"%(self.empid,self.name,self.salary))
    
obj1=Employee(101,'prabhat',4500.500)
obj1.getdata();
obj1.age=45
obj2=Employee(102,'Aman',77000.500)
obj2.getdata();
obj2.wife="Rita"
print(obj1.age)
print(obj2.wife)
