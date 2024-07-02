# LC 350. Interesction of Two Arrays II | Daily - 7/2/24
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        freq1 = dict()
        freq2 = dict()
        res = []
        for num in nums1:
            freq1[num] = freq1.get(num,0) + 1
        for num in nums2:
            freq2[num] = freq2.get(num,0) + 1
        for num, f in freq1.items():
            if num in freq2.keys():
                numInRes = min(f, freq2.get(num))
                for i in range(numInRes):
                    res.append(num)
        return res

'''
TLDR: Find freq, then take the min of the two freq if found. Could be more efficient, but was a daily so I said meh.
'''
