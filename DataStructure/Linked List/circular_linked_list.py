class Node:
    def __init__(self,data):
        self.data=data
        self.next=None


class LinkedList:
    def __init__(self):
        self.last = None
        self.head = None

    def addatend(self,data):
        if not self.head:
            self.head  = Node(data)
            self.head.next = self.head
            self.last = self.head
        else:
            ''' This the naive method '''
            # ptr = self.head
            # while ptr.next != self.head:
            #     ptr = ptr.next
            # newnode = Node(data)
            # ptr.next = newnode
            # newnode.next= self.head
            ''' this is the best way '''
            newnode = Node(data)
            temp = self.last.next
            self.last.next = newnode
            newnode.next = temp
            self.last = newnode
    def addatbeg(self, data):
        # create new node first
        newnode = Node(data)

        #check if the head is empty
        if not self.head:
            self.head = newnode
            self.head.next = self.head
            self.last = self.head
        else:
            newnode.next = self.head
            self.head = newnode
            self.last.next = self.head
    def deleteatbeg(self):
        #check if node is empty:
        if not self.head:
            return self.head
        #check if only one node is there
        elif self.head == self.head.next:
            self.head = None
        else:
            self.head = self.head.next
            self.last.next = self.head
    def showlist(self):
        if not self.head:
            print("list is empty")
            return
            return
        ptr = self.head
        while ptr.next != self.head:
              print(ptr.data)
              ptr=ptr.next
        print(ptr.data)

obj=LinkedList()
# obj.addatend(40)
# obj.addatend(50)
# obj.addatend(60)
# obj.addatend(70)
# obj.addatend(80)
obj.addatbeg(10)
obj.addatbeg(20)
obj.deleteatbeg()
obj.showlist()
