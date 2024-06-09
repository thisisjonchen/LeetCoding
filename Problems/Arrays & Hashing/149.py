# LC 169. Majority Element

# O(2n) = O(n), but with too much space O(n + 2)
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = dict()
        for num in nums:
            freq[num] = freq.get(num,0) + 1
        majority = 0
        majorityNum = 0
        for num, freq in freq.items():
            if freq > majority:
                majority = freq
                majorityNum = num
        return majorityNum
      
