class ListNode:
    def __init__(self, val = None, next_node = None, prev_node = None):
        self.val = val
        self.next = next_node
        self.prev = prev_node


class Deque:
    
    def __init__(self):
        self.head = ListNode()
        self.tail = ListNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    def isEmpty(self) -> bool:
        return self.head.next == self.tail
        
    def append(self, value: int) -> None:
        node = ListNode(value)
        last_node = self.tail.prev
        
        last_node.next = node
        node.next = self.tail
        self.tail.prev = node
        node.prev = last_node
        
            

    def appendleft(self, value: int) -> None:
        node = ListNode(value)
        first_node = self.head.next
        
        self.head.next = node
        node.next = first_node
        first_node.prev = node
        node.prev = self.head

        
    def pop(self) -> int:
        if self.isEmpty():
            return -1
            
        last_node = self.tail.prev
        self.tail.prev = last_node.prev
        last_node.prev.next = self.tail
        
        
        return last_node.val
        
       
    def popleft(self) -> int:
        if self.isEmpty():
            return -1
            
        first_node = self.head.next
        self.head.next = first_node.next
        first_node.next.prev = self.head
        return first_node.val