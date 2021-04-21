from collections import deque
class Stack:
    def __init__(self):
        self.MAX=500
        self.Container=deque()
        self.Top=-1
    @property
    def is_Full(self):
        if self.Top==self.MAX-1:
            return True
        return False
    @property    
    def is_Empty(self):
        if self.Top==-1:
            return True
        return False
    def Push(self,value):
        if not self.is_Full:
            self.Container.append(value)
            self.Top+=1
        else:
            print("Stack is overflow")
    def Pop(self):
        if not self.is_Empty:
            self.Top-=1
            return self.Container.pop()
        print("Stack is  Underflow")
        exit()

    def Reverse_String(self,string):
        for letter in string:
            self.Push(letter)
        s=""    
        while not self.is_Empty:
             s=s+self.Pop()
        return s            


if  __name__ == '__main__':
    ref=Stack()
    print(ref.Reverse_String("We will conquere COVID-19"))    
    print(ref.Container)



