# LC 1509. Minimum Difference Between Largest and Smallest Value in Three Moves

# Gave Up 7/3/2024 | Solution Below
class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) <= 4:
            return 0
            
        nums.sort()

        minDiff = float('inf')
        minDiff = min(minDiff, abs(nums[0] - nums[-4])) # Last Three
        minDiff = min(minDiff, abs(nums[1] - nums[-3])) # First + Last 2
        minDiff = min(minDiff, abs(nums[2] - nums[-2])) # First 2 + Last
        minDiff = min(minDiff, abs(nums[3] - nums[-1])) # First Three

        return minDiff
'''
TLDR: There are four cases here where you can replace the last three, first three, first + last 2, or first 2 + last. Sorting is required for comparison (otherwise the calculations won't make sense)... O(nlogn) time.
'''
        
