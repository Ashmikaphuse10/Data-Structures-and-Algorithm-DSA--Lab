class Queue:
    def __init__(self):
        self.R = -1
        self.F = -1
        self.qt = [0] * 5

    def insert(self, x):
        if self.R == 4:
            print("Queue overflow.")
            return

        self.R = self.R + 1
        self.qt[self.R] = x

        if self.F == -1:
            self.F = 0

    def delete(self):
        if self.F == -1:
            print("Queue underflow.")
            return

        x = self.qt[self.F]

        if self.F == self.R:
            self.F = self.R = -1
        else:
            self.F = self.F + 1

        return x

    def display(self):
        if self.F == -1:
            print("Queue is empty.")
            return

        for i in range(self.F, self.R + 1):
            print(self.qt[i], end=" ")


x1 = Queue()

while True:
    ch = int(input("\nEnter your choice:\n"
                   "1. Add customer\n"
                   "2. Serve customer\n"
                   "3. Display queue\n"
                   "4. Exit\n"))

    if ch == 1:
        x = int(input("Enter customer number: "))
        x1.insert(x)

    elif ch == 2:
        x = x1.delete()
        if x is not None:
            print("Customer served:", x)

    elif ch == 3:
        print("Customers waiting:")
        x1.display()

    elif ch == 4:
        print("Thank you!")
        break

    else:
        print("Enter a valid choice.")
