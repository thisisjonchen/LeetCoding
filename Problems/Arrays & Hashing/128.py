# LC 128. Longest Consecutive Sequence
from types import List

# NeetCode Solution (Couldn't figure it out)
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Cannot use sorted... O(n logn)
        numSet = set(nums)
        longest = 0

        for n in numSet:
            # check if its the start of a sequence
            if (n - 1) not in numSet:
                length = 1
                while (n + length) in numSet:
                    length += 1
                longest = max(length, longest)
        return longest

# Redid 5/17/24
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # CANNOT USE SORTING O(NLOGN), must be done on first pass.
        numSeq = set(nums) #O(n) space
        longest = 0
        for num in numSeq: # O(n)
            if (num-1) not in numSeq: #O(1) lookup
                length = 0
                while (num+length) in numSeq: # Always <= n (if in chain of nums, makes outer loop O(1))
                    length += 1
                longest = max(longest, length)
        return longest
        # Ultimately O(n)

'''
TLDR: Use set. Check for left neighbor. If neighbor exists, continue. If left neighbor does not exist, use a length counter to check for all right neighbors. Store max count.

Explaination:
I couldn't figure this out. I initially tried hashmaps and sorting, but they did not work or had time complexities 
that exceeded the contraint O(n).

NeetCode explained how if we look at it from a "human perspective" we could gauge how to figure this out with neighbors:
Look at a number. Does the number-1  exist? Then that initial number cannot be the start of a sequence. However,
if the number-1 does exist (say the number is 4 and that number-1 is 3), then that number could be the start of a new sequence.
The if (n-1) not in numset checks and safeguards against that problem. Then, we just keep going up. Does n+1 exist? Does n+2 exist?
It is until it doesn't exist the while breaks, the max function checks for current longest length, and when the n of numset runs out,
we return the longest.
'''
