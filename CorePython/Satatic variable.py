#Understand static variable.
class Test:
    a=10 #static variable
    def __init__(self):
        self.x=1 #instance variable
        Test.b=20 #static variable
    def  f1(self):#Instance variable
        x=100 #Local Variable
        self.x=2 #instance variable
        Test.c=30#static variable
    @staticmethod
    def f2(m,n):#static method
       Test.d=40#static variable
    @classmethod
    def f3(cls):#static method
      cls.e=50#static variable
      Test.f=60#static variable
Test.g=50      
obj=Test()
obj.f1()
obj.f2(10,20)
Test.f3()
print(Test.a)
print(Test.__dict__)
