# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next

        # Use fast and slow pointers to find midddle of list
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Reverse second half of the list
        snd = slow.next
        slow.next = prev = None

        while snd:
            temp = snd.next
            snd.next = prev
            prev = snd
            snd = temp

        # Merge the two linked lists
        fst, snd = head, prev
        
        while snd:
            tmp1, tmp2 = fst.next, snd.next
            fst.next = snd
            snd.next = tmp1
            fst, snd = tmp1, tmp2
            
"""
    Solution:
        The problem is that the linked list is only a singlely linked list.
        This means that even if we have a pointer at the end of the list we 
        cannot move backwards. Thus, we can break the solution into three steps.
        1.) Find the mid point of the linked list
        2.) Then, split the lists and reverse the second half of the list
        3.) Finally, merge the two lists in place
"""



"""
    Sketch:
        Iterate through linked list
        Create a copy using a doubly linked list
        Then, reorder singlely linked list using
        doublely linked list

"""