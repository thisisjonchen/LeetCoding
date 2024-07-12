# LC 3162. Find the Number of Good Pairs I

# Time Complexity O(n^2)
class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
        pairs = 0
        for i in range(len(nums2)):
            for j in range(len(nums1)):
                if nums1[j] / (nums2[i] * k) == nums1[j] // (nums2[i] * k):
                    pairs += 1
        return pairs
      
'''
TLDR: Brute Force is easiest here - iterate through both and compare
'''
