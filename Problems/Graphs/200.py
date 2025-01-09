# LC 200. Number of Islands
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def bfs(i, j):
            # verify within valid range (we can't have -1 since in python, that is technically valid but islands don't wrap around)
            if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == "1":
                grid[i][j] = "#"
                # Mark adjacents and their adjacents
                bfs(i+1,j)
                bfs(i-1,j)
                bfs(i,j+1)
                bfs(i,j-1)

        if not grid:
            return 0

        res = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    bfs(i,j)
                    res += 1

        return res

'''
TLDR: Use BFS to find all adjacents and their adjacents. If we find a "1", we mark all connected "1"s with an arbitrary
symbol (I used "#") to skip over it in our next iterations of finding another "1". We only add to our number of islands once
we found the first "1", not when finding its neighbors. 

TC O(m * n), where m = num of rows, n = num of cols
TC O(m * n) due to recursion, num of recur calls could be == to m * n
'''

    
