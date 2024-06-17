# LC 704. Binary Search

# 6/16/24 - Needed Some Help with Finding The Index
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = low + ((high-low) // 2)
            if nums[mid] < target:
                low = mid + 1
            elif nums[mid] > target:
                high = mid - 1
            else:
                return mid
        return -1
'''
TLDR: Two indices, high and low, and mid = low + ((high-low)//2). Adjust highs and lows as necessary according to target.
'''
      
