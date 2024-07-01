# LC 424. Longest Repeating Character Replacement

# Failed 5/19/24 | 26/45 TC
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        maxCount = 0

        for r in range(len(s)):
            kTemp = k
            while (kTemp > 0 and r != len(s)) or (r != len(s) and s[l] == s[r]):
                if s[l] != s[r]:
                    kTemp -= 1
                r += 1
            maxCount = max(maxCount, r - l)
            l += 1
        return maxCount

# Neetcode Solution
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        chars = {}
        l = 0
        maxLen = 0
        for r in range(len(s)):
            chars[s[r]] = chars.get(s[r], 0) + 1
            while (r - l + 1) - max(chars.values()) > k:
                chars[s[l]] -= 1
                l += 1
            maxLen = max(maxLen, r - l + 1)
        return maxLen
# Redone 6/30/24 | O(n)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = set()
        l = 0
        res = 0

        for r in range(len(s)):
            while s[r] in chars:
                chars.remove(s[l])
                l += 1
            chars.add(s[r])
            res = max(res, r - l + 1) # corrected for indexing
        return res
            
'''
TLDR: Using sliding window + count dictionary, we can check and adjust (mostly our left pointer) if necessary and setting maxLen to our window size (r - l + 1) for index adjustment.
'''
                
                    

        
