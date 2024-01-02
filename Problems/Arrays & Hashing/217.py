# LC 217. Contains Duplicate
from typing import List

# Initial Solution O(n) using hashsets
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        mySet = set()
        for n in nums:
            if n in mySet:
                return True
            mySet.add(n)
        return False
        
'''
Explaination:
Using sets (which prevent duplicates), we can check if the respective value in "nums"
exists in the set (or in this case "mySet").

First, we initialize the set. Using a for loop to iterate through the "nums" array,
we can first check if the respective num exists in the set. If so, we return True.
Else, we add it to the set. If we iterate through the entire "nums" array and can't find a
duplicate, we return False.
'''