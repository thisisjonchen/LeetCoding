# LC 1380. Lucky Numbers in a Matrix | Daily LC - 7/19/24
class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        rowMins = {}
        columnMaxes = defaultdict(int)
        for row in range(len(matrix)):
            currMinVal = float("inf")
            currMinColumn = 0
            for column in range(len(matrix[0])):
                val = matrix[row][column]
                if val < currMinVal:
                    currMinVal = val
                    currMinColumn = column
                columnMaxes[column] = max(columnMaxes[column], val)
            rowMins[row] = (currMinVal, currMinColumn)

        luckyNums = []
        for row, val in rowMins.items():
            (rowMinVal, rowMinColumn) = val
            if columnMaxes[rowMinColumn] == rowMinVal:
                luckyNums.append(rowMinVal)

        return luckyNums

'''
TLDR: Iterate through columns and rows, storing maxes and mins accordingly. Used tuple for rowMins to have a relation to columns. Could probably be done in less memory than this O(m + n).
'''


            
            
    


        
        

                
