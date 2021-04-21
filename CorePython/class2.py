'''Defien a class Employee with the instance variables empid,name,salary.Define a constructor to initialize member variables.Define
a function to show employee data'''
class employee:
    def __init__(self,empid,name,salary):
        self.empid=empid
        self.name=name
        self.salary=salary
    def show(self):
        print(self.empid,self.name,self.salary)

em1=employee(100,'prabhat',35000)
em2=employee(101,'Aman',40000)
l=[[em1.empid,em1.name,em1.salary],[em2.empid,em2.name,em2.salary]]
print(sorted(l))
print(em1.__dict__)
