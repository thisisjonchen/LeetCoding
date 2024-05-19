# LC 643. Maximum Average Subarray I
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
'''
TLDR: Useful to use sum() with [:k], then sliding window L pointer is [i-k] and R will be [i]
'''
