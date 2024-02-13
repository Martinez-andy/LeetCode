class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        maxf = 0
        l = 0
        res = 0

        for r, char in enumerate(s):
            count[char] = count.get(char, 0) + 1
            maxf = max(maxf, count[char])

            if r - l + 1 - maxf > k:
                count[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res
        # Result is only updated when we have a new max frequency.
        # Thus we only update max frequency when we find a new one
        
"""
    Problem only wants to know maximum length of something and does not ask us to return
    the instance of maximum lenght. Thus, we can be a little more relaxed with how we track
    the maximum. Only update the maximum frequency and result when we need to. Use a hashmap
    to improve runtime for when we search for max length.
"""