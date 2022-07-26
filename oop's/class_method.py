from cgi import test


class Student:
    college_name='presidncy'
    def __init__(self):
        self.name='prabhat'
        self.age=23

    def test():
        Student.college_name = "Shepa"
        print(Student.college_name)
    
    @classmethod  
    def clginfo(cls):
        Student.test()
        print(cls.college_name)
        print("Hello")
    
    

s1=Student()
Student.clginfo()
 
