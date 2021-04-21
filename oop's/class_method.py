class Student:
    college_name='presidncy'
    def __init__(self):
        self.name='prabhat'
        self.age=23
    @classmethod  
    def clginfo(cls):
        print(cls.college_name)

s1=Student()
Student.clginfo()
 
