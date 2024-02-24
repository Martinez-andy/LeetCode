class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(i: int, curr: List[int], total: int) -> None:
            # Base cases
            
            # Case 1: Found target
            if total == target:
                res.append(curr.copy())
                return None
            
            # Case 2: Index out of bounds or total exceeds target
            if total > target or i >= len(candidates):
                return None
            
            # Handle the construction of decision tree:
            
            # Case 1: Add the i-th element
            curr.append(candidates[i])
            dfs(i, curr, total + candidates[i])
            
            # Case 2: Don't add the i-th element
            curr.pop()
            dfs(i + 1, curr, total)
            return None
        dfs(0, [], 0)
        return res
        
        
        
"""
    This is another backtracking question, we can tell because they ask us to
    return all possible combos that fulfill some criteria. With these backtracking
    questions you really want to try to apply a decison tree of some sort. In this 
    case, we want a tree that decides whether to add the i-th node or not at each level.
    Doing so avoids unique permutations that are not unique combinations. After deciding 
    how to construct the decision tree, all that's left is implementing a recursive DFS
    algorithm. The base cases should handle the cases as well as the conditions outlined
    in the question. The decision tree construction happens after the base cases. 
    Additionally, this dfs algorithm should take in multiple inputs as arguments. These inputs
    should be useful in figuring out the stopping conditions, aka solving the problem.
    
    Side Note:
        We want to add the i-th element multiple times, that is a question specific specification.
        I enforce this by not incrementing i in decision 1
"""