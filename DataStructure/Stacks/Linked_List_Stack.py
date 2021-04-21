class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class StackLinkedList:
    def __init__(self):
        self.top=None
    def push(self,data):
        newnode=Node(data)
        newnode.next=self.top
        self.top=newnode
    def pop(self):
        if not self.top:
            print("Stack is Underflow")
            return
        temp=self.top
        self.top=temp.next
        print("Poped: {}".format(temp.data))

    def peek(self):
        if not self.top:
            print("Stack is Underflow")
            return
        print("Peek item: {}".format(self.top.data))    


    def display(self):
        p=self.top
        while p:
            print(p.data)
            p=p.next

ref=StackLinkedList()
ref.push(3)
ref.push(2)
ref.push(1)
# ref.pop()
# ref.pop()
# ref.pop()
# ref.pop()
ref.peek()
#ref.display()




