from collections import deque

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
                return

    def level_order(self):
        if self.root is None:
            print("Tree is empty")
            return

        q = deque([self.root])
        level = 0

        while q:
            size = len(q)
            print("Level", level, end=": ")

            for i in range(size):
                temp = q.popleft()
                print(temp.data, end=" ")

                if temp.left:
                    q.append(temp.left)

                if temp.right:
                    q.append(temp.right)

            print()
            level += 1

    def height(self, node):
        if node is None:
            return -1

        left = self.height(node.left)
        right = self.height(node.right)

        return 1 + max(left, right)

    def leaves(self, node):
        if node is None:
            return

        if node.left is None and node.right is None:
            print(node.data, end=" ")
        else:
            self.leaves(node.left)
            self.leaves(node.right)


tree = BST()
new_tree = BST()

n = int(input("Enter number of nodes: "))
values = []

for i in range(n):
    x = int(input("Enter value: "))
    values.append(x)
    tree.insert(x)

for x in values:
    new_tree.insert(x)

print("\nOriginal BST:")
tree.level_order()

print("\nNew BST:")
new_tree.level_order()

print("Height:", tree.height(tree.root))

print("Leaf nodes:", end=" ")
tree.leaves(tree.root)