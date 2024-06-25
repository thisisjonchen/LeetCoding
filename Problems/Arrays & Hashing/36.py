# LC 36. Valid Sudoku

# First Attempt 6/24/24 - O(1) Time, Space
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def boxNum(x,y):
            def boxNumY(y):
                if y <= 2:
                    return 0
                elif y <= 5:
                    return 1
                else:
                    return 2
                    
            numY = boxNumY(y)
            if x <= 2:
                if numY == 0:
                    return 0
                elif numY == 1:
                    return 1
                else:
                    return 2
            elif x <= 5:
                if numY == 0:
                    return 3
                elif numY == 1:
                    return 4
                else:
                    return 5
            else:
                if numY == 0:
                    return 6
                elif numY == 1:
                    return 7
                else:
                    return 8

        rows = {num: set() for num in range(9)}
        cols = {num: set() for num in range(9)}
        threeBythree = {num: set() for num in range(9)}

        for x in range(9):
            for y in range(9):
                val = board[x][y]
                if val != ".":
                    # rows
                    if val in rows[x]:
                        return False
                    else:
                        rows[x].add(val)
                    # cols
                    if val in cols[y]:
                        return False
                    else:
                        cols[y].add(val)
                    #threeBythree
                    threeNum = boxNum(x,y)
                    if val in threeBythree[threeNum]:
                        return False
                    else:
                        threeBythree[threeNum].add(val)
        return True

# More Concise Solution From NeetCode:
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        squares = collections.defaultdict(set)  # key = (r /3, c /3) <---

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if (
                    board[r][c] in rows[r]
                    or board[r][c] in cols[c]
                    or board[r][c] in squares[(r // 3, c // 3)]
                ):
                    return False
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])

        return True
'''
TLDR: Brute Force with 27 Hashmaps (9 rows, 9 columns, 9 sub-boxes). Will always result in O(1). Use tuple row // 3 and column // 3 for sub-box indices key.
'''
