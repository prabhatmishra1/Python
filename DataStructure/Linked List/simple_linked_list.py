class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

    def display(self):
        # head =  self
        # while head:
        #     print(head.data,end=' ')
        #     head = head.next

        print(self.data)
        if self.next == None:
            return
        self.next.display()

    def search(self,value,cnt=1):
        # head = self
        # pos = 1
        # while head:
        #     if head.data == value:
        #         return pos
        #     head = head.next
        #     pos += 1
        # return -1
        head = self
        if head.data == value:
            print("Element found at %d"%(cnt))
            return
        if head.next == None:
            return -1
        head.next.search(value,cnt+1)


def insertAtFirst(head, data):
    newNode = Node(data)
    newNode.next = head
    return newNode
    # return head


def insertAtEnd(head, data):
    temp = head
    while temp.next:
        temp = temp.next
    temp.next = Node(data)

def build_linked_list():
    # Alternative
    head = Node(10)
    head.next = Node(20)
    head.next.next = Node(30)
    head.next.next.next = Node(40)
    return head

if __name__ == '__main__':
    # node1 = Node(10)
    # node2 = Node(20)
    # node3 = Node(30)
    # node4 = Node(40)
    # node1.next = node2
    # node2.next = node3

    head = build_linked_list()
    # breakpoint()
    # newhead = insertAtFirst(head,5)
    insertAtEnd(head,50)
    head.display()



