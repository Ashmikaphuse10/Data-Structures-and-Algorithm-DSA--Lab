class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def create():
    x=int(input("Enter the data to create the node(0 to stop):"))
    if x==0:
        return None

    root= Node(x) #object creation
    print(f"Enter left of {x}")
    root.left = create()
    print(f"Enter right of {x}")
    root.right = create()
    return root

def preorder(root):
    if root is not None:
        print(root.data)
        preorder(root.left)
        preorder(root.right)

def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.data)
        inorder(root.right)

def postorder(root):
    if root is not None:
        postorder(root.left)
        postorder(root.right)
        print(root.data)
      

root=create()
print("preorder traversal:")
preorder(root)
print("inorder traversal:")
inorder(root)
print("postorder traversal:")
postorder(root)