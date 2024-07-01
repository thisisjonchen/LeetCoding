# Daily LC 1550. Three Consecutive Odds
class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        numOfOdds = 0
        for num in arr:
            if num % 2 == 1: numOfOdds += 1
            else: numOfOdds = 0
            if numOfOdds == 3: return True
        return False

'''
TLDR: Add to numOfOdds if odd using %, else reset to 0. Return when numOfOdds = 3.
Speedran in 2 mins :)
'''
