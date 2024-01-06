# LC 1. Two Sum
from typing import List

# Initial Solution O(n^2) using brute force w/ nested loops
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums) - 1):
            for j in range(i+1, len(nums)):
                if (nums[i] + nums[j] == target):
                    return [i,j]
            
# Better Solution O(n) using HashMaps (number : index)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        myMap = {}
        for i, n in enumerate(nums):
            diff = target - n # find the difference
            if diff in myMap: # check if the difference exists in the HashMap
                return [myMap[diff], i] # if so, return the [index of difference, current index]
            myMap[n] = i

'''
TLDR: Use hashmap with value as index, index as value. Check for diff value index in hashmap.

Explaination:
This problem has two solutions with time complexities that vary vastly from the other (n^2 vs. n).
I initially tried brute forcing using nested loops, but I knew that it was going to be inefficient.
With hashmaps, however, I would only need one loop O(n) and the hashmap is able to get key-pairs in O(1).
This is much more efficient in that, I can calculate the difference, check to see if the value is in the hashmap;
if not, keep going through, resulting in roughly O(n) max time.
'''