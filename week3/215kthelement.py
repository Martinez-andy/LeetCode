# Initial solution, using a heap. 
import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        res = 0
        for _ in range(len(nums) - k + 1):
            res = heapq.heappop(nums)
        return res
    
# Solution using sorting (one line)
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return sorted(nums)[len(nums) - k]