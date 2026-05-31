class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Deque:
    def __init__(self):
        self.front = None
        self.rear = None

    def isEmpty(self):
        return self.front is None

    def append(self, value):
        new_node = Node(value)
        if self.rear is None:  # If the deque is empty
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def appendleft(self, value):
        new_node = Node(value)
        if self.front is None:  # If the deque is empty
            self.front = self.rear = new_node
        else:
            new_node.next = self.front
            self.front = new_node

    def pop(self):
        if self.isEmpty():
            return -1  # Return -1 if the deque is empty
        if self.front == self.rear:  # Only one element in the deque
            value = self.front.value
            self.front = self.rear = None
            return value
        # Traverse to the second-to-last node
        current = self.front
        while current.next != self.rear:
            current = current.next
        value = self.rear.value
        self.rear = current
        self.rear.next = None
        return value

    def popleft(self):
        if self.isEmpty():
            return -1  # Return -1 if the deque is empty
        value = self.front.value
        self.front = self.front.next
        if self.front is None:  # If the deque becomes empty
            self.rear = None
        return value