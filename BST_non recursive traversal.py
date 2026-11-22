class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        new = Node(data)

        if self.root is None:
            self.root = new
            return

        temp = self.root

        while True:
            if data < temp.data:
                if temp.left is None:
                    temp.left = new
                    return
                temp = temp.left

            elif data > temp.data:
                if temp.right is None:
                    temp.right = new
                    return
                temp = temp.right

            else:
                print("Duplicate ignored")
                return

    def inorder(self):
        stack = []
        temp = self.root

        while temp or stack:
            while temp:
                stack.append(temp)
                temp = temp.left

            temp = stack.pop()
            print(temp.data, end=" ")
            temp = temp.right

    def preorder(self):
        if self.root is None:
            return

        stack = [self.root]

        while stack:
            temp = stack.pop()
            print(temp.data, end=" ")

            if temp.right:
                stack.append(temp.right)

            if temp.left:
                stack.append(temp.left)


tree = BST()

n = int(input("Enter number of nodes: "))

for i in range(n):
    x = int(input("Enter value: "))
    tree.insert(x)

print("Inorder Traversal:")
tree.inorder()

print("\nPreorder Traversal:")
tree.preorder()
