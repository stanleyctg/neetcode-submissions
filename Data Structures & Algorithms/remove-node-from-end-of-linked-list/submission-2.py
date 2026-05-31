# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return []
        
        sz = 0
        sz_head = head
        while sz_head:
            sz += 1
            if sz_head.next:
                sz_head = sz_head.next
            else:
                sz_head = None

        idx_remove = sz - n

        i = 0
        dum = ListNode(None, head)
        cur = dum
        while i < idx_remove:
            cur = cur.next
            i += 1
        cur.next = cur.next.next

        head = dum.next
        return head
