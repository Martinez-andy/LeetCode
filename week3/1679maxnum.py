# Initial solution, used a hashmap. O(2n) essentially.
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        counter = Counter(nums)
        res = 0

        for num in nums:
            comp = k - num
            if comp in counter and counter[comp]:
                counter = self.update(counter, comp)
                if counter[num] != 0:
                    counter = self.update(counter, num)
                    res += 1
                else:
                    del counter[num]
        return res

    def update(self, counter, element):
        counter[element] -= 1
        if counter[element] == 0:
            del counter[element]
        return counter
    
# Two pointer solution. O(n log(n)) but is likely faster because lst.sort() is implemented in C
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        l, r = 0, len(nums) - 1
        numOps = 0
        nums.sort()

        # Check bound
        while l < r:
            duoSum = nums[l] + nums[r]
            if duoSum == k:
                numOps += 1
                l += 1
                r -= 1
            elif duoSum > k:
                r -= 1
            else:
                l += 1
        return numOps

    
