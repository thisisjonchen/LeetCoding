# LC 1636. Sort Array by Increasing Frequency
class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        numToFreq = defaultdict(int) # O(n)
        for num in nums:
            numToFreq[num] += 1
        
        freqToNums = defaultdict(list)
        for num, freq in numToFreq.items():
            freqToNums[freq].append(num)
            freqToNums[freq].sort(reverse=True) # O(nlogn)

        res = []
        for freq, arr in sorted(freqToNums.items()): # O(nlogn)
            for i in range(len(arr)):
                res += [arr[i]] * freq

        return res

  '''
  TLDR: Count freq in dict, then swap and put in another dict with freq : arr(nums). Sort the nums. Then, iterate through the sorted freq in freqToNums, appending to res based on each num's respective freq.
  '''
