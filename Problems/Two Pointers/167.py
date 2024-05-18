# LC. 167 Two Sum II

# Redone 5/17/24
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        li = 0 # O(1) space
        ri = len(numbers) - 1 # O(1) space
        while li < ri: # O(n)
            sum = (numbers[li] + numbers[ri])
            if sum > target:
                ri -= 1
            elif sum < target:
                li += 1
            else:
                return [li+1, ri+1]
        # Ultimately O(n)

'''
TLDR: Simply have two pointers, move left +=1 when the sum is too low and right -= 1 when the sum is too high compared to the target.

Apparently did not have the original solution from a few months back :<
'''
        
