# LC 435. Non-overlapping Intervals
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda i: i[1]) # sorted by ENDTIMES
        # we can just merge and compare the merged intervals arr vs. og intervals arr
        arr = [intervals[0]]
        for i in range(1, len(intervals)):
            prev, curr = arr[-1], intervals[i]
            if prev[1] > curr[0]:
                continue # we do nothing to the arr (skip over the overlap)
            else:
                arr.append(curr)
        return len(intervals) - len(arr)
        
'''
TLDR: SORT BY ENDTIMES. Since intervals with earlier end times interfere less with future intervals, 
we reduce the number of overlaps more effectively.

To explain further, consider intervals [[1,100], [11, 20], [20, 33], [32, 90]]
The correct answer is 2. However, if we sorted by start times, the output would be 3 (we would be removing [1,100], [11, 20], [32, 90]), which is wrong.

By sorting with end times in mind, the new array is [[11, 20], [20, 33], [32, 90], [1,100]]. That way, we can preserve the "smaller" increments. Larger increments ([1,100]) would
require us to remove the smaller increments that lie within the range of the larger increment, which obviously according to the problem, is not ideal as we are
trying to minimize the # of removals. Thus, sort by endtimes and compare.

Also, there is no need for an extra "arr", I kept it for intuition purposes. We can just keep track of the prev.

TC O(nlogn)
SC O(n)
'''
