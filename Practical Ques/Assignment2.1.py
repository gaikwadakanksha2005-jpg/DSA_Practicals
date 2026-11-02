
queue = []

# 1. Enqueue
def enqueue():
    n = int(input("Enter element: "))
    queue.append(n)
    print("Element inserted")

# 2. Dequeue
def dequeue():
    if len(queue) == 0:
        print("Queue is Empty")
    else:
        print("Deleted element:", queue.pop(0))

# 3. Display
def display():
    if len(queue) == 0:
        print("Queue is Empty")
    else:
        print("Queue:", queue)

# 4. Reverse Queue using Stack
def reverse_queue():
    stack = []

    while len(queue) > 0:
        stack.append(queue.pop(0))

    while len(stack) > 0:
        queue.append(stack.pop())

    print("Reversed Queue:", queue)

# 5. Merge Two Queues
def merge_queue():
    q1 = []
    q2 = []

    n = int(input("Enter number of elements in Q1: "))
    for i in range(n):
        x = int(input("Enter element: "))
        q1.append(x)

    n = int(input("Enter number of elements in Q2: "))
    for i in range(n):
        x = int(input("Enter element: "))
        q2.append(x)

    q3 = q1 + q2
    print("Merged Queue:", q3)

# 6. Check Identical Queues
def identical():
    q1 = []
    q2 = []

    n = int(input("Enter number of elements in Q1: "))
    for i in range(n):
        x = int(input("Enter element: "))
        q1.append(x)

    n = int(input("Enter number of elements in Q2: "))
    for i in range(n):
        x = int(input("Enter element: "))
        q2.append(x)

    if q1 == q2:
        print("Queues are Identical")
    else:
        print("Queues are Not Identical")


while True:
    print("\n1. Enqueue")
    print("2. Dequeue")
    print("3. Display")
    print("4. Reverse Queue")
    print("5. Merge Two Queues")
    print("6. Check Identical Queues")
    print("7. Exit")

    ch = int(input("Enter choice: "))

    if ch == 1:
        enqueue()
    elif ch == 2:
        dequeue()
    elif ch == 3:
        display()
    elif ch == 4:
        reverse_queue()
    elif ch == 5:
        merge_queue()
    elif ch == 6:
        identical()
    elif ch == 7:
        break
    else:
        print("Invalid Choice")
