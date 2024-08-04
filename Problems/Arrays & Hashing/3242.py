# LC 3242. Design Neighbor Sum Service
class neighborSum:

    def __init__(self, grid: List[List[int]]):
        self.grid = grid

    def adjacentSum(self, value: int) -> int:
        grid = self.grid
        adjSum = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == value:
                    if col > 0: adjSum += grid[row][col-1]
                    if col < len(grid[0]) - 1: adjSum += grid[row][col+1]
                    if row > 0: adjSum += grid[row-1][col]
                    if row < len(grid) - 1: adjSum += grid[row+1][col]
                    return adjSum 

    def diagonalSum(self, value: int) -> int:
        grid = self.grid
        diaSum = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == value:
                    if col > 0 and row > 0: 
                        diaSum += grid[row-1][col-1]
                    if col < len(grid[0]) - 1 and row > 0: 
                        diaSum += grid[row-1][col+1]
                    if col < len(grid[0]) - 1 and row < len(grid) - 1: 
                        diaSum += grid[row+1][col+1]
                    if col > 0 and row < len(grid) - 1: 
                        diaSum += grid[row+1][col-1]
                    return diaSum

'''
TLDR: Brute force check and verify constraints. If valid, we add to the cumulative sum, respectively.

TC O(n^2) -> Matrix
SC O(1)
'''
