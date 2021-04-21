#All basic concept about self argument
class Student:
       ''' it is used to store the student information'''
       
       def __init__(self,n,a,m):
              self.name=n
              self.age=a
              self.marks=m
              print(id(self)) 
       def talk(self):
             print('name=%s\nage=%d\nmarks=%f'%(self.name,self.age,self.marks))
s=Student('prabhat',23,89)
s.talk()
print(id(s))
print(s.name)
'''
1.within the class to refer the current object we use the aurgument calld as self.

2.it same like this in java.

3.self is used to access the value of currnet object instanse variable.

4.for instance method and constructor always first arugument must be self.

5.by using the self we can create the instance variable.

6.we can  use the self within the class only  outside of the class,if u want then use
  reference variable.

7.self value will be passed by the pyhton virtual matchin implicitly .

8.instead of self we can give the other name like 'delf' but recommended one is  self .


'''
