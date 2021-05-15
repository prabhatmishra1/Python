from collections import deque
class Stack:
    def __init__(self):
        self.stack=deque()
        self.TOP=-1
        self.postfix=deque()
    def infix_to_postfix(self,value=None):
        expression=list()
        expression.extend(value)
        operators=['^','/','*','+','-','/']
        for exp in expression:
            if exp.isalpha():
                self.postfix.append(exp)
            elif exp in operators:  
                while not self.isEmpty and self.priority(exp, self.stack[self.TOP]):# if stack is empty or priority is high
                        self.postfix.append(self.Pop())
                self.Push(exp)
            elif exp=='(':
                self.Push(exp)

            elif exp==")":
                while self.stack[self.TOP] != "(":
                    self.postfix.append(self.Pop())
                self.Pop()        

        while self.isEmpty!=True:
            self.postfix.append(self.Pop())
        
         

    def Push(self, value):
        self.stack.append(value)
        self.TOP+=1

    def Pop(self):
        if self.stack: 
            self.TOP-=1
            return self.stack.pop()    
        print("Stack is underflow")

    @property
    def isEmpty(self):
        if self.TOP==-1:
            return True
        return False        

    def priority(self,a,b):
        priority_table={'^':3,'/':2,'*':2,'+':1,'-': 1,'(':0}
        if priority_table[b]>=priority_table[a]:
            return True
        return False                     




ref=Stack()
ref.infix_to_postfix(value='A+B*(C-D)^E')
# print(ref.stack)
print(ref.postfix)