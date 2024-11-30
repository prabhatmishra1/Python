#name conflict of instance member function.
class parent:
    @staticmethod
    def fun():#method overloading if arguments are same.
        print("Parent class")
class child(parent):
    @staticmethod
    def fun(a):#method hiding if argument are not same.
        print("child class",a)
        parent.fun()

obj=child()
obj.fun(10)

