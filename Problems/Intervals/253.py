# LC 253. Meeting Rooms II
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        # Solution from Neetcode
        intervals.sort(key = lambda i:i[0])
        min_heap = []
        minRooms = 0

        for i in range(len(intervals)):
            curr = intervals[i]
            if min_heap and min_heap[0] <= curr[0]: # comparing heap top (first end time) and curr start time... if heap end time is less than, then we can pop that off
                heapq.heappop(min_heap)
            heapq.heappush(min_heap, curr[1])
            minRooms = max(minRooms, len(min_heap))
        return minRooms

'''
TLDR: I couldn't come up with a solution after reading the hints, which suggested a min_heap.... why is that so? Why are we returning the len(min_heap)

The solution is somewhat un-intuitive. We use a min_heap to keep track of END TIMEs. 
For each interval, we compare the earliest end time in the heap (min_heap[0]) and the current START time (curr[0]). 

Consider the min_heap our rooms: once a meeting end time is met, we can pop it from rooms (min_heap)
Regardless, we push the curr END time to our rooms.

In Neetcode's solution the most confusing thing is, why len(min_heap) as our return? The min_heap represents our rooms, yes, but also all 
*unresolved*, overlapping meetings. This peak can happen at any time, why return len(min_heap)?

I made a small adjustment to make the solution slightly more intuitive with an additional variable minRooms. On every iteration,
we keep track of the max between minRooms vs. len(min_heap) and return minRooms instead. The answer is still the same.

TC O(nlogn)
SC O(n)
'''
