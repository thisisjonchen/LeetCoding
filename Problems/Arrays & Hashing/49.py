# LC 49. Group Anagrams
from typing import List
from collections import defaultdict

# Initial Solution
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        for word in strs:
            key = "".join(sorted(word))
            if key in hashmap:
                hashmap[key].append(word)
            else:
                hashmap[key] = [word]
        return hashmap.values()

# Better Solution using defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)
        for word in strs:
            key = "".join(sorted(word))
            hashmap[key].append(word)
        return hashmap.values()
    
'''
TLDR: Use hashmap (defaultdict) with the sorted word as key. The value will be a list that will be appended to.

Explaination:
My initial solution was to simply create a map, then use a key (which is the "sorted" version of a word)
to group similar words (if sorted, they should be the same). This required an if/else clause that involved
a O(n) operation to iterate through and check if the key is in the hashmap, then either append to the existing
list value, else create a new list value.

When I was looking through the "solutions" tab, I discovered "defaultdict", which removed the need for if/else
and simply plugging/chugging through the key-pairs. The algorithm is similar, but much more concise and efficient.
'''
