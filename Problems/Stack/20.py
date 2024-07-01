# LC 20. Valid Parantheses
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        paran = {")":"(", "]":"[", "}":"{"}
        open = set("([{")
        close = set(")]}")
        for char in s:
            if char in open:
                stack.append(char)
            elif char in close:
                if len(stack) == 0 or stack[-1] != paran.get(char):
                    return False
                else:
                    stack.pop()
        if len(stack) != 0:
            return False
        return True
'''
TLDR: Iterate through s, append to stack if open and check if close. Use sets for O(1) lookup at the cost of a little memory.
'''
