# LC 242. Valid Anagram

# Initial Solution O(n log n) using sorted
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): # check if strings are equal (len)
            return False
        s = sorted(s)
        t = sorted(t)
        for i in range(len(s)):
            if (s[i] != t[i]):
                return False
        return True

# Just a bit more optimized (no need for for loop, just check if strings are equal)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): # check if strings are equal (len)
            return False
        s = sorted(s)
        t = sorted(t)
        return s == t
    
'''
Explaination: 
Given two strings (which may or may not be equal in length), we have to check if strings are equal in length.
If not, return False. Then, we have to sort the two strings (an easy way to verify if they are equal). Finally,
we return s == t. This will return True if they are equal, False if not.
'''