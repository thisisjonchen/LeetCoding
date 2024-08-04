# LC 1508. Range Sum of Sorted Subarray Sums | LC Daily - 8/4/24
class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        newArr = []
        
        for i in range(len(nums)):
            currSum = 0
            for j in range(i, len(nums)):
                currSum += nums[j]
                newArr.append(currSum)
            
        newArr.sort()

        return sum(newArr[left-1:right]) % (10**9 + 7)

'''
TLDR: Brute Force.

TC O(n^2logn) -> The newArr from the nested loops can be n^2, thus with the sort, it becomes n^2logn
SC O(n^2)
'''

            
        
