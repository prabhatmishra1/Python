class Person:
    
    a = 10

    def __init__(self):
        print("parent class constructor")
        self.name = "Ram"
    def m1(self):
        self.mul = "Mil"

    @classmethod
    def test(cls):
        cls.tanks = "TT"
        cls.rank = "MM"
        return "class method"

    @staticmethod
    def avg(a,b):
        return 10
    

class Employee(Person): 

    def __init__(self):
        super().__init__()
        super().test()
        super().avg(10,20)
    
    @classmethod
    def m2(cls):
        super(Employee, cls).__init__(cls)
        print(cls.name)
        super(Employee, cls).m1(cls)
        print(cls.mul)
        cls.data = "data"
        cls.check(Employee)
        print(cls.data)

    def check(self):
        Employee.data = "tata"


ref = Employee()
print(ref.m2())
print(ref.check())

