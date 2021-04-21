#Accessing of base member in derived class.
class base:
    x="static"
    def __init__(self):
        self.a="instanse"
    def instance(self):#instance fun
        print("This is  instance function:")
    @staticmethod   
    def static():#static fun
        print("This is static function:")
class derived(base):
    def __init__(self):
        super().__init__()
    def fun1(self):
        base.static()
        self.instance()
        print("Instance variable=",self.a)
    @staticmethod
    def fun2():
        derived.static()
        print("static variable=",derived.x)
        
obj=derived()
obj.fun1()
derived.fun2()
