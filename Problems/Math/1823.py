# LC 1823. Find the Winner of the Circular Game

# 7/8/24
class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        winner = 0
        for i in range(1, n + 1):
            winner = (winner + k) % i
        return winner + 1

# Retry - 7/30/24 using Circular LL
class ListNode:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.next = next

class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        dummy = root = ListNode(1)
        for i in range(2, n+1): # Establish Circular LL
            root.next = ListNode(i)
            root = root.next
    
        prev = root
        root.next = dummy

        while root.next.val != root.val: # Conditional to catch last fren in game
            root = root.next
            for i in range(k-1): # Count includes initial
                prev = root
                root = root.next
            print(root.val)
            prev.next = root.next # Eliminate root (loser)
        return root.val


'''
TLDR: Needed a hint for this one...this problem is called the "Josephus Problem". Here, we have a for-loop that iterates from 1 -> n, where i here would be the number of "losers". Added a +1 to the result because I observed my TC were less by 1... Don't know the exact reason why.
Retry TLDR: Here, we used circular LL as it was more intuitive. However, it does run slower and require more memory at T-O(n*k) and O(n) space.
'''
