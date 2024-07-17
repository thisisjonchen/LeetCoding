# LC 643. Maximum Average Subarray I

# Attempted with Hint (5/19/24)
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        '''
        Input: List[int], int
        Output: Float (Average)

        Subarray of len == k

        Constraints: 10^-5 error, k is ALWAYS LESS THAN OR EQUAL TO n,
        n can be 10^5 (time complexity...) 

        Approach may involve: sliding window, take the sum then calculate the average at the end
        '''

        curr_sum = sum(nums[:k])  # Initialize the first window sum, O(k)
        max_sum = curr_sum  # Initialize max_sum

        for i in range(k, len(nums)): # O(n)
            curr_sum = curr_sum - nums[i - k] + nums[i]  # Slide the window
            max_sum = max(max_sum, curr_sum)  # Update max_sum

        # Ultimately O(n+k)
        return max_sum / k

# Retry 7/16/24
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        maxSum = 0
        l, r = 0, 0
        while r < k: # Can use sum(nums[:k])
            maxSum += nums[r]
            r += 1
        currSum = maxSum
        while r < len(nums):
            currSum += nums[r] - nums[l]
            l += 1
            r += 1
            maxSum = max(maxSum, currSum)
        return maxSum / k
        
'''
TLDR: Useful to use sum() with [:k], then sliding window L pointer is [i-k] and R will be [i]
'''
