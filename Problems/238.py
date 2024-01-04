# LC 238. Product of Array Except Self
import math
from typing import List
# Initial Solution (Failed, Over-Time with O(n^2) :<)
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = []
        for i in range(len(nums)):
            temp = nums.pop(0)
            answer.append(math.prod(nums))
            nums.append(temp)
        return answer

# Actual Solution (NeetCode <3, O(N))
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums)
        prefix = 1 # "neutral"
        for i in range(len(nums)): # first loop (prefix)... "setting"
            result[i] = prefix 
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums)-1, -1, -1): # second loop (postfix)... "crossing"
            result[i] *= postfix
            postfix *= nums[i]
        return result
    
'''
Explaination:
The constraints on this problem were what made this a medium problem. My first thoughts were dividing (of course, division was prohibited).
Then I tried using a queue method with multiplication. I knew it was going to be quite slow... I sat there. Racking my brains but nothing came to.
I gave up after 40 minutes and went to NeetCode and LeetCode discussions.

Many solutions had similar approaches with prefixes (the product before the specified num[i]) and postfixes (the number that is to be multiplied to
whatever is in result after modification from prefixes). So it first begins with creating an array of [1]'s with nums array length. 1 is a neutral
number with anything times itself being...itself. Makes sense. Same goes for prefix and postfix. Then we start what I named the "setting" 
phase (setting up the result array). Here, we just pull the first index down (result index 0). Then we have to prep the prefix by multiplying it by the 
current number. This prefix is then set to the next array index (result index 1). So on until the first loop is complete. Then we are into what I call
the "crossing stage" (multiplying now in reverse). This follows a similar logic to the first loop with multiplying the postfix, but rather than setting
the result[i] and overriding it, we are now multipyling it. Once this is done, we have our answer.
'''