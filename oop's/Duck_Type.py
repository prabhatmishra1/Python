"""
In Python we cannot specify the type explicitly. Based on provided value at runtime the type will 
be considered automatically. Hence Python is considered as Dynamically Typed Programming 
Language.
def f1(obj):
 obj.talk()
What is the type of obj? We cannot decide at the beginning. At runtime we can pass any type.Then 
how we can decide the type?
At runtime if 'it walks like a duck and talks like a duck,it must be duck'. Python follows this 
principle. This is called Duck Typing Philosophy of Python
"""

class Person:
    def  __init__(self, name, age, abx):
        self.name=name
        self.age=age
        self.abx=abx
        
    def talk(self):
     return "person can talk"

    def  walk(self):
         print("person can walk")

    def code(self):
        print("person can code")

class Student(Person):
    def __init__(self,college,roll):
        super().__init__('Prabhat', 21, 10)
        self.college=college
        self.roll=roll
    def code(self):
       super().code()
       print("also")


s1=Student( 'shepa', 1010)
print(s1.code())
