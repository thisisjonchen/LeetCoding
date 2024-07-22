# LC 2418. Sort the People | Daily LC - 7/22/24
class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        heightToName = dict()
        for i in range(len(names)):
            heightToName[heights[i]] = names[i]

        res = []
        for height, name in sorted(heightToName.items(), reverse=True):
            res.append(name)
        return res
'''
TLDR: Use hashing + sort by height in descending order. O(nlogn) time due to sorting.
'''
