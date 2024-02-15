class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        slow2 = 0
        while True:
            slow2 = nums[slow2]
            slow = nums[slow]
            if slow == slow2:
                return slow
        

"""

    Step 1: Run tortoise and hare algorithm to find intersection point
    Step 2: Initialize another tortoise pointer at the start of the list
    Step 3: Iterate both slow pointers until they meet, then return either slow pointer
    Proof: 
        Algorithm relies on the fact that distance between start of linked list and the cycle
    is equal to the distance between the intersection point of the slow/fast pointer and the
    start of the cycle.
"""