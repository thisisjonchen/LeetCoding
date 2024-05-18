# LC 121. Best Time to Buy and Sell Stock

# Failed Passed 180/212 TC | 5/18/24
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minDay = 0
        maxDay = 1
        profit = 0
        if len(prices) > 1:
            for i in range(len(prices)): # O(n)
                net = prices[maxDay] - prices[minDay]
                if net > profit:
                    maxDay = i
                    profit = net
                else:
                    if prices[i] < prices[minDay]:
                        prices[minDay] = prices[i]
                        minDay = i
                    maxDay = i + 1
        return profit

# NeetCode Solution O(n)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minDay, maxDay = 0,1
        profit = 0
        while maxDay < len(prices):
            if prices[minDay] < prices[maxDay]:
                net = prices[maxDay] - prices[minDay]
                if net > profit:
                    profit = net
            else:
                minDay = maxDay
            maxDay += 1
        return profit
      
'''
TLDR: Hold two variables, minDay and maxDay, compare net to profit if prices are comparable else adjust minDay to be maxDay (switching the window).

Explanation: Somewhat hard to think about but easy to see once coded, we, of course, want a while loop with the conditional of maxDay being less than the
len of the given input "prices" (as maxDay is on the right of left, always). Inside the loop, we check if prices[min] < prices[max], then compute the net
to see if it is greater than the current profit. IF prices[min] > prices[max], that implies that there is a lower min than the one we have existing. And of
course, we want to increment maxDay each cycle to avoid an infinite loop.
'''
            
            
            
