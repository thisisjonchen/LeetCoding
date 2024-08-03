# LC 1460. Make Two Arrays Equal by Reversing Subarrays
class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        freqTar, freqArr = defaultdict(int), defaultdict(int)
        for i in range(len(target)):
            freqTar[target[i]] += 1
            freqArr[arr[i]] += 1
        return freqTar == freqArr

'''
TLDR: Count freq and compare

TC O(n)
SC O(n)
'''
