class Person:
    def __init__(self,ages):
        self.ages=ages
    def __mul__(self,other):
        return self.ages*other.ages


b1=Person(40)
b2=Person(50)

print(b1*b2)
