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
