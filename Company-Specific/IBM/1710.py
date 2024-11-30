# LC 1710. Maximum Units on a Truck
class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x: x[1], reverse=True)
        currBoxes, currUnits = 0, 0
        for i in range(len(boxTypes)):
            boxes = boxTypes[i][0]
            units = boxTypes[i][1]
            if currBoxes + boxes < truckSize:
                currUnits += boxes * units
                truckSize -= boxes
            else:
                currUnits += truckSize * units
                break
        return currUnits

'''
TLDR: First sort the 2D array by the number of units per box (using key=lambda x: x[1]), reversed to have in descending order.
Then, we start going through the boxes, adding them multiplied by their units to the currUnits and tracking currBoxes until the we get to max truckSize.

TC O(nlogn)
SC O(1)... .sort() sorts in place
'''
