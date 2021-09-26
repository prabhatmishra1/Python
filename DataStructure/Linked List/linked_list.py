class Node:
    def __init__(self,data):
        self.data=data
        self.next=None


class LinkedList:
    def __init__(self):
        self.start=None

    def addatbeg(self,value):
        newnode=Node(value)
        newnode.next=self.start
        self.start=newnode

    def addatend(self,value):
        newnode=Node(value)
        if self.start ==None:
            self.start=newnode
        else:
            temp=self.start
            while temp.next!=None:
                temp=temp.next
            temp.next=newnode

    def addafter(self,value,item):
        if self.start ==None:
            print("\nEmpty list cant add")
            return
        else:
            newnode=Node(item)
            value_founded=False
            p=self.start
            while p!=None:
                if p.data==value:
                   print("\n",p.data)
                   print("\n",p.next)
                   temp=p.next
                   p.next=newnode
                   newnode.next=temp
                   value_founded=True
                   break
                p=p.next
            if (not value_founded):
                print("\n{} not found in the list".format(value))

    def addbefore(self,item,value):
        if self.start==None:
            print("EmptyList")
            return
        p=self.start
        while p.next!=None:
            if p.next.data==item:
                newnode=Node(value)
                newnode.next=p.next
                p.next=newnode
                return
            p=p.next
        print("\n{} not found".format(item))

    def addatpos(self,pos,value):
        if self.start==None:
            print("List is Empty")
            return
        if pos==1:
            newnode=Node(value)
            newnode.next=self.start
            self.start=newnode
            return

        cnt,p=1,self.start
        while p!=None:
            if cnt==pos:
                self.addbefore(p.data,value)
                return
            p=p.next
            cnt+=1
        print("\npos {} does not exists".format(pos))

    def deleteatbeg(self):
        if self.start==None:
            print("Empty list")
            return
        self.start=self.start.next

    def deleteatend(self):
        if self.start ==None:
            print("Empty List!!")
            return
        elif self.start.next==None:
            self.start=None
            return
        temp=self.start
        while temp.next.next:
            temp=temp.next
        temp.next=None

    def deleteatpos(self,pos):
        if not self.start:
            print("Empty List")
            return
        if pos==1:
            self.deleteatbeg()
            return
        p=self.start
        cnt=1
        while p.next:
            if cnt==pos-1:
                temp=p.next.next
                p.next=temp
                return
            p=p.next
            cnt+=1

    def search(self,item):
        temp=self.start
        pos=1
        while temp!=None:
            if(temp.data==item):
                print("\n{} found at position {}".format(item,pos),end="\n")
            pos+=1
            temp=temp.next

    def get_length(self):
        if self.start==None:
            return 0
        temp=self.start
        pos=0
        while temp!=None:
            pos+=1
            temp=temp.next
        return pos

    def sort_list(self):
        if self.start==None:
            return "Empty list"
        p=self.start
        for _ in range(1,self.get_length()):
            while p.next!=None:
                if p.data>p.next.data:
                    temp=p.data
                    p.data=p.next.data
                    p.next.data=temp
                    #print(temp.data)
                p=p.next
            p=self.start

    def reverse_lit(self):
        if not self.start:
            print("Empty List")
            return
        p=self.start
        prev=None
        while p:
            nex=p.next
            p.next=prev
            prev=p
            p=nex
        self.start=prev

    def add_values(self,l):
        for value in l:
            self.addatend(value)


    def showlist(self):
        if(self.start==None):
            print("This an Empty List")
            return
        else:
            temp=self.start
            print("Node list are:")
            while temp!=None:
                print(temp.data,end=' ')
                temp=temp.next
            print()
    def take_input(self):
           return input("Enter a value: ")


if __name__ == "__main__":
    print("******Welcome to Linked List Program**********")
    obj=LinkedList()
    while True:
        print("==========================")
        print("1. Insert Node at begning")
        print("2. Insert Node at last")
        print("3. Display the list of Nodes")
        print("4. Exit")
        print("5. Add before the list of Nodes")
        print("6. Add after the list of Nodes")
        print("7. Delete from bigning")
        print("8. Delete from end")
        print("9. Delete from position")
        print("10. insert from position")
        print("11. Get length of Linked List")
        print("12. Add values in Linked List")
        print("13. Sort Linked List")
        print("14. Reverse Linked List")
        print("==========================")
        n=int(input())

        if n==1:
            obj.addatbeg(obj.take_input())

        elif n==2:
            obj.addatend(obj.take_input())
        elif n==3:
            obj.showlist()
        elif n==4:
            exit()
        elif n==5:
            value=input("Enter the node: ")
            item=input("Enter the value: ")
            obj.addbefore(value,item)

        elif n==6:
            value=input("Enter the node: ")
            item=input("Enter the value: ")
            obj.addafter(value,item)
        elif n==7:
            obj.deleteatbeg()
        elif n==8:
            obj.deleteatend()
        elif n==9:

            obj.deleteatpos(int(obj.take_input()))

        elif n==10:
            value=input("Enter the position: ")
            item=input("Enter the value: ")
            obj.addatpos(value,item)

        elif n==11:
            print(obj.get_length())

        elif n==12:
            l=input().split()
            obj.add_values(l)
        elif n==13:
            obj.sort_list()
        elif n==14:
            obj.reverse_lit()
        else:
            print("invalid input ")


