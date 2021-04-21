# Real example of multiple Inheritance.
class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
class student(person):
    def __init__(self,name,age,roll):
        self.rollno=roll
        person.__init__(self,name,age)
class Teacher(person):
    def __init__(self,name,age,salary,subject):
        self.salary=salary
        self.subject=subject
        person.__init__(self,name,age)
        
    
class brightstudent(student,person):
    def __init__(self,name,age,roll,salary,subject,points):
        self.points=points
        student.__init__(self,name,age,roll)
        Teacher.__init__(self,name,age,salary,subject)
obj=brightstudent("prabhat",21,'17mca014',20000,'python',8.4)
print(obj.__dict__)

    
