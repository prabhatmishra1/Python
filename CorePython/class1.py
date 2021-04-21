'''Define a class student with instance variables rollno,name,semester,branch.Also define instance member function for user input data
set values of instance variable  and display student data.'''
class student:
    def __init__(self,rollno,name,semester,branch):
        self.rollno=rollno
        self.name=name
        self.semester=semester
        self.branch=branch
        print("The information of Rollno",self.rollno," student is:")
        print(self.name,self.semester,self.branch,sep="\n")
x=eval(input("Enter Rollno,Name,sesmseter,branch of student :"))
a,b,c,d=x
std=student(a,b,c,d)
x=eval(input("Enter Rollno,Name,sesmseter,branch of student :"))
a,b,c,d=x
st1=student(a,b,c,d)

    
