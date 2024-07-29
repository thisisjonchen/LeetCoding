# LC 1395. Count Number of Teams | Daily LC - 7/29/24
class Solution:
    def numTeams(self, rating: List[int]) -> int:
        res = 0
        for i in range(len(rating)):
            rlarger = []
            rsmaller = []
            llarger = []
            lsmaller = []
            for j in range(0, i):
                if rating[j] < rating[i]:
                    rsmaller.append(rating[j])
                else:
                    rlarger.append(rating[j])
            for k in range(i+1, len(rating)):
                if rating[k] > rating[i]:
                    llarger.append(rating[k])
                else:
                    lsmaller.append(rating[k])
            
            res += len(rlarger) * len(lsmaller)
            res += len(llarger) * len(rsmaller)    
        return res

'''
TLDR: There will be two "cases" here - ascending and descending. Compare to the "middle" soldier and find values less than and greather than it on both sides of it. In the result we add the multiples accordingly.
Ascending = len(rlarger) * len(lsmaller) and Descending = len(llarger) * len(smaller). 
