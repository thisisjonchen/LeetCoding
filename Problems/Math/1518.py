# LC 1518. Water Bottles | Daily - 7/7/24

# Time Complexity: O(log(numBottles))
class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        total = numBottles
        while numBottles >= numExchange:
            total += numBottles // numExchange
            numBottles = (numBottles // numExchange) + numBottles % numExchange
        return total
      
# Time Complexity: O(1) - From Solutions
class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        return numBottles + (numBottles-1)//(numExchange-1)
'''
TLDR: Just iterate until numBottles < numExchange, where numBottles // numExchange is the actual amt of bottles substituted and numBottles % numExchange is the remainder not substituted (to be exchanged next).
Could probably do in O(1), but the solution is quite unintuitive from reading the problem.
'''
