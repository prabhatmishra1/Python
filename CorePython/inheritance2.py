#Write a python script to understand inheritance.
class old:
    def swap(self,a,b):
       print("a=",a,"b=",b) 
       temp=0
       temp=a
       self.a=b
       self.b=temp
       
       print("a=",a,"b=",b)

class child(old):
    def show(self,a,b):
       super().swap(a,b)
       print("After swaping:")
       print(self.a,self.b)
obj=child()
obj.show(10,20)

