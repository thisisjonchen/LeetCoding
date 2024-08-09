# LC 840. Magic Squares In Grid | LC Daily - 8/9/24
class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        if len(grid[0]) < 3 or len(grid) < 3:
            return 0

        sums = dict()
        squares = 0
        for i in range(len(grid) -2): # Row
            for j in range(len(grid[0]) -2): # Col
                arr = []
                for x in range(3):
                    sums["row" + str(x + 1)] = grid[x+i][0+j] + grid[x+i][1+j] + grid[x+i][2+j]
                    arr += [grid[x+i][0+j], grid[x+i][1+j], grid[x+i][2+j]]
                
                for y in range(3):
                    sums["col" + str(y + 1)] = grid[0+i][y+j] + grid[1+i][y+j] + grid[2+i][y+j]
                    arr += [grid[0+i][y+j], grid[1+i][y+j], grid[2+i][y+j]]

                sums["diag1"] = grid[0+i][0+j] + grid[1+i][1+j] + grid[2+i][2+j]
                arr += [grid[0+i][0+j], grid[1+i][1+j], grid[2+i][2+j]]
                sums["diag2"] = grid[0+i][2+j] + grid[1+i][1+j] + grid[2+i][0+j]
                arr += [grid[0+i][2+j], grid[1+i][1+j], grid[2+i][0+j]]
                
                if (grid[x+i][0+j] != grid[x+i][1+j] != grid[x+i][2+j]) and (grid[0+i][y+j] != grid[1+i][y+j] != grid[2+i][y+j]) and (grid[0+i][0+j] != grid[1+i][1+j] != grid[2+i][2+j]) and (grid[0+i][2+j] != grid[1+i][1+j] != grid[2+i][0+j]):
                    valid = True
                    for num in arr:
                        if not 1 <= num <= 9:
                            valid = False
                    if valid and sums["row1"] == sums["row2"] == sums["row3"] == sums["col1"] == sums["col2"] == sums["col3"] == sums["diag1"] == sums["diag2"]:
                        squares += 1
                sums.clear()
        return squares

'''
TLDR: Brute force and ensure that your conditionals are correct.
'''
            

                
                

                

            

                
                

                
