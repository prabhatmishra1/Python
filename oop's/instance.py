class Student:
    def __init__(self):
        self.a=10
        self.b=20
        self.c=20
    def m1(self):
        self.d="prabhat"
    def m2(self):
       self.e=30
    def delete(self):
        del self.a
        del self.b
        del self.c
        del self.d

s1=Student()
s1.m1()
s2=Student()
s2.m2()
s2.x=50
s2.z=90
s1.delete()
s2.delete()
print(s1.__dict__)
print(s2.__dict__)
