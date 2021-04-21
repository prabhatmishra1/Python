# Data Hiding
class Test:
    x=10
    __h=20
    def __init__(self):
        self.__a=10
    def instance(self):
        print("Instance=",self.__a)
    def fun():
        print("__h=",Test.__h)
obj=Test()
obj.instance()
Test.fun()
#cant not acsess print(Test.__h)
print(obj._Test__a)
print(obj.__dict__)#Access of instance variable
print(Test._Test__h)#Access of static variable
