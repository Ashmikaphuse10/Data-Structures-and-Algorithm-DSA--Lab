stack=[]

def push():
    a=input("Enter a name of the book being returned:")
    stack.append(a)
    print("The book has been returned.")

def pop():
    stack.pop()
    print("The book has popped successfully.")

def peek():
    print(f"Top  book is {stack[-1]}")

while True:
    ch=int(input("Enter a choice\n 1. for push\n 2. for pop\n 3. for peek\n 4. for print\n 5. for exit "))
    if ch==1:
        push()
    elif ch==2:
        pop()
    elif ch==3:
        peek()
    elif ch==4:
        for i in stack:
            print(i)
    elif ch==5:
        exit()
    else:
        print("please enter a valid choice.")
        break
