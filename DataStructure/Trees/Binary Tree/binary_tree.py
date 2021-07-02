class BinaryTree:
    def __init__(self,data) -> None:
        self.left=None
        self.data=data
        self.right=None
   
    @staticmethod  
    def preorder(root):
        if root==None:
            return
        print(f"{root.data}",end=" " )
        BinaryTree.preorder(root.left)
        BinaryTree.preorder(root.right)

    @staticmethod  
    def inorder(root):
        if root==None:
            return
        BinaryTree.inorder(root.left)
        print(f"{root.data}",end=" ")
        BinaryTree.inorder(root.right)     
    
    @staticmethod  
    def postorder(root):
        if root==None:
            return
        BinaryTree.postorder(root.left)
        BinaryTree.postorder(root.right)
        print(f"{root.data}",end=" ")


def build_binary_tree():
    '''inserting node in B-tree'''
    root=BinaryTree(4)
    root.left=BinaryTree(5)
    root.right=BinaryTree(10)
    root.left.left=BinaryTree(7)
    root.left.right=BinaryTree(8)
    root.right.right=BinaryTree(1)
    #print(root.right.right.__dict__)
    return root

if __name__== "__main__":
    root=build_binary_tree()

    ''' print nodes in Preorder'''
    print("Preorder")
    BinaryTree.preorder(root)
    
    ''' print nodes in  Inorder'''
    print("\nInorder")
    BinaryTree.inorder(root)

    ''' print nodes in  Postorder'''
    print("\nPostorder")
    BinaryTree.postorder(root)