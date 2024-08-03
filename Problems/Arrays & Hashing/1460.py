# LC 1460. Make Two Arrays Equal by Reversing Subarrays | LC Daily - 8/3/24
class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        freqTar = defaultdict(int)
        for num in target:
            freqTar[num] += 1
        freqArr = defaultdict(int)
        for num in arr:
            freqArr[num] += 1
        if freqArr == freqTar:
            return True
        return False

'''
TLDR: Count freq and compare
'''
