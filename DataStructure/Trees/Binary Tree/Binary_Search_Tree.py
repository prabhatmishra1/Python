class BinaryTree:
    def __init__(self,data):
        self.left  = None
        self.data  = data
        self.right = None
    
    def create(self, node):
        #Discard duplicate
        
        if self.data == node.data:
            return
        #if node is less then root node then insert left side 
        if  node.data < self.data:
            #check if left has something
            if self.left:
                self.left.create(node)
            else:
                self.left = node
        #It means node will go to the right side         
        else:
            #check if right have something
            if self.right:
                self.right.create(node)
            else:
                self.right = node 

    def display(self,root):
        # In-order Traversal 
        if root == None:
            return     
        self.display(root.left)
        print(root.data)
        self.display(root.right) 

    def search(self, root, key):
        if not root:
            return 
        if key < root.data:
           return self.search(root.left, key)
        elif key > root.data:
            return self.search(root.right, key) 
        else:
            return root 

    def findMin(self, root):
        if not root.left:
            return root        
        return self.findMin(root.left)

    def findMax(self, root):
        if not root.right:
            return root        
        return self.findMax(root.right)    
                         
    def delete(self, val):
        if val < self.data:
            if self.left:
                self.left = self.left.delete(val)
        elif val > self.data:
            if self.right:
                self.right = self.right.delete(val)
        else:
            if self.left is None and self.right is None:
                return None
            elif self.left is None:
                return self.right
            elif self.right is None:
                return self.left

            min_val = self.right.findMin(self.right).data
            self.data = min_val
            self.right = self.right.delete(min_val)

        return self
        




        


def build_tree():

    root=BinaryTree(50)
    root.create(BinaryTree(20))
    root.create(BinaryTree(70))
    root.create(BinaryTree(90))
    root.create(BinaryTree(10))
    root.create(BinaryTree(40))
    root.create(BinaryTree(60))
    root.create(BinaryTree(60))
    #print(root.right.left.)
    return root
if __name__ == "__main__":
    root = build_tree()
    #root.display(root)
    # node=root.search(root, 21)
    # print(f"{node.data} exists in the Tree" if node else "key does not exists in the Tree")
    # min_node = root.findMin(root)
    # print(min_node.data)
    # max_node = root.findMax(root)
    #print(max_node.data)
    root.delete(20)
    root.display(root)


    
    
