# LC 3238. Find the Number of Winning Players | Aug 3 Biweekly P1
class Solution:
    def winningPlayerCount(self, n: int, pick: List[List[int]]) -> int:
        pick.sort()
        counter = defaultdict(int)
        winners = 0
        previousWinner = False
        for i in range(len(pick)):
            if i > 0 and pick[i][0] != pick[i-1][0]:
                counter.clear()
                previousWinner = False
            counter[pick[i][1]] += 1
            if pick[i][0] == 0 or pick[i][0] < counter[pick[i][1]]:
                if i > 0 and pick[i][0] == pick[i-1][0] and previousWinner:
                    continue
                winners += 1
                previousWinner = True
        return winners

  '''
  TLDR: Sort players and keep track of the ball color and count using a defaultdict. Also, make sure that if it was a winner, we cannot add to the number of winners again.

  TC O(nlogn)
  SC O(n)
  '''
