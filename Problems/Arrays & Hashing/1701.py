# LC 1701. Average Waiting Time
class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        totalWait = customers[0][1]
        time = totalWait + customers[0][0]
        for i in range(1, len(customers)):
            if (customers[i][0]) > time:
                totalWait += customers[i][1]
                time = customers[i][0] + customers[i][1]
            else:
                totalWait += time + customers[i][1] - customers[i][0]
                time = time + customers[i][1]
        return totalWait / len(customers)
'''
TLDR: Keep track of time and observe pattern. If the customer arrival time > time, set time to customer arrival + their wait time. Return avg with totalWait / len(customers).
'''
