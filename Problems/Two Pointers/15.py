# LC 15. 3Sum

# Solution with Hint - 6/25/24
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i, x in enumerate(nums):
            if x > 0: # skip positives
                break
            
            if i > 0 and x == nums[i-1]: # skip duplis [0,0...]
                continue
            
            l = i + 1
            r = len(nums) - 1

            while l < r:
                target = x + nums[l] + nums[r]
                if target > 0:
                    r -= 1
                elif target < 0:
                    l += 1
                else:
                    res.append([x,nums[l],nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l-1] and l < r: # skip duplis, two sum
                        l += 1
        return res

# Retry 7/17/24
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for x in range(len(nums)):
            if nums[x] > 0:
                break
            if x > 0 and nums[x] == nums[x-1]:
                continue
            
            l, r = x + 1, len(nums) - 1
            while l < r:
                target = nums[x] + nums[r] + nums[l]
                if target > 0: r -= 1
                elif target < 0: l += 1
                else: 
                    res.append([nums[x],nums[l],nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                    r -= 1
        return res
'''
TLDR: Fix one num and make it a two sum problem. To skip duplis, enforce "continues" and l+=1 at the "three-pointer" level and "two-pointer" level.
'''
            

