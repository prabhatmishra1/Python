class Person:
    def  __init__(self):
        self.name='name'
        self.age='age'
        self.abx=10
        
    def talk(self):
     return "person can talk"

    def  walk(self):
         print("person can walk")

    def code(self):
        print("adadad")
     


class Student(Person):
    def __init__(self,college,roll):
        super().__init__()
        self.college=college
        self.roll=roll
    def  code(self):
       super().code()
       print("jai")


s1=Student( 'shepa', 1010)
print(s1.code())
