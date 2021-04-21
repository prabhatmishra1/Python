from collections import deque
class Queue:
    def __init__(self):
        self.rear=-1
        self.front=-1
        self.Table=deque(maxlen=3)

    def insert(self,data):
        if self.Table:
            if self.isFull:
                print("Queue Overflow")
            else:    
                self.Table.append(data)
                self.rear+=1
        else:
            self.front+=1
            self.rear+=1
            self.Table.append(data)
    def delete(self):
        if self.Table:
            self.Table.popleft()
        else:
            print("Queue is underflow")
    @property
    def isFull(self):
        return len(self.Table)>=self.Table.maxlen
                      

    def display(self):
          print(self.Table)      


ref=Queue()
ref.insert(1)
ref.insert(2)
ref.insert(3)
ref.delete()
ref.delete()
ref.delete()
ref.delete()
ref.display() 
print(ref.front)
print(ref.rear)   

    
    
    