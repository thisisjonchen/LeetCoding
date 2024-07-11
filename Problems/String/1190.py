# LC 1190. Reverse Substrings Between Each Pair of Parentheses

# Time Complexity O(n^2)
class Solution:
    def reverseParentheses(self, s: str) -> str:
        pos = []

        for i in range(len(s)):
            if s[i] == "(":
                pos.append(i)
            elif s[i] == ")":
                lastOpen = pos.pop()
                s = s[0:lastOpen] + s[lastOpen:i][::-1] + s[i:len(s)]

        res = ""
        for char in s:
            if char not in "()":
                res += char
        return res

'''
TLDR: Iterate through string - if s[i] == "(", we append to stack, else if s[i] == ")", we pop from stack and reverse everything between the last opening parantheses and the current s[i] closing parantheses.
Then, iterate through again to remove any parantheses. Note: Reversing ([::-1]) inside the for loop will result in N^2 time.
'''
