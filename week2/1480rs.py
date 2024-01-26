# Initial solution: Used the idea of a prefix sum
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        # Use prefix sum logic
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
        return nums
    
# Optimized solution
    # Already had optimal solution