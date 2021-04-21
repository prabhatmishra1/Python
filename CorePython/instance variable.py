#creating a instance  veriable.
class Account:
    '''def __init__(self):# Through init()
      self.a=100
      self.b=5000'''
  
    '''def fun(self,a,b):# Through function
         self.x=a
         self.y=b'''

obj=Account()
#print(obj.__dict__)#for knowing the instance variable.
#obj.fun(10,20)
print(obj.__dict__)#for knowing the instance variable.
obj.a=100 #through outside the class.
print(obj.__dict__)#for knowing the instance variable.
