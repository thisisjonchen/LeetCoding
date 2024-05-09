# LC 11. Container With Most Water

class Solution:
    def maxArea(self, height: List[int]) -> int:
        size = len(height)
        distance = size - 1
        leftIndex = 0
        rightIndex = size - 1
        containerMax = min(height[leftIndex],height[rightIndex]) * distance
        while distance != 0:
            if height[leftIndex] <= height[rightIndex]:
                leftIndex += 1
            else:
                rightIndex -= 1
            distance -= 1
            containerMax = max(containerMax, (min(height[leftIndex],height[rightIndex])*distance))
        return containerMax

        '''
        TLDR: Keep track of left and right indexes, move inward dependent on whichever "height" is smaller

        Explaination: First, initialize left and right variables alongside size and distance (which is size-1). With a 
        while loop of the condition distance != 0, we move inwards dependent on whether left or right is smaller and then
        retrieving the container size by multiplying the smaller of the two heights times the distance between. We 
        keep doing so until we reach distance == 0. Then, we return the containerMax.
        '''
