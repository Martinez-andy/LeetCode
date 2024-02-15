class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Use a two pointer approach
        dummy = ListNode(0, head)
        l, r = dummy, head
        while 0 < n and r:
            r = r.next
            n -= 1
        
        while r:
            r = r.next
            l = l.next
        l.next = l.next.next
        return dummy.next
    
"""
    Notes:
        Use left and right pointers to create the distance of n nodes.
    Now that we've found the proper distance we can move the right pointer
    forward until we reach the end, AKA None pointer. At that point, the
    left pointer is right before the node we need to delete so we can remove
    it by putting l.next = l.next.next
"""