# LC 3239. Minimum Number of Flips to Make Binary Grid Palindromic I | Aug 3 Biweekly Contest P2
class Solution:
    def minFlips(self, grid: List[List[int]]) -> int:
        rowSwaps = 0
        for row in range(len(grid)): # Rows
            for column in range(len(grid[0]) // 2):
                if grid[row][column] != grid[row][len(grid[0]) -1 - column]:
                    rowSwaps += 1

        colSwaps = 0
        for column in range(len(grid[0])): # Columns
            for row in range(len(grid) // 2):
                if grid[row][column] != grid[len(grid) -1 - row][column]:
                    colSwaps += 1
        
        return min(colSwaps, rowSwaps)

'''
TLDR: Try "swapping" in rows, then columns, and return the min. Actual swapping is unnecessary, just keep track of count.

TC O(n^2)
SC O(1)
'''
        
