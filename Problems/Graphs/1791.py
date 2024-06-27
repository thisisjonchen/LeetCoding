# LC 1791. Find Center of Star Graph | O(1) Time, Space
class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        if edges[0][0] == edges[1][0] or edges[0][0] == edges[1][1]:
            return edges[0][0]
        elif edges[0][1] == edges[1][1] or edges[0][1] == edges[1][0]:
            return edges[0][1]
'''
TLDR: Compare and return whatever matches in the first two edges
'''
