# LC 567. Permutation in String
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1Chars, s2Chars = defaultdict(int), defaultdict(int)
        for i in range(len(s1)):
            s1Chars[s1[i]] += 1
            s2Chars[s2[i]] += 1

        l, r = 0, len(s1) - 1
        while r < len(s2):
            if s1Chars == s2Chars:
                return True
            s2Chars[s2[l]] -= 1
            if s2Chars[s2[l]] == 0: del s2Chars[s2[l]]
            l += 1
            r += 1
            if r < len(s2): s2Chars[s2[r]] += 1
        return False

'''
TLDR: use dicts (hashmaps) and sliding window. When decrementing the left pointer char in the dict, make sure to delete it if the count is 0.

TC O(n)
SC O(26) => O(1)... max O(52?) for 2 hashmaps of 26 chars each.
'''
            
        
