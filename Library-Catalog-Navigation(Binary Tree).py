class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def create():
    x = int(input("Enter book ID (0 to stop): "))

    if x == 0:
        return None

    root = Node(x)

    print(f"Enter left book of {x}")
    root.left = create()

    print(f"Enter right book of {x}")
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


root = create()

print("Preorder traversal:")
preorder(root)

print("Inorder traversal:")
inorder(root)

print("Postorder traversal:")
postorder(root)