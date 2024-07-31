# LC 1653. Minimum Deletions to Make String Balanced | LC Daily - 7/30/24

# T-O(n), S-O(n)
class Solution:
    def minimumDeletions(self, s: str) -> int:
        stack = []
        res = 0
        for char in s:
            if char == "b":
                stack.append(char)
            else:
                if stack and stack[-1] == "b":
                    stack.pop()
                    res += 1
        return res

# Better (from Solutions - Cred: SonuDutta):
class Solution:
    def minimumDeletions(self, s: str) -> int:
        bCount = 0
        minDeletions = 0
        for char in s:
            if char == 'a':
                minDeletions = min(minDeletions + 1, bCount)
            else:
                bCount += 1   
        return minDeletions

'''
TLDR: In better, essentially keeping track of min between "a" and "b". "b"s are incremented only for comparison, while "a"s are the condition for the comparison.
'''

