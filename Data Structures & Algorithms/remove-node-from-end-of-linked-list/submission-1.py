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
        dummy = head
        while dummy:
            sz += 1
            if dummy.next:
                dummy = dummy.next
            else:
                dummy = None

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
