class Node:
    def __init__(self, val, next_node=None):
        self.val = val
        self.next = next_node

class LinkedList:
    def __init__(self):
        self.head = Node(None)
    
    def get(self, index: int) -> int:
        cur = self.head
        i = 0
        while cur.next:
            if i == index:
                return cur.next.val
            cur = cur.next
            i += 1
        return -1
        

    def insertHead(self, val: int) -> None:
        cur = self.head
        new_node = Node(val)
        if cur.next is None:
            cur.next = new_node
            return

        new_node.next = cur.next
        cur.next = new_node
        

    def insertTail(self, val: int) -> None:
        cur = self.head
        new_node = Node(val)
        while cur.next:
            cur = cur.next
        cur.next = new_node

    def remove(self, index: int) -> bool:
        cur = self.head
        i = 0
        while cur.next:
            if i == index:
                cur.next = cur.next.next
                return True
            cur = cur.next
            i+= 1
        return False 
        

    def getValues(self) -> List[int]:
        elem = []
        cur = self.head
        while cur.next:
            cur = cur.next
            elem.append(cur.val)
        return elem
        
