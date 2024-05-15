# LC 70. Climbing Stairs

class Solution:
    def climbStairs(self, n: int) -> int:
        one, two = 1,0
        for i in range(n):
            temp = one
            one = one + two
            two = temp
        return one

'''
TLDR: Initialize two variables, one (leading) and two (following), summing in the range of n-1 then return one.

Explaination: Here, we are kind of "backtracking" where the last TWO elements will always require 1 step each.
As such, we are condensing the two steps into one thus range(n-1). It can also be done with one,two = 1,0 with range(n).
Then, we move "backward" from the last elements toward element index 0 where we then return one, which will be based on the sums
of previous one + two at each respective step, but not the total number of steps.
'''
