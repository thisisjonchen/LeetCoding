# LC 2134. Minimum Swaps to Group All 1's Together II | LC Daily - 8/2/24

# Solution from Solutions | Cred: Vandy_Code (Gave Up)
class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        k = nums.count(1)
        mx = cnt = sum(nums[:k])
        n = len(nums)
        for i in range(k, n + k):
            cnt += nums[i % n]
            cnt -= nums[(i - k + n) % n]
            mx = max(mx, cnt)
        return k - mx

  '''
  TLDR: Will revisit.
  '''
