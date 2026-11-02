
# Queue Implementation using Linked List

class Node:
    def __init__(self,val):
        self.data=val
        self.next=None

class Queue:
    def __init__(self):
        self.front=None
        self.rear=None

    def isempty(self):
        return self.front is None

    # 1. Enqueue
    def enqueue(self,new_node):
        if self.isempty():
            self.front=new_node
            self.rear=new_node
        else:
            self.rear.next=new_node
            self.rear=new_node

    # 2. Dequeue
    def dequeue(self):
        if self.isempty():
            print("Queue is Empty")
        else:
            temp=self.front
            print("Deleted Element:",temp.data)
            self.front=self.front.next
            temp=None

            if self.front is None:
                self.rear=None

    # 3. Display
    def print(self):
        if self.isempty():
            print("Queue is Empty")
        else:
            print("Queue contains...")
            temp=self.front
            while temp:
                print(temp.data)
                temp=temp.next

    # 4. Reverse Queue using Stack
    def reverse(self):
        stack=[]

        temp=self.front
        while temp:
            stack.append(temp.data)
            temp=temp.next

        self.front=None
        self.rear=None

        while len(stack)>0:
            self.enqueue(Node(stack.pop()))

    # 5. Merge Two Queues
    def merge(self,q1,q2):
        temp=q1.front

        while temp:
            self.enqueue(Node(temp.data))
            temp=temp.next

        temp=q2.front

        while temp:
            self.enqueue(Node(temp.data))
            temp=temp.next

    # 6. Check Identical Queues
    def identical(self,q2):
        temp1=self.front
        temp2=q2.front

        while temp1 and temp2:
            if temp1.data != temp2.data:
                print("Queues are Not Identical")
                return
            temp1=temp1.next
            temp2=temp2.next

        if temp1 is None and temp2 is None:
            print("Queues are Identical")
        else:
            print("Queues are Not Identical")


# Main Program

q=Queue()
q.enqueue(Node(10))
q.enqueue(Node(20))
q.enqueue(Node(30))
q.enqueue(Node(40))
q.enqueue(Node(50))

print("Original Queue:")
q.print()

# Dequeue
q.dequeue()

print("After Dequeue:")
q.print()

# Reverse Queue
print("Reversed Queue:")
q.reverse()
q.print()

# Create Two Queues
q1=Queue()
q2=Queue()

q1.enqueue(Node(10))
q1.enqueue(Node(20))
q1.enqueue(Node(30))

q2.enqueue(Node(40))
q2.enqueue(Node(50))

# Merge Two Queues
q3=Queue()
q3.merge(q1,q2)

print("Merged Queue:")
q3.print()

# Check Identical
print("Check Identical Queues:")
q1.identical(q2)
