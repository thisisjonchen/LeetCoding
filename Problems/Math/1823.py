# LC 1823. Find the Winner of the Circular Game
class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        winner = 0
        for i in range(1, n + 1):
            winner = (winner + k) % i
        return winner + 1

'''
TLDR: Needed a hint for this one...this problem is called the "Josephus Problem". Here, we have a for-loop that iterates from 1 -> n, where i here would be the number of "losers". Added a +1 to the result because I observed my TC were less by 1... Don't know the exact reason why.
'''
