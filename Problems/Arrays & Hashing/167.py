# LC 167. Two Sum II - Input Array Is Sorted
from typing import List

# Initial Solution (O(n^2))
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i, n in enumerate(numbers):
            diff = target - n
            if diff in numbers:
                compareIdx = numbers.index(diff)
                if compareIdx != i:
                    return [min(i,compareIdx)+1, max(i, compareIdx)+1]
                
'''
Explaination:
This problem followed a similar route to Two Sum (hence, the name, Two Sum II), but disallowed the use of 
dicts or similar as it broke the contraint of constant extra space. I tried brute-forcing the here with 
finding the target (similar to two sum) and seeing if the diff was in numbers. Then, if so, I compared
the index of the diff and if it was exact of the current num I was comparing it to. If not, I was able to return.
However, this solution was in O(n^2) time because of the "if diff in numbers".
'''
    