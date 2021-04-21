#Write a python script to understand Inheritance.
class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def showage(self):
        print("Age=",self.age)

    def showname(self):
        print("Name=",self.name)
class student(person):#define inheritance
    def __init__(self,roll,name,age):
        super().__init__(name,age)#We can pass value in this way.
        #super().__init__("prabhat",21)# Other way to calling constructor
        self.roll=roll
        #person.__init__(self,name,age)#calling parents class constructor first
    def showroll(self):
        print("Rollno=",self.roll)


obj=student(100,'prabhat',21)
obj.showroll()
obj.showage()
obj.showname()
