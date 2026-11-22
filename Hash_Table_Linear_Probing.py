class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def hash(self, key):
        return key % self.size

    def insert_without_replacement(self, key):
        index = self.hash(key)

        for i in range(self.size):
            pos = (index + i) % self.size

            if self.table[pos] == key:
                print("Duplicate key")
                return

            if self.table[pos] is None:
                self.table[pos] = key
                return

        print("Hash table is full")

    def insert_with_replacement(self, key):
        home = self.hash(key)

        if key in self.table:
            print("Duplicate key")
            return

        if self.table[home] is None:
            self.table[home] = key
            return

        old = self.table[home]

        if self.hash(old) != home:
            self.table[home] = key

            for i in range(1, self.size):
                pos = (home + i) % self.size

                if self.table[pos] is None:
                    self.table[pos] = old
                    return

        else:
            for i in range(1, self.size):
                pos = (home + i) % self.size

                if self.table[pos] is None:
                    self.table[pos] = key
                    return

        print("Hash table is full")

    def search(self, key):
        index = self.hash(key)

        for i in range(self.size):
            pos = (index + i) % self.size

            if self.table[pos] is None:
                return -1

            if self.table[pos] == key:
                return pos

        return -1

    def display(self):
        print("\nIndex\tKey")
        for i in range(self.size):
            print(i, "\t", self.table[i] if self.table[i] is not None else "EMPTY")


size = int(input("Enter hash table size: "))
ht = HashTable(size)

choice = int(input("1. Without replacement\n2. With replacement\nEnter choice: "))

n = int(input("Enter number of keys: "))

for i in range(n):
    key = int(input("Enter key: "))

    if choice == 1:
        ht.insert_without_replacement(key)
    elif choice == 2:
        ht.insert_with_replacement(key)
    else:
        print("Invalid choice")
        break

key = int(input("\nEnter key to search: "))
pos = ht.search(key)

if pos != -1:
    print("Key found at index", pos)
else:
    print("Key not found")

ht.display()
