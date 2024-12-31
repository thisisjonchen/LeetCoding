# LC 56. Merge Intervals
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = [intervals[0]]
        for i in range(1, len(intervals)):
            prev, curr = res[-1], intervals[i]
            if prev[1] >= curr[0]: # if prev end >= curr == overlapping somehow
                if curr[1] > prev[1]:
                    res.pop()
                    res.append([prev[0], curr[1]])
                # if prev end > curr start AND prev end also > curr end, we keep as is and continue
            else: # if not overlap, we append the interval to the new list
                res.append(curr)
        return res

'''
TLDR: Think of it in terms of a stack. Check the top of res, and compare the start + end times with curr. If prev end > curr start, then overlap (so marge). 
There are two cases here:
1. Use curr end
2. Use prev end
To check which to use, simply compare end times and use that. We always use prev's start time since the intervals are sorted, and it is assumed that prev's is earlier or equal to the curr.

If not overlapping, just append it to res.

TC O(nlogn)
SC O(n) (possible no intervals can be merged)
'''

        
