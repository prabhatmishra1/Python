from collections import deque
class Stack:
    def __init__(self):
        self.Table=deque()
        self.TOP=-1
    def Push(self,expression):
        left_parenthsis=['(', '{', '[']
        right_parenthsis=[')', '}', ']']
        for value in expression:
            if value in left_parenthsis:
                self.Table.append(value)
                self.TOP+=1
            elif value in right_parenthsis:
                if self.is_underflow():
                    print("Right parenthiss are more then left parenthsis")
                    return False
                else:
                    if not self.match(self.Pop(),value):
                        print("Invalid Expression")
                        return False
        if self.TOP==-1:
            return True
        else:
            print("left parenthiss are more then right parenthsis")
            return False   
    
    def match(self,a,b):
        if a=='[' and b==']':
            return True
        if a=='{' and b=='}':
            return True
        if a=='(' and b==')':
            return True
        return False

    def Pop(self):
        if not self.is_underflow():
            self.TOP-=1
            return self.Table.pop()
        else:
            print("Stack is Underflow")
            return
    def Peek(self):
        return self.Table[-1]           
    def is_underflow(self):
        if self.TOP==-1:
            return True
        return False
             



ref=Stack() 
valid=ref.Push("A*(B-C+D")
if valid:
    print("Valid expression")
else:
    print("Invalid expression")    
