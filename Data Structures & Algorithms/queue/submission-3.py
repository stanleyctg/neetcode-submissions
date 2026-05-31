class ListNode:
    def __init__(self, val = None, next_node = None):
        self.val = val
        self.next = next_node

class Deque:
    
    def __init__(self):
        self.head = ListNode()
        self.tail = self.head


    def isEmpty(self) -> bool:
        return (self.head.next is None)
        

    def append(self, value: int) -> None:
        node = ListNode(value)
        self.tail.next = node
        self.tail = node

    def appendleft(self, value: int) -> None:
        node = ListNode(value)
        node.next = self.head.next
        self.head.next = node
        if self.head == self.tail:
            self.tail = node
    
    def pop(self) -> int:
        if self.isEmpty():
            return -1
        cur = self.head
        while cur.next != self.tail:
            cur = cur.next
        value = cur.next.val
        self.tail = cur
        cur.next = None
        return (value)
            




    def popleft(self) -> int:
        if self.isEmpty():
            return -1
        value = self.head.next.val

        self.head.next  = self.head.next.next
        if self.head.next is None:
            self.tail = self.head
        return (value)
        

        
        
