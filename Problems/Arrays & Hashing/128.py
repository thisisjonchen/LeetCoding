# LC 128. Longest Consecutive Sequence
from types import List

# NeetCode Solution (Couldn't figure it out)
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Cannot use sorted... O(nlogn)
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

'''
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