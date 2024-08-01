# LC 1717. Maximum Score From Removing Substrings

# Failed 7/12/24 | 7/76 TC
class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        s = list(s)
        stack = []
        points = 0

        high = "ab" if x >= y else "ba"
        low = "ab" if x <= y else "ba"

        while len(s) > 0:
            curr = s.pop()
            if stack:
                prev = stack[-1]
                blob = curr + prev
                if curr == "a" and prev == "b" and blob == high:
                    stack.pop()
                    points += x
                elif curr == "b" and prev == "a" and blob == high:
                    stack.pop()
                    points += y
                else:
                    stack.append(curr)
            else:
                stack.append(curr)

        while len(stack) > 0:
            curr = stack.pop()
            if stack:
                prev = stack[-1]
                blob = curr + prev
                if curr == "a" and prev == "b" and blob == low:
                    stack.pop()
                    points += x
                elif curr == "b" and prev == "a" and blob == low:
                    stack.pop()
                    points += y

        return points

# Solution from Solutions
class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        def remove_substring(s, first, second, points):
            stack = []
            score = 0
            for char in s:
                if stack and stack[-1] == first and char == second:
                    stack.pop()
                    score += points
                else:
                    stack.append(char)
            return ''.join(stack), score
        
        # Determine the order based on the points
        if x > y:
            # Remove "ab" first
            s, score1 = remove_substring(s, 'a', 'b', x)
            s, score2 = remove_substring(s, 'b', 'a', y)
        else:
            # Remove "ba" first
            s, score1 = remove_substring(s, 'b', 'a', y)
            s, score2 = remove_substring(s, 'a', 'b', x)
        
        return score1 + score2

# Retry - 7/30/24
class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        stack = []

        greaterPoint = max(x,y)
        lesserPoint = min(x,y)
        if x >= y: greater, lesser = "ab", "ba"
        else: greater, lesser = "ba", "ab"

        score = 0
        for char in s:
            if stack and (stack[-1] + char) == greater:
                stack.pop()
                score += greaterPoint
            else:
                stack.append(char)
        
        temp = []
        for char in stack:
            if temp and (temp[-1] + char) == lesser:
                temp.pop()
                score += lesserPoint
            else:
                temp.append(char)

        return score  

'''
TLDR: Use high pass and low pass on string, based on point values (GREEDY).
'''
