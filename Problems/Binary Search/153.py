# LC 153. Find Minimum in Rotated Sorted Array
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        # note that, compared to reg binary search, this is l < r
        while l < r:
            if nums[l] > nums[r]:
                # if left is greater than right, move toward right
                l += 1
            elif nums[l] < nums[r]:
                # if right is greater than left, move toward left
                r -= 1
            # no case where left == right since elements guaranteed to be unique
        # at end, l should be equal to r, so we can return either 
        return nums[l]

'''
TLDR: For our "comparison", just use nums @ l and r, not mid. We move toward either side (guaranteed) as the array is already sorted, but rotated.

TC O(logn)
SC O(1)
'''

