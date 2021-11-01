class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

    def display(self):
        ''' using for loop '''
        # head =  self
        # while head:
        #     print(head.data,end=' ')
        #     head = head.next

        ''' recursive way'''
        print(self.data)
        if self.next == None:
            return
        self.next.display()

        ''' print int list '''
        # if self.next:
        #     list.append(self.next.display())
        #     return  list().append()


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
    head = newNode
    return head
    # return head


def insertAtEnd(head, data):
    temp = head
    while temp.next:
        temp = temp.next
    temp.next = Node(data)

def insertAtPos(head,pos,data):
    ''' Count the position and once found found then
        update the linked list
    '''
    if head == None:
        return "Empty List"
    if pos == 1:
        return insertAtFirst(head, data)
    cnt = 1
    temp = head
    while temp!=None:
        temp = temp.next
        cnt += 1
        if cnt == pos:
            print(cnt)
            break
    newNode  = Node(data)
    newNode.next = temp.next
    temp.next =  newNode


def insertAtSoreted(head,data):
    #Create Node first
    newNode = Node(data)
    #step 1 : Check if the head is None
    if head == None:
        head  = newNode
        return head
    if data < head.data:
        newNode.next = head
        return newNode
    else:
        cur = head
        while cur.next and cur.next.data < data:
            # print(cur.data)
            cur = cur.next

        print("data",cur.data)
        newNode.next = cur.next
        cur.next = newNode
        return head
def  reverse(head):
    ''' There are multipal ways to reverse the linked list
    1. use stack concept
    2. use multipal pointer
    3. recursive way
    '''
    # 2. multipal pointer

    '''prevNode, currentNode, nextNode = (None, head, head)

    while nextNode:
        nextNode = currentNode.next
        currentNode.next = prevNode
        prevNode = currentNode
        currentNode = nextNode
    head = prevNode
    return head'''

    # 3. Recursive

    if head == None:
        return head
    if head.next == None:
        return head

    rec_head = reverse(head.next)
    rec_tail = head.next
    rec_tail.next = head
    head.next = None
    return head
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
    # head = insertAtFirst(head,5)
    # insertAtEnd(head,50)
    # insertAtPos(head, 3, 3)
    # insertAtSoreted(head, 15)
    head = insertAtSoreted(head, 5)
    # head=reverse(head)
    head.display()



