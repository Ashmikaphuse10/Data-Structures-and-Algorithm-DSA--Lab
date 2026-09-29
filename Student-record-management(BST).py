class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class Stack:
    def __init__(self):
        self.TOP = -1
        self.st = [0] * 100

    def push(self, x):
        if self.TOP == 99:
            print("Stack Overflow")
            return

        self.TOP += 1
        self.st[self.TOP] = x

    def pop(self):
        if self.TOP == -1:
            print("Stack Underflow")
            return None

        x = self.st[self.TOP]
        self.TOP -= 1
        return x


def insert(root, data):
    new_node = Node(data)

    if root is None:
        return new_node

    temp = root

    while True:
        if data < temp.data:
            if temp.left is None:
                temp.left = new_node
                break
            temp = temp.left

        elif data > temp.data:
            if temp.right is None:
                temp.right = new_node
                break
            temp = temp.right

        else:
            print("Duplicate admission number.")
            break

    return root


def preorder(root):
    if root is None:
        return

    s = Stack()
    s.push(root)

    while s.TOP != -1:
        temp = s.pop()
        print(temp.data)

        if temp.right is not None:
            s.push(temp.right)

        if temp.left is not None:
            s.push(temp.left)


def inorder(root):
    if root is None:
        return

    s = Stack()

    while root is not None or s.TOP != -1:

        while root is not None:
            s.push(root)
            root = root.left

        root = s.pop()
        print(root.data)
        root = root.right


root = None

n = int(input("Enter number of students: "))

for i in range(n):
    data = int(input("Enter student admission number: "))
    root = insert(root, data)


print("Preorder traversal:")
preorder(root)

print("Inorder traversal:")
inorder(root)
