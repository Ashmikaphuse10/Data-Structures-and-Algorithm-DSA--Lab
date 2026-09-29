class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LL:
    def __init__(self):
        self.head = None

    def insert_beginning(self, val):
        new_node = Node(val)

        new_node.next = self.head
        self.head = new_node

        print("Book inserted at beginning.")

    def insert_end(self, val):
        new_node = Node(val)

        if self.head is None:
            self.head = new_node
            print("Book inserted at end.")
            return

        temp = self.head

        while temp.next is not None:
            temp = temp.next

        temp.next = new_node

        print("Book inserted at end.")

    def delete_beginning(self):
        if self.head is None:
            print("Library catalog is empty...")
            return

        x = self.head.data
        self.head = self.head.next

        print("Book deleted:", x)

    def display(self):
        if self.head is None:
            print("Library catalog is empty...")
            return

        temp = self.head

        print("Library Catalog:")

        while temp is not None:
            print(temp.data, end=" -> ")
            temp = temp.next

        print("None")


obj1 = LL()

while True:
    ch = int(input(
        "\nEnter your choice:\n"
        "1. Insert at beginning\n"
        "2. Insert at end\n"
        "3. Delete from beginning\n"
        "4. Display\n"
        "5. Exit\n"
    ))

    if ch == 1:
        val = int(input("Enter book ID: "))
        obj1.insert_beginning(val)

    elif ch == 2:
        val = int(input("Enter book ID: "))
        obj1.insert_end(val)

    elif ch == 3:
        obj1.delete_beginning()

    elif ch == 4:
        obj1.display()

    elif ch == 5:
        print("Thank you!")
        break

    else:
        print("Enter a valid choice.")
