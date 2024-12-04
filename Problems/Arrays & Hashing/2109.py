# LC 2109. Adding Spaces to a String | LC Daily - 12/3/24
class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        spaceIdx, res = 0, ""
        if spaces[spaceIdx] == 0:
            res += " "
            spaceIdx += 1
        for i in range(len(s)):
            res += s[i]
            if spaceIdx < len(spaces):
                if spaces[spaceIdx] == i+1:
                    res += " "
                    spaceIdx += 1
        return res

'''
TLDR: keep track of spaceIdx. Add when needed while looping through s.

TC O(n)
SC O(1)
'''


        
