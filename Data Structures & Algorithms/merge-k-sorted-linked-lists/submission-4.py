# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        node = ListNode()
        pointer = node
        space = []
        for lst in lists:
            while lst:
                space.append(lst.val)
                lst = lst.next
        space.sort()

        for items in space:
            pointer.next = ListNode(items)
            pointer = pointer.next
        return node.next

    

        