# LC 3. Longest Substring Without Repeating Characters

# Failed Attempt, Passed 407/987 TC | 5/18/24
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 1:
            return len(s)
        l, r = 0, 1
        chars = set()
        count, maxCount = 0, 1
        while r < len(s):
            if len(chars) == 0:
                chars.add(s[l])
                count += 1
            if s[r] in chars:
                l = r
                chars.clear()
                maxCount = max(maxCount, count)
                count = 0
            else:
                chars.add(s[r])
                count += 1
            r += 1
        return max(maxCount, count)
        
# Re-Done 5/25/24 - GREAT MEMORY Usage (Beats 99.66%), but Time Complexity could be better.
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = set()
        longest = 0
        curr = 0
        p = 0
        while p < len(s):
            if s[p] not in chars:
                curr += 1
                chars.add(s[p])
            else:
                curr = 0
                while s[p] in chars:
                    chars.remove(s[p])
                    p -= 1
            longest = max(curr, longest)
            p += 1
        return longest

# Re-Done 6/30/24 - O(n) Time While Beating 97.80% Memory!
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
TLDR: Sliding Window, for with variable r (unchangable outside of for loop), but adjust the left pointer accordingly - remove until we hit the duplicate of s[r].
'''

                
        
