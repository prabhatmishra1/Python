class Employee:
    ''' This class made for Employee'''
    def __init__(self,empid,name,salary):
        self.id=empid
        self.name=name
        self.salary=salary
    def show(self):
        print("{}{}{}".format(self.id,self.name,self.salary))
        
e1=Employee('12','prabhat','3000')
e1.show()
print(e1.__doc__)
print(help(e1))

    
