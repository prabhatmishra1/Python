#ploymorphism
class Animals:
    def __init__(self,name):
        self.name=name

    def talk(self):
         raise NotImplementedError("Derived class must be Implemented")
class cat(Animals):
    def talk(self):
        return "Meow"
class dog(Animals):
    def talk(self):
        return "woof"
animals=[cat("Rekha"),cat("Soniya"),dog("moti"),dog("Gabbar")]

for animal in animals:
    print(animal.name,"-",animal.talk())
