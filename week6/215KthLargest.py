import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [-n for n in nums]
        heapq.heapify(nums)

        ans = None
        for _ in range(k):
            ans = heapq.heappop(nums)
        return -ans
    
"""
    Redid this question. Again heap related, could be done with a 
    sorted array but question asks for solutino that doesn't sort
    the array
"""