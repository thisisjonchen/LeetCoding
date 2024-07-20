# LC 1605. Find Valid Matrix Given Row and Column Sums | Daily - 7/20/24
class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        res = [[0] * len(colSum) for _ in range(len(rowSum))]
        for i in range(len(rowSum)):
            for j in range(len(colSum)):
                mini = min(rowSum[i],colSum[j])
                res[i][j] = mini
                rowSum[i] -= mini
                colSum[j] -= mini
        return res
'''
TLDR: Set two nested loops iterating through rowSum and colSum respectively and find the min at each point. At that index (for rowSum and colSum),
put it in res. Subtract from rowSum and colSum after. O(mn) time for m = rowSum and n = colSum.
'''
            
                
        
            
