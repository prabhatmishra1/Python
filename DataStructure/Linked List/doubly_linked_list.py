class Node:
    def __init__(self,data):
        self.prev = None
        self.data = data
        self.next = None

def display(head):
    ptr = head
    while ptr:
        print(ptr.data)
        ptr = ptr.next

def addatbeg(head,data):
    # create node first
    newnode = Node(data)
    if not head:
        return Node(data)
    newnode.next = head
    return newnode
def addatend(head, data):
    newnode = Node(data)
    if not head:
        return newnode
    else:
        ptr =  head
        while ptr.next:
            ptr = ptr.next
        ptr.next = newnode
        newnode.prev = ptr
        return head

def create_doubly_linked_list():
    head = Node(10)
    head.next = Node(20)
    head.next.prev = head
    head.next.next = Node(30)
    head.next.next.prev = head.next
    return head


if __name__ == '__main__':
    head = create_doubly_linked_list()
    # head = addatbeg(head, 5)
    head  = addatend(head, 40)
    head = addatend(head, 50)
    display(head)
