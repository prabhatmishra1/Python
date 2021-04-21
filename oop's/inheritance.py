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

obj.marry()
