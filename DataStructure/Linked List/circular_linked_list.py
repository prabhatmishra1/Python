class Node:
    def __init__(self,data):
        self.data=data
        self.next=None


class LinkedList:
    def __init__(self):
        self.last=None

    def addatend(self,data):
        newnnode=Node(data)
        if not self.last:
            self.last=newnnode
            self.last.next=self.last
        else:
            newnnode.next=self.last.next
            self.last.next=newnnode

    def showlist(self):
        if not self.last:
            print("list is empty")
            return
        p=self.last.next
        while p!=self.last.next:
              print("adad")
              print(p.data)
              p=p.next     





obj=LinkedList()
obj.addatend(40)
obj.showlist()