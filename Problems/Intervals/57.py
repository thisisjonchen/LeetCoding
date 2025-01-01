# LC 57. Insert Interval
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]

        arr = []
        inserted = False
        for i in range(len(intervals)):
            if intervals[i][0] >= newInterval[0] and not inserted: # inserted conditional to avoid duplicate insertions of newInterval
                arr.append(newInterval)
                arr.append(intervals[i])
                inserted = True
            else:
                arr.append(intervals[i])
        
        # if we reached the end and not yet inserted, append at end
        if not inserted:
            arr.append(newInterval)

        # Merge all intervals
        res = [arr[0]]
        for i in range(1, len(arr)):
            prev, curr = res[-1], arr[i]
            if prev[1] >= curr[0]:
                # if prev end is less than curr end
                if prev[1] < curr[1]:
                    res.pop()
                    res.append([prev[0], curr[1]])
                # else keep same
            else:
                res.append(curr)
        return res

'''
TLDR: A continuation of merge intervals (56) so do that one first. In terms of algo, just find a position to insert relative to the start (intervals[i][0]) and then merge all intervals respectively.
If you don't know how to merge, please see LC 56.

TC O(n)
SC O(n)
'''
