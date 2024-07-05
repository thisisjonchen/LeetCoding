# LC 2058. Find the Minimum and Maximum Number of Nodes Between Critical Points | Daily - 7/5/24
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        points = []
        prev = head
        curr = head.next
        index = 1

        while curr.next is not None:
            if (curr.val > prev.val and curr.val > curr.next.val) or (curr.val < prev.val and curr.val < curr.next.val):
                points.append(index)
            curr = curr.next
            prev = prev.next
            index += 1

        if len(points) < 2:
            return [-1,-1]
    
        minDistance = float('inf')
        maxDistance = points[-1] - points[0]
        for i in range(len(points) - 1):
            minDistance = min(minDistance, points[i+1] - points[i])
        return [minDistance, maxDistance]

  '''
  TLDR: Find all the local maximas/minimas, then to find max, it is the distance between first and last; min, go through the points with i and i+1 to find min distance.
  '''
