# LC 387. First Unique Character in a String
class Solution:
    def firstUniqChar(self, s: str) -> int:
        chars = dict()
        for char in s:
            chars[char] = chars.get(char, 0) + 1
        for i in range(len(s)):
            if chars[s[i]] == 1:
                return i
        return -1
