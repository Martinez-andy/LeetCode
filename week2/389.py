import collections
# My initial solution
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        counterT = collections.Counter(t)
        counterS = collections.Counter(s)

        # Iterate over keys in counterT
        for key in counterT.keys():
            # If counted values don't match we know we cound the extra char
            if counterT[key] != counterS[key]:
                return key
        return ""
    
# Optimized solution




# Notes