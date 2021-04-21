from collections import deque
class Stack:
    def __init__(self):
        self.MAX=3
        self.Table=deque()
        self.TOP=-1
    def Push(self,value):
        if not self.is_overflow():
           self.Table.append(value)
           self.TOP+=1
        else:
            print("Stack is Overflow")
    def Pop(self):
        if not self.is_underflow():
            self.TOP-=1
            return self.Table.pop()
        else:
            print("Stack is Underflow")
    def Peek(self):
        return self.Table[-1]           
    def is_underflow(self):
        if self.TOP==-1:
            return True
        return False

    def is_overflow(self):
        if self.MAX-1 == self.TOP:
            return True
        return False        

             



ref=Stack() 
ref.Push(1)
ref.Push(2)
ref.Push(3)
print(ref.Pop())
print(ref.Table) 