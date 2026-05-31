class ListNode:
    def __init__(self, val, next_node=None):
        self.val = val
        self.next = next_node
        
class LinkedList:
    def __init__(self):
        self.head = ListNode(None)

    def get(self, index: int) -> int:
        i = 0
        cur = self.head.next
        while cur:
            if i == index:
                return cur.val
            cur = cur.next
            i += 1
        return -1
        
    
    def insertHead(self, val: int) -> None:
        cur = self.head
        new_node = ListNode(val)
        if cur.next is None:
            cur.next = new_node
            return 
        new_node.next = cur.next
        cur.next = new_node

    def insertTail(self, val: int) -> None:
        cur = self.head
        while cur.next != None:
            cur = cur.next
        cur.next = ListNode(val)
        
        
    def remove(self, index: int) -> bool:
        cur = self.head
        i = 0
        while cur.next is not None:
            if i == index:
                cur.next = cur.next.next
                return True
            cur = cur.next
            i += 1
        return False

 
        

    def getValues(self) -> List[int]:
        elem = []
        cur = self.head
        while cur.next != None:
            cur = cur.next
            elem.append(cur.val)        
        return elem


        
