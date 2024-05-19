# LC 3046. Split the Array
class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        numsDict = {}
        for num in nums: # O(n)
            numsDict[num] = numsDict.get(num,0) + 1
            if numsDict[num] > 2: # Has to be split between two arrays, so if freq > 2, means duplicate in either array (not-distinct)
                return False
        return True

'''
TLDR: Just check the frequencies of the numbers. Since we split nums into two arrays comprised of distinct numbers, freq CANNOT be above 2.
'''
