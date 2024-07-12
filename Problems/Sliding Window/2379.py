# LC 2379. Minimum Recolors to Get K Consecutive Black Blocks

# First Try, A Bit Long, O(n)
class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        res = float('inf')
        whites = 0
        blacks = 0
        l, r = 0, 0

        while r < len(blocks):
            if blocks[r] == "W":
                whites += 1
            elif blocks[r] == "B":
                blacks += 1
                if blacks == k:
                    return 0
            r += 1
            if r >= k:
                res = min(res, whites)
                if blocks[l] == "W":
                    whites -= 1
                elif blocks[l] == "B":
                    blacks -= 1
                l += 1
        return res

# Shorter Solution from Solutions, O(n)
class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        l = 0
        recolor = 0
        globalRecolor = float("inf")

        for r in range(len(blocks)):
            if blocks[r] == "W":
                recolor += 1
            
            if r - l + 1 > k:
                if blocks[l] == "W":
                    recolor -= 1
                l += 1
            
            if r - l + 1 == k:
                globalRecolor = min(globalRecolor, recolor)
            
        return globalRecolor

'''
TLDR: If blocks[r] == "W", increase recolor and if the window size is greater than k, shorten the window by incrementing l. Keep track of the min.
Improvement: rather than only keep track of r, use r - l + 1 in sliding window.
'''


