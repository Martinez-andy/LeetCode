# Original Solution
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        set1 = set(nums1)
        set2 = set(nums2)
        largerSet = set1 if max(len(set1), len(set2)) == len(set1) else set2

        for ele in largerSet:
            if ele in set1 and ele in set2:
                res.append(ele)
        return res

# Optimized and sorta hacky solution
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1 = set(nums1)
        set2 = set(nums2)

        return list(set1 & set2)
    
# Using sum method

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s, t = self.strSum(s), self.strSum(t)
        return chr(t - s + ord('a') - 1)
    
    def strSum(self, s: str) -> int:
        res = 0
        for char in s:
            res += ord(char) - ord('a') + 1
        return res