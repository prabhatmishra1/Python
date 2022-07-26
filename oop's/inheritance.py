#Inheritance Concept

class A:
    '''about heritance'''
    def __init__(self):
        print('A class')
    def property(self):
        print('Land+Gold+Fame+Home')
    def  marry(self):
        print('Subhalakhmi')

class B():
     def __init__(self):
         print('B class')
     def marry(self):
          print('sunny leon')

class C(A,B):
    pass

obj=C()

#obj.marry()

class Person:
    """
    Person class
    """
    def __init__(self, name="Ram", age=21):
        self.name = name
        self.age = age
    
    def breath(self):
        print("person can breath")

    @classmethod
    def nation(cls):
        cls.nation_name = "India" 
    

class Employee(Person):
    """
    Employee class
    """
    def __init__(self, company="TCS", salary=50000, name="Rama", age=221000):
        Person.__init__(self, name, age)
        self.company = company
        self.salary = salary

    def service(self):
        print("Employee can provide service")
    
    def test(self):
        print(Person.nation_name)

ref = Person()
ref.nation()
print(ref.nation_name)

class Manager(Employee):
     
    def  __init__(self, department):
        self.department = department
        Employee.__init__(self, company="HP",
            salary=230000, name="Shiva", age=23)
    def manage(self):
        print("manager manages things")

    
    



