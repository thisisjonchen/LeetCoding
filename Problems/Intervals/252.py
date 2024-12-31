class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        '''
        intervals.sort() # sort intervals into order
        # Check if any intervals are conflicting
        if not intervals:
            return True

        earliestStart, latestEnd = intervals[0][0], intervals[0][1]
        for i in range(1, len(intervals)):
            currStart, currEnd = intervals[i][0], intervals[i][1]
            if (currStart - latestEnd) < 0 or (currEnd - earliestStart) < 0:
                return False
            earliestStart = min(currStart, earliestStart)
            latestEnd = max(currEnd, latestEnd)
        return True
        '''

        # A more succinct solution is just checking if intervals[i-1][end] > intervals[i][start]'
        # Again, no intervals should overlap.

        intervals.sort(key=lambda i: i[0]) # can sort explicitly by the first index (start times)
        for i in range(1, len(intervals)):
            curr, prev = intervals[i], intervals[i-1]
            if prev[1] > curr[0]:
                return False
        return True

'''
TLDR: Simply check the end time of the and the start time of the current time. If prev end is > curr start, then overlap == False. Else, if nothing, return True

TC O(nlogn)
SC O(1)
'''
