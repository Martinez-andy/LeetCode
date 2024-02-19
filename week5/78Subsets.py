# Recursive solution using dfs:
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []
        def dfs(i: int) -> None:
            if i >= len(nums):
                res.append(subset.copy())
                return None
            # Decision 1: Add i-th element
            subset.append(nums[i])
            dfs(i + 1)
            # Decision 2: Don't add i-th element
            subset.pop()
            dfs(i + 1)
            return None
        dfs(0)
        return res


# Iterative solution:
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for j in nums:
            res += [i + [j] for i in res]
        return res
        
"""
    Solution Notes:
        In general, these "return all possible combinations" solutions are backtracking
    questions. However, in this case an iterative solution exists. The idea is to start 
    with an empty list and then to add the current element into every list in the results
    list. For example, res = [[], [1]] then when we add 2 to the list we get:
    res = [[], [1], [2], [1, 2]]. Doing this will produce all possible subsets of the graph.
    However, backtracking is the more general solution and I think it works for more cases 
    than the iterative solution does.
"""